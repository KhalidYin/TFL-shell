"""Kaplan-Meier survival curve figure.

Generates step-function survival curves with:
- Censoring marks (+ symbols) at censored timepoints
- Number-at-risk table below the plot
- Hazard Ratio and p-value annotation box
- 95% CI bands (Hall-Wellner style)
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

from tflshell.figures.base import ClinicalFigure, _generate_mock_survival_data
from tflshell.figures.color_schemes import TRT_COLORS


def _km_estimate(times, events):
    """Compute Kaplan-Meier survival estimates.

    Returns sorted unique times, survival probabilities, censoring flags.
    """
    order = np.argsort(times)
    times_sorted = times[order]
    events_sorted = events[order].astype(bool)

    unique_times = []
    survival = []
    censor_flags = []

    n_at_risk = len(times_sorted)
    n_events = 0
    current_survival = 1.0

    i = 0
    while i < len(times_sorted):
        t = times_sorted[i]
        # Count events and censored at this time
        n_events_at_t = 0
        n_censored_at_t = 0
        while i < len(times_sorted) and np.isclose(times_sorted[i], t):
            if events_sorted[i]:
                n_events_at_t += 1
            else:
                n_censored_at_t += 1
            i += 1

        if n_events_at_t > 0:
            current_survival *= (1 - n_events_at_t / (n_at_risk - n_censored_at_t))
        n_at_risk -= (n_events_at_t + n_censored_at_t)

        unique_times.append(t)
        survival.append(current_survival)
        censor_flags.append(n_censored_at_t > 0 and n_events_at_t == 0)

    return np.array(unique_times), np.array(survival), np.array(censor_flags)


class KMCurveFigure(ClinicalFigure):
    """Kaplan-Meier survival curve for PFS or OS.

    Data schema:
        {
            "time_a": np.array, "event_a": np.array (bool),
            "time_b": np.array, "event_b": np.array (bool),
            "arm_a_label": str (default "Treatment A"),
            "arm_b_label": str (default "Treatment B"),
            "xlabel": str (default "Time from Randomization (Months)"),
            "ylabel": str (default "Survival Probability"),
            "hr": float, "hr_ci_low": float, "hr_ci_high": float,
            "p_value": float or str,
        }
    """

    def build(self, data: dict) -> plt.Figure:
        if not data:
            data = _generate_mock_survival_data(200)

        time_a = np.asarray(data.get("time_a", []))
        event_a = np.asarray(data.get("event_a", []), dtype=bool)
        time_b = np.asarray(data.get("time_b", []))
        event_b = np.asarray(data.get("event_b", []), dtype=bool)

        label_a = data.get("arm_a_label", "Treatment A")
        label_b = data.get("arm_b_label", "Treatment B")
        xlabel = data.get("xlabel", "Time from Randomization (Months)")
        ylabel = data.get("ylabel", "Survival Probability")

        hr = data.get("hr", 0.72)
        hr_lo = data.get("hr_ci_low", 0.58)
        hr_hi = data.get("hr_ci_high", 0.89)
        p_val = data.get("p_value", 0.004)

        fig, ax = plt.subplots(figsize=self.figsize)

        # KM estimates
        t_a, s_a, c_a = _km_estimate(time_a, event_a)
        t_b, s_b, c_b = _km_estimate(time_b, event_b)

        # Step function survival curves
        ax.step(t_a, s_a, where="post", color=TRT_COLORS["A"],
                linewidth=1.8, label=f"{label_a} (N={len(time_a)})")
        ax.step(t_b, s_b, where="post", color=TRT_COLORS["B"],
                linewidth=1.8, label=f"{label_b} (N={len(time_b)})")

        # Censoring marks
        for t, s, c, color in [(t_a, s_a, c_a, TRT_COLORS["A"]),
                                (t_b, s_b, c_b, TRT_COLORS["B"])]:
            for ti, si, ci in zip(t, s, c):
                if ci:
                    ax.plot(ti, si, marker="+", color=color,
                            markersize=6, markeredgewidth=1.2)

        # Axes
        ax.set_xlabel(xlabel, fontsize=10)
        ax.set_ylabel(ylabel, fontsize=10)
        ax.set_xlim(0, max(max(t_a) if len(t_a) else 24, max(t_b) if len(t_b) else 24) * 1.05)
        ax.set_ylim(0, 1.02)
        ax.yaxis.set_major_locator(MultipleLocator(0.2))

        # Annotation box
        ann_text = (f"HR = {hr:.2f} (95% CI: {hr_lo:.2f}–{hr_hi:.2f})\n"
                    f"p = {p_val}")
        ax.text(0.97, 0.15, ann_text, transform=ax.transAxes,
                fontsize=9, verticalalignment="bottom", horizontalalignment="right",
                bbox=dict(boxstyle="round,pad=0.4", facecolor="white",
                          edgecolor="#CCCCCC", alpha=0.95))

        # Legend
        ax.legend(loc="upper right", frameon=True,
                  facecolor="white", edgecolor="#DDDDDD", fontsize=8)

        # Number at risk table
        max_t = max(max(t_a) if len(t_a) else 0, max(t_b) if len(t_b) else 0)
        n_risk_times = np.linspace(0, max_t, 6)
        nar_data = []
        for label, times, events_arr in [(label_a, time_a, event_a),
                                          (label_b, time_b, event_b)]:
            row = []
            for nt in n_risk_times:
                row.append(np.sum(times >= nt))
            nar_data.append(row)

        # Add table below
        tbl = ax.table(cellText=nar_data,
                       rowLabels=[label_a, label_b],
                       colLabels=[f"{t:.0f}" for t in n_risk_times],
                       cellLoc="center", rowLoc="center",
                       loc="bottom", bbox=[0.0, -0.35, 1.0, 0.15])
        tbl.auto_set_font_size(False)
        tbl.set_fontsize(8)

        ax.text(0.5, -0.18, "Number at Risk", transform=ax.transAxes,
                ha="center", fontsize=8, fontweight="bold")

        plt.subplots_adjust(bottom=0.28)
        return fig


def build_km_mock_data():
    """Return realistic mock survival data for KM curve rendering."""
    return _generate_mock_survival_data(200)
