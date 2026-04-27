"""Swimmer plot — Duration of treatment and response.

Horizontal bars for each subject showing treatment duration.
Markers for: first response (circle), progression (triangle), ongoing (+).
Sorted by treatment duration, grouped by arm.
"""

import numpy as np
import matplotlib.pyplot as plt

from tflshell.figures.base import ClinicalFigure, _generate_mock_tumor_data
from tflshell.figures.color_schemes import TRT_COLORS, BOR_COLORS


class SwimmerFigure(ClinicalFigure):
    """Swimmer plot of treatment duration with response markers.

    Data schema:
        {
            "subjects": list[dict] with: arm, duration, bor, ttr, has_pd, ongoing,
            "xlabel": str, "ylabel": str,
        }
    """

    def build(self, data: dict) -> plt.Figure:
        if not data:
            data = self._mock_swimmer_data()

        subjects = data.get("subjects", [])
        # Sort by arm then duration descending
        subjects.sort(key=lambda s: (s.get("arm", "A"), -s.get("duration", 0)))
        xlabel = data.get("xlabel", "Time from First Dose (Months)")
        ylabel = data.get("ylabel", "Subjects")

        fig, ax = plt.subplots(figsize=self.figsize)

        y = 0
        y_labels = []
        for subj in subjects:
            arm = subj.get("arm", "A")
            dur = subj.get("duration", 12)
            bor = subj.get("bor", "SD")
            ttr = subj.get("ttr", None)
            has_pd = subj.get("has_pd", False)
            ongoing = subj.get("ongoing", False)

            bar_color = TRT_COLORS.get(arm, "#999999")
            bor_color = BOR_COLORS.get(bor, "#999999")

            # Main bar: treatment duration
            ax.barh(y, dur, height=0.7, color=bar_color, alpha=0.7,
                    edgecolor="none", linewidth=0)

            # BOR segment at end of bar
            ax.barh(y, dur, height=0.7, color=bor_color, alpha=1.0,
                    left=0, linewidth=0)

            # First response marker
            if ttr is not None and ttr <= dur:
                ax.scatter(ttr, y, marker="o", facecolor="white",
                           edgecolor="#333333", s=30, zorder=5, linewidth=1)

            # PD marker
            if has_pd:
                ax.scatter(dur, y, marker="^", color="red",
                           s=35, zorder=6, linewidth=1)

            # Ongoing marker
            if ongoing:
                ax.scatter(dur, y, marker="+", color="#333333",
                           s=40, zorder=5, linewidth=1.5)

            y_labels.append(f"S{y + 1}")
            y += 1

        ax.set_xlabel(xlabel, fontsize=10)
        ax.set_ylabel(ylabel, fontsize=10)
        ax.set_ylim(-1, len(subjects))
        ax.set_yticks([])

        # Legend
        from matplotlib.patches import Patch
        legend_items = [
            Patch(facecolor=TRT_COLORS["A"], alpha=0.7, label="Treatment A"),
            Patch(facecolor=TRT_COLORS["B"], alpha=0.7, label="Treatment B"),
            plt.Line2D([0], [0], marker="o", color="w", markerfacecolor="white",
                       markeredgecolor="#333333", markersize=8, linewidth=0,
                       label="First Response"),
            plt.Line2D([0], [0], marker="^", color="red", markersize=8,
                       linewidth=0, label="Progression"),
            plt.Line2D([0], [0], marker="+", color="#333333", markersize=10,
                       linewidth=0, label="Ongoing at Cutoff"),
        ]
        ax.legend(handles=legend_items, loc="lower right", fontsize=7,
                  frameon=True, facecolor="white", edgecolor="#DDDDDD",
                  ncol=2)

        return fig

    @staticmethod
    def _mock_swimmer_data(n_subjects=40, seed=42):
        rng = np.random.default_rng(seed)
        subjects = []
        for i in range(n_subjects):
            arm = "A" if i < n_subjects // 2 else "B"
            dur = rng.exponential(15) + 1
            bor = rng.choice(["CR", "PR", "SD", "PD"], p=[0.05, 0.25, 0.40, 0.30])
            ttr = rng.exponential(4) + 1 if bor in ("CR", "PR") else None
            has_pd = bor == "PD" or rng.random() < 0.2
            ongoing = not has_pd and rng.random() < 0.3
            subjects.append({
                "arm": arm, "duration": dur, "bor": bor,
                "ttr": ttr, "has_pd": has_pd, "ongoing": ongoing,
            })
        return {"subjects": subjects}
