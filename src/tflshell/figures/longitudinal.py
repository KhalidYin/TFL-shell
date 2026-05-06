"""Longitudinal line plot — Mean (+/- SD) change from baseline over time."""

import matplotlib.pyplot as plt
import numpy as np

from tflshell.figures.base import ClinicalFigure
from tflshell.figures.color_schemes import TRT_COLORS


class LongitudinalFigure(ClinicalFigure):
    """Line plot of mean (+/- SD) over scheduled visits by treatment arm.

    Data schema:
        {
            "visits": list[str],
            "arm_a_mean": list[float], "arm_a_sd": list[float],
            "arm_b_mean": list[float], "arm_b_sd": list[float],
            "arm_a_label": str, "arm_b_label": str,
            "xlabel": str, "ylabel": str,
            "ref_line": float (horizontal reference line value),
        }
    """

    def build(self, data: dict) -> plt.Figure:
        if not data:
            data = self._mock_longitudinal_data()

        visits = data.get("visits", ["Baseline", "Wk 4", "Wk 8", "Wk 12", "Wk 16"])
        arm_a_mean = data.get("arm_a_mean", [])
        arm_a_sd = data.get("arm_a_sd", [])
        arm_b_mean = data.get("arm_b_mean", [])
        arm_b_sd = data.get("arm_b_sd", [])
        arm_a_label = data.get("arm_a_label", "Group 1")
        arm_b_label = data.get("arm_b_label", "Group 2")
        xlabel = data.get("xlabel", "Visit")
        ylabel = data.get("ylabel", "Mean (+/- SD)")
        ref_line = data.get("ref_line", None)

        x = np.arange(len(visits))
        fig, ax = plt.subplots(figsize=self.figsize)

        # Group 1
        ax.errorbar(
            x - 0.15,
            arm_a_mean,
            yerr=arm_a_sd,
            color=TRT_COLORS["A"],
            marker="o",
            markersize=6,
            linewidth=1.8,
            capsize=4,
            capthick=1.2,
            label=arm_a_label,
        )

        # Group 2
        ax.errorbar(
            x + 0.15,
            arm_b_mean,
            yerr=arm_b_sd,
            color=TRT_COLORS["B"],
            marker="s",
            markersize=6,
            linewidth=1.8,
            capsize=4,
            capthick=1.2,
            label=arm_b_label,
        )

        if ref_line is not None:
            ax.axhline(y=ref_line, color="#666666", linestyle="--", linewidth=0.8, alpha=0.6)

        ax.set_xticks(x)
        ax.set_xticklabels(visits, fontsize=8)
        ax.set_xlabel(xlabel, fontsize=10)
        ax.set_ylabel(ylabel, fontsize=10)
        ax.legend(
            loc="upper right", fontsize=8, frameon=True, facecolor="white", edgecolor="#DDDDDD"
        )
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        return fig

    @staticmethod
    def _mock_longitudinal_data():
        rng = np.random.default_rng(42)
        visits = ["Baseline", "Week 4", "Week 8", "Week 12", "Week 16", "Week 20"]
        # Simulate a treatment effect
        arm_a_mean = [10.0, 9.5, 9.0, 8.2, 7.5, 7.0]
        arm_a_sd = [2.0, 2.1, 2.3, 2.5, 2.6, 2.8]
        arm_b_mean = [10.0, 9.8, 9.6, 9.5, 9.3, 9.1]
        arm_b_sd = [1.9, 2.0, 2.1, 2.2, 2.4, 2.5]
        return {
            "visits": visits,
            "arm_a_mean": arm_a_mean,
            "arm_a_sd": arm_a_sd,
            "arm_b_mean": arm_b_mean,
            "arm_b_sd": arm_b_sd,
        }
