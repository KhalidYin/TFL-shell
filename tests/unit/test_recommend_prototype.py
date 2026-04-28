import json

from tflshell.main import main
from tflshell.recommend import InputSource, RecommendRequest, recommend_shells


def test_recommend_defaults_to_core_sections_when_context_is_sparse():
    request = RecommendRequest(
        sources=[InputSource(content_text="Need a governed shell recommendation for CSR review.")],
        include_figures=False,
    )

    result = recommend_shells(request)

    assert result.task_mode == "recommend"
    assert result.recommendation_state["base_package"]["sections"] == ["14.1", "14.3", "16.2"]
    assert "study_phase" in result.ambiguity_state["missing_fields"]
    assert "therapeutic_area" in result.ambiguity_state["missing_fields"]
    assert result.interpreted_context["therapeutic_area"] == "Unknown"


def test_recommend_detects_non_oncology_efficacy_and_special_signals():
    request = RecommendRequest(
        sources=[
            InputSource(
                source_type="sap",
                content_text=(
                    "Phase II non-oncology study with time-to-first exacerbation as the primary endpoint. "
                    "PK, biomarker, safety population, and responder analyses are included."
                ),
            )
        ],
        include_figures=False,
    )

    result = recommend_shells(request)
    base_package = result.recommendation_state["base_package"]

    assert result.interpreted_context["study_phase"] == "Phase II"
    assert result.interpreted_context["therapeutic_area"] == "Non-Oncology"
    assert "14.2" in base_package["sections"]
    assert "14.4" in base_package["sections"]
    assert "Respiratory Exacerbation" in base_package["shell_families"]
    assert "Special Assessments" in base_package["shell_families"]
    assert "Safety Population" in result.interpreted_context["analysis_populations"]


def test_recommend_cli_supports_json_output(capsys):
    exit_code = main(
        [
            "recommend",
            "--text",
            "Phase II non-oncology responder study with cardiovascular event monitoring.",
            "--json",
            "--no-figures",
        ]
    )

    captured = capsys.readouterr()
    payload = json.loads(captured.out)

    assert exit_code == 0
    assert payload["task_mode"] == "recommend"
    assert payload["interpreted_context"]["therapeutic_area"] == "Non-Oncology"
    assert "14.2" in payload["recommendation_state"]["base_package"]["sections"]
