"""Figure registry and mock-data dispatch for shell rendering."""

import io

import numpy as np

from tflshell.figures.base import _generate_mock_subgroup_data
from tflshell.figures.box_plot import BoxPlotFigure
from tflshell.figures.cdf import CDFFigure
from tflshell.figures.concentration_qtc import ConcentrationQTcFigure
from tflshell.figures.edish import EDISHFigure
from tflshell.figures.forest import ForestFigure
from tflshell.figures.heatmap import LabToxicityHeatmapFigure
from tflshell.figures.km_curve import KMCurveFigure
from tflshell.figures.longitudinal import LongitudinalFigure
from tflshell.figures.pk_profile import PKProfileFigure
from tflshell.figures.spider import SpiderFigure
from tflshell.figures.swimmer import SwimmerFigure
from tflshell.figures.waterfall import WaterfallFigure

FIGURE_CLASS_MAP = {
    "km_curve": KMCurveFigure,
    "waterfall": WaterfallFigure,
    "spider": SpiderFigure,
    "swimmer": SwimmerFigure,
    "forest": ForestFigure,
    "box_plot": BoxPlotFigure,
    "longitudinal": LongitudinalFigure,
    "cdf": CDFFigure,
    "edish": EDISHFigure,
    "lab_toxicity_heatmap": LabToxicityHeatmapFigure,
    "concentration_qtc": ConcentrationQTcFigure,
    "pk_profile": PKProfileFigure,
    "food_effect_profile": PKProfileFigure,
}


def generate_figure_buffer(tfl_item, mock_data: dict | None = None) -> io.BytesIO:
    """Generate a PNG buffer for a TFL figure item."""
    figure_class = FIGURE_CLASS_MAP.get(tfl_item.figure_type)
    if figure_class is None:
        raise ValueError(
            f"Unknown figure_type '{tfl_item.figure_type}' for {tfl_item.id}. "
            f"Valid types: {list(FIGURE_CLASS_MAP.keys())}"
        )

    if mock_data is None:
        mock_data = build_mock_figure_data(tfl_item.figure_type)

    figure = figure_class(
        figsize=(tfl_item.figure_width_inches, tfl_item.figure_height_inches),
        dpi=200,
    )
    return figure.render(mock_data)


def build_mock_figure_data(figure_type: str) -> dict:
    """Build deterministic shell-only mock data for supported clinical figure types."""
    rng = np.random.default_rng(42)
    n = 200

    if figure_type == "km_curve":
        time_a = rng.weibull(1.3, n) * 10
        time_b = rng.weibull(1.6, n) * 12
        event_a = rng.binomial(1, 0.7, n).astype(bool)
        event_b = rng.binomial(1, 0.6, n).astype(bool)
        return {
            "_shell_mock": True,
            "time_a": time_a,
            "event_a": event_a,
            "time_b": time_b,
            "event_b": event_b,
            "arm_a_label": "Group 1",
            "arm_b_label": "Group 2",
            "hr": 0.72,
            "hr_ci_low": 0.58,
            "hr_ci_high": 0.89,
            "p_value": 0.004,
        }

    if figure_type == "waterfall":
        best_pct = np.clip(rng.normal(-25, 30, 80), -100, 200)
        bor = []
        groups = []
        for index, percent_change in enumerate(best_pct):
            if percent_change < -100:
                bor.append("CR")
            elif percent_change < -30:
                bor.append("PR")
            elif percent_change < 20:
                bor.append("SD")
            else:
                bor.append("PD")
            groups.append(index % 3)
        return {"_shell_mock": True, "best_pct": best_pct, "bor": bor, "groups": groups, "color_by": "bor"}

    if figure_type == "spider":
        data = SpiderFigure._mock_spider_data()
        data["_shell_mock"] = True
        return data

    if figure_type == "swimmer":
        data = SwimmerFigure._mock_swimmer_data()
        data["_shell_mock"] = True
        return data

    if figure_type == "forest":
        return {"_shell_mock": True, "rows": _generate_mock_subgroup_data()}

    if figure_type == "box_plot":
        visits = ["Baseline", "Week 4", "Week 8", "Week 12", "Week 16"]
        arm_a = {}
        arm_b = {}
        for visit in visits:
            arm_a[visit] = rng.lognormal(3.5, 0.35, 50).tolist()
            arm_b[visit] = rng.lognormal(3.55, 0.35, 50).tolist()
        return {
            "_shell_mock": True,
            "visits": visits,
            "arm_a_values": arm_a,
            "arm_b_values": arm_b,
            "parameter": "ALT (U/L)",
            "uln": 55,
        }

    if figure_type == "longitudinal":
        visits = ["Baseline", "Wk 4", "Wk 8", "Wk 12", "Wk 16", "Wk 20"]
        return {
            "_shell_mock": True,
            "visits": visits,
            "arm_a_mean": [10.0, 9.5, 9.0, 8.2, 7.5, 7.0],
            "arm_a_sd": [2.0, 2.1, 2.3, 2.5, 2.6, 2.8],
            "arm_b_mean": [10.0, 9.8, 9.6, 9.5, 9.3, 9.1],
            "arm_b_sd": [1.9, 2.0, 2.1, 2.2, 2.4, 2.5],
        }

    if figure_type == "cdf":
        return {
            "_shell_mock": True,
            "arm_a_values": rng.normal(-6, 8, 120),
            "arm_b_values": rng.normal(-2, 8, 120),
            "xlabel": "Change from Baseline at Protocol-Defined Visit",
            "reference_value": 0,
        }

    if figure_type == "edish":
        return {
            "_shell_mock": True,
            "peak_alt_xuln": np.exp(rng.normal(-0.1, 0.8, 120)),
            "peak_tbl_xuln": np.exp(rng.normal(-0.3, 0.6, 120)),
            "group": np.where(np.arange(120) % 2 == 0, "Group 1", "Group 2"),
        }

    if figure_type == "lab_toxicity_heatmap":
        return {
            "_shell_mock": True,
            "grades": rng.choice([0, 1, 2, 3, 4], size=(45, 7), p=[0.55, 0.2, 0.14, 0.08, 0.03]),
            "parameters": ["Hgb", "Platelets", "Neutrophils", "ALT", "AST", "TBL", "Creatinine"],
        }

    if figure_type == "concentration_qtc":
        concentration = rng.uniform(0, 800, 140)
        return {
            "_shell_mock": True,
            "concentration": concentration,
            "delta_qtcf": 1.5 + 0.008 * concentration + rng.normal(0, 5, len(concentration)),
        }

    if figure_type in ("pk_profile", "food_effect_profile"):
        time = np.array([0, 0.5, 1, 2, 4, 8, 12, 24], dtype=float)
        profile_a = np.array([0, 42, 76, 88, 62, 34, 20, 6], dtype=float)
        profile_b = np.array([0, 30, 61, 74, 58, 36, 23, 8], dtype=float)
        labels = ("Fasted", "Fed") if figure_type == "food_effect_profile" else ("Group 1", "Group 2")
        return {
            "_shell_mock": True,
            "time_hours": time,
            "arm_a_mean": profile_a,
            "arm_a_sd": np.maximum(profile_a * 0.15, 1),
            "arm_b_mean": profile_b,
            "arm_b_sd": np.maximum(profile_b * 0.15, 1),
            "arm_a_label": labels[0],
            "arm_b_label": labels[1],
        }

    return {"_shell_mock": True}


def supported_figure_types() -> set[str]:
    """Return supported figure_type values."""
    return set(FIGURE_CLASS_MAP)
