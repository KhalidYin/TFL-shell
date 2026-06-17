"""TFL Shell Catalog v2.3 — controlled multi-arm-expansion shell library.

Column convention for standard controlled tables:
  Col 0 = structural labels (first column)
  Col 1 = Group 1 (N=XX)
  Col 2 = Group 2 (N=XX)
  Col 3 = ... (expansion placeholder for additional groups where applicable)
  Col 4 = Overall (N=XX) only where clinically standard and explicitly retained

Placeholder styles per column type:
  n (%)   → xx (xx.x)
  Count   → xx
  Mean SD → xx.x (xx.x)
  CI      → [xx.x, xx.x]
  HR/p    → x.xx / x.xxx

Section 14.4: Tables + Figures ONLY (no listings).
Section 16.2: All patient-level listings (including PK/ADA/Biomarker moved from 14.4).
"""

from tflshell.data.common import F, L, S141, S142, S143, S144, S162, T, TFLItem
from tflshell.data.sections.section_14_1 import build_14_1_items
from tflshell.data.sections.section_14_2 import build_14_2_items
from tflshell.data.sections.section_14_3 import build_14_3_items
from tflshell.data.sections.section_14_4 import build_14_4_items
from tflshell.data.sections.section_16_2 import build_16_2_items
from tflshell.models.catalog import TFLCatalog
from tflshell.models.enums import Section, TFLType


def _default_shell_family(item: TFLItem) -> str:
    title = item.title.lower()
    if item.section == S141:
        return "Demographics and Baseline"
    if item.section == S142:
        if item.non_oncology_only:
            return "Non-Oncology Efficacy"
        if item.oncology_only:
            return "Oncology Efficacy"
        return "General Efficacy"
    if item.section == S143:
        if any(keyword in title for keyword in ("dose-limiting", "mtd", "rp2d", "holter")):
            return "Phase I Safety and Dose Escalation"
        return "Safety"
    if item.section == S144:
        if any(
            keyword in title for keyword in ("food effect", "crossover", "relative bioavailability")
        ):
            return "Phase I Clinical Pharmacology"
        return "Special Assessments"
    if item.section == S162:
        if any(keyword in title for keyword in ("dose-limiting", "food-effect", "clinical events")):
            return "Specialized Patient Listings"
        if item.non_oncology_only:
            return "Non-Oncology Listings"
        if item.oncology_only:
            return "Oncology Listings"
        return "Patient Listings"
    return item.section.title


def _default_study_phase_scope(item: TFLItem) -> str:
    title = item.title.lower()
    if any(
        keyword in title
        for keyword in (
            "dose-limiting",
            "mtd",
            "rp2d",
            "food effect",
            "crossover",
            "relative bioavailability",
        )
    ):
        return "Phase I"
    if item.non_oncology_only and item.section == S142:
        return "Phase II-III"
    if item.oncology_only and item.section in (S142, S162):
        return "Phase I-III (oncology-focused)"
    if item.section in (S141, S143, S162):
        return "Phase I-III"
    if item.section == S142:
        return "Phase I-III (conditional for Phase I)"
    if item.section == S144:
        return "Phase I-III (core in Phase I; conditional in Phase II-III)"
    return "Phase I-III"


def _default_coverage_summary(item: TFLItem) -> str:
    title = item.title.lower()
    if any(keyword in title for keyword in ("dose-limiting", "mtd", "rp2d")):
        return "Core (Phase I)"
    if any(
        keyword in title for keyword in ("food effect", "crossover", "relative bioavailability")
    ):
        return "Conditional (Phase I)"
    if item.non_oncology_only and item.section == S142:
        return "Core (Phase II-III, Non-Oncology)"
    if item.non_oncology_only and item.section == S162:
        return "Conditional (Phase II-III, Non-Oncology)"
    if item.oncology_only and item.section in (S142, S162):
        return "Core (Oncology)"
    if item.section in (S141, S143, S162):
        return "Core"
    if item.section == S142:
        return "Core (Phase II-III); Conditional (Phase I)"
    if item.section == S144:
        return "Core (Phase I); Conditional (Phase II-III)"
    return "Core"


def _apply_governance_metadata(items: list[TFLItem]) -> None:
    for item in items:
        if item.placeholder_columns:
            _normalize_shell_rows(item)
        if not item.shell_family:
            item.shell_family = _default_shell_family(item)
        if not item.study_phase_scope:
            item.study_phase_scope = _default_study_phase_scope(item)
        if not item.coverage_summary:
            item.coverage_summary = _default_coverage_summary(item)


