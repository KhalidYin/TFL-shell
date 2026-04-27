"""Forest plot — Subgroup analysis with hazard ratio and 95% CI.

Horizontal point estimates with error bars.
Diamond for overall effect. Reference line at HR=1.
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
                                      n_trt_a, n_trt_b, events_a, events_b,
            "xlabel": str (default "Hazard Ratio (95% CI)"),
        }
    """

    def build(self, data: dict) -> plt.Figure:
        if not data:
            data = {"rows": _generate_mock_subgroup_data()}

        rows = data.get("rows", [])
        xlabel = data.get("xlabel", "Hazard Ratio (95% CI)")
        n = len(rows)

        fig, ax = plt.subplots(figsize=(8, max(3, n * 0.45)))

        y_positions = list(range(n - 1, -1, -1))

        for i, row in enumerate(rows):
            hr = row["hr"]
            ci_low = row["ci_low"]
            ci_high = row["ci_high"]
            is_overall = row.get("subgroup") == "Overall"
            y = y_positions[i]

            color = "#000000" if is_overall else "#333333"
            marker_size = 70 if is_overall else 40
            linewidth = 2.5 if is_overall else 1.5

            # CI line
            ax.plot([ci_low, ci_high], [y, y], color=color, linewidth=linewidth)

            # Point estimate
            if is_overall:
                # Diamond for overall
                diamond_w = max(0.02, ci_high - ci_low)
                ax.scatter(hr, y, color="#000000", s=marker_size, zorder=5,
                           marker="D", linewidth=1)
            else:
                ax.scatter(hr, y, color=color, s=marker_size, zorder=5, linewidth=1)

        # Reference line
        ax.axvline(x=1.0, color="#666666", linestyle="--", linewidth=1, alpha=0.7)

        # Labels
        ax.set_yticks(y_positions)
        ax.set_yticklabels([r["subgroup"] for r in rows], fontsize=8)
        ax.set_xlabel(xlabel, fontsize=10)

        # Info table on right side
        for i, row in enumerate(rows):
            y = y_positions[i]
            info = f"{row['hr']:.2f} [{row['ci_low']:.2f}, {row['ci_high']:.2f}]"
            ax.text(ax.get_xlim()[1] * 1.02, y, info, fontsize=7,
                    verticalalignment="center", fontfamily="monospace")

        # Footer
        ax.text(0.5, -1.8, "<-- Favors Treatment A  |  Favors Treatment B -->",
                transform=ax.transAxes, ha="center", fontsize=8, color="#666666")

        ax.set_ylim(-1.5, n + 0.2)
        ax.set_xlim(0.1, ax.get_xlim()[1] * 1.5)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        return fig
