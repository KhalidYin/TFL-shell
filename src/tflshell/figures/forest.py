"""Forest plot — Subgroup analysis with hazard ratio and 95% CI v2.2.

Horizontal point estimates with error bars.
Diamond marker for overall effect, circle markers for subgroups.
Supports log-scale x-axis. Reference line at HR=1.
"""

import numpy as np
import matplotlib.pyplot as plt

from tflshell.figures.base import ClinicalFigure, _generate_mock_subgroup_data
from tflshell.figures.color_schemes import TRT_COLORS


class ForestFigure(ClinicalFigure):
    """Forest plot of treatment effect by subgroup.

    Data schema:
        {
            "rows": list[dict] with: subgroup, hr, ci_low, ci_high,
            "xlabel": str,
            "xscale": str ("linear" or "log", default "linear"),
            "favors_left_label": str (default "Favors Treatment A"),
            "favors_right_label": str (default "Favors Treatment B"),
        }
    """

    def build(self, data: dict) -> plt.Figure:
        if not data:
            data = {"rows": _generate_mock_subgroup_data()}

        rows = data.get("rows", [])
        xlabel = data.get("xlabel", "Hazard Ratio (95% CI)")
        xscale = data.get("xscale", "linear")
        favors_left = data.get("favors_left_label", "Favors Treatment A")
        favors_right = data.get("favors_right_label", "Favors Treatment B")
        n = len(rows)

        fig, ax = plt.subplots(figsize=(8, max(3, n * 0.45)))

        y_positions = list(range(n - 1, -1, -1))

        if xscale == "log":
            ax.set_xscale("log")
            ax.set_xlim(0.15, 3.0)
            ax.set_xticks([0.25, 0.5, 1.0, 2.0])
            ax.set_xticklabels(["0.25", "0.50", "1.0", "2.0"])
        else:
            x_min = min(r["ci_low"] for r in rows) * 0.8
            x_max = max(r["ci_high"] for r in rows) * 1.2
            ax.set_xlim(x_min, x_max)

        for i, row in enumerate(rows):
            hr = row["hr"]
            ci_low = row["ci_low"]
            ci_high = row["ci_high"]
            is_overall = row.get("subgroup") == "Overall"
            y = y_positions[i]

            color = "#000000" if is_overall else "#333333"
            linewidth = 2.5 if is_overall else 1.5

            # CI line
            ax.plot([ci_low, ci_high], [y, y], color=color, linewidth=linewidth, zorder=2)

            # Point estimate
            if is_overall:
                ax.scatter(hr, y, color="#000000", s=100, zorder=3,
                           marker="D", linewidth=1, edgecolors="white")
            else:
                ax.scatter(hr, y, color=color, s=50, zorder=3,
                           marker="o", linewidth=1)

            # HR/CI text
            hr_text = f'{hr:.2f} ({ci_low:.2f}, {ci_high:.2f})'
            if xscale == "log":
                ax.text(2.8, y, hr_text, fontsize=7, fontfamily="monospace",
                        verticalalignment="center")
            else:
                ax.text(ax.get_xlim()[1] * 1.02, y, hr_text, fontsize=7,
                        fontfamily="monospace", verticalalignment="center")

        # Reference line at HR=1
        ax.axvline(x=1.0, color="#666666", linestyle="--", linewidth=1.0, alpha=0.7)

        # Labels
        ax.set_yticks(y_positions)
        ax.set_yticklabels([r["subgroup"] for r in rows], fontsize=9, fontweight="bold")
        ax.set_xlabel(xlabel, fontsize=10)

        # Footer — favors annotation
        ax.text(0.5, -0.15, f"<-- {favors_left}  |  {favors_right} -->",
                transform=ax.transAxes, ha="center", fontsize=8, color="#666666",
                fontstyle="italic")

        ax.set_ylim(-1.2, n + 0.2)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.grid(axis="x", alpha=0.3, linestyle=":")

        return fig
