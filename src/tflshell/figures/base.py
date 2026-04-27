"""Abstract base class for clinical figures.

All clinical figure types inherit from ClinicalFigure and implement:
  - build(data) -> plt.Figure
  - render(data) -> io.BytesIO (PNG buffer)
"""

import io
import matplotlib
matplotlib.use("Agg")  # Non-interactive backend — required for headless generation
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

from tflshell.figures import color_schemes


class ClinicalFigure(ABC):
    """Abstract base for all clinical figures.

    Subclasses must override build() to create the matplotlib Figure.

    Usage:
        fig = KMCurveFigure(figsize=(8, 5), dpi=150)
        buf = fig.render(data_dict)  # Returns BytesIO PNG buffer
    """

    def __init__(self, figsize=(6.5, 4.5), dpi=200):
        self.figsize = figsize
        self.dpi = dpi
        plt.style.use(color_schemes.PLOT_STYLE)

    @abstractmethod
    def build(self, data: dict) -> plt.Figure:
        """Build the matplotlib Figure from the provided data dict.

        Args:
            data: Figure-specific data dict. Each subclass documents its schema.

        Returns:
            matplotlib Figure object ready for rendering.
        """
        ...

    def render(self, data: dict) -> io.BytesIO:
        """Build figure, render to PNG in memory, return BytesIO buffer.

        The buffer is suitable for embedding in DOCX via python-docx.
        """
        fig = self.build(data)
        buf = io.BytesIO()
        fig.savefig(buf, format="png", dpi=self.dpi, bbox_inches="tight",
                    facecolor="white", edgecolor="none")
        buf.seek(0)
        plt.close(fig)  # Free memory — critical for batch generation
        return buf


def _generate_mock_demographics(n=300, seed=42):
    """Generate mock demographics data for figures."""
    import numpy as np
    rng = np.random.default_rng(seed)
    arms = ["Treatment A"] * (n // 2) + ["Treatment B"] * (n - n // 2)
    ages = rng.normal(58, 12, n).clip(18, 90)
    sex = rng.choice(["Male", "Female"], n)
    return {"arm": arms, "age": ages, "sex": sex}


def _generate_mock_survival_data(n=300, seed=42):
    """Generate mock survival data for KM curves."""
    import numpy as np
    rng = np.random.default_rng(seed)
    half = n // 2
    arm_a_time = rng.weibull(1.2, half) * 12
    arm_b_time = rng.weibull(1.5, n - half) * 14
    arm_a_event = rng.binomial(1, 0.7, half).astype(bool)
    arm_b_event = rng.binomial(1, 0.6, n - half).astype(bool)
    return {
        "time_a": arm_a_time, "event_a": arm_a_event,
        "time_b": arm_b_time, "event_b": arm_b_event,
    }


def _generate_mock_tumor_data(n=200, seed=42):
    """Generate mock tumor response data for waterfall/spider/swimmer."""
    import numpy as np
    rng = np.random.default_rng(seed)
    best_pct = rng.normal(-25, 30, n)
    best_pct = np.clip(best_pct, -100, 200)
    bor = []
    for pct in best_pct:
        if pct <= -100:
            bor.append("CR")
        elif pct <= -30:
            bor.append("PR")
        elif pct <= 20:
            bor.append("SD")
        else:
            bor.append("PD")
    duration = rng.exponential(12, n)
    ttr = rng.exponential(3, n)  # time to response
    return {"best_pct": best_pct, "bor": bor, "duration": duration, "ttr": ttr}


def _generate_mock_lab_data(n=200, seed=42):
    """Generate mock lab data for box/longitudinal plots."""
    import numpy as np
    rng = np.random.default_rng(seed)
    visits = ["Baseline", "Week 4", "Week 8", "Week 12", "Week 16"]
    arms = ["Treatment A", "Treatment B"]
    data = {}
    for arm in arms:
        for param in ["ALT (U/L)", "AST (U/L)", "ALP (U/L)"]:
            baseline = rng.lognormal(3.5, 0.4, n)
            key = f"{arm}_{param}"
            data[key] = {visits[0]: baseline}
            for i, v in enumerate(visits[1:], 1):
                data[key][v] = baseline + rng.normal(-2, 8, n) * i
    return data


def _generate_mock_ae_data(seed=42):
    """Generate mock AE frequency data."""
    import numpy as np
    rng = np.random.default_rng(seed)
    soc_pt = {
        "Gastrointestinal disorders": [
            ("Nausea", 25, 18), ("Diarrhea", 20, 15), ("Vomiting", 15, 10),
            ("Constipation", 12, 14), ("Abdominal pain", 10, 8),
        ],
        "General disorders": [
            ("Fatigue", 30, 22), ("Asthenia", 18, 15), ("Pyrexia", 12, 10),
        ],
        "Skin disorders": [
            ("Rash", 20, 8), ("Pruritus", 10, 6),
        ],
        "Nervous system disorders": [
            ("Headache", 15, 12), ("Dizziness", 10, 8),
        ],
    }
    return soc_pt


def _generate_mock_subgroup_data(seed=42):
    """Generate mock subgroup analysis data for forest plots."""
    import numpy as np
    rng = np.random.default_rng(seed)
    subgroups = [
        ("Overall", None),
        ("Age <65", None), ("Age >=65", None),
        ("Male", None), ("Female", None),
        ("ECOG 0", None), ("ECOG 1", None),
        ("Prior Therapy 0-1", None), ("Prior Therapy >=2", None),
    ]
    result = []
    for i, (name, _) in enumerate(subgroups):
        hr = rng.normal(0.75, 0.15)
        hr = max(0.3, min(1.5, hr))
        ci_low = hr * rng.uniform(0.7, 0.9)
        ci_high = hr * rng.uniform(1.1, 1.4)
        result.append({
            "subgroup": name,
            "hr": hr,
            "ci_low": ci_low,
            "ci_high": ci_high,
            "n_trt_a": rng.integers(100, 150),
            "n_trt_b": rng.integers(100, 150),
            "events_a": rng.integers(30, 80),
            "events_b": rng.integers(30, 80),
        })
    return result
