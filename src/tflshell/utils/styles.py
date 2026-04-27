"""python-docx style utilities for TFL shell documents."""

from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from tflshell import config


def set_default_font(doc, font_name=None, font_size=None):
    """Set default document font."""
    style = doc.styles["Normal"]
    style.font.name = font_name or config.FONT_NAME
    style.font.size = Pt(font_size or config.FONT_SIZE_BODY)


def setup_all_styles(doc):
    """Register all custom styles for the TFL shell document."""
    F = config.FONT_NAME

    set_default_font(doc, F, config.FONT_SIZE_BODY)

    # Ensure Heading 1-3 are properly styled for TOC collection
    _setup_heading_style(doc, "Heading 1", config.FONT_SIZE_H1, config.HEADER_BG_HEX)
    _setup_heading_style(doc, "Heading 2", config.FONT_SIZE_H2, "1F4E79")
    _setup_heading_style(doc, "Heading 3", config.FONT_SIZE_H3, "2E75B6")


def _setup_heading_style(doc, style_name, size, color_hex):
    """Configure a heading style for TOC collection."""
    try:
        style = doc.styles[style_name]
    except KeyError:
        import docx.enum.style
        style = doc.styles.add_style(style_name, docx.enum.style.WD_STYLE_TYPE.PARAGRAPH)
    style.font.name = config.FONT_NAME
    style.font.size = Pt(size)
    style.font.bold = True
    style.font.color.rgb = RGBColor.from_string(color_hex)
    style.paragraph_format.space_before = Pt(12)
    style.paragraph_format.space_after = Pt(6)
    style.paragraph_format.keep_with_next = True


def add_style_run(paragraph, text, font_name=None, font_size=None,
                  bold=False, italic=False, color_hex=None):
    """Add a formatted run to a paragraph."""
    run = paragraph.add_run(text)
    run.font.name = font_name or config.FONT_NAME
    run.font.size = Pt(font_size or config.FONT_SIZE_BODY)
    run.font.bold = bold
    run.font.italic = italic
    if color_hex:
        run.font.color.rgb = RGBColor.from_string(color_hex)
    return run
