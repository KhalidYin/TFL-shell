from __future__ import annotations

import sys
from pathlib import Path


def _bootstrap_repo_imports() -> None:
    repo_root = Path(__file__).resolve().parents[5]
    src_path = repo_root / "src"
    if str(src_path) not in sys.path:
        sys.path.insert(0, str(src_path))


_bootstrap_repo_imports()

from tflshell.generators.xlsx_toc import XlsxTocGenerator  # noqa: E402


def generate(catalog, output_path: str, **kwargs) -> str:
    generator = XlsxTocGenerator(catalog, output_path=output_path)
    return str(generator.generate())
