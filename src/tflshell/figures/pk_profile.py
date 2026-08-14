"""Mean concentration-time profile for pharmacokinetic shell figures."""

import matplotlib.pyplot as plt
import numpy as np

from tflshell.figures.base import ClinicalFigure
from tflshell.figures.color_schemes import TRT_COLORS


class PKProfileFigure(ClinicalFigure):
    """Mean concentration over nominal time, optionally with variability bands."""

    def build(self, data: dict) -> plt.Figure:
        time = np.asarray(data["time_hours"], dtype=float)
        fig, ax = plt.subplots(figsize=self.figsize)
        for key, color, marker in (("a", TRT_COLORS["A"], "o"), ("b", TRT_COLORS["B"], "s")):
            mean = np.asarray(data[f"arm_{key}_mean"], dtype=float)
            sd = np.asarray(data[f"arm_{key}_sd"], dtype=float)
            label = data.get(f"arm_{key}_label", f"Group {1 if key == 'a' else 2}")
            ax.errorbar(time, mean, yerr=sd, color=color, marker=marker, capsize=3, label=label)
        ax.set_xlabel("Nominal Time After Dose (hours)")
        ax.set_ylabel("Mean Drug Concentration")
        if data.get("log_scale", False):
            ax.set_yscale("log")
        ax.legend(fontsize=8)
        ax.spines[["top", "right"]].set_visible(False)
        return fig
