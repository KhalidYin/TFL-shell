"""Spider plot — Percentage change in tumor burden over time.

Each line = one subject. Trajectories of % change from baseline.
Colored by BOR. Terminal markers: triangle=PD, X=death.
"""

import matplotlib.pyplot as plt
import numpy as np

from tflshell.figures.base import ClinicalFigure
from tflshell.figures.color_schemes import BOR_COLORS


class SpiderFigure(ClinicalFigure):
    """Spider plot of tumor burden trajectories.

    Data schema:
        {
            "subjects": list[dict] with keys: bor, timepoints (list), pct_changes (list),
            "xlabel": str, "ylabel": str,
        }
    """

    def build(self, data: dict) -> plt.Figure:
        if not data:
            data = self._mock_spider_data()

        subjects = data.get("subjects", [])
        xlabel = data.get("xlabel", "Time from First Dose (Months)")
        ylabel = data.get("ylabel", "% Change from Baseline in Tumor Burden")

        fig, ax = plt.subplots(figsize=self.figsize)

        for subj in subjects:
            bor = subj.get("bor", "SD")
            color = BOR_COLORS.get(bor, BOR_COLORS["NE"])
            times = subj.get("timepoints", [])
            pcts = subj.get("pct_changes", [])
            has_pd = subj.get("has_pd", False)
            has_death = subj.get("has_death", False)

            ax.plot(times, pcts, color=color, linewidth=0.5, alpha=0.6)
            if has_pd and times:
                ax.scatter(times[-1], pcts[-1], marker="^", color=color, s=20, alpha=0.8, zorder=5)
            if has_death and times:
                ax.scatter(
                    times[-1], pcts[-1], marker="x", color="black", s=25, alpha=0.9, zorder=6
                )

        ax.axhline(y=0, color="gray", linestyle="-", linewidth=0.8, alpha=0.5)
        ax.axhline(y=20, color="gray", linestyle="--", linewidth=0.5, alpha=0.4)
        ax.axhline(y=-30, color="gray", linestyle="--", linewidth=0.5, alpha=0.4)

        ax.set_xlabel(xlabel, fontsize=10)
        ax.set_ylabel(ylabel, fontsize=10)
        ax.set_xlim(0, 26)
        y_abs = max(abs(ax.get_ylim()[0]), abs(ax.get_ylim()[1])) if subjects else 100
        ax.set_ylim(-y_abs, y_abs)

        # Legend
        from matplotlib.patches import Patch

        bors = set(s.get("bor", "SD") for s in subjects)
        from tflshell.figures.color_schemes import BOR_ORDER

        legend_patches = [Patch(facecolor=BOR_COLORS[b], label=b) for b in BOR_ORDER if b in bors]
        legend_patches.append(
            plt.Line2D([0], [0], marker="^", color="gray", markersize=8, linewidth=0, label="PD")
        )
        legend_patches.append(
            plt.Line2D(
                [0], [0], marker="x", color="black", markersize=8, linewidth=0, label="Death"
            )
        )
        ax.legend(
            handles=legend_patches,
            loc="upper left",
            fontsize=7,
            frameon=True,
            facecolor="white",
            edgecolor="#DDDDDD",
        )

        return fig

    @staticmethod
    def _mock_spider_data(n_subjects=40, seed=42):
        rng = np.random.default_rng(seed)
        subjects = []
        bors = ["CR", "PR", "SD", "PD"]
        bor_probs = [0.05, 0.25, 0.45, 0.25]
        visits = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]

        for _ in range(n_subjects):
            bor = rng.choice(bors, p=bor_probs)
            n_visits = rng.integers(4, len(visits))
            times = visits[: n_visits + 1]
            base_effect = {"CR": -70, "PR": -40, "SD": -5, "PD": 30}[bor]
            noise = rng.normal(0, 8, len(times))
            drift = np.linspace(0, base_effect, len(times))
            pcts = drift + noise
            has_pd = bor == "PD" or rng.random() < 0.15
            has_death = rng.random() < 0.05

            subjects.append(
                {
                    "bor": bor,
                    "timepoints": times,
                    "pct_changes": pcts.tolist(),
                    "has_pd": has_pd,
                    "has_death": has_death,
                }
            )

        return {"subjects": subjects}
