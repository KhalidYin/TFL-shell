from tflshell.data.definitions import build_catalog
from tflshell.models.enums import Section


def test_section_14_1_is_modular_catalog_slice():
    catalog = build_catalog()
    items = catalog.by_section(Section.SEC_14_1)

    assert len(items) == 17
    assert all(item.section == Section.SEC_14_1 for item in items)


def test_demographics_table_does_not_mix_oncology_disease_characteristics():
    item = build_catalog().get("T14.1.1")
    labels = {row["label"].strip() for row in item.shell_data_rows_rich}

    assert item.title == "Summary of Demographic Characteristics"
    assert item.applicability_label == "General"
    assert "Height (cm)" in labels
    assert "ECOG Performance Status" not in labels
    assert "Disease Stage at Baseline" not in labels
    assert "Histological Type" not in labels


def test_baseline_disease_characteristics_are_marked_oncology_specific():
    item = build_catalog().get("T14.1.2")
    labels = {row["label"].strip() for row in item.shell_data_rows_rich}

    assert item.title == "Summary of Baseline Oncology Disease Characteristics"
    assert item.applicability_label == "Oncology only"
    assert "ECOG Performance Status, n (%)" in labels
    assert "Disease Stage, n (%)" in labels
