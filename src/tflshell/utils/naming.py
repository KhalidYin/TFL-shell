"""TFL ID validation, display naming, and file naming utilities.

Supports two ID formats:
  - Flat: [Type][Section].[Sequence]     e.g. T14.1.1, F14.2.3, L16.2.5
  - Sub-numbered: [Type][Section].[Sub].[Seq]  e.g. T14.3.1.1 (for 14.3 only)
"""

import re

TFL_ID_PATTERN = re.compile(r"^([TFL])(14\.[1-4]|16\.2)\.(\d+)(?:\.(\d+))?$")


def validate_tfl_id(tfl_id: str) -> bool:
    return bool(TFL_ID_PATTERN.match(tfl_id))


def parse_tfl_id(tfl_id: str) -> dict[str, str] | None:
    m = TFL_ID_PATTERN.match(tfl_id)
    if not m:
        return None
    type_map = {"T": "Table", "F": "Figure", "L": "Listing"}
    result = {
        "type": type_map[m.group(1)],
        "section": m.group(2),
        "sequence": int(m.group(3)),
    }
    if m.group(4):
        result["sub"] = int(m.group(3))
        result["sequence"] = int(m.group(4))
    return result


def display_number_from_id(tfl_id: str) -> str:
    parsed = parse_tfl_id(tfl_id)
    if not parsed:
        return tfl_id
    if "sub" in parsed:
        return f"{parsed['section']}.{parsed['sub']}.{parsed['sequence']}"
    return f"{parsed['section']}.{parsed['sequence']}"


def display_label_from_id(tfl_id: str) -> str:
    parsed = parse_tfl_id(tfl_id)
    if not parsed:
        return tfl_id
    if "sub" in parsed:
        return f"{parsed['type']} {parsed['section']}.{parsed['sub']}.{parsed['sequence']}"
    return f"{parsed['type']} {parsed['section']}.{parsed['sequence']}"


def make_filename(base: str, version: str, extension: str) -> str:
    return f"{base}_v{version}{extension}"
