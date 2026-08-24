"""Waterfall plot — Best percentage change in target lesions v2.2.

Each bar = one subject, sorted by % change (largest increase to largest reduction).
Supports two coloring modes:
  - BOR-based (default): bars colored by Best Overall Response per RECIST
  - Group-based: bars colored by treatment group assignment
Reference lines at +20% (PD threshold) and -30% (PR threshold).
"""

import matplotlib.pyplot as plt
import numpy as np

from tflshell.figures.base import ClinicalFigure, _generate_mock_tumor_data
from tflshell.figures.color_schemes import BOR_COLORS, BOR_ORDER, TRT_COLORS_LIST


class WaterfallFigure(ClinicalFigure):
    """Waterfall plot of best % change in target lesion sum.

    Data schema:
        {
            "best_pct": np.array (best % change per subject),
            "bor": list[str] (BOR category per subject: CR/PR/SD/PD/NE),
            "groups": list[int] (optional, treatment group index 0/1/2),
            "color_by": str ("bor" or "group", default "bor"),
            "xlabel": str, "ylabel": str,
        }
    """

    def build(self, data: dict) -> plt.Figure:
        if not data:
            data = _generate_mock_tumor_data(80)

        best_pct = np.asarray(data.get("best_pct", []))
        bor = data.get("bor", [])
        groups = data.get("groups", None)
        color_by = data.get("color_by", "bor")

        xlabel = data.get("xlabel", "Subjects")
        ylabel = data.get("ylabel", "Best % Change from Baseline in Target Lesion Sum")

        # Sort by best_pct descending
        order = np.argsort(best_pct)[::-1]
        best_pct = best_pct[order]
        bor = [bor[i] for i in order]
        if groups:
            groups = [groups[i] for i in order]

        x = np.arange(len(best_pct))

        fig, ax = plt.subplots(figsize=self.figsize)

        if color_by == "group" and groups:
            group_colors_list = [TRT_COLORS_LIST[g % len(TRT_COLORS_LIST)] for g in groups]
            ax.bar(
                x, best_pct, color=group_colors_list, width=0.9, edgecolor="none", linewidth=0
            )
        else:
            bor_colors = [BOR_COLORS.get(b, BOR_COLORS["NE"]) for b in bor]
            ax.bar(x, best_pct, color=bor_colors, width=0.9, edgecolor="none", linewidth=0)

        # Reference lines
        ax.axhline(y=20, color="red", linestyle="--", linewidth=1.0, alpha=0.7)
        ax.axhline(y=-30, color="green", linestyle="--", linewidth=1.0, alpha=0.7)
        ax.axhline(y=0, color="gray", linestyle="-", linewidth=0.5, alpha=0.4)

        ax.text(len(x) - 1, 21, "+20% (PD)", fontsize=8, color="red", ha="right")
        ax.text(len(x) - 1, -31, "−30% (PR)", fontsize=8, color="green", ha="right")

        ax.set_xlabel(xlabel, fontsize=10)
        ax.set_ylabel(ylabel, fontsize=10)
        ax.set_xlim(-1, len(x))
        y_max = max(max(best_pct) * 1.1, 50)
        y_min = min(min(best_pct) * 1.1, -110)
        ax.set_ylim(y_min, y_max)
        ax.set_xticks([])
        ax.grid(axis="y", alpha=0.3, linestyle=":")

        # Legend
        if color_by == "group" and groups:
            from matplotlib.patches import Patch

            arm_names = data.get("arm_labels", ["Group 1", "Group 2", "Group 3"])
            legend_patches = [
                Patch(facecolor=TRT_COLORS_LIST[i], label=arm_names[i]) for i in sorted(set(groups))
            ]
            ax.legend(
                handles=legend_patches,
                loc="upper right",
                frameon=True,
                facecolor="white",
                edgecolor="#DDDDDD",
                fontsize=8,
            )
        else:
            from matplotlib.patches import Patch

            legend_patches = [
                Patch(facecolor=BOR_COLORS[b], label=b, edgecolor="none")
                for b in BOR_ORDER
                if b in set(bor)
            ]
            ax.legend(
                handles=legend_patches,
                loc="upper right",
                frameon=True,
                facecolor="white",
                edgecolor="#DDDDDD",
                fontsize=8,
                title="BOR",
                title_fontsize=8,
            )

        return fig
