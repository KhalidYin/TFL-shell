import re

from tflshell.data.definitions import CONTROLLED_TABLE_ABBREVIATIONS, build_catalog
from tflshell.models.enums import TFLType


def test_primary_continuous_endpoint_uses_independent_comparison_group():
    item = build_catalog().get("T14.2.1")

    assert item.layout_profile == "model-comparison"
    assert item.leaf_column_count == 5
    assert item.header_rows[0][1]["label"] == "Treatment Estimates"
    assert item.header_rows[0][2]["label"] == "Treatment Comparison"
    difference = next(
        row for row in item.shell_data_rows_rich if "LS Mean Difference" in row["label"]
    )
    assert difference["values"][:2] == ["", ""]
    assert difference["values"][2]
    assert not any("Week 24" in row["label"] for row in item.shell_data_rows_rich)
    assert any(
        "Protocol-Defined Primary Visit" in row["label"] for row in item.shell_data_rows_rich
    )


def test_metabolic_continuous_and_responder_shells_do_not_put_comparison_in_group_one():
    catalog = build_catalog()

    for item_id in ("T14.2.32", "T14.2.33"):
        item = catalog.get(item_id)
        assert item.layout_profile == "model-comparison"
        assert item.comparison_position == "Independent Treatment Comparison column group"
        assert all(len(row["values"]) == 4 for row in item.shell_data_rows_rich)

    continuous = catalog.get("T14.2.32")
    model_rows = [row for row in continuous.shell_data_rows_rich if "LS Mean" in row["label"]]
    assert model_rows
    assert all(row["values"][2] and row["values"][3] for row in model_rows)


def test_model_shells_use_protocol_defined_visit_or_target_language():
    catalog = build_catalog()
    continuous_labels = [row["label"] for row in catalog.get("T14.2.32").shell_data_rows_rich]
    responder_labels = [row["label"] for row in catalog.get("T14.2.33").shell_data_rows_rich]

    assert any("Protocol-Defined Visit" in label for label in continuous_labels)
    assert any("Protocol-Defined" in label for label in responder_labels)
    assert not any("Week 24" in label for label in continuous_labels)


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
            assert any(note.startswith("Statistical definitions:") for note in item.footnotes), (
                item.id
            )

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
        "T14.3.1.8",   # duplicate threshold PT summary
        "T14.3.1.9",   # generic AE-by-cycle summary
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
        assert any("Protocol-Defined Post-Baseline Visit" in row["label"] for row in item.shell_data_rows_rich)

    pro = catalog.get("T14.4.5")
    assert pro.layout_profile == "model-comparison"
    assert pro.header_rows[0][1]["label"] == "Treatment Estimates"
    assert pro.header_rows[0][2]["label"] == "Treatment Comparison"
    comparison = next(row for row in pro.shell_data_rows_rich if "LS Mean Difference" in row["label"])
    assert comparison["values"][:2] == ["", ""]


def test_explicit_statistic_columns_contain_statistic_labels_not_result_placeholders():
    catalog = build_catalog()
    for item_id in ("T14.3.3.2", "T14.3.4.1", "T14.4.11", "T14.4.12"):
        item = catalog.get(item_id)
        assert item.placeholder_columns[1] == "Statistic"
        populated = [
            row["values"][0]
            for row in item.shell_data_rows_rich
            if row["values"] and any(value not in ("", "...") for value in row["values"][1:])
        ]
        assert populated
        assert all(value not in {"xx", "xx.x", "xx (xx.x)", "xx.x (xx.x)"} for value in populated)
