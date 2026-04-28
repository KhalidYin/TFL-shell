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
