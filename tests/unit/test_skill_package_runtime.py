import importlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SKILL_DIR = ROOT / ".trae" / "skills" / "tfls-shell"


def _import_runtime_module(module_name: str):
    if str(SKILL_DIR) not in sys.path:
        sys.path.insert(0, str(SKILL_DIR))
    return importlib.import_module(module_name)


def test_catalog_loader_reads_package_catalog_subset():
    catalog_loader = _import_runtime_module("runtime.catalog_loader")

    payload = catalog_loader.load_catalog_subset()

    assert payload["governed_sections"] == ["14.1", "14.2", "14.3", "14.4", "16.2"]
    assert payload["item_count"] >= 1
    assert len(payload["items"]) == payload["item_count"]
    assert catalog_loader.get_item("T14.1.1")["display_label"] == "Table 14.1.1"


def test_registry_loader_reads_package_contract_registry():
    registry_loader = _import_runtime_module("runtime.registry_loader")

    registry = registry_loader.load_contract_registry()

    assert "xlsx_master_sheet" in registry["contracts"]
    assert "xlsx_workbook" in registry["contracts"]
    assert "docx_layout" in registry["contracts"]
    assert registry_loader.get_contract("docx_shell_template")["helper_module"] == "scripts/alignment_contracts.py"
    assert set(registry_loader.list_contracts()) >= {
        "xlsx_master_sheet",
        "xlsx_workbook",
        "docx_shell_template",
        "docx_layout",
        "sop_governance_doc",
    }


def test_wrappers_expose_unified_generate_entrypoint():
    xlsx_wrapper = _import_runtime_module("runtime.wrappers.xlsx_wrapper")
    docx_wrapper = _import_runtime_module("runtime.wrappers.docx_wrapper")
    sop_wrapper = _import_runtime_module("runtime.wrappers.sop_wrapper")

    assert callable(xlsx_wrapper.generate)
    assert callable(docx_wrapper.generate)
    assert callable(sop_wrapper.generate)


def test_package_catalog_subset_matches_json_asset():
    payload = json.loads((SKILL_DIR / "package_assets" / "catalog_subset.json").read_text(encoding="utf-8"))

    assert payload["catalog_version"] == "product-aligned-subset-v1"
    assert payload["item_count"] == len(payload["items"])


def test_output_manifest_captures_product_output_contract():
    payload = json.loads((SKILL_DIR / "package_assets" / "output_manifest.json").read_text(encoding="utf-8"))

    assert payload["manifest_version"] == "product-aligned-output-contract-v1"
    assert payload["formal_outputs"]["xlsx_toc_workbook"]["sheet_names"] == [
        "TOC_Master",
        "14.1_Demographics",
        "14.2_Efficacy",
        "14.3_Safety",
        "14.4_Special",
        "16.2_Listings",
        "Field_Definitions",
        "Usage_Guide",
        "Change_Log",
    ]
    assert payload["formal_outputs"]["docx_shell_template"]["heading_contract"]["tfl_shell_heading_style"] == "Heading 4"
    assert payload["formal_outputs"]["sop_governance_doc"]["scope_text"] == "14.1, 14.2, 14.3, 14.4, and 16.2"
