"""Subject-by-parameter laboratory toxicity heatmap."""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import BoundaryNorm, ListedColormap

from tflshell.figures.base import ClinicalFigure


class LabToxicityHeatmapFigure(ClinicalFigure):
    """Worst protocol-defined toxicity grade by subject and laboratory parameter."""

    def build(self, data: dict) -> plt.Figure:
        grades = np.asarray(data["grades"], dtype=float)
        parameters = data["parameters"]
        fig, ax = plt.subplots(figsize=self.figsize)
        cmap = ListedColormap(["#F2F2F2", "#FFF2B2", "#F8C471", "#E74C3C", "#7D3C98"])
        norm = BoundaryNorm([-0.5, 0.5, 1.5, 2.5, 3.5, 4.5], cmap.N)
        image = ax.imshow(grades, aspect="auto", interpolation="nearest", cmap=cmap, norm=norm)
        ax.set_xticks(np.arange(len(parameters)), labels=parameters, rotation=45, ha="right")
        ax.set_yticks([])
        ax.set_xlabel("Laboratory Parameter")
        ax.set_ylabel("Subjects")
        colorbar = fig.colorbar(image, ax=ax, ticks=[0, 1, 2, 3, 4], fraction=0.04, pad=0.02)
        colorbar.set_label("Worst Toxicity Grade")
        return fig
