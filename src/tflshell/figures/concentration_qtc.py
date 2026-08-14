"""Concentration-QTcF scatter and fitted trend figure."""

import matplotlib.pyplot as plt
import numpy as np

from tflshell.figures.base import ClinicalFigure
from tflshell.figures.color_schemes import TRT_COLORS


class ConcentrationQTcFigure(ClinicalFigure):
    """Plasma concentration versus placebo-adjusted change from baseline QTcF."""

    def build(self, data: dict) -> plt.Figure:
        concentration = np.asarray(data["concentration"], dtype=float)
        delta_qtcf = np.asarray(data["delta_qtcf"], dtype=float)
        fig, ax = plt.subplots(figsize=self.figsize)
        ax.scatter(concentration, delta_qtcf, s=18, alpha=0.45, color=TRT_COLORS["A"])

        fit = np.polyfit(concentration, delta_qtcf, deg=1)
        x_line = np.linspace(0, concentration.max(), 100)
        y_line = np.polyval(fit, x_line)
        residual_sd = np.std(delta_qtcf - np.polyval(fit, concentration), ddof=2)
        ax.plot(x_line, y_line, color="#1F4E79", linewidth=2, label="Illustrative fitted trend")
        ax.fill_between(x_line, y_line - 1.64 * residual_sd, y_line + 1.64 * residual_sd, alpha=0.15)
        ax.axhline(10, color="#8B2E2E", linestyle="--", linewidth=1, label="10 ms reference")
        ax.set_xlabel("Plasma Drug Concentration")
        ax.set_ylabel("Placebo-Adjusted Change from Baseline QTcF (ms)")
        ax.legend(fontsize=8)
        ax.spines[["top", "right"]].set_visible(False)
        return fig
