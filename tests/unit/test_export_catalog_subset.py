import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / ".trae" / "skills" / "tfls-shell" / "scripts" / "export_catalog_subset.py"


def test_export_catalog_subset_writes_stable_structure(tmp_path):
    output_path = tmp_path / "catalog_subset.json"
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--output", str(output_path)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    payload = json.loads(output_path.read_text(encoding="utf-8"))
    assert payload["catalog_version"] == "product-aligned-subset-v1"
    assert payload["governed_sections"] == ["14.1", "14.2", "14.3", "14.4", "16.2"]
    assert payload["item_count"] == len(payload["items"])
    assert payload["item_count"] >= 1
