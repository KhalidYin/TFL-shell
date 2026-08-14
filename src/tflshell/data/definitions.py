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

import re

from tflshell.data.common import S141, S142, S143, S144, S162, L, T, TFLItem
from tflshell.data.sections.section_14_1 import build_14_1_items
from tflshell.data.sections.section_14_2 import build_14_2_items
from tflshell.data.sections.section_14_3 import build_14_3_items
from tflshell.data.sections.section_14_4 import build_14_4_items
from tflshell.data.sections.section_16_2 import build_16_2_items
from tflshell.models.catalog import TFLCatalog

# Abbreviations are added only when they occur in visible table information
# (title, population, columns, or row labels). Keep this list controlled so
# shell footnotes remain deterministic and reviewable.
CONTROLLED_TABLE_ABBREVIATIONS = (
    (r"\bAE\b", "AE", "adverse event"),
    (r"\bTEAE(?:s)?\b", "TEAE", "treatment-emergent adverse event"),
    (r"\bSAE(?:s)?\b", "SAE", "serious adverse event"),
    (r"\bAESI(?:s)?\b", "AESI", "adverse event of special interest"),
    (r"\bSOC\b", "SOC", "system organ class"),
    (r"\bPT(?:s)?\b", "PT", "preferred term"),
    (r"\bCTCAE\b", "CTCAE", "Common Terminology Criteria for Adverse Events"),
    (r"\bATC\b", "ATC", "Anatomical Therapeutic Chemical"),
    (r"\bWHO\b", "WHO", "World Health Organization"),
    (r"\bBL\b", "BL", "baseline"),
    (r"\bChg\b", "Chg", "change from baseline"),
    (r"\bWk\b", "Wk", "week"),
    (r"\bBMI\b", "BMI", "body mass index"),
    (r"\bECOG\b", "ECOG", "Eastern Cooperative Oncology Group"),
    (r"\bITT\b", "ITT", "intent-to-treat"),
    (r"\bFAS\b", "FAS", "full analysis set"),
    (r"\bPP\b", "PP", "per-protocol"),
    (r"\bPFS\b", "PFS", "progression-free survival"),
    (r"\bOS\b", "OS", "overall survival"),
    (r"\bTTD\b", "TTD", "time to treatment discontinuation"),
    (r"\bDOR\b", "DOR", "duration of response"),
    (r"\bTTR\b", "TTR", "time to response"),
    (r"\bTFST\b", "TFST", "time to first subsequent therapy"),
    (r"\bBOR\b", "BOR", "best overall response"),
    (r"\bORR\b", "ORR", "objective response rate"),
    (r"\bDCR\b", "DCR", "disease control rate"),
    (r"\bCR\b", "CR", "complete response"),
    (r"\bPR\b", "PR", "partial response"),
    (r"\bNE\b", "NE", "not evaluable"),
    (r"\bRECIST\b", "RECIST", "Response Evaluation Criteria in Solid Tumors"),
    (r"\bICR\b", "ICR", "independent central review"),
    (r"\bKM\b", "KM", "Kaplan-Meier"),
    (r"\bNI\b", "NI", "non-inferiority"),
    (r"\bMMRM\b", "MMRM", "mixed model for repeated measures"),
    (r"\bMAR\b", "MAR", "missing at random"),
    (r"\bCMH\b", "CMH", "Cochran-Mantel-Haenszel"),
    (r"\bLS\b", "LS", "least squares"),
    (r"\bSE\b", "SE", "standard error"),
    (r"\bCI\b", "CI", "confidence interval"),
    (r"\bHR\b", "HR", "hazard ratio"),
    (r"\bGMR\b", "GMR", "geometric mean ratio"),
    (r"\bCV\b", "CV", "coefficient of variation"),
    (r"\bPK\b", "PK", "pharmacokinetic"),
    (r"\bCmax\b", "Cmax", "maximum observed concentration"),
    (r"\bCmin\b", "Cmin", "minimum observed concentration"),
    (r"\bCtrough\b", "Ctrough", "trough concentration"),
    (r"\bTmax\b", "Tmax", "time to maximum observed concentration"),
    (r"\bCLr\b", "CLr", "renal clearance"),
    (r"\bMACE\b", "MACE", "major adverse cardiovascular event"),
    (r"\bALT\b", "ALT", "alanine aminotransferase"),
    (r"\bAST\b", "AST", "aspartate aminotransferase"),
    (r"\bALP\b", "ALP", "alkaline phosphatase"),
    (r"\bTBL\b", "TBL", "total bilirubin"),
    (r"\bULN\b", "ULN", "upper limit of normal"),
    (r"\bECG\b", "ECG", "electrocardiogram"),
    (r"\bQTcF\b", "QTcF", "QT interval corrected using Fridericia's formula"),
    (r"\bQRS\b", "QRS", "ventricular depolarization complex"),
    (r"\bBP\b", "BP", "blood pressure"),
    (r"\bRR\b", "RR", "respiratory rate"),
    (r"\bSBP\b", "SBP", "systolic blood pressure"),
    (r"\bDBP\b", "DBP", "diastolic blood pressure"),
    (r"\bSpO2\b", "SpO2", "peripheral oxygen saturation"),
    (r"\bINR\b", "INR", "international normalized ratio"),
    (r"\bHDL-C\b", "HDL-C", "high-density lipoprotein cholesterol"),
    (r"\bLDL-C\b", "LDL-C", "low-density lipoprotein cholesterol"),
    (r"\bTSH\b", "TSH", "thyroid-stimulating hormone"),
    (r"\bCK-MB\b", "CK-MB", "creatine kinase-MB"),
    (r"\bNT-proBNP\b", "NT-proBNP", "N-terminal pro-B-type natriuretic peptide"),
    (r"\bAKI\b", "AKI", "acute kidney injury"),
    (r"\bKDIGO\b", "KDIGO", "Kidney Disease: Improving Global Outcomes"),
    (r"\bUPCR\b", "UPCR", "urine protein-to-creatinine ratio"),
    (r"\bIRR\b", "IRR", "infusion-related reaction"),
    (r"\bDLT(?:s)?\b", "DLT", "dose-limiting toxicity"),
    (r"\bMTD\b", "MTD", "maximum tolerated dose"),
    (r"\bRP2D\b", "RP2D", "recommended Phase II dose"),
    (r"\bADA\b", "ADA", "anti-drug antibody"),
    (r"\bN[Aa]b\b", "NAb", "neutralizing antibody"),
    (r"\bPRO\b", "PRO", "patient-reported outcome"),
    (r"\bEORTC\b", "EORTC", "European Organisation for Research and Treatment of Cancer"),
    (r"\bQLQ-C30\b", "QLQ-C30", "Quality of Life Questionnaire-Core 30"),
    (r"\bGHS\b", "GHS", "global health status"),
    (r"\bANOVA\b", "ANOVA", "analysis of variance"),
    (r"\bAUC(?:0)?\b", "AUC", "area under the concentration-time curve"),
    (r"\bHbA1c\b", "HbA1c", "glycated hemoglobin"),
    (r"\bFPG\b", "FPG", "fasting plasma glucose"),
    (r"\bEGFR\b", "EGFR", "epidermal growth factor receptor"),
    (r"\beGFR\b", "eGFR", "estimated glomerular filtration rate"),
    (r"\bPD-L1\b", "PD-L1", "programmed death-ligand 1"),
    (r"\bTPS\b", "TPS", "tumor proportion score"),
    (r"\bEOT\b", "EOT", "end of treatment"),
    (r"\bTC\b", "TC", "total cholesterol"),
    (r"\bTG\b", "TG", "triglycerides"),
    (r"(?<!-)\bHDL\b(?!-)", "HDL", "high-density lipoprotein"),
    (r"(?<!-)\bLDL\b(?!-)", "LDL", "low-density lipoprotein"),
    (r"\bNCEP\b", "NCEP", "National Cholesterol Education Program"),
    (r"\bATP\b", "ATP", "Adult Treatment Panel"),
    (r"\bT3\b", "T3", "triiodothyronine"),
    (r"\bT4\b", "T4", "thyroxine"),
    (r"\bIgG\b", "IgG", "immunoglobulin G"),
    (r"\bIgA\b", "IgA", "immunoglobulin A"),
    (r"\bIgM\b", "IgM", "immunoglobulin M"),
    (r"\bIgE\b", "IgE", "immunoglobulin E"),
    (r"\bCD3\b", "CD3", "cluster of differentiation 3"),
    (r"\bCD4\b", "CD4", "cluster of differentiation 4"),
    (r"\bCD8\b", "CD8", "cluster of differentiation 8"),
    (r"\bCD19\b", "CD19", "cluster of differentiation 19"),
    (r"\bCD16\b", "CD16", "cluster of differentiation 16"),
    (r"\bCD56\b", "CD56", "cluster of differentiation 56"),
    (r"\bNK\b", "NK", "natural killer"),
    (r"\bIL-6\b", "IL-6", "interleukin 6"),
    (r"\bIL-1b(?:eta)?\b", "IL-1beta", "interleukin 1 beta"),
    (r"\bIL-10\b", "IL-10", "interleukin 10"),
    (r"\bTNF-a(?:lpha)?\b", "TNF-alpha", "tumor necrosis factor alpha"),
    (r"\bIFN-g(?:amma)?\b", "IFN-gamma", "interferon gamma"),
    (r"\bICH\b", "ICH", "International Council for Harmonisation"),
    (r"\bE2A\b", "E2A", "ICH Clinical Safety Data Management guidance"),
    (r"\bHMG-CoA\b", "HMG-CoA", "3-hydroxy-3-methylglutaryl-coenzyme A"),
)


