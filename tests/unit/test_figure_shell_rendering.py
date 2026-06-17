from docx import Document

from tflshell.data.definitions import build_catalog
from tflshell.figures.registry import generate_figure_buffer, supported_figure_types
from tflshell.generators.docx_shell import DocxShellGenerator
from tflshell.models.catalog import TFLCatalog


def test_all_catalog_figure_types_have_registry_renderer():
    catalog = build_catalog()
    figure_types = {item.figure_type for item in catalog.figures() if item.figure_type}

    assert figure_types <= supported_figure_types()


def test_representative_figure_types_generate_non_empty_png_buffers():
    catalog = build_catalog()
    representatives = {}
    for item in catalog.figures():
        representatives.setdefault(item.figure_type, item)

    assert representatives
    for item in representatives.values():
        buffer = generate_figure_buffer(item)
        assert buffer.getbuffer().nbytes > 10_000, item.id


def test_docx_shell_embeds_generated_figure_image(tmp_path):
    figure_item = build_catalog().get("F14.2.4")
    output_path = tmp_path / "figure_shell.docx"

    DocxShellGenerator(
        TFLCatalog([figure_item]),
        output_path=str(output_path),
        generate_figures=True,
    ).generate()

    doc = Document(output_path)
    paragraphs = "\n".join(paragraph.text for paragraph in doc.paragraphs)

    assert len(doc.inline_shapes) >= 1
    assert "INSERT FIGURE HERE" not in paragraphs
