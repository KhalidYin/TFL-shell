"""Phase-aware recommendation tests driven by oncology/non-oncology fixtures."""

import json
from pathlib import Path

from tflshell.data.definitions import build_catalog
from tflshell.recommend import InputSource, RecommendRequest, recommend_shells

FIXTURES_DIR = Path(__file__).resolve().parents[1] / "fixtures"


def _load_fixture(name: str) -> dict:
    return json.loads((FIXTURES_DIR / name).read_text(encoding="utf-8"))


def _build_request(fixture: dict) -> RecommendRequest:
    description = fixture["description"]
    ctx = fixture["study_context"]
    return RecommendRequest(
        sources=[InputSource(content_text=description)],
        therapeutic_area_hint=ctx["therapeutic_area"].lower(),
        study_phase_hint=ctx["study_phase"].lower().replace(" ", "-"),
        include_figures=True,
        include_listings=True,
    )


def test_oncology_phase2_fixture_drives_correct_sections_and_families():
    fixture = _load_fixture("oncology_phase2.json")
    request = _build_request(fixture)
    result = recommend_shells(request)
    base = result.recommendation_state["base_package"]

    for section in fixture["expected_sections"]:
        assert section in base["sections"], f"Missing section {section}"

    for family in fixture["expected_families"]:
        assert family in base["shell_families"], f"Missing family {family}"

    assert base["total_items"] >= fixture["min_expected_shells"]

    assert result.interpreted_context["therapeutic_area"] == "Oncology"
    assert result.interpreted_context["study_phase"] == "Phase II"


def test_non_oncology_phase2_fixture_drives_correct_sections_and_families():
    fixture = _load_fixture("non_oncology_phase2.json")
    request = _build_request(fixture)
    result = recommend_shells(request)
    base = result.recommendation_state["base_package"]

    for section in fixture["expected_sections"]:
        assert section in base["sections"], f"Missing section {section}"

    for family in fixture["expected_families"]:
        assert family in base["shell_families"], f"Missing family {family}"

    assert base["total_items"] >= fixture["min_expected_shells"]

    assert result.interpreted_context["therapeutic_area"] == "Non-Oncology"
    assert result.interpreted_context["study_phase"] == "Phase II"


def test_fixtures_cover_both_therapeutic_areas():
    onc = _load_fixture("oncology_phase2.json")
    non_onc = _load_fixture("non_oncology_phase2.json")

    assert onc["study_context"]["therapeutic_area"] == "Oncology"
    assert non_onc["study_context"]["therapeutic_area"] == "Non-Oncology"
    assert onc["study_context"]["study_phase"] == "Phase II"
    assert non_onc["study_context"]["study_phase"] == "Phase II"


def test_phase_aware_recommend_excludes_figures_and_listings_when_requested():
    fixture = _load_fixture("oncology_phase2.json")
    request = RecommendRequest(
        sources=[InputSource(content_text=fixture["description"])],
        therapeutic_area_hint="oncology",
        study_phase_hint="phase-ii",
        include_figures=False,
        include_listings=False,
    )
    result = recommend_shells(request)
    catalog = build_catalog()
    base_ids = result.recommendation_state["base_package"]["shell_ids"]

    for shell_id in base_ids:
        item = catalog.get(shell_id)
        assert item is not None
        assert item.tfl_type.name != "FIGURE", f"FIGURE {shell_id} present despite include_figures=False"
        assert item.tfl_type.name != "LISTING", f"LISTING {shell_id} present despite include_listings=False"
