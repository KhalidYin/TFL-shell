"""Shared catalog constants and templates."""

from tflshell.models.enums import Section, TFLType
from tflshell.models.tfl_item import TFLItem

T, F, L = TFLType.TABLE, TFLType.FIGURE, TFLType.LISTING
S141, S142, S143, S144 = (
    Section.SEC_14_1,
    Section.SEC_14_2,
    Section.SEC_14_3,
    Section.SEC_14_4,
)
S162 = Section.SEC_16_2

H2_SIMPLE = [
    "Parameter\nCategory / Statistic",
    "Group 1\n(N=XX)",
    "Group 2\n(N=XX)",
    "...",
    "Overall\n(N=XX)",
]
H2_NPCT = [
    "Parameter\nCategory",
    "Group 1\n(N=XX)\nn (%)",
    "Group 2\n(N=XX)\nn (%)",
    "...",
    "Overall\n(N=XX)\nn (%)",
]
H2_SOCPT = [
    "System Organ Class\nPreferred Term",
    "Group 1\n(N=XX)\nn (%)",
    "Group 2\n(N=XX)\nn (%)",
    "...",
    "Overall\n(N=XX)\nn (%)",
]
H2_EVENTS = [
    "Parameter\nCategory",
    "Group 1\n(N=XX)\nn (%) [E]",
    "Group 2\n(N=XX)\nn (%) [E]",
    "...",
    "Overall\n(N=XX)\nn (%) [E]",
]
H2_EFF = [
    "Endpoint\nStatistic",
    "Group 1\n(N=XX)",
    "Group 2\n(N=XX)",
    "...",
    "Overall\n(N=XX)",
]
H2_LAB = [
    "Parameter\nVisit",
    "Statistic",
    "Group 1\n(N=XX)",
    "Group 2\n(N=XX)",
    "...",
    "Overall\n(N=XX)",
]

MODEL_COMPARISON_HEADER = [
    [
        {"label": "Parameter / Visit / Statistic", "rowspan": 2, "alignment": "left"},
        {"label": "Treatment Estimates", "colspan": 2},
        {"label": "Treatment Comparison", "colspan": 2},
    ],
    [
        {"label": "Group 1\n(N=XX)"},
        {"label": "Group 2\n(N=XX)"},
        {"label": "Group 1 vs Group 2\nEstimate"},
        {"label": "95% CI / p-value"},
    ],
]

EROW = ["[Additional rows omitted in master shell]", "", "", ""]
EROW5 = ["[Additional rows omitted in master shell]", "", "", "", ""]
EROW6 = ["[Additional rows omitted in master shell]", "", "", "", "", ""]
