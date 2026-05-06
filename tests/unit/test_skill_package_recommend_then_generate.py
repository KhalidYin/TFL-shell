import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / ".trae" / "skills" / "tfls-shell" / "scripts" / "recommend_then_generate.py"


def _run_script(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )


def test_recommend_then_generate_creates_project_aligned_xlsx_from_text(tmp_path):
    result = _run_script(
        "--text",
        "Phase II non-oncology study with time-to-first exacerbation endpoint and safety population.",
        "--type",
        "xlsx",
        "--output-dir",
        str(tmp_path),
        "--json",
        "--no-figures",
    )

    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["task_mode"] == "recommend_then_generate"
    assert payload["interpreted_context"]["therapeutic_area"] == "Non-Oncology"
    assert "14.2" in payload["recommendation_summary"]["sections"]
    assert payload["generation_results"]["requested_outputs"] == ["xlsx"]
    assert payload["generation_results"]["artifact_count"] == 1
    assert payload["generation_results"]["artifacts"][0]["file_name"].startswith("TFL_TOC_v")
    assert tmp_path.joinpath(payload["generation_results"]["artifacts"][0]["file_name"]).exists()


def test_recommend_then_generate_returns_schema_first_payload(tmp_path):
    result = _run_script(
        "--text",
        "Phase II non-oncology study with time-to-first exacerbation endpoint and safety population.",
        "--type",
        "xlsx",
        "--output-dir",
        str(tmp_path),
        "--json",
        "--no-figures",
    )

    assert result.returncode == 0
    payload = json.loads(result.stdout)

    assert payload["runtime_summary"]["mode"] in ("repo_backed", "standalone")
    assert payload["runtime_summary"]["catalog_source"].endswith(
        "package_assets/catalog_subset.json"
    )
    assert payload["runtime_summary"]["registry_source"].endswith(
        "package_assets/contract_registry.json"
    )
    assert payload["runtime_summary"]["wrapper_layer"] == "runtime/wrappers"
    assert payload["request_summary"]["task_mode"] == "recommend_then_generate"
    assert payload["request_summary"]["source_count"] == 1
    assert payload["ingestion_state"]["recognized_sources"][0]["source_type"] == "user_prompt"
    assert payload["extraction_state"]["study_context"]["study_phase"] == "Phase II"
    assert "section_scope" in payload["normalization_state"]["mapped_governance_fields"]
    assert isinstance(payload["ambiguity_state"]["missing_fields"], list)
    assert payload["recommendation_state"]["base_package"]["total_items"] >= 1
    assert "optimization_suggestions" in payload


def test_recommend_then_generate_includes_validation_results(tmp_path):
    result = _run_script(
        "--text",
        "Phase II non-oncology study with time-to-first exacerbation endpoint and safety population.",
        "--type",
        "xlsx",
        "--output-dir",
        str(tmp_path),
        "--json",
        "--no-figures",
    )

    assert result.returncode == 0
    payload = json.loads(result.stdout)

    assert payload["validation_results"]["catalog_validation"]["warning_count"] >= 0
    assert payload["validation_results"]["cross_output_checks"]["requested_outputs"] == ["xlsx"]
    assert payload["validation_results"]["cross_output_checks"]["artifact_count"] == 1
    assert "declared_references" in payload["validation_results"]
    assert payload["package_bundle"]["self_contained_ready"] is True
    assert payload["package_bundle"]["contract_registry"]["present"] is True
    assert payload["package_bundle"]["catalog_subset"]["present"] is True
    assert payload["package_bundle"]["output_manifest"]["present"] is True
    assert payload["package_bundle"]["minimal_runtime_requirements"]["present"] is True
    assert payload["package_bundle"]["example_requests"]["present"] is True


