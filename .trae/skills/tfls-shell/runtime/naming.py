from __future__ import annotations

from pathlib import Path

from runtime.version_loader import get_version


def make_filename(prefix: str, version: str, extension: str) -> str:
    ext = extension or ""
    if ext and not ext.startswith("."):
        ext = f".{ext}"
    return f"{prefix}_v{version}{ext}"


def parse_version_from_path(file_path: str | Path) -> str | None:
    import re

    name = Path(file_path).name
    match = re.search(r"v(\d+\.\d+\.\d+)", name)
    return match.group(1) if match else None
