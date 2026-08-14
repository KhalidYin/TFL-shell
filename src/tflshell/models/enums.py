"""Enumerations for TFL shell domain v2.1."""

from enum import Enum


class TFLType(Enum):
    TABLE = "Table"
    FIGURE = "Figure"
    LISTING = "Listing"


class Section(Enum):
    SEC_14_1 = ("14.1", "Demographics and Baseline Characteristics")
    SEC_14_2 = ("14.2", "Efficacy Analysis")
    SEC_14_3 = ("14.3", "Safety Analysis")
    SEC_14_4 = ("14.4", "Special Assessments")
    SEC_16_2 = ("16.2", "Patient Data Listings")

    def __init__(self, number: str, title: str):
        self._number = number
        self._title = title

    @property
    def number(self) -> str:
        return self._number

    @property
    def title(self) -> str:
        return self._title

    @classmethod
    def from_number(cls, number: str):
        for section in cls:
            if section.number == number:
                return section
        raise ValueError(f"Unknown section number: {number}")


class TherapeuticArea(Enum):
    ONCOLOGY = "Oncology"
    NON_ONCOLOGY = "Non-Oncology"
    GENERAL = "General"


class FigureType(Enum):
    KM_CURVE = "km_curve"
    WATERFALL = "waterfall"
    SPIDER = "spider"
    SWIMMER = "swimmer"
    FOREST = "forest"
    BOX_PLOT = "box_plot"
    LONGITUDINAL = "longitudinal"
    CDF = "cdf"
    EDISH = "edish"
    LAB_TOXICITY_HEATMAP = "lab_toxicity_heatmap"
    CONCENTRATION_QTC = "concentration_qtc"
    PK_PROFILE = "pk_profile"
    FOOD_EFFECT_PROFILE = "food_effect_profile"


class TFLStatus(Enum):
    SHELL = "Shell"
    IN_PROGRESS = "In Progress"
    COMPLETE = "Complete"
    NA = "N/A"
