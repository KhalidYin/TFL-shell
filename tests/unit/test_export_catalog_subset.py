import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "Skill" / "tfls-shell" / "scripts" / "export_catalog_subset.py"
CONTRACT_SCRIPT = (
    ROOT / "Skill" / "tfls-shell" / "scripts" / "export_product_contracts.py"
)


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


def test_export_product_contracts_writes_manifest_and_registry(tmp_path):
    manifest_path = tmp_path / "output_manifest.json"
    registry_path = tmp_path / "contract_registry.json"
    result = subprocess.run(
        [
            sys.executable,
            str(CONTRACT_SCRIPT),
            "--manifest-output",
            str(manifest_path),
            "--registry-output",
            str(registry_path),
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    assert manifest["manifest_version"] == "product-aligned-output-contract-v1"
    assert manifest["formal_outputs"]["xlsx_toc_workbook"]["sheet_names"][0] == "TOC_Master"
    assert (
        manifest["formal_outputs"]["docx_shell_template"]["body_contract"][
            "table_and_listing_body_table_count"
        ]
        >= 1
    )
    assert registry["registry_version"] == "1.1.0"
    assert "xlsx_workbook" in registry["contracts"]
    assert "docx_layout" in registry["contracts"]
