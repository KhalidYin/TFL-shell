"""Three-line table (三线表) format for python-docx tables v2.1.

Supports:
  - Multi-line column headers (split on \n, auto-break on / and (N=xx))
  - Shell rows using first-column structure plus XX placeholders
  - First column left-aligned, data columns consistent
  - NO vertical gridlines, NO internal horizontal gridlines
"""

from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from tflshell import config
from tflshell.docx_utils.xml_helpers import (
    set_table_borders, set_cell_bottom_border, set_cell_text,
)


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
    """Split a column header into multiple lines for readability.

    Rules:
      - Explicit \n splits first
      - 'Statistic / Category' → 'Statistic /\nCategory' (break after /)
      - 'Treatment A (N=xx)' → 'Treatment A\n(N=xx)' (break before N=)
      - 'n (%)' keeps as-is when short enough
    """
    if "\n" in text:
        return text.split("\n")

    # Break on ' / ' pattern: put category on new line
    if " / " in text and len(text) > 18:
        parts = text.split(" / ", 1)
        return [parts[0] + " /", parts[1]]

    # Break before (N=xx) pattern for treatment columns
    if "(N=" in text and len(text) > 12:
        idx = text.index("(N=")
        if idx > 0:
            return [text[:idx].strip(), text[idx:].strip()]

    return [text]


def _format_header_cell(cell, header_text: str, is_first_col: bool = False):
    """Set multi-line header text in a cell, left-aligned for all shell columns."""
    lines = _split_header_text(header_text)
    alignment = WD_ALIGN_PARAGRAPH.LEFT

    # Clear existing
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
        # Multi-line: each line in its own paragraph
        first = True
        for i, line in enumerate(lines):
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


def create_three_line_table(doc, rows, cols, headers, data_rows=None,
                            font_size=None, font_name=None):
    font_size = font_size or config.FONT_SIZE_TABLE
    font_name = font_name or config.FONT_NAME

    table = doc.add_table(rows=rows, cols=cols)
    table.autofit = True

    # Header row with multi-line support
    for col_idx, header_text in enumerate(headers):
        cell = table.rows[0].cells[col_idx]
        _format_header_cell(cell, header_text, is_first_col=(col_idx == 0))

    # Data rows: use shell rows if provided, else fill with XX placeholders
    for row_idx in range(1, rows):
        for col_idx in range(cols):
            cell = table.rows[row_idx].cells[col_idx]
            if data_rows and row_idx - 1 < len(data_rows):
                row_data = data_rows[row_idx - 1]
                val = row_data[col_idx] if col_idx < len(row_data) else "XX"
            else:
                val = "XX"
            set_cell_text(cell, val, bold=False,
                          font_size=font_size, font_name=font_name,
                          alignment=WD_ALIGN_PARAGRAPH.LEFT)

    apply_three_line_format(table)
    return table
