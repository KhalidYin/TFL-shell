from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_catalog_sections_are_split_from_definitions_module():
    definitions_text = (ROOT / "src" / "tflshell" / "data" / "definitions.py").read_text(
        encoding="utf-8"
    )
    sections_dir = ROOT / "src" / "tflshell" / "data" / "sections"

    for module_name, builder_name in {
        "section_14_1.py": "build_14_1_items",
        "section_14_2.py": "build_14_2_items",
        "section_14_3.py": "build_14_3_items",
        "section_14_4.py": "build_14_4_items",
        "section_16_2.py": "build_16_2_items",
    }.items():
        module_path = sections_dir / module_name
        assert module_path.exists()
        assert builder_name in module_path.read_text(encoding="utf-8")
        assert f"items.extend({builder_name}())" in definitions_text

    assert definitions_text.count("TFLItem(") == 0
