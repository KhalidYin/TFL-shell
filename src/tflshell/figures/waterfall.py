"""Waterfall plot — Best percentage change in target lesions.

Each bar = one subject, sorted by % change (largest increase to largest reduction).
Bars colored by Best Overall Response.
Reference lines at +20% (PD threshold) and -30% (PR threshold).
"""

import numpy as np
import matplotlib.pyplot as plt

from tflshell.figures.base import ClinicalFigure, _generate_mock_tumor_data
from tflshell.figures.color_schemes import BOR_COLORS, BOR_ORDER


class WaterfallFigure(ClinicalFigure):
    """Waterfall plot of best % change in target lesion sum.

    Data schema:
        {
            "best_pct": np.array (best % change per subject, sorted descending),
            "bor": list[str] (BOR category per subject: CR/PR/SD/PD/NE),
            "xlabel": str,
            "ylabel": str,
            "title": str,
        }
    """

    def build(self, data: dict) -> plt.Figure:
        if not data:
            data = _generate_mock_tumor_data(80)

        best_pct = np.asarray(data.get("best_pct", []))
        bor = data.get("bor", [])
        xlabel = data.get("xlabel", "Subjects")
        ylabel = data.get("ylabel", "Best % Change from Baseline in Target Lesion Sum")

        # Sort by best_pct descending
        order = np.argsort(best_pct)[::-1]
        best_pct = best_pct[order]
        bor = [bor[i] for i in order]

        colors = [BOR_COLORS.get(b, BOR_COLORS["NE"]) for b in bor]
        x = np.arange(len(best_pct))

        fig, ax = plt.subplots(figsize=self.figsize)
        bars = ax.bar(x, best_pct, color=colors, width=0.9, edgecolor="none", linewidth=0)

        # Reference lines
        ax.axhline(y=20, color="gray", linestyle="--", linewidth=1.0, alpha=0.7)
        ax.axhline(y=-30, color="gray", linestyle="--", linewidth=1.0, alpha=0.7)
        ax.axhline(y=0, color="gray", linestyle="-", linewidth=0.5, alpha=0.4)

        ax.text(len(x) - 1, 21, "+20% (PD)", fontsize=8, color="gray", ha="right")
        ax.text(len(x) - 1, -31, "−30% (PR)", fontsize=8, color="gray", ha="right")

        ax.set_xlabel(xlabel, fontsize=10)
        ax.set_ylabel(ylabel, fontsize=10)
        ax.set_xlim(-1, len(x))
        y_max = max(max(best_pct) * 1.1, 50)
        y_min = min(min(best_pct) * 1.1, -110)
        ax.set_ylim(y_min, y_max)
        ax.set_xticks([])

        # Legend
        from matplotlib.patches import Patch
        legend_patches = [Patch(facecolor=BOR_COLORS[b], label=b, edgecolor="none")
                          for b in BOR_ORDER if b in set(bor)]
        ax.legend(handles=legend_patches, loc="upper right",
                  frameon=True, facecolor="white", edgecolor="#DDDDDD",
                  fontsize=8, title="BOR", title_fontsize=8)

        return fig
