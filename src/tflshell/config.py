"""Configuration constants for TFLshell v2.0."""

import os

VERSION = "2.1.0"

PACKAGE_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(PACKAGE_ROOT))
DEFAULT_OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output")

DOCX_FILENAME = "TFL_Shell_Template_v2.0.docx"
XLSX_FILENAME = "TFL_TOC_v2.0.xlsx"
SOP_FILENAME = "TFL_Shell_SOP_v2.0.docx"
TOC_FILENAME = "TFL_Table_of_Contents_v2.0.docx"

SOP_DOC_NUMBER = "SOP-TFL-001"
SOP_VERSION = "2.0"

# Page setup
PAGE_WIDTH_INCHES = 11.0  # Landscape letter
PAGE_HEIGHT_INCHES = 8.5
MARGIN_INCHES = 0.75

# Fonts
FONT_NAME = "Times New Roman"
FONT_SIZE_COVER_TITLE = 24
FONT_SIZE_H1 = 14
FONT_SIZE_H2 = 12
FONT_SIZE_H3 = 11
FONT_SIZE_BODY = 10
FONT_SIZE_TABLE = 9
FONT_SIZE_FOOTNOTE = 8
FONT_SIZE_BADGE = 8
FONT_SIZE_HEADER_BLOCK = 9

# Three-line table border sizes (in eighths of a point)
THREE_LINE_THICK_SZ = 12  # ~1.5pt
THREE_LINE_THIN_SZ = 4    # ~0.5pt

# Figure settings (v2.1: reduced for landscape letter fit)
FIGURE_DPI = 150
FIGURE_DEFAULT_WIDTH = 5.5
FIGURE_DEFAULT_HEIGHT = 3.2

# Placeholders
SPONSOR_PLACEHOLDER = "[Sponsor Name]"
PROTOCOL_PLACEHOLDER = "[Protocol Number]"
STUDY_TITLE_PLACEHOLDER = "[Study Title / Compound Name]"

# Colors
HEADER_BG_HEX = "003366"
HEADER_FG_HEX = "FFFFFF"
ROW_ALT_BG_HEX = "F2F2F2"
ROW_COMPLETE_BG_HEX = "C6EFCE"
ROW_IN_PROGRESS_BG_HEX = "FCE4D6"
ROW_NA_BG_HEX = "D9D9D9"
THREE_LINE_BORDER_COLOR = "000000"
