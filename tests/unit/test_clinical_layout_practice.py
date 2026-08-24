import re

from tflshell.data.definitions import CONTROLLED_TABLE_ABBREVIATIONS, build_catalog
from tflshell.models.enums import TFLType


def test_primary_continuous_endpoint_uses_treatment_rows_and_inline_reference_comparison():
    item = build_catalog().get("T14.2.1")

    assert item.layout_profile == "treatment-row"
    assert item.leaf_column_count == 8
    assert item.header_rows[0][2]["label"] == "Baseline\nMean (SD)"
    assert item.header_rows[0][4]["label"] == "Within-Group Difference"
    assert item.header_rows[0][5]["label"] == "Between-Group Difference"
    group_1 = next(row for row in item.shell_data_rows_rich if row["label"] == "Group 1")
    group_2 = next(row for row in item.shell_data_rows_rich if row["label"] == "Group 2")
    assert group_1["values"][5:] == ["Reference", "—"]
    assert group_2["values"][5] == "xx.x (xx.x)"
    assert "p=" in group_2["values"][6]
    assert not any("Week 24" in row["label"] for row in item.shell_data_rows_rich)
    assert any(
        "Protocol-Defined Primary Visit" in row["label"] for row in item.shell_data_rows_rich
    )


def test_metabolic_continuous_shell_uses_visit_parameter_and_treatment_hierarchy():
    catalog = build_catalog()
    continuous = catalog.get("T14.2.32")

    assert continuous.layout_profile == "treatment-row"
    assert continuous.comparison_position == "Comparison shown on each non-reference treatment row"
    assert continuous.shell_data_rows_rich[0]["label"] == "Protocol-Defined Visit"
    assert continuous.shell_data_rows_rich[1]["label"] == "HbA1c (%)"
    assert continuous.shell_data_rows_rich[2]["indent_level"] == 2
    group_2_rows = [row for row in continuous.shell_data_rows_rich if row["label"] == "Group 2"]
    assert group_2_rows
    assert all(row["values"][5] and row["values"][6] for row in group_2_rows)

    responder = catalog.get("T14.2.33")
    assert responder.layout_profile == "model-comparison"
    assert responder.comparison_position == "Independent Treatment Comparison column group"


def test_model_shells_use_protocol_defined_visit_or_target_language():
    catalog = build_catalog()
    continuous_labels = [row["label"] for row in catalog.get("T14.2.32").shell_data_rows_rich]
    responder_labels = [row["label"] for row in catalog.get("T14.2.33").shell_data_rows_rich]

    assert any("Protocol-Defined Visit" in label for label in continuous_labels)
    assert any("Protocol-Defined" in label for label in responder_labels)
    assert not any("Week 24" in label for label in continuous_labels)


def test_continuous_sensitivity_and_ni_comparisons_stay_on_non_reference_rows():
    catalog = build_catalog()

    sensitivity = catalog.get("T14.2.4")
    assert sensitivity.layout_profile == "treatment-row"
    assert sensitivity.header_rows[0][3]["label"] == "Within-Group Difference"
    assert sensitivity.header_rows[0][4]["label"] == "Between-Group Difference"
    sensitivity_group_2 = next(
        row for row in sensitivity.shell_data_rows_rich if row["label"] == "Group 2"
    )
    assert sensitivity_group_2["values"][4] == "xx.x (xx.x)"

    ni = catalog.get("T14.2.5")
    test_group = next(row for row in ni.shell_data_rows_rich if row["label"] == "Group 1 (Test)")
    control = next(row for row in ni.shell_data_rows_rich if row["label"] == "Group 2")
    assert test_group["values"][4] == "xx.x (xx.x)"
    assert control["values"][4:6] == ["Reference", "—"]
    assert not any("Difference vs." in row["label"] for row in ni.shell_data_rows_rich)


def test_subject_detail_content_is_not_presented_as_a_summary_table():
    catalog = build_catalog()

    for item_id in ("T14.3.2.2", "T14.3.2.4", "T14.3.2.5", "T14.3.3.4"):
        item = catalog.get(item_id)
        assert "Subject" not in item.placeholder_columns
        assert not any("Narrative ID" in column for column in item.placeholder_columns)
        assert all(len(row["values"]) == 4 for row in item.shell_data_rows_rich)