def _visible_table_text(item: TFLItem) -> str:
    row_labels = [item._normalize_row(row)["label"] for row in item.shell_rows]
    return " ".join((item.title, item.population, *item.placeholder_columns, *row_labels))


def _table_abbreviation_definitions(item: TFLItem) -> list[str]:
    text = " ".join((_visible_table_text(item), *item.footnotes))
    definitions = [
        f"{label} = {meaning}"
        for pattern, label, meaning in CONTROLLED_TABLE_ABBREVIATIONS
        if re.search(pattern, text)
    ]
    response_context = bool(
        re.search(r"\b(?:CR|PR|PD|BOR|ORR|DCR|RECIST)\b|\bresponse\b", text, re.I)
    )
    if re.search(r"Mean\s*\(SD\)", text):
        definitions.append("SD = standard deviation")
    if response_context and re.search(r"\bSD\b", text):
        definitions.append("SD (response) = stable disease")
    elif re.search(r"\bSD\b", text):
        definitions.append("SD = standard deviation")
    if re.search(r"\bPD\b", text):
        meaning = (
            "progressive disease"
            if re.search(r"\b(?:CR|PR|BOR|ORR|DCR)\b", text)
            else "pharmacodynamic"
        )
        definitions.append(f"PD = {meaning}")
    return list(dict.fromkeys(definitions))