def _normalize_controlled_text(text: str) -> str:
    replacements = {
        "XXX Group 1": "Group 1",
        "XXX Group 2": "Group 2",
        "Treatment A": "Group 1",
        "Treatment B": "Group 2",
        "Group1": "Group 1",
        "Group2": "Group 2",
        "G1": "Group 1",
        "G2": "Group 2",
        "Gx": "Group",
        "Control": "Group 2",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def _normalize_placeholder_columns(columns: list[str]) -> list[str]:
    normalized: list[str] = []
    for col in columns:
        text = _normalize_controlled_text(col)
        if text.startswith("...\n...\n"):
            normalized.append("...")
            normalized.append(text.replace("...\n...\n", "", 1))
        else:
            normalized.append(text)
    return normalized


def _normalize_shell_rows(item: TFLItem) -> None:
    normalized_rows = []
    data_col_count = max(len(item.placeholder_columns) - 1, 0)
    for row in item.shell_rows:
        rich = item._normalize_row(row)
        rich["label"] = _normalize_controlled_text(rich["label"])
        rich["values"] = [_normalize_controlled_text(str(value)) for value in rich["values"]]
        if data_col_count:
            if not rich["values"]:
                rich["values"] = [""] * data_col_count
            elif len(rich["values"]) > data_col_count:
                rich["values"] = rich["values"][:data_col_count]
            elif len(rich["values"]) < data_col_count:
                rich["values"].extend([""] * (data_col_count - len(rich["values"])))
        normalized_rows.append(rich)
    item.shell_rows = normalized_rows


def _assign_controlled_source_listing(item: TFLItem) -> None:
    if item.tfl_type == L:
        item.source_listing = item.id
        return

    title = item.title.lower()
    program_ref = item.program_ref.lower() if item.program_ref else ""

    if any(
        token in title
        for token in (
            "tumor response",
            "best overall response",
            "objective response",
            "disease control",
            "target lesion",
            "waterfall",
            "spider",
            "swimmer",
        )
    ):
        item.source_listing = "L16.2.10"
        return
    if any(
        token in title
        for token in (
            "progression-free survival",
            "overall survival",
            "duration of response",
            "time to response",
            "time to first subsequent therapy",
            "landmark os",
            "landmark analysis",
            "forest plot",
            "pfs status",
        )
    ):
        item.source_listing = "L16.2.11"
        if "subsequent therapy" in title:
            item.source_listing = "L16.2.19"
        return
    if any(token in title for token in ("subsequent anti-cancer", "tfst")):
        item.source_listing = "L16.2.19"
        return
    if any(
        token in title
        for token in (
            "primary efficacy",
            "secondary efficacy",
            "sensitivity analysis",
            "non-inferiority",
            "tipping point",
        )
    ):
        item.source_listing = "L16.2.3"
        return
    if any(token in title for token in ("respiratory exacerbation",)):
        item.source_listing = "L16.2.35"
        return
    if any(token in title for token in ("cardiovascular", "mace", "heart failure hospitalization")):
        item.source_listing = "L16.2.36"
        return
    if (
        any(token in title for token in ("autoimmune flare", "responder"))
        and item.non_oncology_only
    ):
        item.source_listing = "L16.2.37"
        return
    if (
        any(token in title for token in ("clinical event", "exacerbation"))
        and item.non_oncology_only
    ):
        item.source_listing = "L16.2.34"
        return
    if any(token in title for token in ("dose-limiting", "mtd", "rp2d")):
        item.source_listing = "L16.2.32"
        return
    if any(token in title for token in ("food effect", "crossover", "relative bioavailability")):
        item.source_listing = "L16.2.33"
        return
    if any(
        token in title for token in ("pk concentration", "pk concentrations", "concentration-time")
    ):
        item.source_listing = "L16.2.14"
        return
    if any(
        token in title
        for token in (
            "pk parameter",
            "pk parameters",
            "ctrough",
            "steady-state",
            "urine pk",
            "pharmacokinetic (pk) plot",
            "pk plot",
        )
    ):
        item.source_listing = "L16.2.15"
        return
    if any(token in title for token in ("ada", "neutralizing antibody", "nab")):
        item.source_listing = "L16.2.16"
        return
    if any(token in title for token in ("biomarker", "gene aberration", "pd ")) or program_ref in {
        "t_pd_summary.sas",
        "t_pd_bio_chg.sas",
        "f_pd_time.sas",
        "f_biomarker_box.sas",
    }:
        item.source_listing = "L16.2.17"
        return
    if (
        any(token in title for token in ("quality of life", "pro "))
        or program_ref == "t_pro_summary.sas"
    ):
        item.source_listing = "L16.2.18"
        return
    if any(
        token in title
        for token in (
            "adverse event",
            "teae",
            "aesi",
            "infusion-related",
            "serious adverse",
            "deaths",
            "hy's law",
            "hys law",
        )
    ):
        if "hys" in title:
            item.source_listing = "L16.2.23"
        elif "aesi" in title:
            item.source_listing = "L16.2.22"
        elif "death" in title:
            item.source_listing = "L16.2.20"
        elif "serious" in title:
            item.source_listing = "L16.2.5"
        elif "infusion-related" in title:
            item.source_listing = "L16.2.29"
        else:
            item.source_listing = "L16.2.4"
        return
    if any(token in title for token in ("concomitant medication", "medication")):
        item.source_listing = "L16.2.6"
        return
    if any(
        token in title
        for token in (
            "analysis populations",
            "study drug exposure",
            "exposure by duration",
            "dose intensity",
            "dose modifications",
        )
    ):
        item.source_listing = "L16.2.12"
        return
    if any(
        token in title
        for token in ("surgical and procedure history", "anti-cancer surgery", "radiotherapy")
    ):
        item.source_listing = "L16.2.21"
        return
    if any(token in title for token in ("laboratory", "hematology", "chemistry")):
        item.source_listing = "L16.2.7"
        return
    if any(
        token in title
        for token in ("vital sign", "weight", "spo2", "respiratory rate", "temperature")
    ):
        item.source_listing = "L16.2.8"
        return
    if any(token in title for token in ("ecg", "qtcf", "holter")):
        item.source_listing = "L16.2.9"
        return
    if any(token in title for token in ("ecog performance status",)):
        item.source_listing = "L16.2.13"
        return
    if any(token in title for token in ("physical examination",)):
        item.source_listing = "L16.2.24"
        return
    if any(token in title for token in ("urinalysis", "urine chemistry")):
        item.source_listing = "L16.2.25"
        return
    if any(token in title for token in ("coagulation",)):
        item.source_listing = "L16.2.26"
        return
    if any(token in title for token in ("cardiac biomarkers", "immunoglobulin")):
        item.source_listing = "L16.2.27"
        return
    if any(token in title for token in ("lymphocyte", "cytokine")):
        item.source_listing = "L16.2.28"
        return
    if any(token in title for token in ("demographic", "baseline")):
        item.source_listing = "L16.2.2"
        return
    if any(token in title for token in ("disposition", "screen failure")):
        item.source_listing = "L16.2.1"
        return
    if any(token in title for token in ("protocol deviation", "estimand strategy")):
        item.source_listing = "L16.2.3"
        return
    if item.source_listing == "L16.2.1 / L16.2.2":
        item.source_listing = ""


def _normalize_controlled_shells(items: list[TFLItem]) -> list[TFLItem]:
    removed_ids = {"T14.2.3", "T14.2.17", "T14.2.18", "T14.3.1.11", "T14.3.1.12"}
    retained: list[TFLItem] = []

    for item in items:
        if item.id in removed_ids:
            continue

        item.placeholder_columns = _normalize_placeholder_columns(item.placeholder_columns)
        _normalize_shell_rows(item)
        item.population = _normalize_controlled_text(item.population)
        item.figure_description = _normalize_controlled_text(item.figure_description)
        item.footnotes = [_normalize_controlled_text(note) for note in item.footnotes]
        item.dataset_source = _normalize_controlled_text(item.dataset_source)
        _assign_controlled_source_listing(item)
        retained.append(item)

    return retained


def build_catalog() -> TFLCatalog:
    items: list[TFLItem] = []

    items.extend(build_14_1_items())
    items.extend(build_14_2_items())
    items.extend(build_14_3_items())
    items.extend(build_14_4_items())
    items.extend(build_16_2_items())

    items = _normalize_controlled_shells(items)
    _apply_governance_metadata(items)
    return TFLCatalog(items)
