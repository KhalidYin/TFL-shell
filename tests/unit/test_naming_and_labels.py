from tflshell.data.definitions import build_catalog
from tflshell.utils.naming import display_label_from_id, display_number_from_id, make_filename


def test_display_label_derivation_matches_catalog_items():
    catalog = build_catalog()

    for item in catalog.all():
        assert item.display_label == display_label_from_id(item.id)
        assert item.display_number == display_number_from_id(item.id)


def test_generated_filename_uses_version_prefix():
    assert make_filename("TFL_Shell_Template", "2.1.0", ".docx") == "TFL_Shell_Template_v2.1.0.docx"


def test_governed_arm_labels_use_normalized_terms():
    catalog = build_catalog()
    forbidden_tokens = (
        "XXX Group 1",
        "XXX Group 2",
        "Treatment A",
        "Treatment B",
        "Group1",
        "Group2",
        "G1",
        "G2",
        "Gx",
    )

    for item in catalog.all():
        for header in item.placeholder_columns:
            assert not any(token in header for token in forbidden_tokens), (item.id, header)
