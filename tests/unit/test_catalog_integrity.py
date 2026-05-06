import json
from pathlib import Path

from tflshell.data.definitions import build_catalog


def test_catalog_validate_has_no_warnings():
    catalog = build_catalog()

    assert catalog.validate() == []


def test_catalog_summary_counts_match_total():
    catalog = build_catalog()
    stats = catalog.summary_stats()

    assert stats["total"] == len(catalog.all())
    assert stats["tables"] + stats["figures"] + stats["listings"] == stats["total"]
    assert stats["oncology_only"] + stats["non_oncology_only"] + stats["general"] == stats["total"]


def test_all_items_have_governance_metadata_labels():
    catalog = build_catalog()

    for item in catalog.all():
        assert item.shell_family_label
        assert item.study_phase_scope_label
        assert item.coverage_summary_label


def test_phase_i_and_non_oncology_content_gaps_are_now_represented():
    catalog = build_catalog()
    item_ids = {item.id for item in catalog.all()}

    assert "T14.3.4.17" in item_ids
    assert "T14.3.4.18" in item_ids
    assert "T14.4.15" in item_ids
    assert "T14.4.16" in item_ids
    assert "T14.2.23" in item_ids
    assert "T14.2.24" in item_ids
    assert "T14.2.25" in item_ids
    assert "L16.2.32" in item_ids
    assert "L16.2.33" in item_ids
    assert "L16.2.34" in item_ids


def test_non_oncology_shells_have_explicit_applicability():
    catalog = build_catalog()
    non_oncology_items = [item for item in catalog.all() if item.non_oncology_only]

    assert len(non_oncology_items) >= 18
    assert all(item.applicability_label == "Non-Oncology only" for item in non_oncology_items)


def test_non_oncology_family_expansion_is_present():
    catalog = build_catalog()
    family_names = {item.shell_family_label for item in catalog.all() if item.non_oncology_only}

    assert "Respiratory Exacerbation" in family_names
    assert "Cardiovascular MACE and HF Hospitalization" in family_names
    assert "Autoimmune Flare and Responder" in family_names


def test_removed_redundant_subgroup_tables_are_not_in_catalog():
    catalog = build_catalog()
    item_ids = {item.id for item in catalog.all()}

    assert "T14.2.3" not in item_ids
    assert "T14.2.17" not in item_ids
    assert "T14.2.18" not in item_ids
    assert "T14.3.1.11" not in item_ids
    assert "T14.3.1.12" not in item_ids


def test_no_table_uses_forbidden_ellipsis_header_pattern_or_mismatched_value_counts():
    catalog = build_catalog()

    for item in catalog.all():
        if item.placeholder_columns:
            assert all("...\n...\n" not in col for col in item.placeholder_columns)

        if item.tfl_type.name != "TABLE":
            continue

        expected_value_count = max(len(item.placeholder_columns) - 1, 0)
        for row in item.shell_data_rows_rich:
            assert len(row["values"]) == expected_value_count, item.id


def test_landmark_table_retains_separate_expansion_and_hr_columns():
    catalog = build_catalog()
    item = catalog.get("T14.2.20")

    assert item is not None
    assert item.placeholder_columns[0] == "PFS Status at 6M"
    assert item.placeholder_columns[1].startswith("Group 1")
    assert "n/N" in item.placeholder_columns[1]
    assert "Med OS" in item.placeholder_columns[1]
    assert item.placeholder_columns[2].startswith("Group 2")
    assert "n/N" in item.placeholder_columns[2]
    assert "Med OS" in item.placeholder_columns[2]
    assert item.placeholder_columns[3] == "..."
    assert item.placeholder_columns[4] == "HR [95% CI]"


def test_representative_source_listing_mappings_are_specific():
    catalog = build_catalog()

    assert catalog.get("T14.2.9").source_listing == "L16.2.10"
    assert catalog.get("T14.2.15").source_listing == "L16.2.11"
    assert catalog.get("T14.2.20").source_listing == "L16.2.11"
    assert catalog.get("T14.2.21").source_listing == "L16.2.19"
    assert catalog.get("T14.3.4.17").source_listing == "L16.2.32"
    assert catalog.get("T14.4.15").source_listing == "L16.2.33"


def test_catalog_consistency_with_output_manifest():
    catalog = build_catalog()
    stats = catalog.summary_stats()
    section_summary = catalog.section_summary()

    manifest_path = (
        Path(__file__).parent.parent.parent
        / ".trae"
        / "skills"
        / "tfls-shell"
        / "package_assets"
        / "output_manifest.json"
    )
    assert manifest_path.exists(), f"Manifest not found at {manifest_path}"

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    catalog_entry = manifest["catalog_summary"]

    assert catalog_entry["total"] == stats["total"], (
        f"Manifest total ({catalog_entry['total']}) != catalog total ({stats['total']})"
    )

    assert catalog_entry["tables"] == stats["tables"], (
        f"Manifest tables ({catalog_entry['tables']}) != catalog tables ({stats['tables']})"
    )

    assert catalog_entry["figures"] == stats["figures"], (
        f"Manifest figures ({catalog_entry['figures']}) != catalog figures ({stats['figures']})"
    )

    assert catalog_entry["listings"] == stats["listings"], (
        f"Manifest listings ({catalog_entry['listings']}) != catalog listings ({stats['listings']})"
    )

    assert catalog_entry["oncology_only"] == stats["oncology_only"], (
        f"Manifest oncology_only ({catalog_entry['oncology_only']}) "
        f"!= catalog ({stats['oncology_only']})"
    )

    assert catalog_entry["non_oncology_only"] == stats["non_oncology_only"], (
        f"Manifest non_oncology_only ({catalog_entry['non_oncology_only']}) "
        f"!= catalog ({stats['non_oncology_only']})"
    )

    assert catalog_entry["general"] == stats["general"], (
        f"Manifest general ({catalog_entry['general']}) != catalog general ({stats['general']})"
    )

    manifest_sections = manifest["section_summary"]
    for sec_num, counts in section_summary.items():
        manifest_sec = manifest_sections.get(sec_num)
        assert manifest_sec is not None, f"Section {sec_num} missing from manifest"
        assert manifest_sec["total"] == counts["total"], (
            f"Section {sec_num}: manifest total {manifest_sec['total']} != catalog {counts['total']}"
        )
        assert manifest_sec["tables"] == counts["tables"], (
            f"Section {sec_num}: manifest tables {manifest_sec['tables']} != catalog {counts['tables']}"
        )

    governed_sections = manifest.get("governed_sections", [])
    expected_sections = ["14.1", "14.2", "14.3", "14.4", "16.2"]
    assert governed_sections == expected_sections, (
        f"Manifest governed_sections ({governed_sections}) != expected ({expected_sections})"
    )

    docx_heading_count = manifest["formal_outputs"]["docx_shell_template"]["heading_contract"][
        "tfl_shell_heading_count"
    ]
    assert docx_heading_count == stats["total"], (
        f"DOCX heading count ({docx_heading_count}) != catalog total ({stats['total']})"
    )
