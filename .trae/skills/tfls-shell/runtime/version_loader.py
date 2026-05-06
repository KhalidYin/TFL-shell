from __future__ import annotations

import json
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = PACKAGE_ROOT / "package_assets" / "output_manifest.json"


def get_version() -> str:
    if MANIFEST_PATH.exists():
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        return manifest.get("product_version", "0.0.0")
    return "0.0.0"


def get_manifest() -> dict:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