def test_pk_period_comparisons_use_grouped_headers():
    catalog = build_catalog()

    for item_id in ("T14.4.15", "T14.4.16"):
        item = catalog.get(item_id)
        assert item.layout_profile == "model-comparison"
        assert item.header_rows[0][1]["label"] == "Treatment Estimates"
        assert "Comparison" in item.header_rows[0][2]["label"]


def test_wide_listing_declares_sort_order_and_structural_example():
    item = build_catalog().get("L16.2.38")

    assert item.layout_profile == "listing-wide"
    assert "visit sequence" in item.sorting_note
    assert item.shell_data_rows[0][0] == "xxx"
    assert "rows omitted" not in item.shell_data_rows[0][0]


def test_medication_tables_use_atc_structural_headers():
    catalog = build_catalog()

    assert catalog.get("T14.1.4").placeholder_columns[0] == "ATC Level 3\nPreferred Name"
    assert catalog.get("T14.1.9").placeholder_columns[0] == "ATC Level 2\nPreferred Name"
    assert catalog.get("T14.1.16").placeholder_columns[0] == "ATC Level 3\nPreferred Name"


def test_listings_do_not_show_a_source_listing_reference():
    listings = [item for item in build_catalog().all() if item.tfl_type == TFLType.LISTING]

    assert listings
    assert all(item.source_listing == "" for item in listings)
    assert all(
        not any(note.startswith("Source Listing:") for note in item.footnote_text())
        for item in listings
    )


def test_tables_with_controlled_abbreviations_explain_them_in_footnotes():
    for item in build_catalog().tables():
        abbreviation_notes = [note for note in item.footnotes if note.startswith("Abbreviations:")]
        if abbreviation_notes:
            assert " = " in abbreviation_notes[-1], item.id

        source_text = " ".join(
            (
                item.title,
                item.population,
                *item.placeholder_columns,
                *[row["label"] for row in item.shell_data_rows_rich],
                *[
                    note
                    for note in item.footnotes
                    if not note.startswith(("Abbreviations:", "Statistical definitions:"))
                ],
            )
        )
        explained_text = " ".join(abbreviation_notes)
        for pattern, label, _meaning in CONTROLLED_TABLE_ABBREVIATIONS:
            if re.search(pattern, source_text):
                assert f"{label} =" in explained_text, f"{item.id}: {label}"

    representatives = {
        "T14.1.4": ("ATC =",),
        "T14.2.1": ("LS =", "SE =", "CI ="),
        "T14.3.1.3": ("TEAE =", "SOC =", "CTCAE ="),
        "T14.3.3.22": ("CD3 =", "CD16 =", "CD56 ="),
        "T14.3.3.23": ("IL-6 =", "TNF-alpha =", "IFN-gamma ="),
        "T14.4.15": ("PK =", "GMR =", "AUC ="),
    }
    catalog = build_catalog()
    for item_id, expected_terms in representatives.items():
        note_text = " ".join(catalog.get(item_id).footnotes)
        assert all(term in note_text for term in expected_terms), item_id


def test_statistical_displays_have_context_specific_definitions():
    catalog = build_catalog()

    for item in catalog.tables():
        visible_text = " ".join(
            (
                item.title,
                *item.placeholder_columns,
                *[row["label"] for row in item.shell_data_rows_rich],
            )
        )
        if re.search(r"\bn\s*(?:/\s*N\d*)?\s*\(%\)", visible_text):
            assert any(
                note.startswith("Statistical definitions:") for note in item.footnotes
            ), item.id

    assert any(
        note.startswith("Statistical definitions:") for note in catalog.get("T14.2.1").footnotes
    )
    assert "model, covariate, missing-data, and multiplicity" in " ".join(
        catalog.get("T14.2.1").footnotes
    )
    assert "Time origin, event definitions, and censoring rules" in " ".join(
        catalog.get("T14.2.14").footnotes
    )
    assert "Percentages use" in " ".join(catalog.get("T14.3.1.1").footnotes)
    assert "n/N denotes" in " ".join(catalog.get("T14.2.20").footnotes)
    assert "Percentages use" not in " ".join(catalog.get("T14.2.20").footnotes)