def _enrich_table_definition_footnotes(item: TFLItem) -> None:
    if item.tfl_type != T:
        return

    visible_text = _visible_table_text(item)
    abbreviations = _table_abbreviation_definitions(item)
    if abbreviations:
        item.footnotes.append("Abbreviations: " + "; ".join(abbreviations) + ".")

    definitions: list[str] = []
    percentage_display = bool(re.search(r"\bn\s*(?:/\s*N\d*)?\s*\(%\)", visible_text))
    ratio_display = bool(re.search(r"\bn\s*/\s*N\d*\b", visible_text))
    if percentage_display:
        if not item.denominator_note:
            if any(token in visible_text for token in ("AE", "TEAE", "SAE", "AESI")):
                item.denominator_note = (
                    "Percentages use the number of subjects in the Safety Population within "
                    "each treatment group unless otherwise specified."
                )
            elif "Visit" in visible_text or "Cycle" in visible_text:
                item.denominator_note = (
                    "Percentages use subjects evaluable at the corresponding visit or cycle "
                    "within each treatment group unless otherwise specified."
                )
            else:
                item.denominator_note = (
                    "Percentages use the stated analysis population within each treatment "
                    "group unless otherwise specified."
                )
        definitions.append(item.denominator_note)
    elif ratio_display:
        definitions.append(
            "n/N denotes the number of subjects meeting the stated criterion over the "
            "number of evaluable subjects for that criterion and treatment group."
        )

    if re.search(r"LS Mean|p-value|\b(?:HR|GMR|MMRM|ANOVA|Cox)\b", visible_text):
        definitions.append(
            "Model-based estimates, contrasts, confidence intervals, and p-values follow "
            "the model, covariate, missing-data, and multiplicity specifications in the SAP."
        )
    if re.search(
        r"Mean\s*\(SD\)|Median\s*\(|\bMin\b|\bMax\b|Geometric Mean|\bGeo Mean\b",
        visible_text,
    ):
        definitions.append(
            "Descriptive statistics are calculated from non-missing observations unless "
            "the SAP states otherwise."
        )
    if re.search(r"survival|time to|duration of response|\bPFS\b|\bOS\b", visible_text, re.I):
        definitions.append(
            "Time origin, event definitions, and censoring rules follow the endpoint "
            "specifications in the SAP."
        )
    if definitions:
        item.footnotes.append("Statistical definitions: " + " ".join(dict.fromkeys(definitions)))


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
        return "Conditional (Phase I)"
    if any(
        keyword in title for keyword in ("food effect", "crossover", "relative bioavailability")
    ):
        return "Conditional (Phase I)"
    if any(keyword in title for keyword in ("cytokine", "holter", "immune-related", "irae")):
        return "Conditional (Protocol-Defined Subset)"
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


