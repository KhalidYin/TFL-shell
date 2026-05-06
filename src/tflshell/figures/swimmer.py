"""Swimmer plot — Duration of treatment and response v2.2.

Horizontal bars for each subject showing treatment duration.
Post-treatment follow-up bars in light gray.
Response markers: star (CR), diamond (PR), circle (first response), triangle (PD), + (ongoing).
Sorted by treatment duration descending.
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

from tflshell.figures.base import ClinicalFigure
from tflshell.figures.color_schemes import TRT_COLORS, TRT_COLORS_LIST


class SwimmerFigure(ClinicalFigure):
    """Swimmer plot of treatment duration with response markers.

    Data schema:
        {
            "subjects": list[dict] with keys:
                arm: str/int (0, 1, 2 for color index),
                duration: float (months on treatment),
                pd_time: float or None (time of progression/death),
                resp_time: float or None (time of first response),
                resp_type: str or None (CR/PR/SD),
                bor: str (BOR category),
                ongoing: bool,
            "xlabel": str, "ylabel": str,
        }
    """

    def build(self, data: dict) -> plt.Figure:
        if not data:
            data = self._mock_swimmer_data()

        subjects = data.get("subjects", [])
        subjects.sort(key=lambda s: -s.get("duration", 0))
        xlabel = data.get("xlabel", "Time from First Dose (Months)")
        ylabel = data.get("ylabel", "Subjects")

        fig, ax = plt.subplots(figsize=self.figsize)

        for i, subj in enumerate(subjects):
            y = len(subjects) - 1 - i

            arm = subj.get("arm", 0)
            dur = subj.get("duration", 12)
            pd_time = subj.get("pd_time", None)
            resp_time = subj.get("resp_time", None)
            resp_type = subj.get("resp_type", None)
            bor = subj.get("bor", "SD")
            ongoing = subj.get("ongoing", False)

            arm_color = (
                TRT_COLORS_LIST[arm % len(TRT_COLORS_LIST)]
                if isinstance(arm, int)
                else TRT_COLORS.get(arm, "#999999")
            )

            # Main treatment bar
            ax.barh(
                y, dur, height=0.6, color=arm_color, alpha=0.7, edgecolor="white", linewidth=0.5
            )

            # Post-treatment follow-up bar (light gray)
            if pd_time is not None and pd_time > dur:
                ax.barh(
                    y,
                    pd_time - dur,
                    left=dur,
                    height=0.6,
                    color="lightgray",
                    alpha=0.5,
                    edgecolor="white",
                    linewidth=0.5,
                )

            # Response markers
            if resp_time is not None and resp_type:
                marker_map = {"CR": "*", "PR": "D"}
                marker = marker_map.get(resp_type, "o")
                marker_size = {"CR": 12, "PR": 10}.get(resp_type, 8)
                ax.plot(
                    resp_time,
                    y,
                    marker=marker,
                    color="gold",
                    markersize=marker_size,
                    markeredgecolor="black",
                    markeredgewidth=0.8,
                    zorder=5,
                )

            # First response marker (circle) if resp_time but no specific type
            elif resp_time is not None and resp_time <= dur:
                ax.scatter(
                    resp_time,
                    y,
                    marker="o",
                    facecolor="white",
                    edgecolor="#333333",
                    s=30,
                    zorder=5,
                    linewidth=1,
                )

            # PD marker (triangle)
            if pd_time is not None:
                ax.plot(
                    pd_time,
                    y,
                    marker="v",
                    color="black",
                    markersize=8,
                    markeredgecolor="white",
                    markeredgewidth=0.5,
                    zorder=5,
                )

            # Ongoing marker
            if ongoing:
                ax.scatter(dur, y, marker="+", color="#333333", s=40, zorder=5, linewidth=1.5)

        # Labels
        ax.set_yticks(range(len(subjects)))
        ax.set_yticklabels([s.get("id", f"S{i + 1}") for s in reversed(subjects)], fontsize=7)
        ax.set_xlabel(xlabel, fontsize=10)
        ax.set_ylabel(ylabel, fontsize=10)
        ax.set_xlim(0, max(s.get("duration", 12) for s in subjects) * 1.2)
        ax.grid(axis="x", alpha=0.3, linestyle=":")

        # Legend
        from matplotlib.patches import Patch

        legend_items = [
            Patch(facecolor=TRT_COLORS_LIST[0], alpha=0.7, label="Group 1"),
            Patch(facecolor=TRT_COLORS_LIST[1], alpha=0.7, label="Group 2"),
        ]
        if len(TRT_COLORS_LIST) >= 3:
            legend_items.append(Patch(facecolor=TRT_COLORS_LIST[2], alpha=0.7, label="Group 3"))
        legend_items.extend(
            [
                Patch(facecolor="lightgray", alpha=0.5, label="Post-Treatment FU"),
                Line2D(
                    [0],
                    [0],
                    marker="*",
                    color="gold",
                    label="CR",
                    markerfacecolor="gold",
                    markersize=10,
                    linewidth=0,
                    markeredgecolor="black",
                ),
                Line2D(
                    [0],
                    [0],
                    marker="D",
                    color="gold",
                    label="PR",
                    markerfacecolor="gold",
                    markersize=8,
                    linewidth=0,
                    markeredgecolor="black",
                ),
                Line2D(
                    [0],
                    [0],
                    marker="v",
                    color="black",
                    label="PD",
                    markerfacecolor="black",
                    markersize=8,
                    linewidth=0,
                ),
                Line2D(
                    [0],
                    [0],
                    marker="+",
                    color="#333333",
                    markersize=10,
                    linewidth=0,
                    label="Ongoing at Cutoff",
                ),
            ]
        )
        ax.legend(
            handles=legend_items,
            loc="lower right",
            fontsize=7,
            frameon=True,
            facecolor="white",
            edgecolor="#DDDDDD",
            ncol=2,
        )

        return fig

    @staticmethod
    def _mock_swimmer_data(n_subjects=14, seed=42):
        rng = np.random.default_rng(seed)
        subjects = []
        for i in range(n_subjects):
            arm = rng.choice([0, 1, 2]) if n_subjects > 8 else rng.choice([0, 1])
            dur = rng.exponential(15) + 2
            bor = rng.choice(["CR", "PR", "SD", "PD"], p=[0.08, 0.22, 0.40, 0.30])
            ttr = rng.exponential(4) + 1 if bor in ("CR", "PR") else None
            has_pd = bor == "PD" or rng.random() < 0.25
            pd_t = (
                dur + rng.exponential(4) + 0.5
                if has_pd and rng.random() < 0.5
                else (dur + 0.1 if has_pd else None)
            )
            ongoing = not has_pd and rng.random() < 0.3
            subjects.append(
                {
                    "id": f"Subj {i + 1:03d}",
                    "arm": arm,
                    "duration": dur,
                    "bor": bor,
                    "resp_time": ttr,
                    "resp_type": bor if bor in ("CR", "PR") else None,
                    "pd_time": pd_t,
                    "ongoing": ongoing,
                }
            )
        return {"subjects": subjects}
