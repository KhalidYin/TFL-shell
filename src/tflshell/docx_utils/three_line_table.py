"""Three-line table (三线表) format for python-docx tables v2.2.

Supports:
  - Rich row metadata (bold, indent) via dict-format data_rows
  - Gray header background for visual distinction
  - Left-aligned parameter column, center-aligned data columns
  - Explicit column widths (param col wider than data cols)
  - Backward-compatible with flat list[str] data_rows
"""

from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from tflshell import config
from tflshell.docx_utils.xml_helpers import (
    set_table_borders, set_cell_bottom_border, set_cell_text,
    set_cell_shading, set_table_autofit_to_page,
)
from tflshell.presentation import get_presentation_profile


def apply_three_line_format(table, thick_sz=None, thin_sz=None, color=None):
    thick_sz = thick_sz or config.THREE_LINE_THICK_SZ
    thin_sz = thin_sz or config.THREE_LINE_THIN_SZ
    color = color or config.THREE_LINE_BORDER_COLOR
    set_table_borders(table, top_sz=thick_sz, bottom_sz=thick_sz,
                      thin_sz=thin_sz, color=color)
    if table.rows:
        for cell in table.rows[0].cells:
            set_cell_bottom_border(cell, sz=thin_sz, color=color)


def _split_header_text(text: str) -> list[str]:
    """Split a column header into multiple lines for readability."""
    if "\n" in text:
        return text.split("\n")

    if " / " in text and len(text) > 18:
        parts = text.split(" / ", 1)
        return [parts[0] + " /", parts[1]]

    if "(N=" in text and len(text) > 12:
        idx = text.index("(N=")
        if idx > 0:
            return [text[:idx].strip(), text[idx:].strip()]

    return [text]


def _format_header_cell(cell, header_text: str, alignment=None):
    """Set multi-line header text in a cell, bold."""
    if alignment is None:
        alignment = WD_ALIGN_PARAGRAPH.LEFT
    lines = _split_header_text(header_text)

    for p in cell.paragraphs:
        p.clear()

    if len(lines) == 1:
        p = cell.paragraphs[0] if cell.paragraphs else cell.add_paragraph()
        p.alignment = alignment
        run = p.add_run(lines[0])
        run.font.name = config.FONT_NAME
        run.font.size = Pt(config.FONT_SIZE_TABLE)
        run.font.bold = True
    else:
        first = True
        for line in lines:
            if first:
                p = cell.paragraphs[0] if cell.paragraphs else cell.add_paragraph()
                first = False
            else:
                p = cell.add_paragraph()
            p.alignment = alignment
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            run = p.add_run(line)
            run.font.name = config.FONT_NAME
            run.font.size = Pt(config.FONT_SIZE_TABLE)
            run.font.bold = True


def _render_data_row(table, row_idx, row_data, col_count, font_size, font_name, profile):
    """Render a single data row with rich formatting support.

    Spacing rules:
      - Bold category headers: extra space above (6pt) to separate from previous group
      - Indented sub-items: tight spacing (0pt above, 1pt after) within the group
      - Normal rows: standard 1pt spacing
    """
    if isinstance(row_data, dict):
        label = row_data.get("label", "")
        bold = row_data.get("bold", False)
        indent = row_data.get("indent", False)
        values = row_data.get("values", [])
    else:
        label = row_data[0] if len(row_data) > 0 else ""
        values = list(row_data[1:]) if len(row_data) > 1 else []
        bold = False
        indent = False

    expected_value_count = max(col_count - 1, 0)
    if len(values) != expected_value_count:
        raise ValueError(
            f"Row '{label}' has {len(values)} value cells but expected "
            f"{expected_value_count} based on the table header."
        )

    # Spacing: bold category headers get extra space above to separate groups
    if bold:
        space_before = profile.table.group_header_space_before
        space_after = profile.table.group_header_space_after
    elif indent:
        space_before = profile.table.indented_row_space_before
        space_after = profile.table.indented_row_space_after
    else:
        space_before = profile.table.standard_row_space_before
        space_after = profile.table.standard_row_space_after

    # Column 0: Parameter / Label — left-aligned, optional bold/indent
    display_label = (profile.table.indent_prefix if indent else "") + label
    set_cell_text(table.cell(row_idx, 0), display_label,
                  bold=bold, font_size=font_size, font_name=font_name,
                  alignment=WD_ALIGN_PARAGRAPH.LEFT,
                  space_before=space_before, space_after=space_after,
                  line_spacing=profile.table.cell_line_spacing)

    # Columns 1+: Numeric values — center-aligned, inherit bold from row
    for col_idx in range(1, col_count):
        val = values[col_idx - 1]
        set_cell_text(table.cell(row_idx, col_idx), val,
                      bold=bold, font_size=font_size, font_name=font_name,
                      alignment=WD_ALIGN_PARAGRAPH.CENTER,
                      space_before=space_before, space_after=space_after,
                      line_spacing=profile.table.cell_line_spacing)


def create_three_line_table(doc, rows, cols, headers, data_rows=None,
                            font_size=None, font_name=None,
                            presentation_profile="csr_standard"):
    """Create a three-line table with rich formatting support.

    Args:
        doc: python-docx Document.
        rows: Total number of rows (including header).
        cols: Number of columns.
        headers: List of column header strings.
        data_rows: List of dicts or list[list[str]] for data rows.
        font_size: Override default font size.
        font_name: Override default font name.

    Returns:
        python-docx Table object.
    """
    font_size = font_size or config.FONT_SIZE_TABLE
    font_name = font_name or config.FONT_NAME
    profile = get_presentation_profile(presentation_profile)

    table = doc.add_table(rows=rows, cols=cols)
    table.autofit = True
    set_table_autofit_to_page(table, width_pct=profile.table.width_pct)

    # ---- Header row ----
    for col_idx, header_text in enumerate(headers):
        cell = table.rows[0].cells[col_idx]
        # First column (Parameter) left-aligned; data columns center-aligned
        align = WD_ALIGN_PARAGRAPH.LEFT if col_idx == 0 else WD_ALIGN_PARAGRAPH.CENTER
        _format_header_cell(cell, header_text, alignment=align)
        set_cell_shading(cell, config.HEADER_ROW_BG_HEX)

    # ---- Data rows ----
    if data_rows:
        for row_idx in range(1, rows):
            data_idx = row_idx - 1
            if data_idx < len(data_rows):
                _render_data_row(table, row_idx, data_rows[data_idx],
                                 cols, font_size, font_name, profile)
            else:
                # Fill extra rows with XX
                for col_idx in range(cols):
                    set_cell_text(table.cell(row_idx, col_idx), "XX",
                                  font_size=font_size, font_name=font_name,
                                  alignment=WD_ALIGN_PARAGRAPH.CENTER,
                                  line_spacing=profile.table.cell_line_spacing)
    else:
        # No data rows provided: fill with XX placeholders
        for row_idx in range(1, rows):
            for col_idx in range(cols):
                align = WD_ALIGN_PARAGRAPH.LEFT if col_idx == 0 else WD_ALIGN_PARAGRAPH.CENTER
                set_cell_text(table.cell(row_idx, col_idx), "XX",
                              font_size=font_size, font_name=font_name,
                              alignment=align,
                              line_spacing=profile.table.cell_line_spacing)

    # ---- Apply three-line borders ----
    apply_three_line_format(table)
    return table
