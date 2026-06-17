import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "Skill" / "tfls-shell" / "scripts" / "validate_outputs.py"


def test_validate_outputs_accepts_current_product_outputs():
    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--docx",
            str(ROOT / "output" / "TFL_Shell_Template_v2.1.0.docx"),
            "--xlsx",
            str(ROOT / "output" / "TFL_TOC_v2.1.0.xlsx"),
            "--sop",
            str(ROOT / "output" / "TFL_Shell_SOP_v2.1.0.docx"),
            "--json",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["passed"] is True
    assert payload["cross_output_checks"]["xlsx_workbook"]["sheet_names_match_contract"] is True
    assert (
        payload["cross_output_checks"]["docx_layout"][
            "body_table_count_matches_table_and_listing_shells"
        ]
        is True
    )
    assert (
        payload["cross_output_checks"]["sop_governance_doc"]["classification_confidential_present"]
        is True
    )
    assert "xlsx_workbook" in payload["declared_references"]
    assert "docx_layout" in payload["declared_references"]