def _expand_compound_semantic_rows(item: TFLItem) -> None:
    """Populate explicit Visit/Timepoint/Statistic columns encoded in legacy row labels."""
    semantic_columns: list[str] = []
    for column in item.placeholder_columns[1:]:
        flat = column.replace("\n", " ").strip()
        if flat in {"Visit", "Timepoint", "Statistic"}:
            semantic_columns.append(flat)
        else:
            break
    if not semantic_columns:
        return

    expanded_rows = []
    for row in item.shell_rows:
        rich = item._normalize_row(row)
        label = rich["label"]
        values = list(rich["values"])
        if "\u2014" in label:
            left, statistic = (part.strip() for part in label.rsplit("\u2014", 1))
            if semantic_columns[0] == "Statistic":
                rich["label"] = left
                rich["values"] = [statistic, *values]
            elif semantic_columns[:2] in (["Visit", "Statistic"], ["Timepoint", "Statistic"]):
                rich["label"] = ""
                rich["values"] = [left, statistic, *values]
        elif semantic_columns[0] == "Statistic" and re.search(r",\s*n\s*\(%\)\s*$", label):
            structural_label = re.sub(r",\s*n\s*\(%\)\s*$", "", label).rstrip()
            rich["label"] = structural_label
            rich["values"] = ["n (%)", *values]
        elif semantic_columns[0] == "Statistic" and rich["indent"] and values:
            rich["label"] = ""
            rich["values"] = [label.strip(), *values]
        expanded_rows.append(rich)
    item.shell_rows = expanded_rows


def _normalize_shell_rows(item: TFLItem) -> None:
    normalized_rows = []
    data_col_count = max(len(item.placeholder_columns) - 1, 0)
    for row in item.shell_rows:
        rich = item._normalize_row(row)
        rich["label"] = _normalize_controlled_text(rich["label"])
        rich["values"] = [_normalize_controlled_text(str(value)) for value in rich["values"]]
        if data_col_count:
            if rich["label"].startswith("[") and rich["values"] and set(rich["values"]) == {"..."}:
                rich["values"] = ["..."] * data_col_count
            elif not rich["values"]:
                rich["values"] = [""] * data_col_count
            elif len(rich["values"]) > data_col_count:
                rich["values"] = rich["values"][:data_col_count]
            elif len(rich["values"]) < data_col_count:
                rich["values"].extend([""] * (data_col_count - len(rich["values"])))
        normalized_rows.append(rich)
    item.shell_rows = normalized_rows


def _assign_controlled_source_listing(item: TFLItem) -> None:
    if item.tfl_type == L:
        item.source_listing = ""
        return

    title = item.title.lower()
    program_ref = item.program_ref.lower() if item.program_ref else ""
    generic_source = item.source_listing in ("", "L16.2.1 / L16.2.2")
    if not generic_source:
        return

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
        item.source_listing = ""
        if "Source listing is study-specific" not in item.table_notes:
            item.table_notes = " ".join(
                part
                for part in (
                    item.table_notes,
                    "Source listing is study-specific to the endpoint.",
                )
                if part
            )
        return
    if any(token in title for token in ("glycemic", "metabolic", "body weight target")):
        item.source_listing = "L16.2.38"
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
        if "hy's law" in title or "hys law" in title:
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
    if any(
        token in title
        for token in (
            "laboratory",
            "hematology",
            "chemistry",
            "lipid",
            "glucose",
            "thyroid",
            "renal safety",
            "pancreatic enzyme",
        )
    ):
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
    if generic_source:
        item.source_listing = ""


def _normalize_controlled_shells(items: list[TFLItem]) -> list[TFLItem]:
    removed_ids = {
        "T14.2.3",
        "T14.2.17",
        "T14.2.18",
        "T14.3.1.8",
        "T14.3.1.9",
        "T14.3.1.11",
        "T14.3.1.12",
        "T14.3.1.16",
        "T14.3.1.17",
        "T14.3.1.18",
        "T14.3.1.21",
        "T14.3.1.22",
        "T14.3.1.29",
        "T14.3.1.30",
    }
    retained: list[TFLItem] = []

    for item in items:
        if item.id in removed_ids:
            continue

        item.placeholder_columns = _normalize_placeholder_columns(item.placeholder_columns)
        _expand_compound_semantic_rows(item)
        _normalize_shell_rows(item)
        item.population = _normalize_controlled_text(item.population)
        item.figure_description = _normalize_controlled_text(item.figure_description)
        item.footnotes = [_normalize_controlled_text(note) for note in item.footnotes]
        item.dataset_source = _normalize_controlled_text(item.dataset_source)
        _assign_controlled_source_listing(item)
        _enrich_table_definition_footnotes(item)
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
