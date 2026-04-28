"""Box plot — Laboratory parameters by visit with side-by-side treatment arms."""

import numpy as np
import matplotlib.pyplot as plt

from tflshell.figures.base import ClinicalFigure, _generate_mock_lab_data
from tflshell.figures.color_schemes import TRT_COLORS, TRT_COLORS_LIST


class BoxPlotFigure(ClinicalFigure):
    """Side-by-side box plots of lab values by visit.

    Data schema:
        {
            "visits": list[str],
            "arm_a_values": {visit: list[float]},
            "arm_b_values": {visit: list[float]},
            "parameter": str (e.g. "ALT (U/L)"),
            "uln": float (upper limit of normal reference line),
        }
    """

    def build(self, data: dict) -> plt.Figure:
        if not data:
            data = self._mock_box_data()

        visits = data.get("visits", ["Baseline", "Wk 4", "Wk 8", "Wk 12"])
        arm_a = data.get("arm_a_values", {})
        arm_b = data.get("arm_b_values", {})
        param = data.get("parameter", "ALT (U/L)")
        uln = data.get("uln", None)

        fig, ax = plt.subplots(figsize=self.figsize)
        n_visits = len(visits)
        width = 0.35
        x = np.arange(n_visits)

        box_config = dict(widths=width, patch_artist=True,
                          flierprops=dict(marker="o", markersize=3, alpha=0.5),
                          boxprops=dict(linewidth=1), whiskerprops=dict(linewidth=1),
                          capprops=dict(linewidth=1), medianprops=dict(linewidth=1.5, color="#333333"))

        for i, v in enumerate(visits):
            if v in arm_a:
                bp = ax.boxplot(arm_a[v], positions=[i - width / 2], **box_config)
                for patch in bp["boxes"]:
                    patch.set_facecolor(TRT_COLORS["A"])
                    patch.set_alpha(0.6)

            if v in arm_b:
                bp = ax.boxplot(arm_b[v], positions=[i + width / 2], **box_config)
                for patch in bp["boxes"]:
                    patch.set_facecolor(TRT_COLORS["B"])
                    patch.set_alpha(0.6)

        if uln is not None:
            ax.axhline(y=uln, color="#666666", linestyle="--", linewidth=1, alpha=0.7)
            ax.text(n_visits - 0.5, uln + uln * 0.02, "ULN", fontsize=7, color="#666666")

        ax.set_xticks(x)
        ax.set_xticklabels(visits, fontsize=8)
        ax.set_ylabel(param, fontsize=10)

        # Legend
        from matplotlib.patches import Patch
        legend_items = [
            Patch(facecolor=TRT_COLORS["A"], alpha=0.6, label="Group 1"),
            Patch(facecolor=TRT_COLORS["B"], alpha=0.6, label="Group 2"),
        ]
        ax.legend(handles=legend_items, loc="upper right", fontsize=8)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        return fig

    @staticmethod
    def _mock_box_data():
        rng = np.random.default_rng(42)
        visits = ["Baseline", "Week 4", "Week 8", "Week 12", "Week 16"]
        arm_a = {}
        arm_b = {}
        for v in visits:
            arm_a[v] = rng.lognormal(3.5, 0.3, 50).tolist()
            arm_b[v] = rng.lognormal(3.5, 0.3, 50).tolist()
        return {
            "visits": visits,
            "arm_a_values": arm_a,
            "arm_b_values": arm_b,
            "parameter": "ALT (U/L)",
            "uln": 55,
        }
