"""Clinical color palettes for figures — colorblind-friendly.

Color schemes follow industry conventions for clinical trial reporting.
"""

# Treatment arm colors (colorblind-friendly: Wong's palette adapted)
TRT_COLORS = {
    "A": "#0072B2",  # Blue
    "B": "#D55E00",  # Vermillion/Orange
    "C": "#009E73",  # Bluish-green
}

TRT_COLORS_LIST = ["#0072B2", "#D55E00", "#009E73"]

# Best Overall Response colors (RECIST convention)
BOR_COLORS = {
    "CR": "#006837",   # Dark green
    "PR": "#66BD63",   # Medium green
    "SD": "#4575B4",   # Blue
    "PD": "#D73027",   # Red
    "NE": "#BDBDBD",   # Gray
}

BOR_ORDER = ["CR", "PR", "SD", "PD", "NE"]

# CTCAE Grade colors (modified from NCI CTCAE palette)
GRADE_COLORS = {
    1: "#FFF5CC",   # Very light yellow
    2: "#FED976",   # Light yellow
    3: "#FD8D3C",   # Orange
    4: "#E31A1C",   # Red
    5: "#800026",   # Dark red
}

# AE severity/relationship colors
AE_COLORS = {
    "Related": "#D73027",
    "Not Related": "#4575B4",
}

# Subgroup colors
SUBGROUP_COLORS = {
    "Overall": "#000000",
    "Age <65": "#0072B2",
    "Age >=65": "#D55E00",
    "Male": "#0072B2",
    "Female": "#D55E00",
}

# Reference line styles
REF_LINE_STYLE = {"color": "#666666", "linestyle": "--", "linewidth": 1.0, "alpha": 0.8}
THICK_REF_STYLE = {"color": "#666666", "linestyle": "-", "linewidth": 1.5, "alpha": 0.6}

# Confidence interval / band styling
CI_ALPHA = 0.15
CI_BAND_ALPHA = 0.2

# General plot styling
PLOT_STYLE = {
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "axes.edgecolor": "#333333",
    "axes.grid": False,
    "axes.titlesize": 12,
    "axes.labelsize": 10,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 8,
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
}
