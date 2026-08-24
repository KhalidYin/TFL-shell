"""Empirical cumulative distribution figure for continuous endpoints."""

import matplotlib.pyplot as plt
import numpy as np

from tflshell.figures.base import ClinicalFigure
from tflshell.figures.color_schemes import TRT_COLORS


class CDFFigure(ClinicalFigure):
    """Empirical CDF by treatment group.

    Required data keys are ``arm_a_values`` and ``arm_b_values``. Optional keys
    control treatment labels and the endpoint x-axis label.
    """

    def build(self, data: dict) -> plt.Figure:
        arm_a = np.asarray(data["arm_a_values"], dtype=float)
        arm_b = np.asarray(data["arm_b_values"], dtype=float)
        fig, ax = plt.subplots(figsize=self.figsize)

        for values, color, label in (
            (arm_a, TRT_COLORS["A"], data.get("arm_a_label", "Group 1")),
            (arm_b, TRT_COLORS["B"], data.get("arm_b_label", "Group 2")),
        ):
            ordered = np.sort(values)
            cumulative = np.arange(1, len(ordered) + 1) / len(ordered)
            ax.step(ordered, cumulative, where="post", linewidth=1.8, color=color, label=label)

        if "reference_value" in data:
            ax.axvline(data["reference_value"], color="#666666", linestyle="--", linewidth=1)
        ax.set_xlabel(data.get("xlabel", "Change from Baseline"))
        ax.set_ylabel("Cumulative Probability")
        ax.set_ylim(0, 1.02)
        ax.legend(fontsize=8)
        ax.spines[["top", "right"]].set_visible(False)
        return fig