def test_recommend_then_generate_validates_xlsx_master_sheet_against_recommendation(tmp_path):
    result = _run_script(
        "--text",
        "Phase II non-oncology study with time-to-first exacerbation endpoint and safety population.",
        "--type",
        "xlsx",
        "--output-dir",
        str(tmp_path),
        "--json",
        "--no-figures",
    )

    assert result.returncode == 0
    payload = json.loads(result.stdout)
    workbook_checks = payload["validation_results"]["cross_output_checks"]["xlsx_master_sheet"]
    workbook_refs = payload["validation_results"]["declared_references"]["xlsx_master_sheet"]

    assert workbook_checks["present"] is True
    assert workbook_checks["ids_match_catalog"] is True
    assert workbook_checks["labels_match_catalog"] is True
    assert workbook_checks["sections_match_catalog"] is True
    assert workbook_checks["applicability_match_catalog"] is True
    assert workbook_checks["shell_families_match_catalog"] is True
    assert workbook_checks["types_match_catalog"] is True
    assert workbook_checks["study_phase_scope_match_catalog"] is True
    assert workbook_checks["coverage_summary_match_catalog"] is True
    assert workbook_checks["populations_match_catalog"] is True
    assert workbook_checks["master_row_count"] == len(
        payload["recommendation_state"]["base_package"]["shell_ids"]
    )
    assert workbook_refs["helper_module"].endswith("alignment_contracts.py")
    assert "Type" in workbook_refs["detail_keys"]
    assert "Study Phase Scope" in workbook_refs["detail_keys"]
    assert "Population" in workbook_refs["detail_keys"]
    full_workbook_checks = payload["validation_results"]["cross_output_checks"]["xlsx_workbook"]
    full_workbook_refs = payload["validation_results"]["declared_references"]["xlsx_workbook"]
    assert full_workbook_checks["sheet_names_match_contract"] is True
    assert full_workbook_checks["catalog_sheet_headers_match_contract"] is True
    assert full_workbook_checks["section_sheet_row_counts_match_catalog"] is True
    assert full_workbook_checks["usage_placeholder_contract_present"] is True
    assert "Workbook Sheets" in full_workbook_refs["detail_keys"]


def test_recommend_then_generate_validates_docx_headings_against_recommendation(tmp_path):
    result = _run_script(
        "--text",
        "Phase II non-oncology study with time-to-first exacerbation endpoint and safety population.",
        "--type",
        "docx",
        "--output-dir",
        str(tmp_path),
        "--json",
        "--no-figures",
    )

    assert result.returncode == 0
    payload = json.loads(result.stdout)
    docx_checks = payload["validation_results"]["cross_output_checks"]["docx_shell_template"]
    docx_refs = payload["validation_results"]["declared_references"]["docx_shell_template"]

    assert docx_checks["present"] is True
    assert docx_checks["heading_count_matches_catalog"] is True
    assert docx_checks["heading_labels_match_catalog"] is True
    assert docx_checks["section_headings_cover_recommendation"] is True
    assert docx_checks["display_label_lines_match_catalog"] is True
    assert docx_checks["title_lines_match_catalog"] is True
    assert docx_checks["analysis_set_lines_match_catalog"] is True
    assert docx_checks["protocol_lines_present"] is True
    assert docx_checks["sponsor_lines_present"] is True
    assert docx_checks["heading_count"] == len(
        payload["recommendation_state"]["base_package"]["shell_ids"]
    )
    assert docx_refs["helper_module"].endswith("alignment_contracts.py")
    assert "Analysis Set" in docx_refs["detail_keys"]
    assert "Protocol" in docx_refs["detail_keys"]
    assert "Sponsor" in docx_refs["detail_keys"]
    layout_checks = payload["validation_results"]["cross_output_checks"]["docx_layout"]
    layout_refs = payload["validation_results"]["declared_references"]["docx_layout"]
    assert layout_checks["section_count_matches_contract"] is True
    assert layout_checks["page_size_matches_landscape_letter"] is True
    assert layout_checks["margins_match_contract"] is True
    assert layout_checks["body_table_count_matches_table_and_listing_shells"] is True
    assert "Body Table Count" in layout_refs["detail_keys"]


def test_recommend_then_generate_validates_sop_governance_language(tmp_path):
    result = _run_script(
        "--text",
        "Phase II non-oncology study with time-to-first exacerbation endpoint and safety population.",
        "--type",
        "sop",
        "--output-dir",
        str(tmp_path),
        "--json",
        "--no-figures",
    )

    assert result.returncode == 0
    payload = json.loads(result.stdout)
    sop_checks = payload["validation_results"]["cross_output_checks"]["sop_governance_doc"]
    sop_refs = payload["validation_results"]["declared_references"]["sop_governance_doc"]

    assert sop_checks["present"] is True
    assert sop_checks["title_matches_template"] is True
    assert sop_checks["scope_matches_governed_sections"] is True
    assert sop_checks["mentions_cross_output_alignment"] is True
    assert sop_checks["mentions_quality_gates"] is True
    assert sop_checks["header_table_labels_present"] is True
    assert sop_checks["classification_confidential_present"] is True
    assert sop_checks["required_heading_structure_present"] is True
    assert sop_checks["appendix_headings_present"] is True
    assert sop_refs["helper_module"].endswith("alignment_contracts.py")
    assert "Classification" in sop_refs["detail_keys"]
    assert "Appendix A" in sop_refs["detail_keys"]
    assert "Appendix B" in sop_refs["detail_keys"]
