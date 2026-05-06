"""Skill package runtime layer."""

from __future__ import annotations

import sys
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]


def has_full_repo_backend() -> bool:
    """Check whether the upstream tflshell product (src/tflshell) is importable."""
    repo_root = PACKAGE_ROOT.parents[2]
    src_path = repo_root / "src"
    if not src_path.is_dir():
        return False
    try:
        if str(src_path) not in sys.path:
            sys.path.insert(0, str(src_path))
        import tflshell  # noqa: F401
        return True
    except ImportError:
        return False


def has_package_assets() -> bool:
    catalog = PACKAGE_ROOT / "package_assets" / "catalog_subset.json"
    registry = PACKAGE_ROOT / "package_assets" / "contract_registry.json"
    manifest = PACKAGE_ROOT / "package_assets" / "output_manifest.json"
    return catalog.exists() and registry.exists() and manifest.exists()


def runtime_mode() -> dict:
    return {
        "package_root": str(PACKAGE_ROOT),
        "has_package_assets": has_package_assets(),
        "has_repo_backend": has_full_repo_backend(),
        "mode": "repo_backed" if has_full_repo_backend() else "standalone",
    }
