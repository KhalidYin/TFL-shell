"""TFL ID validation, display naming, and file naming utilities."""

import re

TFL_ID_PATTERN = re.compile(r"^([TFL])(14\.[1-4]|16\.2)\.(\d+)$")


def validate_tfl_id(tfl_id: str) -> bool:
    """Check whether a TFL ID conforms to the standard format.

    Valid format: [Type][Section].[Sequence]
    - Type: T (Table), F (Figure), L (Listing)
    - Section: 14.1, 14.2, 14.3, 14.4, 16.2
    - Sequence: 1-3 digit number
    """
    return bool(TFL_ID_PATTERN.match(tfl_id))


def parse_tfl_id(tfl_id: str) -> dict[str, str] | None:
    """Parse a TFL ID into its components. Returns None if invalid."""
    m = TFL_ID_PATTERN.match(tfl_id)
    if not m:
        return None
    type_map = {"T": "Table", "F": "Figure", "L": "Listing"}
    return {
        "type": type_map[m.group(1)],
        "section": m.group(2),
        "sequence": int(m.group(3)),
    }


def display_number_from_id(tfl_id: str) -> str:
    """Return the reviewer-facing number without the leading type letter."""
    parsed = parse_tfl_id(tfl_id)
    return f"{parsed['section']}.{parsed['sequence']}" if parsed else tfl_id


def display_label_from_id(tfl_id: str) -> str:
    """Return the reviewer-facing TFL label, e.g. 'Table 14.2.11'."""
    parsed = parse_tfl_id(tfl_id)
    if not parsed:
        return tfl_id
    return f"{parsed['type']} {parsed['section']}.{parsed['sequence']}"


def make_filename(base: str, version: str, extension: str) -> str:
    """Generate a versioned filename.

    Example: make_filename('TFL_Shell_Template', '1.0', '.docx')
      -> 'TFL_Shell_Template_v1.0.docx'
    """
    return f"{base}_v{version}{extension}"
