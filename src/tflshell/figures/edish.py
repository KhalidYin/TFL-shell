"""Evaluation of Drug-Induced Serious Hepatotoxicity (eDISH) plot."""

import matplotlib.pyplot as plt
import numpy as np

from tflshell.figures.base import ClinicalFigure
from tflshell.figures.color_schemes import TRT_COLORS


class EDISHFigure(ClinicalFigure):
    """Peak ALT or AST xULN against peak total bilirubin xULN."""

    def build(self, data: dict) -> plt.Figure:
        x = np.asarray(data["peak_alt_xuln"], dtype=float)
        y = np.asarray(data["peak_tbl_xuln"], dtype=float)
        groups = np.asarray(data.get("group", ["Group 1"] * len(x)))
        fig, ax = plt.subplots(figsize=self.figsize)

        for label, color in (("Group 1", TRT_COLORS["A"]), ("Group 2", TRT_COLORS["B"])):
            mask = groups == label
            if mask.any():
                ax.scatter(x[mask], y[mask], s=20, alpha=0.65, color=color, label=label)

        ax.axvline(3, color="#555555", linestyle="--", linewidth=1)
        ax.axhline(2, color="#555555", linestyle="--", linewidth=1)
        ax.text(3.2, 2.15, "Potential Hy's Law region", fontsize=8, color="#8B2E2E")
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_xlabel("Peak ALT or AST (× ULN)")
        ax.set_ylabel("Peak Total Bilirubin (× ULN)")
        ax.legend(fontsize=8)
        ax.spines[["top", "right"]].set_visible(False)
        return fig