def test_ae_grade_is_a_row_hierarchy_not_a_result_column():
    catalog = build_catalog()

    for item in catalog.tables():
        if not item.id.startswith("T14.3.1."):
            continue
        assert all("Grade" not in column for column in item.placeholder_columns[1:]), item.id

    grade_table = catalog.get("T14.3.1.3")
    assert any("Grade" in row["label"] for row in grade_table.shell_data_rows_rich)
    assert len(grade_table.placeholder_columns) == 5


def test_redundant_or_nonstandard_ae_tables_are_retired():
    catalog_ids = {item.id for item in build_catalog().all()}
    retired = {
        "T14.3.1.8",  # duplicate threshold PT summary
        "T14.3.1.9",  # generic AE-by-cycle summary
        "T14.3.1.16",  # duplicate SOC/grade summary
        "T14.3.1.17",  # duplicate full SOC/PT frequency table
        "T14.3.1.18",  # nonstandard relationship-by-grade layout
        "T14.3.1.21",  # group-specific duplicate grade table
        "T14.3.1.22",  # generic AE-by-cycle detail
        "T14.3.1.29",  # group-specific SAE criterion cross-tab
        "T14.3.1.30",  # non-comparable recurrent-event layout
    }

    assert retired.isdisjoint(catalog_ids)


def test_dictionary_versions_appear_once_per_table():
    for item in build_catalog().tables():
        notes = item.footnote_text()
        assert not any(note.startswith("Coding dictionary versions:") for note in notes)
        for name, version in item.dictionary_versions.items():
            matching_notes = [note for note in notes if name in note and version in note]
            assert len(matching_notes) == 1, f"{item.id}: {name} {version}"


def test_by_visit_endpoint_layouts_put_visit_first_and_separate_comparisons():
    catalog = build_catalog()

    for item_id in ("T14.4.4", "T14.4.5", "T14.4.6"):
        item = catalog.get(item_id)
        assert item.placeholder_columns[0].startswith("Visit /"), item_id
        assert item.shell_data_rows_rich[0]["label"] == "Baseline", item_id
        assert any(
            "Protocol-Defined Post-Baseline Visit" in row["label"]
            for row in item.shell_data_rows_rich
        )

    pro = catalog.get("T14.4.5")
    assert pro.layout_profile == "model-comparison"
    assert pro.header_rows[0][1]["label"] == "Treatment Estimates"
    assert pro.header_rows[0][2]["label"] == "Treatment Comparison"
    comparison = next(
        row for row in pro.shell_data_rows_rich if "LS Mean Difference" in row["label"]
    )
    assert comparison["values"][:2] == ["", ""]


def test_summary_statistic_fields_render_as_hierarchical_rows_not_separate_columns():
    catalog = build_catalog()
    for item_id in ("T14.3.3.2", "T14.3.3.19", "T14.3.4.1", "T14.4.11", "T14.4.12"):
        item = catalog.get(item_id)
        assert item.layout_profile == "hierarchical-summary"
        assert not any(
            column.replace("\n", " ").strip() == "Statistic"
            for column in item.placeholder_columns[1:]
        )
        assert item.placeholder_columns[0].endswith("Statistic")
        statistic_rows = [
            row
            for row in item.shell_data_rows_rich
            if row["label"] == "n"
            or row["label"].startswith(("Mean (SD)", "Geo Mean (CV%)", "Fold Chg from BL"))
        ]
        assert statistic_rows, item_id
        assert all(row["indent_level"] >= 1 for row in statistic_rows)

    hematology = catalog.get("T14.3.3.2")
    labels = [row["label"] for row in hematology.shell_data_rows_rich]
    assert labels.count("Baseline") == 2  # one per displayed parameter, not one per statistic
    assert any(row["indent_level"] == 2 for row in hematology.shell_data_rows_rich)
