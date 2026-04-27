"""Mock clinical data generation for TFL figure rendering.

Each function returns a dict suitable for consumption by ClinicalFigure.build().
Uses numpy with fixed seeds for reproducibility.
"""

import numpy as np

DEFAULT_SEED = 42


def mock_demographics(n=300, seed=DEFAULT_SEED):
    """Generate mock demographics data."""
    rng = np.random.default_rng(seed)
    half = n // 2
    arms = ["Treatment A"] * half + ["Treatment B"] * (n - half)
    ages = rng.normal(58, 12, n).clip(18, 90)
    sex = rng.choice(["Male", "Female"], n, p=[0.55, 0.45])
    race = rng.choice(["White", "Black", "Asian", "Other"], n, p=[0.7, 0.1, 0.15, 0.05])
    bmi = rng.normal(26, 5, n).clip(16, 45)
    return {"arm": arms, "age": ages, "sex": sex, "race": race, "bmi": bmi}


def mock_survival_data(n=300, seed=DEFAULT_SEED):
    """Generate mock PFS/OS data with realistic event distributions.

    Returns data suitable for KMCurveFigure.
    """
    rng = np.random.default_rng(seed)
    half = n // 2
    arm_a_time = rng.weibull(1.3, half) * 10
    arm_b_time = rng.weibull(1.6, n - half) * 12
    arm_a_event = rng.binomial(1, 0.72, half).astype(bool)
    arm_b_event = rng.binomial(1, 0.62, n - half).astype(bool)
    # Admin censoring at 36 months
    arm_a_time = np.minimum(arm_a_time, 36)
    arm_b_time = np.minimum(arm_b_time, 36)
    return {
        "time_a": arm_a_time, "event_a": arm_a_event,
        "time_b": arm_b_time, "event_b": arm_b_event,
        "arm_a_label": "Treatment A", "arm_b_label": "Treatment B",
        "ylabel": "Survival Probability",
        "hr": 0.72, "hr_ci_low": 0.58, "hr_ci_high": 0.89,
        "p_value": 0.004,
    }


def mock_pfs_data(n=300, seed=DEFAULT_SEED):
    """Generate mock PFS-specific data."""
    data = mock_survival_data(n, seed)
    data["ylabel"] = "Progression-Free Survival Probability"
    data["hr"] = 0.68
    data["hr_ci_low"] = 0.54
    data["hr_ci_high"] = 0.85
    data["p_value"] = 0.002
    return data


def mock_tumor_data(n=200, seed=DEFAULT_SEED):
    """Generate mock tumor response data for waterfall/spider/swimmer."""
    rng = np.random.default_rng(seed)
    best_pct = rng.normal(-25, 32, n).clip(-100, 200)
    bor = []
    for pct in best_pct:
        if pct < -100: bor.append("CR")
        elif pct < -30: bor.append("PR")
        elif pct < 20: bor.append("SD")
        else: bor.append("PD")
    duration = rng.exponential(12, n) + 2
    ttr = rng.exponential(3.5, n) + 1
    return {"best_pct": best_pct, "bor": bor, "duration": duration, "ttr": ttr}


def mock_lab_data(n=200, seed=DEFAULT_SEED):
    """Generate mock lab data for box/longitudinal plots."""
    rng = np.random.default_rng(seed)
    visits = ["Baseline", "Week 4", "Week 8", "Week 12", "Week 16"]
    arms = ["Treatment A", "Treatment B"]
    data = {"visits": visits}
    for arm_prefix, mean_shift in [("arm_a", 0.0), ("arm_b", -0.15)]:
        for param in ["ALT (U/L)", "AST (U/L)", "ALP (U/L)"]:
            baseline = rng.lognormal(3.5, 0.4, n)
            key = f"{arm_prefix}_{param}"
            data[key] = {visits[0]: baseline.tolist()}
            for i, v in enumerate(visits[1:], 1):
                shifted = baseline + rng.normal(mean_shift * i * 2, 6, n)
                data[key][v] = shifted.tolist()
    return data


def mock_vital_signs_data(n=200, seed=DEFAULT_SEED):
    """Generate mock vital signs data."""
    rng = np.random.default_rng(seed)
    visits = ["Baseline", "Week 2", "Week 4", "Week 8", "Week 12", "Week 16"]
    return {
        "visits": visits,
        "arm_a_sbp_mean": [128, 127, 126, 125, 125, 124],
        "arm_a_sbp_sd": [12, 13, 12, 11, 13, 12],
        "arm_b_sbp_mean": [129, 128, 128, 127, 127, 126],
        "arm_b_sbp_sd": [11, 12, 11, 13, 12, 11],
    }


def mock_ae_data(seed=DEFAULT_SEED):
    """Generate mock AE frequencies by SOC/PT."""
    import numpy as np
    rng = np.random.default_rng(seed)
    return {
        "Gastrointestinal disorders": [
            ("Nausea", 25, 18, 6, 2),
            ("Diarrhea", 20, 15, 4, 1),
            ("Vomiting", 15, 10, 3, 1),
            ("Constipation", 12, 14, 2, 0),
        ],
        "General disorders": [
            ("Fatigue", 30, 22, 5, 1),
            ("Asthenia", 18, 15, 4, 2),
            ("Pyrexia", 12, 10, 2, 0),
        ],
        "Skin disorders": [
            ("Rash", 20, 8, 3, 1),
            ("Pruritus", 10, 6, 1, 0),
        ],
        "Nervous system disorders": [
            ("Headache", 15, 12, 2, 0),
            ("Dizziness", 10, 8, 2, 0),
        ],
    }


def mock_subgroup_data(seed=DEFAULT_SEED):
    """Generate mock forest plot subgroup data."""
    rng = np.random.default_rng(seed)
    subgroups = [
        "Overall", "Age <65", "Age >=65", "Male", "Female",
        "ECOG 0", "ECOG 1", "Prior Therapy 0-1", "Prior Therapy >=2",
        "Non-Smoker", "Smoker",
    ]
    result = []
    for name in subgroups:
        hr = rng.normal(0.75, 0.12)
        hr = max(0.3, min(1.5, hr))
        ci_ratio = rng.uniform(0.12, 0.22)
        result.append({
            "subgroup": name,
            "hr": hr,
            "ci_low": max(0.15, hr - ci_ratio),
            "ci_high": min(3.0, hr + ci_ratio),
            "n_trt_a": rng.integers(80, 150),
            "n_trt_b": rng.integers(80, 150),
            "events_a": rng.integers(25, 75),
            "events_b": rng.integers(25, 75),
        })
    return {"rows": result}
