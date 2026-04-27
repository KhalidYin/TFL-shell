"""Kaplan-Meier survival curve figure v2.2.

Generates step-function survival curves with:
- 95% CI bands (Greenwood's formula)
- Censoring marks (+ symbols)
- Two-subplot layout (3:1 ratio): KM curves + number-at-risk table
- Hazard Ratio and p-value annotation box
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

from tflshell.figures.base import ClinicalFigure, _generate_mock_survival_data
from tflshell.figures.color_schemes import TRT_COLORS


def _km_estimate(times, events):
    """Compute Kaplan-Meier survival estimates with Greenwood CI.

    Returns:
        unique_times: sorted unique event/censor times
        survival: KM survival probability at each time
        ci_lower, ci_upper: 95% confidence interval bounds
        censor_flags: bool array, True if only censoring at this time
    """
    order = np.argsort(times)
    times_sorted = times[order]
    events_sorted = events[order].astype(bool)

    unique_times = []
    survival = []
    ci_lower = []
    ci_upper = []
    censor_flags = []
    variance = []
    var_at_time = []

    n_at_risk = len(times_sorted)
    current_survival = 1.0
    current_var = 0.0

    i = 0
    while i < len(times_sorted):
        t = times_sorted[i]
        n_events_at_t = 0
        n_censored_at_t = 0
        while i < len(times_sorted) and np.isclose(times_sorted[i], t):
            if events_sorted[i]:
                n_events_at_t += 1
            else:
                n_censored_at_t += 1
            i += 1

        n_before_event = n_at_risk - n_censored_at_t

        if n_events_at_t > 0 and n_before_event > 0:
            ratio = 1 - n_events_at_t / n_before_event
            current_survival *= ratio
            # Greenwood: var += d / (n * (n - d)), avoid div-by-zero when n == d
            denominator = n_before_event * (n_before_event - n_events_at_t)
            if denominator > 0:
                current_var += n_events_at_t / denominator

        n_at_risk -= (n_events_at_t + n_censored_at_t)

        se_factor = np.sqrt(current_var) if current_var > 0 else 0
        std_err = se_factor * max(current_survival, 1e-10)
        lower = max(0, current_survival - 1.96 * std_err)
        upper = min(1, current_survival + 1.96 * std_err)
        if current_survival <= 0:
            lower = 0
            upper = 0

        unique_times.append(t)
        survival.append(current_survival)
        ci_lower.append(lower)
        ci_upper.append(upper)
        censor_flags.append(n_censored_at_t > 0 and n_events_at_t == 0)

    return (np.array(unique_times), np.array(survival),
            np.array(ci_lower), np.array(ci_upper), np.array(censor_flags))


class KMCurveFigure(ClinicalFigure):
    """Kaplan-Meier survival curve for PFS or OS.

    Data schema:
        {
            "time_a": np.array, "event_a": np.array (bool),
            "time_b": np.array, "event_b": np.array (bool),
            "arm_a_label": str (default "Treatment A"),
            "arm_b_label": str (default "Treatment B"),
            "xlabel": str, "ylabel": str,
            "hr": float, "hr_ci_low": float, "hr_ci_high": float,
            "p_value": float or str,
            "risk_table_times": list (optional, timepoints for risk table),
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

        # Two-subplot layout: KM curves (3 parts) + risk table (1 part)
        fig, (ax_km, ax_risk) = plt.subplots(
            2, 1, figsize=(self.figsize[0], self.figsize[1] * 1.3),
            gridspec_kw={'height_ratios': [3, 1]}, sharex=True
        )

        # ---- KM estimates with CI ----
        t_a, s_a, ci_lo_a, ci_hi_a, c_a = _km_estimate(time_a, event_a)
        t_b, s_b, ci_lo_b, ci_hi_b, c_b = _km_estimate(time_b, event_b)

        color_a = TRT_COLORS.get("A", "#0072B2")
        color_b = TRT_COLORS.get("B", "#D55E00")

        # CI bands
        ax_km.fill_between(t_a, ci_lo_a, ci_hi_a, alpha=0.08, color=color_a, step="post")
        ax_km.fill_between(t_b, ci_lo_b, ci_hi_b, alpha=0.08, color=color_b, step="post")

        # Step function survival curves
        ax_km.step(t_a, s_a, where="post", color=color_a,
                   linewidth=1.8, label=f"{label_a} (N={len(time_a)})")
        ax_km.step(t_b, s_b, where="post", color=color_b,
                   linewidth=1.8, label=f"{label_b} (N={len(time_b)})")

        # Censoring marks
        for t, s, c, color in [(t_a, s_a, c_a, color_a), (t_b, s_b, c_b, color_b)]:
            for ti, si, ci in zip(t, s, c):
                if ci:
                    ax_km.plot(ti, si, marker="+", color=color,
                               markersize=6, markeredgewidth=1.2)

        # Axes
        ax_km.set_ylabel(ylabel, fontsize=10, fontweight="bold")
        max_time = max(max(t_a) if len(t_a) else 24, max(t_b) if len(t_b) else 24)
        ax_km.set_xlim(0, max_time * 1.05)
        ax_km.set_ylim(0, 1.02)
        ax_km.yaxis.set_major_locator(MultipleLocator(0.2))
        ax_km.grid(True, alpha=0.3, linestyle=":")

        # HR/p-value annotation box
        ann_text = (f"HR = {hr:.2f} (95% CI: {hr_lo:.2f}–{hr_hi:.2f})\n"
                    f"p = {p_val}")
        ax_km.text(0.97, 0.15, ann_text, transform=ax_km.transAxes,
                   fontsize=9, verticalalignment="bottom", horizontalalignment="right",
                   bbox=dict(boxstyle="round,pad=0.4", facecolor="white",
                             edgecolor="#CCCCCC", alpha=0.95))

        # Censoring annotation
        ax_km.annotate('+ Censored', xy=(0.02, 0.12), xycoords='axes fraction',
                       fontsize=7, fontstyle='italic', color='gray')

        # Legend
        ax_km.legend(loc="upper right", frameon=True,
                     facecolor="white", edgecolor="#DDDDDD", fontsize=8)

        # ---- Number at risk table ----
        risk_times = data.get("risk_table_times",
                              list(np.linspace(0, max_time, 6)))

        ax_risk.set_xlim(0, max_time * 1.05)
        ax_risk.set_ylim(0, 1)
        ax_risk.axis("off")

        # Risk table text annotations
        col_width = 1.0 / len(risk_times)
        for j, t_val in enumerate(risk_times):
            ax_risk.text(j * col_width + col_width / 2, 0.85, f'{t_val:.0f}',
                         ha='center', va='center', fontsize=8,
                         fontweight='bold', transform=ax_risk.transAxes)

        for i, (label, times_arr, color) in enumerate([
            (label_a, time_a, color_a), (label_b, time_b, color_b)
        ]):
            y_pos = 0.55 - i * 0.25
            short_label = label.split(" ")[0] if " " in label else label
            ax_risk.text(-0.02, y_pos, short_label, ha='right', va='center',
                         fontsize=8, fontweight='bold', color=color,
                         transform=ax_risk.transAxes)

            for j, t_val in enumerate(risk_times):
                n_risk = np.sum(times_arr >= t_val)
                ax_risk.text(j * col_width + col_width / 2, y_pos, f'{n_risk:d}',
                             ha='center', va='center', fontsize=8,
                             transform=ax_risk.transAxes)

        ax_risk.text(0.5, -0.3, xlabel, ha='center', va='center',
                     fontsize=10, fontweight='bold', transform=ax_risk.transAxes)
        ax_risk.text(0, 1.15, 'Number at Risk', ha='left', va='center',
                     fontsize=8, fontweight='bold', transform=ax_risk.transAxes)

        plt.tight_layout()
        return fig


def build_km_mock_data():
    return _generate_mock_survival_data(200)
