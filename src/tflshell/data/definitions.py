"""TFL Shell Catalog v2.2 — shell-first structure with ... expansion pattern.

Column convention for ALL tables:
  Col 0 = structural labels (first column)
  Col 1 = XXX Group 1 (N=XX)
  Col 2 = XXX Group 2 (N=XX)
  Col 3 = ... (expansion placeholder)
  Col 4 = Overall (N=XX)

Placeholder styles per column type:
  n (%)   → xx (xx.x)
  Count   → xx
  Mean SD → xx.x (xx.x)
  CI      → [xx.x, xx.x]
  HR/p    → x.xx / x.xxx

Section 14.4: Tables + Figures ONLY (no listings).
Section 16.2: All patient-level listings (including PK/ADA/Biomarker moved from 14.4).
"""

from tflshell.models.enums import TFLType, Section
from tflshell.models.tfl_item import TFLItem
from tflshell.models.catalog import TFLCatalog

T, F, L = TFLType.TABLE, TFLType.FIGURE, TFLType.LISTING
S141, S142, S143, S144 = Section.SEC_14_1, Section.SEC_14_2, Section.SEC_14_3, Section.SEC_14_4
S162 = Section.SEC_16_2

# Standard 5-column header templates (v2.2: "..." and "Overall" are separate columns)
H2_SIMPLE = ["Parameter\nCategory / Statistic",
             "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)",
             "...", "Overall\n(N=XX)"]
H2_NPCT = ["Parameter\nCategory",
            "XXX Group 1\n(N=XX)\nn (%)", "XXX Group 2\n(N=XX)\nn (%)",
            "...", "Overall\n(N=XX)\nn (%)"]
H2_SOCPT = ["System Organ Class\nPreferred Term",
             "XXX Group 1\n(N=XX)\nn (%)", "XXX Group 2\n(N=XX)\nn (%)",
             "...", "Overall\n(N=XX)\nn (%)"]
H2_EVENTS = ["Parameter\nCategory",
              "XXX Group 1\n(N=XX)\nn (%) [E]", "XXX Group 2\n(N=XX)\nn (%) [E]",
              "...", "Overall\n(N=XX)\nn (%) [E]"]
H2_EFF = ["Endpoint\nStatistic",
           "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)",
           "...", "Overall\n(N=XX)"]
H2_LAB = ["Parameter\nVisit", "Statistic",
           "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)",
           "...", "Overall\n(N=XX)"]

# Shared ellipsis rows (v2.2: 5-column standard)
EROW = ["[...]", "...", "...", "...", "..."]
EROW5 = ["[...]", "...", "...", "...", "..."]
EROW6 = ["[...]", "...", "...", "...", "...", "..."]


def build_catalog() -> TFLCatalog:
    items: list[TFLItem] = []

    # =====================================================================
    # 14.1 DEMOGRAPHICS AND BASELINE (12 items)
    # =====================================================================

    items.append(TFLItem(
        id="T14.1.1", title="Summary of Demographic Characteristics",
        tfl_type=T, section=S141, sort_key=1,
        population="Intent-to-Treat (ITT) Population",
        placeholder_columns=H2_SIMPLE,
        shell_rows=[
            {"label": "Age (years)", "bold": True},
            {"label": "  n", "indent": True, "values": ["xx", "xx", "...", "xx"]},
            {"label": "  Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Median (Min, Max)", "indent": True, "values": ["xx.x (xx, xx)", "xx.x (xx, xx)", "...", "xx.x (xx, xx)"]},
            {"label": "Age Group", "bold": True},
            {"label": "  < 65 years", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  >= 65 years", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Sex", "bold": True},
            {"label": "  Male", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Female", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Race", "bold": True},
            {"label": "  White", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Black or African American", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Asian", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Other", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Ethnicity", "bold": True},
            {"label": "  Hispanic or Latino", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Not Hispanic or Latino", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Weight (kg)", "bold": True},
            {"label": "  Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "BMI (kg/m²)", "bold": True},
            {"label": "  Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "ECOG Performance Status", "bold": True},
            {"label": "  0 — Fully active", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  1 — Restricted in strenuous activity", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Disease Stage at Baseline", "bold": True},
            {"label": "  Stage III", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Stage IV", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Histological Type", "bold": True},
            {"label": "  Adenocarcinoma", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Squamous Cell Carcinoma", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Other", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["Percentages based on number of subjects in each treatment group.",
                   "Age calculated relative to date of informed consent."],
        dataset_source="ADSL", program_ref="t_demog_summary.sas",
    ))

    items.append(TFLItem(
        id="T14.1.2", title="Summary of Baseline Disease Characteristics",
        tfl_type=T, section=S141, sort_key=2,
        population="Intent-to-Treat (ITT) Population",
        placeholder_columns=H2_SIMPLE,
        shell_rows=[
            ["ECOG Performance Status, n (%)", "", "", "", ""],
            ["  0 — Fully active", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["  1 — Restricted in strenuous activity", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["  2 — Ambulatory, unable to work", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Disease Stage, n (%)", "", "", "", ""],
            ["  Stage III", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["  Stage IV", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Time Since Initial Diagnosis (months)", "", "", "", ""],
            ["  Mean (SD)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            EROW,
        ],
        footnotes=["Baseline = last non-missing assessment on/before first dose.",
                   "ECOG PS: 0=Fully active, 1=Restricted, 2=Ambulatory, 3=Limited self-care, 4=Completely disabled."],
        dataset_source="ADSL, ADRS", program_ref="t_baseline_chars.sas",
    ))

    items.append(TFLItem(
        id="T14.1.3", title="Summary of Medical History by System Organ Class and Preferred Term",
        tfl_type=T, section=S141, sort_key=3,
        population="Safety Population",
        placeholder_columns=H2_SOCPT,
        shell_rows=[
            {"label": "Any Medical History Condition", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Vascular disorders", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Hypertension", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Hypotension", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Cardiac disorders", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Coronary Artery Disease", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Gastrointestinal disorders", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Gastroesophageal reflux disease", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Constipation", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Metabolism and nutrition disorders", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Diabetes mellitus", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Hyperlipidemia", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["MedDRA version [xx.x] used for coding medical history terms."],
        dataset_source="ADMH", program_ref="t_mh_soc_pt.sas",
        dictionary_versions={"MedDRA": "[xx.x]"},
    ))

    items.append(TFLItem(
        id="T14.1.4", title="Summary of Prior Medications by ATC Class and Preferred Name",
        tfl_type=T, section=S141, sort_key=4,
        population="Safety Population",
        placeholder_columns=H2_SOCPT,
        shell_rows=[
            ["Any Prior Medication", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Drugs for acid-related disorders", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["  Omeprazole", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["  Pantoprazole", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Antibacterials for systemic use", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            EROW,
        ],
        footnotes=["WHO Drug Dictionary [version] used for medication coding."],
        dataset_source="ADCM", program_ref="t_prior_meds.sas",
        dictionary_versions={"WHO-DD": "[version]"},
    ))

    items.append(TFLItem(
        id="T14.1.5", title="Subject Disposition",
        tfl_type=T, section=S141, sort_key=5,
        population="All Randomized Subjects",
        placeholder_columns=H2_NPCT,
        shell_rows=[
            {"label": "Subjects Screened", "values": ["xx", "xx", "...", "xx"]},
            {"label": "Subjects Randomized", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Subjects Treated (>=1 dose)", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Completed Treatment", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Discontinued Treatment", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Adverse Event", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Death", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Progressive Disease", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Withdrawal by Subject", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Physician Decision", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Protocol Violation", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Lost to Follow-up", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["Percentages: N=treated per arm for discontinuation reasons.",
                   "Primary reason for discontinuation per CRF EOT page."],
        dataset_source="ADSL", program_ref="t_disposition.sas",
    ))

    items.append(TFLItem(
        id="T14.1.6", title="Major Protocol Deviations",
        tfl_type=T, section=S141, sort_key=6,
        population="All Randomized Subjects",
        placeholder_columns=H2_NPCT,
        shell_rows=[
            ["Any Major Protocol Deviation", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Inclusion/Exclusion Criteria Not Met", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Received Wrong Treatment/Incorrect Dose", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Missed >=2 Consecutive Efficacy Assessments", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            EROW,
        ],
        dataset_source="ADSL, DV", program_ref="t_prot_dev.sas",
    ))

    items.append(TFLItem(
        id="T14.1.7", title="Analysis Populations",
        tfl_type=T, section=S141, sort_key=7,
        population="All Subjects",
        placeholder_columns=H2_NPCT,
        shell_rows=[
            ["Screened", "xx", "xx", "...", "xx"],
            ["Randomized", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Intent-to-Treat (ITT)", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Safety Population", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Per-Protocol (PP)", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            EROW,
        ],
        footnotes=["ITT: All randomized with >=1 dose. Safety: All with >=1 dose. PP: ITT with no major PDs."],
        dataset_source="ADSL", program_ref="t_populations.sas",
    ))

    items.append(TFLItem(
        id="T14.1.8", title="Medical History by SOC/PT — Incidence >=2% in Any Arm",
        tfl_type=T, section=S141, sort_key=8,
        population="Safety Population",
        placeholder_columns=H2_SOCPT,
        shell_rows=[
            ["Gastrointestinal disorders", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["  Gastroesophageal reflux disease", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Musculoskeletal disorders", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["  Back pain", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            EROW,
        ],
        dataset_source="ADMH", program_ref="t_mh_2pct.sas",
        dictionary_versions={"MedDRA": "[xx.x]"},
    ))

    items.append(TFLItem(
        id="T14.1.9", title="Prior and Concomitant Medications by ATC Level 2 and Preferred Name",
        tfl_type=T, section=S141, sort_key=9,
        population="Safety Population",
        placeholder_columns=H2_SOCPT,
        shell_rows=[
            ["Prior Medications — Any", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Concomitant Medications — Any", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Drugs for acid-related disorders", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Analgesics", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            EROW,
        ],
        dataset_source="ADCM", program_ref="t_conmed_atc.sas",
        dictionary_versions={"WHO-DD": "[version]"},
    ))

    items.append(TFLItem(
        id="T14.1.10", title="Summary of Study Drug Exposure — Duration, Cycles, Dose Intensity",
        tfl_type=T, section=S141, sort_key=10,
        population="Safety Population",
        placeholder_columns=H2_SIMPLE,
        shell_rows=[
            {"label": "Duration of Exposure (weeks)", "bold": True},
            {"label": "  n", "indent": True, "values": ["xx", "xx", "...", "xx"]},
            {"label": "  Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Median (Min, Max)", "indent": True, "values": ["xx.x (xx, xx)", "xx.x (xx, xx)", "...", "xx.x (xx, xx)"]},
            {"label": "Number of Cycles Administered", "bold": True},
            {"label": "  n", "indent": True, "values": ["xx", "xx", "...", "xx"]},
            {"label": "  Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Median (Min, Max)", "indent": True, "values": ["xx.x (xx, xx)", "xx.x (xx, xx)", "...", "xx.x (xx, xx)"]},
            {"label": "Cumulative Dose (mg)", "bold": True},
            {"label": "  Mean (SD)", "indent": True, "values": ["xxxx.x (xxx.x)", "xxxx.x (xxx.x)", "...", "xxxx.x (xxx.x)"]},
            {"label": "  Median (Min, Max)", "indent": True, "values": ["xxxx.x (xx, xxxx)", "xxxx.x (xx, xxxx)", "...", "xxxx.x (xx, xxxx)"]},
            {"label": "Relative Dose Intensity (%)", "bold": True},
            {"label": "  n", "indent": True, "values": ["xx", "xx", "...", "xx"]},
            {"label": "  Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Median (Min, Max)", "indent": True, "values": ["xx.x (xx, xx)", "xx.x (xx, xx)", "...", "xx.x (xx, xx)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        dataset_source="ADEX", program_ref="t_exposure_summary.sas",
    ))

    items.append(TFLItem(
        id="T14.1.11", title="Summary of Genomic/Biomarker Baseline Characteristics",
        tfl_type=T, section=S141, sort_key=11,
        oncology_only=True,
        population="ITT Population with Biomarker Data",
        placeholder_columns=H2_SIMPLE,
        shell_rows=[
            ["PD-L1 TPS >=50%", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["PD-L1 TPS 1-49%", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["EGFR Mutation Positive", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            EROW,
        ],
        dataset_source="ADSL, ADBM", program_ref="t_biomarker_baseline.sas",
    ))


    items.append(TFLItem(
        id="T14.1.12", title="Subject Disposition by Country and Site",
        tfl_type=T, section=S141, sort_key=12,
        population="All Randomized Subjects",
        placeholder_columns=["Country\nSite", "Screened\nn", "Randomized\nn",
                             "Treated\nn (%)", "Completed\nn (%)", "Discontinued\nn (%)"],
        shell_rows=[
            {"label": "Country A", "bold": True},
            {"label": "  Site 001", "indent": True, "values": ["xx", "xx", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"]},
            {"label": "  Site 002", "indent": True, "values": ["xx", "xx", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"]},
            {"label": "Country B", "bold": True},
            {"label": "  Site 003", "indent": True, "values": ["xx", "xx", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "...", "..."]},
        ],
        dataset_source="ADSL", program_ref="t_disp_site.sas",
    ))

    items.append(TFLItem(
        id="T14.1.13", title="Screening Summary — Screen Failure Reasons by Eligibility Criterion",
        tfl_type=T, section=S141, sort_key=13,
        population="All Screened Subjects",
        placeholder_columns=["Eligibility Criterion", "Screen Failures\nn", "Reason\nCategory"],
        shell_rows=[
            {"label": "Inclusion Criterion 1: Age >=18", "values": ["xx", "Age <18"]},
            {"label": "Inclusion Criterion 2: ECOG 0-1", "values": ["xx", "ECOG >=2"]},
            {"label": "Exclusion Criterion 1: Prior malignancy", "values": ["xx", "History of prior cancer"]},
            {"label": "Exclusion Criterion 2: Active infection", "values": ["xx", "Active HBV/HCV/HIV"]},
            {"label": "Total Screen Failures", "bold": True, "values": ["xx", ""]},
            {"label": "[...]", "values": ["...", "..."]},
        ],
        dataset_source="ADSL", program_ref="t_screen_fail.sas",
    ))

    items.append(TFLItem(
        id="T14.1.14", title="Major Protocol Deviations — by Category and Subcategory",
        tfl_type=T, section=S141, sort_key=14,
        population="All Randomized Subjects",
        placeholder_columns=["Deviation Category\nSubcategory",
                             "G1\nn (%)", "G2\nn (%)", "...", "Overall\nn (%)"],
        shell_rows=[
            {"label": "Eligibility Criteria", "bold": True},
            {"label": "  Inclusion criteria not met", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Exclusion criteria not met", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Study Procedure", "bold": True},
            {"label": "  Missed efficacy assessment", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Out-of-window visit", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Study Treatment", "bold": True},
            {"label": "  Wrong dose administered", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Non-compliance <80%", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Concomitant Medication", "bold": True},
            {"label": "  Prohibited medication taken", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        dataset_source="ADSL, DV", program_ref="t_protdev_cat.sas",
    ))

    items.append(TFLItem(
        id="T14.1.15", title="Surgical and Procedure History by Body System",
        tfl_type=T, section=S141, sort_key=15,
        population="Safety Population",
        placeholder_columns=["Body System\nProcedure",
                             "G1\nn (%)", "G2\nn (%)", "...", "Overall\nn (%)"],
        shell_rows=[
            {"label": "Any Surgical/Procedure History", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Cardiovascular", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Coronary artery bypass graft", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Pacemaker insertion", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Gastrointestinal", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Cholecystectomy", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Appendectomy", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Musculoskeletal", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Joint replacement", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        dataset_source="ADSL, ADMH", program_ref="t_surg_hist.sas",
    ))

    items.append(TFLItem(
        id="T14.1.16", title="Prior and Concomitant Medications by WHO ATC Level 3 — >=5% in Any Arm",
        tfl_type=T, section=S141, sort_key=16,
        population="Safety Population",
        placeholder_columns=["ATC Level 3\nPreferred Name",
                             "Prior\nn (%)", "Concomitant\nn (%)", "...", "Overall\nn (%)"],
        shell_rows=[
            {"label": "A02BC — Proton Pump Inhibitors", "bold": True},
            {"label": "  Omeprazole", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Pantoprazole", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "N02BE — Anilides (Paracetamol)", "bold": True},
            {"label": "  Paracetamol", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "C10AA — HMG-CoA Reductase Inhibitors", "bold": True},
            {"label": "  Atorvastatin", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["WHO Drug Global [version]. Prior = stopped before first dose. Concomitant = any use on/after first dose."],
        dataset_source="ADSL, ADCM", program_ref="t_conmed_atc3.sas",
        dictionary_versions={"WHO-DD": "[version]"},
    ))

    items.append(TFLItem(
        id="T14.1.17", title="Study Drug Exposure by Duration Category",
        tfl_type=T, section=S141, sort_key=17,
        population="Safety Population",
        placeholder_columns=["Exposure Duration",
                             "G1\nn (%)", "G2\nn (%)", "...", "Overall\nn (%)"],
        shell_rows=[
            {"label": "Duration of Exposure", "bold": True},
            {"label": "  Mean (SD), weeks", "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Median (Min, Max), weeks", "values": ["xx.x (xx, xx)", "xx.x (xx, xx)", "...", "xx.x (xx, xx)"]},
            {"label": "Exposure by Duration Category", "bold": True},
            {"label": "  >=1 month (<30 days)", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  >=3 months (>=90 days)", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  >=6 months (>=180 days)", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  >=12 months (>=360 days)", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        dataset_source="ADSL, ADEX", program_ref="t_expo_durcat.sas",
    ))

    # =====================================================================
    # 14.2 EFFICACY (32 items: 11 general + 21 oncology)
    # =====================================================================

    items.append(TFLItem(
        id="T14.2.1", title="Primary Efficacy Endpoint — Primary Analysis",
        tfl_type=T, section=S142, sort_key=1,
        population="Intent-to-Treat (ITT) Population",
        placeholder_columns=["Parameter",
                             "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)",
                             "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "Subjects in Analysis", "bold": True, "values": ["xx", "xx", "...", "xx"]},
            {"label": "Baseline", "bold": True},
            {"label": "  Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Median (Min, Max)", "indent": True, "values": ["xx.x (xx, xx)", "xx.x (xx, xx)", "...", "xx.x (xx, xx)"]},
            {"label": "End of Study (Week 24)", "bold": True},
            {"label": "  Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "Change from Baseline at Week 24", "bold": True},
            {"label": "  LS Mean (SE)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  LS Mean Difference vs. Control", "indent": True, "values": ["", "xx.x", "...", ""]},
            {"label": "  95% CI", "indent": True, "values": ["", "[xx.x, xx.x]", "...", ""]},
            {"label": "  p-value", "indent": True, "values": ["", "x.xxx", "...", ""]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["ANCOVA with treatment as fixed effect, baseline as covariate, stratified by [stratification factors].",
                   "MMRM under MAR for missing data. Two-sided 95% CI. Multiplicity adjustment per hierarchical testing procedure."],
        dataset_source="ADSL, ADEFF", program_ref="t_primary_eff.sas",
    ))

    items.append(TFLItem(
        id="T14.2.2", title="Secondary Efficacy Endpoints — Summary",
        tfl_type=T, section=S142, sort_key=2,
        population="Intent-to-Treat (ITT) Population",
        placeholder_columns=["Endpoint\nStatistic",
                             "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)",
                             "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "Key Secondary Endpoint 1 — Change from BL at Week 24", "bold": True},
            {"label": "  LS Mean (SE)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  LS Mean Difference (95% CI)", "indent": True, "values": ["xx.x [xx.x, xx.x]", "", "...", ""]},
            {"label": "  p-value (adjusted)", "indent": True, "values": ["x.xxx", "", "...", ""]},
            {"label": "Key Secondary Endpoint 2 — Response Rate", "bold": True},
            {"label": "  n (%)", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Odds Ratio (95% CI)", "indent": True, "values": ["x.xx [x.xx, x.xx]", "", "...", ""]},
            {"label": "  p-value (adjusted)", "indent": True, "values": ["x.xxx", "", "...", ""]},
            {"label": "Key Secondary Endpoint 3 — Time to Event", "bold": True},
            {"label": "  Events / N (%)", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Median, months (95% CI)", "indent": True, "values": ["xx.x (xx.x, xx.x)", "xx.x (xx.x, xx.x)", "...", "xx.x (xx.x, xx.x)"]},
            {"label": "  HR (95% CI)", "indent": True, "values": ["x.xx [x.xx, x.xx]", "", "...", ""]},
            {"label": "  p-value (adjusted)", "indent": True, "values": ["x.xxx", "", "...", ""]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["Endpoints tested per hierarchical fixed-sequence procedure. Adjusted p-values shown.",
                   "Response defined per protocol SAP [ref]. ANCOVA/CMH/Cox models as appropriate per endpoint type."],
        dataset_source="ADSL, ADEFF, ADTTE", program_ref="t_secondary_eff.sas",
    ))

    items.append(TFLItem(
        id="T14.2.3", title="Subgroup Analysis of Primary Endpoint",
        tfl_type=T, section=S142, sort_key=3,
        population="Intent-to-Treat (ITT) Population",
        placeholder_columns=["Subgroup\nLevel",
                             "XXX Group 1\nn / Estimate", "XXX Group 2\nn / Estimate",
                             "...\n...\nEffect [95% CI]", "Interaction\np-value"],
        shell_rows=[
            ["Overall", "xx / xx.x", "xx / xx.x", "...", "xx.x [xx.x, xx.x]", "—"],
            ["Age <65", "xx / xx.x", "xx / xx.x", "...", "xx.x [xx.x, xx.x]", "x.xxx"],
            ["Age >=65", "xx / xx.x", "xx / xx.x", "...", "xx.x [xx.x, xx.x]", ""],
            ["Male", "xx / xx.x", "xx / xx.x", "...", "xx.x [xx.x, xx.x]", "x.xxx"],
            ["Female", "xx / xx.x", "xx / xx.x", "...", "xx.x [xx.x, xx.x]", ""],
            EROW5,
        ],
        footnotes=["Subgroup analyses are exploratory."],
        dataset_source="ADSL, ADEFF", program_ref="t_subgroup_primary.sas",
    ))

    items.append(TFLItem(
        id="T14.2.4", title="Sensitivity Analysis of Primary Endpoint",
        tfl_type=T, section=S142, sort_key=4,
        population="ITT and PP Populations",
        placeholder_columns=["Analysis\nPopulation / Missing Data",
                             "XXX Group 1\nLS Mean", "XXX Group 2\nLS Mean",
                             "...\n...\nDifference", "95% CI"],
        shell_rows=[
            ["Primary (MMRM / ITT / MAR)", "xx.x", "xx.x", "...", "xx.x", "[xx.x, xx.x]"],
            ["PP Analysis (Completers)", "xx.x", "xx.x", "...", "xx.x", "[xx.x, xx.x]"],
            ["Multiple Imputation (100 imputations)", "xx.x", "xx.x", "...", "xx.x", "[xx.x, xx.x]"],
            ["Tipping Point (δ=1.0)", "xx.x", "xx.x", "...", "xx.x", "[xx.x, xx.x]"],
            EROW5,
        ],
        dataset_source="ADSL, ADEFF", program_ref="t_sensitivity_eff.sas",
    ))

    items.append(TFLItem(
        id="T14.2.5", title="Non-Inferiority Analysis of Primary Endpoint",
        tfl_type=T, section=S142, sort_key=5,
        population="Per-Protocol (PP) Population",
        placeholder_columns=["Parameter",
                             "XXX Group 1\n(N=XX)", "Control\n(N=XX)",
                             "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "Primary Endpoint — LS Mean (SE)", "bold": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "Difference vs. Control (95% CI)", "values": ["xx.x [xx.x, xx.x]", "", "...", ""]},
            {"label": "Non-Inferiority Margin (Δ)", "values": ["xx.x", "", "...", ""]},
            {"label": "Lower Bound of 95% CI > −Δ?", "values": ["Yes / No", "", "...", ""]},
            {"label": "NI Conclusion", "bold": True, "values": ["Non-inferiority met / not met", "", "...", ""]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["NI margin per regulatory guidance. Analysis population: PP (primary), ITT (supportive)."],
        dataset_source="ADSL, ADEFF", program_ref="t_ni_analysis.sas",
    ))

    items.append(TFLItem(
        id="T14.2.6", title="Tipping Point Analysis for Primary Endpoint",
        tfl_type=T, section=S142, sort_key=6,
        population="ITT Population",
        placeholder_columns=["Tipping Point Parameter\nShift Value",
                             "p-value", "Conclusion"],
        shell_rows=[
            ["Tipping Point Analysis", "", ""],
            ["  Placebo-arm shift (delta) = 0.0", "x.xxx", "Statistically significant"],
            ["  Placebo-arm shift (delta) = 0.5", "x.xxx", "Remains significant"],
            ["  Placebo-arm shift (delta) = 1.0", "x.xxx", "Borderline"],
            ["  Placebo-arm shift (delta) = 1.5", "x.xxx", "Not significant — tipping point reached"],
            ["[...]", "...", "..."],
        ],
        dataset_source="ADSL, ADEFF", program_ref="t_tipping_point.sas",
    ))

    items.append(TFLItem(
        id="T14.2.7", title="Sensitivity Analysis by Estimand Strategy",
        tfl_type=T, section=S142, sort_key=7,
        population="ITT Population",
        placeholder_columns=["Estimand Strategy\nIntercurrent Event Handling",
                             "Difference", "95% CI", "p-value"],
        shell_rows=[
            ["Treatment Policy — Ignore rescue therapy", "xx.x", "[xx.x, xx.x]", "x.xxx"],
            ["Composite — Rescue = treatment failure", "xx.x", "[xx.x, xx.x]", "x.xxx"],
            ["Hypothetical — Rescue subjects censored", "xx.x", "[xx.x, xx.x]", "x.xxx"],
            EROW,
        ],
        dataset_source="ADSL, ADEFF", program_ref="t_estimand_sens.sas",
    ))

    items.append(TFLItem(
        id="T14.2.8", title="Time to Deterioration (TTD) — Quality of Life",
        tfl_type=T, section=S142, sort_key=8,
        population="ITT Population with PRO Data",
        placeholder_columns=["Parameter",
                             "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)",
                             "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "Number of Subjects", "bold": True, "values": ["xx", "xx", "...", "xx"]},
            {"label": "Events, n (%)", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Censored, n (%)", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Median TTD, months (95% CI)", "bold": True, "values": ["xx.x (xx.x, xx.x)", "xx.x (xx.x, xx.x)", "...", "xx.x (xx.x, xx.x)"]},
            {"label": "TTD Rate at 6 months, % (95% CI)", "values": ["xx.x (xx.x, xx.x)", "xx.x (xx.x, xx.x)", "...", "xx.x (xx.x, xx.x)"]},
            {"label": "TTD Rate at 12 months, % (95% CI)", "values": ["xx.x (xx.x, xx.x)", "xx.x (xx.x, xx.x)", "...", "xx.x (xx.x, xx.x)"]},
            {"label": "Hazard Ratio (95% CI)", "bold": True, "values": ["x.xx [x.xx, x.xx]", "", "...", ""]},
            {"label": "p-value (stratified log-rank)", "values": ["x.xxx", "", "...", ""]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["TTD defined as time from randomization to first deterioration in [PRO instrument] score >= [threshold] points.",
                   "KM estimates; Brookmeyer-Crowley CI for median. Stratified Cox/log-rank by baseline factors."],
        dataset_source="ADSL, ADPRO", program_ref="t_ttd_qol.sas",
    ))

    # General efficacy figures
    items.append(TFLItem(
        id="F14.2.1", title="Forest Plot — Primary Endpoint by Subgroup",
        tfl_type=F, section=S142, sort_key=9,
        population="Intent-to-Treat (ITT) Population",
        figure_description="Forest plot: treatment effect [95% CI] per subgroup, overall diamond, ref line at null.",
        dataset_source="ADSL, ADEFF", program_ref="f_forest_primary.sas",
        figure_type="forest", figure_width_inches=6, figure_height_inches=3.5,
    ))

    items.append(TFLItem(
        id="F14.2.2", title="Longitudinal Plot — Primary Endpoint Over Time",
        tfl_type=F, section=S142, sort_key=10,
        population="Intent-to-Treat (ITT) Population",
        figure_description="Line plot: Mean (±SE) primary endpoint by visit, two arms.",
        dataset_source="ADSL, ADEFF", program_ref="f_longitudinal_eff.sas",
        figure_type="longitudinal", figure_width_inches=5.5, figure_height_inches=3.2,
    ))

    items.append(TFLItem(
        id="F14.2.3", title="Cumulative Distribution Function Plot of Primary Endpoint",
        tfl_type=F, section=S142, sort_key=11,
        population="Intent-to-Treat (ITT) Population",
        figure_description="CDF plot: X=Change from Baseline, Y=Cumulative Proportion, two arms.",
        dataset_source="ADSL, ADEFF", program_ref="f_cdf_eff.sas",
        figure_type="cdf", figure_width_inches=5.5, figure_height_inches=3.2,
    ))

    # --- Oncology-Specific Efficacy (13 tables + 7 figures) ---

    items.append(TFLItem(
        id="T14.2.9", title="Tumor Response — Best Overall Response (BOR)",
        tfl_type=T, section=S142, sort_key=12, oncology_only=True,
        population="Intent-to-Treat (ITT) Population",
        placeholder_columns=H2_NPCT,
        shell_rows=[
            {"label": "Best Overall Response (BOR)", "bold": True},
            {"label": "  Complete Response (CR)", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Partial Response (PR)", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Stable Disease (SD)", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Progressive Disease (PD)", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Not Evaluable (NE)", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Objective Response Rate (ORR = CR+PR)", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  95% CI (Clopper-Pearson)", "indent": True, "values": ["[xx.x, xx.x]", "[xx.x, xx.x]", "...", "[xx.x, xx.x]"]},
            {"label": "Disease Control Rate (DCR = CR+PR+SD)", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  95% CI (Clopper-Pearson)", "indent": True, "values": ["[xx.x, xx.x]", "[xx.x, xx.x]", "...", "[xx.x, xx.x]"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["RECIST v1.1 by Independent Central Review (ICR). Confirmed responses only (repeat assessment >=4 weeks after initial response).",
                   "CR = Disappearance of all target and non-target lesions. PR = >=30% decrease in sum of diameters.",
                   "95% CI calculated using Clopper-Pearson exact method."],
        dataset_source="ADSL, ADRS", program_ref="t_bor.sas",
    ))

    items.append(TFLItem(
        id="T14.2.10", title="Tumor Response — Objective Response Rate (ORR)",
        tfl_type=T, section=S142, sort_key=13, oncology_only=True,
        population="Intent-to-Treat (ITT) Population",
        placeholder_columns=["Parameter",
                             "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)",
                             "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "Responders (CR+PR), n (%)", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  95% CI (Clopper-Pearson)", "indent": True, "values": ["[xx.x, xx.x]", "[xx.x, xx.x]", "...", "[xx.x, xx.x]"]},
            {"label": "Stratified Analysis", "bold": True},
            {"label": "  Odds Ratio (95% CI)", "indent": True, "values": ["x.xx [x.xx, x.xx]", "", "...", ""]},
            {"label": "  p-value (CMH, stratified)", "indent": True, "values": ["x.xxx", "", "...", ""]},
            {"label": "  Risk Difference, % (95% CI)", "indent": True, "values": ["xx.x [xx.x, xx.x]", "", "...", ""]},
            {"label": "Sensitivity: Unconfirmed Responses", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["ORR = CR + PR per RECIST v1.1 (ICR). Confirmed responses only (>=4 weeks after initial response).",
                   "CMH test stratified by randomization stratification factors."],
        dataset_source="ADSL, ADRS", program_ref="t_orr.sas",
    ))

    items.append(TFLItem(
        id="T14.2.11", title="Tumor Response — Disease Control Rate (DCR)",
        tfl_type=T, section=S142, sort_key=14, oncology_only=True,
        population="Intent-to-Treat (ITT) Population",
        placeholder_columns=["Parameter",
                             "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)",
                             "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "DCR (CR+PR+SD), n (%)", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  95% CI (Clopper-Pearson)", "indent": True, "values": ["[xx.x, xx.x]", "[xx.x, xx.x]", "...", "[xx.x, xx.x]"]},
            {"label": "Clinical Benefit Rate (CR+PR+SD>=24 wks)", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  95% CI (Clopper-Pearson)", "indent": True, "values": ["[xx.x, xx.x]", "[xx.x, xx.x]", "...", "[xx.x, xx.x]"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["DCR = CR + PR + SD (SD must be maintained for >=6 weeks after first dose).",
                   "Clinical Benefit Rate defined as CR + PR + SD lasting >=24 weeks."],
        dataset_source="ADSL, ADRS", program_ref="t_dcr.sas",
    ))

    items.append(TFLItem(
        id="T14.2.12", title="Tumor Response — Duration of Response (DOR)",
        tfl_type=T, section=S142, sort_key=15, oncology_only=True,
        population="Responders (Confirmed CR or PR)",
        placeholder_columns=["Parameter",
                             "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)",
                             "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "Number of Responders", "bold": True, "values": ["xx", "xx", "...", "xx"]},
            {"label": "Events (Progression or Death), n (%)", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Censored, n (%)", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Median DOR, months (95% CI)", "bold": True, "values": ["xx.x (xx.x, xx.x)", "xx.x (xx.x, xx.x)", "...", "xx.x (xx.x, xx.x)"]},
            {"label": "DOR Rate at 6 months, % (95% CI)", "values": ["xx.x (xx.x, xx.x)", "xx.x (xx.x, xx.x)", "...", "xx.x (xx.x, xx.x)"]},
            {"label": "DOR Rate at 12 months, % (95% CI)", "values": ["xx.x (xx.x, xx.x)", "xx.x (xx.x, xx.x)", "...", "xx.x (xx.x, xx.x)"]},
            {"label": "Hazard Ratio (95% CI)", "bold": True, "values": ["x.xx [x.xx, x.xx]", "", "...", ""]},
            {"label": "p-value (stratified log-rank)", "values": ["x.xxx", "", "...", ""]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["DOR: time from first documented CR/PR to first PD (RECIST 1.1, ICR) or death.",
                   "KM estimates; Brookmeyer-Crowley CI for median. Stratified Cox/log-rank by baseline factors."],
        dataset_source="ADSL, ADRS, ADTTE", program_ref="t_dor.sas",
    ))

    items.append(TFLItem(
        id="T14.2.13", title="Tumor Response — Time to Response (TTR)",
        tfl_type=T, section=S142, sort_key=16, oncology_only=True,
        population="Responders (Confirmed CR or PR)",
        placeholder_columns=["Parameter",
                             "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)",
                             "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "Number of Responders", "bold": True, "values": ["xx", "xx", "...", "xx"]},
            {"label": "Mean (SD), months", "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "Median, months", "values": ["xx.x", "xx.x", "...", "xx.x"]},
            {"label": "Min, Max", "values": ["xx.x, xx.x", "xx.x, xx.x", "...", "xx.x, xx.x"]},
            {"label": "<=12 weeks, n (%)", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": ">12 to 24 weeks, n (%)", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": ">24 weeks, n (%)", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["TTR: time from randomization to first documented CR or PR (confirmed)."],
        dataset_source="ADSL, ADRS", program_ref="t_ttr.sas",
    ))

    items.append(TFLItem(
        id="T14.2.14", title="Progression-Free Survival (PFS) — Primary Analysis",
        tfl_type=T, section=S142, sort_key=17, oncology_only=True,
        population="Intent-to-Treat (ITT) Population",
        placeholder_columns=["Parameter",
                             "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)",
                             "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "Number of Subjects", "bold": True, "values": ["xx", "xx", "...", "xx"]},
            {"label": "Events (Progression or Death), n (%)", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Censored, n (%)", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Median PFS, months (95% CI)", "bold": True, "values": ["xx.x (xx.x, xx.x)", "xx.x (xx.x, xx.x)", "...", "xx.x (xx.x, xx.x)"]},
            {"label": "Stratified Cox Model", "bold": True},
            {"label": "  Hazard Ratio (95% CI)", "indent": True, "values": ["x.xx [x.xx, x.xx]", "", "...", ""]},
            {"label": "  p-value (stratified log-rank)", "indent": True, "values": ["x.xxx", "", "...", ""]},
            {"label": "PFS Rate (KM Estimate)", "bold": True},
            {"label": "  6-month PFS Rate, % (95% CI)", "indent": True, "values": ["xx.x (xx.x, xx.x)", "xx.x (xx.x, xx.x)", "...", "xx.x (xx.x, xx.x)"]},
            {"label": "  12-month PFS Rate, % (95% CI)", "indent": True, "values": ["xx.x (xx.x, xx.x)", "xx.x (xx.x, xx.x)", "...", "xx.x (xx.x, xx.x)"]},
            {"label": "  18-month PFS Rate, % (95% CI)", "indent": True, "values": ["xx.x (xx.x, xx.x)", "xx.x (xx.x, xx.x)", "...", "xx.x (xx.x, xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["PFS: time from randomization to first documented PD (RECIST 1.1, ICR) or death from any cause.",
                   "KM estimates. Brookmeyer-Crowley CI for median. Greenwood CI for landmark rates.",
                   "Stratified Cox/log-rank by baseline stratification factors (ECOG PS, disease stage, prior lines)."],
        dataset_source="ADSL, ADTTE", program_ref="t_pfs_primary.sas",
    ))

    items.append(TFLItem(
        id="T14.2.15", title="Overall Survival (OS) — Primary Analysis",
        tfl_type=T, section=S142, sort_key=18, oncology_only=True,
        population="Intent-to-Treat (ITT) Population",
        placeholder_columns=["Parameter",
                             "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)",
                             "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "Number of Subjects", "bold": True, "values": ["xx", "xx", "...", "xx"]},
            {"label": "Deaths, n (%)", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Censored, n (%)", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Median OS, months (95% CI)", "bold": True, "values": ["xx.x (xx.x, NR)", "xx.x (xx.x, NR)", "...", "xx.x (xx.x, NR)"]},
            {"label": "Stratified Cox Model", "bold": True},
            {"label": "  Hazard Ratio (95% CI)", "indent": True, "values": ["x.xx [x.xx, x.xx]", "", "...", ""]},
            {"label": "  p-value (stratified log-rank)", "indent": True, "values": ["x.xxx", "", "...", ""]},
            {"label": "OS Rate (KM Estimate)", "bold": True},
            {"label": "  6-month OS Rate, % (95% CI)", "indent": True, "values": ["xx.x (xx.x, xx.x)", "xx.x (xx.x, xx.x)", "...", "xx.x (xx.x, xx.x)"]},
            {"label": "  12-month OS Rate, % (95% CI)", "indent": True, "values": ["xx.x (xx.x, xx.x)", "xx.x (xx.x, xx.x)", "...", "xx.x (xx.x, xx.x)"]},
            {"label": "  24-month OS Rate, % (95% CI)", "indent": True, "values": ["xx.x (xx.x, xx.x)", "xx.x (xx.x, xx.x)", "...", "xx.x (xx.x, xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["OS: time from randomization to death from any cause. NR = Not Reached.",
                   "KM estimates. Brookmeyer-Crowley CI for median. Greenwood CI for landmark rates.",
                   "Stratified Cox/log-rank by baseline stratification factors."],
        dataset_source="ADSL, ADTTE", program_ref="t_os_primary.sas",
    ))

    items.append(TFLItem(
        id="T14.2.16", title="PFS — Sensitivity Analysis",
        tfl_type=T, section=S142, sort_key=19, oncology_only=True,
        population="Intent-to-Treat (ITT) Population",
        placeholder_columns=["Analysis",
                             "Med PFS G1\n(months)", "Med PFS G2\n(months)", "...\n...\nHR [95% CI]", "p-value"],
        shell_rows=[
            ["Primary (ICR, RECIST 1.1)", "xx.x", "xx.x", "...", "x.xx [x.xx, x.xx]", "x.xxx"],
            ["Investigator Assessment", "xx.x", "xx.x", "...", "x.xx [x.xx, x.xx]", "x.xxx"],
            ["PP Population", "xx.x", "xx.x", "...", "x.xx [x.xx, x.xx]", "x.xxx"],
            EROW5,
        ],
        dataset_source="ADSL, ADTTE", program_ref="t_pfs_sensitivity.sas",
    ))

    items.append(TFLItem(
        id="T14.2.17", title="PFS — Subgroup Analysis",
        tfl_type=T, section=S142, sort_key=20, oncology_only=True,
        population="Intent-to-Treat (ITT) Population",
        placeholder_columns=["Subgroup\nLevel",
                             "G1 n/N\nMed PFS", "G2 n/N\nMed PFS",
                             "...\n...\nHR [95% CI]", "Interaction\np-value"],
        shell_rows=[
            ["Overall", "xx/xx, xx.x", "xx/xx, xx.x", "...", "x.xx [x.xx, x.xx]", "—"],
            ["Age <65", "xx/xx, xx.x", "xx/xx, xx.x", "...", "x.xx [x.xx, x.xx]", "x.xxx"],
            ["Age >=65", "xx/xx, xx.x", "xx/xx, xx.x", "...", "x.xx [x.xx, x.xx]", ""],
            EROW5,
        ],
        dataset_source="ADSL, ADTTE", program_ref="t_pfs_subgroup.sas",
    ))

    items.append(TFLItem(
        id="T14.2.18", title="OS — Subgroup Analysis",
        tfl_type=T, section=S142, sort_key=21, oncology_only=True,
        population="Intent-to-Treat (ITT) Population",
        placeholder_columns=["Subgroup\nLevel",
                             "G1 n/N\nMed OS", "G2 n/N\nMed OS",
                             "...\n...\nHR [95% CI]", "Interaction\np-value"],
        shell_rows=[
            ["Overall", "xx/xx, xx.x", "xx/xx, xx.x", "...", "x.xx [x.xx, x.xx]", "—"],
            ["Age <65", "xx/xx, xx.x", "xx/xx, xx.x", "...", "x.xx [x.xx, x.xx]", "x.xxx"],
            EROW5,
        ],
        dataset_source="ADSL, ADTTE", program_ref="t_os_subgroup.sas",
    ))

    items.append(TFLItem(
        id="T14.2.19", title="Summary of Target Lesion Changes from Baseline",
        tfl_type=T, section=S142, sort_key=22, oncology_only=True,
        population="ITT with Measurable Disease and Post-Baseline Assessment",
        placeholder_columns=["Parameter",
                             "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)",
                             "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "Subjects with Baseline and >=1 Post-BL Assessment", "bold": True, "values": ["xx", "xx", "...", "xx"]},
            {"label": "Best % Change from Baseline in Target Lesion Sum", "bold": True},
            {"label": "  Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Median", "indent": True, "values": ["xx.x", "xx.x", "...", "xx.x"]},
            {"label": "  Min, Max", "indent": True, "values": ["xx.x, xx.x", "xx.x, xx.x", "...", "xx.x, xx.x"]},
            {"label": "Best % Change Category", "bold": True},
            {"label": "  >=20% Increase (PD)", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  -30% to +20% (SD)", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  >= -30% Decrease (PR/CR)", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  >= -100% (CR)", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["Target lesion sum per RECIST 1.1. Best % change = min(post-baseline sum) - baseline sum / baseline sum * 100."],
        dataset_source="ADSL, ADRS", program_ref="t_target_lesion.sas",
    ))

    items.append(TFLItem(
        id="T14.2.20", title="Landmark Analysis of OS by 6-Month PFS Status",
        tfl_type=T, section=S142, sort_key=23, oncology_only=True,
        population="ITT Alive and On-Study at 6 Months",
        placeholder_columns=["PFS Status at 6M",
                             "G1 n/N\nMed OS", "G2 n/N\nMed OS", "...\n...\nHR [95% CI]"],
        shell_rows=[
            ["Progression-Free at 6M", "xx/xx, NR", "xx/xx, NR", "...", "x.xx [x.xx, x.xx]"],
            ["Progressed by 6M", "xx/xx, xx.x", "xx/xx, xx.x", "...", "x.xx [x.xx, x.xx]"],
            EROW,
        ],
        dataset_source="ADSL, ADTTE", program_ref="t_landmark_os.sas",
    ))

    items.append(TFLItem(
        id="T14.2.21", title="Time to First Subsequent Therapy (TFST)",
        tfl_type=T, section=S142, sort_key=24, oncology_only=True,
        population="ITT Population",
        placeholder_columns=["Parameter",
                             "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)",
                             "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "Number of Subjects", "bold": True, "values": ["xx", "xx", "...", "xx"]},
            {"label": "Subjects with Subsequent Therapy, n (%)", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Censored, n (%)", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Median TFST, months (95% CI)", "bold": True, "values": ["xx.x (xx.x, xx.x)", "xx.x (xx.x, xx.x)", "...", "xx.x (xx.x, xx.x)"]},
            {"label": "Hazard Ratio (95% CI)", "bold": True, "values": ["x.xx [x.xx, x.xx]", "", "...", ""]},
            {"label": "p-value (stratified log-rank)", "values": ["x.xxx", "", "...", ""]},
            {"label": "Subsequent Therapy Type", "bold": True},
            {"label": "  Chemotherapy", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Targeted Therapy", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Immunotherapy", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["TFST: time from randomization to first subsequent anti-cancer therapy or death.",
                   "KM estimates. Brookmeyer-Crowley CI for median."],
        dataset_source="ADSL, ADTTE, ADCM", program_ref="t_tfst.sas",
    ))

    # Oncology figures
    items.append(TFLItem(
        id="F14.2.4", title="Waterfall Plot — Best Percentage Change in Target Lesions",
        tfl_type=F, section=S142, sort_key=25, oncology_only=True,
        population="ITT with Measurable Disease and Post-Baseline Assessment",
        figure_description="Waterfall: best % change per subject, BOR-colored bars, ref lines +20%/-30%.",
        dataset_source="ADSL, ADRS", program_ref="f_waterfall.sas",
        figure_type="waterfall", figure_width_inches=6.5, figure_height_inches=3.5,
    ))

    items.append(TFLItem(
        id="F14.2.5", title="Spider Plot — Percentage Change in Tumor Burden Over Time",
        tfl_type=F, section=S142, sort_key=26, oncology_only=True,
        population="ITT with Measurable Disease",
        figure_description="Spider: % change trajectories, BOR-colored lines, PD/death terminal markers.",
        dataset_source="ADSL, ADRS", program_ref="f_spider.sas",
        figure_type="spider", figure_width_inches=6, figure_height_inches=3.5,
    ))

    items.append(TFLItem(
        id="F14.2.6", title="Swimmer Plot — Duration of Treatment and Response",
        tfl_type=F, section=S142, sort_key=27, oncology_only=True,
        population="Safety Population",
        figure_description="Swimmer: horizontal bars showing treatment duration, response/progression/ongoing markers.",
        dataset_source="ADSL, ADEX, ADRS", program_ref="f_swimmer.sas",
        figure_type="swimmer", figure_width_inches=6.5, figure_height_inches=4,
    ))

    items.append(TFLItem(
        id="F14.2.7", title="Kaplan-Meier Plot — Progression-Free Survival",
        tfl_type=F, section=S142, sort_key=28, oncology_only=True,
        population="Intent-to-Treat (ITT) Population",
        figure_description="KM PFS: step-function curves, + censoring, number-at-risk table, HR/p-value annotation.",
        dataset_source="ADSL, ADTTE", program_ref="f_km_pfs.sas",
        figure_type="km_curve", figure_width_inches=6, figure_height_inches=3.5,
    ))

    items.append(TFLItem(
        id="F14.2.8", title="Kaplan-Meier Plot — Overall Survival",
        tfl_type=F, section=S142, sort_key=29, oncology_only=True,
        population="Intent-to-Treat (ITT) Population",
        figure_description="KM OS: step-function curves, + censoring, number-at-risk table, HR/p-value annotation.",
        dataset_source="ADSL, ADTTE", program_ref="f_km_os.sas",
        figure_type="km_curve", figure_width_inches=6, figure_height_inches=3.5,
    ))

    items.append(TFLItem(
        id="F14.2.9", title="Forest Plot — PFS by Subgroup",
        tfl_type=F, section=S142, sort_key=30, oncology_only=True,
        population="Intent-to-Treat (ITT) Population",
        figure_description="Forest PFS: HR [95% CI] per subgroup, overall diamond at bottom.",
        dataset_source="ADSL, ADTTE", program_ref="f_forest_pfs.sas",
        figure_type="forest", figure_width_inches=6, figure_height_inches=3.5,
    ))

    items.append(TFLItem(
        id="F14.2.10", title="Forest Plot — OS by Subgroup",
        tfl_type=F, section=S142, sort_key=31, oncology_only=True,
        population="Intent-to-Treat (ITT) Population",
        figure_description="Forest OS: HR [95% CI] per subgroup, overall diamond at bottom.",
        dataset_source="ADSL, ADTTE", program_ref="f_forest_os.sas",
        figure_type="forest", figure_width_inches=6, figure_height_inches=3.5,
    ))

    items.append(TFLItem(
        id="T14.2.22", title="PK/PD Exposure-Response Correlation Analysis",
        tfl_type=T, section=S142, sort_key=32,
        population="PK/PD Evaluable Population",
        placeholder_columns=["PK Parameter\nQuartile", "N",
                             "Response Rate (%)", "95% CI"],
        shell_rows=[
            ["AUC0-tau — Q1 (lowest)", "xx", "xx.x%", "[xx.x, xx.x]"],
            ["AUC0-tau — Q2", "xx", "xx.x%", "[xx.x, xx.x]"],
            ["AUC0-tau — Q3", "xx", "xx.x%", "[xx.x, xx.x]"],
            ["AUC0-tau — Q4 (highest)", "xx", "xx.x%", "[xx.x, xx.x]"],
            EROW,
        ],
        dataset_source="ADSL, ADPK, ADEFF", program_ref="t_pkpd_corr.sas",
    ))

    # =====================================================================


    # --- 14.3.1 AE Expansion (CDISC ADAE) ---
    items.append(TFLItem(
        id="T14.3.1.24", title="Immune-Related Adverse Events (irAEs) by Preferred Term",
        tfl_type=T, section=S143, sort_key=24, oncology_only=True,
        population="Safety Population",
        placeholder_columns=["Preferred Term",
                             "G1\nn (%)", "G2\nn (%)", "...", "Overall\nn (%)"],
        shell_rows=[
            {"label": "Any irAE", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Pneumonitis", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Colitis", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Hepatitis", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Dermatitis / Rash", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Thyroiditis", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Nephritis", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["irAEs per protocol-defined list (MedDRA SMQ). Confirmed by adjudication. CTCAE [xx]."],
        dataset_source="ADSL, ADAE", program_ref="t_irae_pt.sas",
        dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.25", title="Infusion-Related Reactions — Onset Timing, Maximum Grade, and Management",
        tfl_type=T, section=S143, sort_key=25,
        population="Safety Population",
        placeholder_columns=["IRR Characteristic",
                             "G1\nn (%)", "G2\nn (%)", "...", "Overall\nn (%)"],
        shell_rows=[
            {"label": "Subjects with Any IRR", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Maximum CTCAE Grade", "bold": True},
            {"label": "  Grade 1", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Grade 2", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Grade >=3", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Onset Timing", "bold": True},
            {"label": "  First infusion (Cycle 1)", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Subsequent infusions", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Management", "bold": True},
            {"label": "  Infusion rate slowed", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Infusion interrupted", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Prophylaxis in subsequent cycles", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["IRR = any AE during or within 24h of infusion start. CTCAE [xx]."],
        dataset_source="ADSL, ADAE, ADEX", program_ref="t_irr_detail.sas",
        dictionary_versions={"CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.26", title="TEAE Outcomes by System Organ Class — Resolved / Recovering / Not Recovered",
        tfl_type=T, section=S143, sort_key=26,
        population="Safety Population",
        placeholder_columns=["System Organ Class",
                             "Recovered\nn (%)", "Recovering\nn (%)",
                             "Not Recovered\nn (%)", "Fatal\nn (%)", "Unknown\nn (%)"],
        shell_rows=[
            {"label": "Gastrointestinal disorders", "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"]},
            {"label": "General disorders", "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"]},
            {"label": "Blood and lymphatic system disorders", "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"]},
            {"label": "Skin and subcutaneous tissue disorders", "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"]},
            {"label": "Nervous system disorders", "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "...", "..."]},
        ],
        footnotes=["Outcome at last follow-up. Recovered = resolved no sequelae. MedDRA [xx.x]."],
        dataset_source="ADSL, ADAE", program_ref="t_ae_outcome.sas",
        dictionary_versions={"MedDRA": "[xx.x]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.27", title="Late-Onset TEAEs (>90 Days from First Dose) by SOC and PT",
        tfl_type=T, section=S143, sort_key=27,
        population="Safety Population with >90 Days Exposure",
        placeholder_columns=["System Organ Class\nPreferred Term",
                             "G1\nn (%)", "G2\nn (%)", "...", "Overall\nn (%)"],
        shell_rows=[
            {"label": "Any Late-Onset TEAE", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Blood and lymphatic system disorders", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Anaemia", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Neutropenia", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Skin disorders", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Rash", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Gastrointestinal disorders", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["Late-onset = AE start >90 days after first dose in subjects with >90 days on treatment. MedDRA [xx.x]."],
        dataset_source="ADSL, ADAE", program_ref="t_ae_late.sas",
        dictionary_versions={"MedDRA": "[xx.x]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.28", title="TEAEs by Post-Baseline Time Window — Onset Distribution",
        tfl_type=T, section=S143, sort_key=28,
        population="Safety Population",
        placeholder_columns=["Time Window",
                             "G1\nn (%) [E]", "G2\nn (%) [E]", "...", "Overall\nn (%) [E]"],
        shell_rows=[
            {"label": "0-30 Days", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "31-90 Days", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "91-180 Days", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": ">180 Days", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "Follow-up (>30d post-last-dose)", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["TEAEs assigned to window by onset date. [E] = total events. MedDRA [xx.x]."],
        dataset_source="ADSL, ADAE", program_ref="t_ae_timewindow.sas",
        dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.29", title="Treatment-Emergent SAEs by PT and ICH E2A Criterion — Group 1",
        tfl_type=T, section=S143, sort_key=29,
        population="Safety Population",
        placeholder_columns=["Preferred Term",
                             "Death\nn", "Life-Threat\nn", "Hospital\nn",
                             "Disability\nn", "Cong. Anom.\nn", "Other\nn", "Total\nn (%)"],
        shell_rows=[
            {"label": "Pneumonia", "values": ["xx", "xx", "xx", "0", "0", "xx", "xx (xx.x)"]},
            {"label": "Febrile Neutropenia", "values": ["xx", "xx", "xx", "0", "0", "0", "xx (xx.x)"]},
            {"label": "Sepsis", "values": ["xx", "xx", "xx", "0", "0", "xx", "xx (xx.x)"]},
            {"label": "Pulmonary Embolism", "values": ["xx", "xx", "xx", "0", "0", "0", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "...", "...", "...", "..."]},
        ],
        footnotes=["SAE per ICH E2A. Multiple criteria per event possible. SAE listing: L16.2.5. MedDRA [xx.x]."],
        dataset_source="ADSL, ADAE", program_ref="t_sae_crit.sas",
        dictionary_versions={"MedDRA": "[xx.x]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.30", title="Recurrent TEAEs — Subjects with Same PT >=2 Occurrences",
        tfl_type=T, section=S143, sort_key=30,
        population="Safety Population",
        placeholder_columns=["System Organ Class\nPreferred Term",
                             "Subjects >=2\nEvents\nn (%)", "Median Events\nper Subject",
                             "G1 [E]", "G2 [E]"],
        shell_rows=[
            {"label": "Gastrointestinal disorders", "bold": True, "values": ["xx (xx.x)", "xx", "[xx]", "[xx]"]},
            {"label": "  Nausea", "indent": True, "values": ["xx (xx.x)", "xx", "[xx]", "[xx]"]},
            {"label": "  Diarrhoea", "indent": True, "values": ["xx (xx.x)", "xx", "[xx]", "[xx]"]},
            {"label": "Blood and lymphatic system disorders", "bold": True, "values": ["xx (xx.x)", "xx", "[xx]", "[xx]"]},
            {"label": "  Anaemia", "indent": True, "values": ["xx (xx.x)", "xx", "[xx]", "[xx]"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["[E] = total number of events. Recurrence = same PT >=2 separate occurrences."],
        dataset_source="ADSL, ADAE", program_ref="t_ae_recur.sas",
        dictionary_versions={"MedDRA": "[xx.x]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.31", title="TEAEs During Follow-up Period (>30 Days Post Last Dose)",
        tfl_type=T, section=S143, sort_key=31,
        population="Safety Population with Follow-up Data",
        placeholder_columns=["System Organ Class\nPreferred Term",
                             "G1\nn (%)", "G2\nn (%)", "...", "Overall\nn (%)"],
        shell_rows=[
            {"label": "Any TEAE During Follow-up", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Blood and lymphatic system disorders", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Anaemia", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Gastrointestinal disorders", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Neoplasms benign, malignant", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["Follow-up period = >30 days after last dose through end of study. MedDRA [xx.x]."],
        dataset_source="ADSL, ADAE", program_ref="t_ae_followup.sas",
        dictionary_versions={"MedDRA": "[xx.x]"},
    ))

    # 14.3 SAFETY — 30 items (AE → Deaths → Labs → VS → ECG)
    # =====================================================================

    items.append(TFLItem(
        id="T14.3.1.1", title="Overall Summary of Treatment-Emergent Adverse Events",
        tfl_type=T, section=S143, sort_key=1,
        population="Safety Population",
        placeholder_columns=["Adverse Event Category",
                             "XXX Group 1\n(N=XX)\nn (%) [E]",
                             "XXX Group 2\n(N=XX)\nn (%) [E]",
                             "...", "Overall\n(N=XX)\nn (%) [E]"],
        shell_rows=[
            {"label": "Any TEAE", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "Drug-Related TEAE", "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "CTCAE Grade >=3 TEAE", "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "Drug-Related Grade >=3 TEAE", "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "Serious TEAE (SAE)", "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "Drug-Related SAE", "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "TEAE Leading to Treatment Discontinuation", "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "TEAE Leading to Dose Interruption", "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "TEAE Leading to Dose Reduction", "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "Fatal TEAE (Grade 5)", "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["TEAE: onset on/after first dose through 30 days after last dose. CTCAE v[xx]. MedDRA [xx.x]."],
        dataset_source="ADSL, ADAE", program_ref="t_ae_overview.sas",
        dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.2", title="TEAEs by System Organ Class and Preferred Term (>=5% in Any Arm)",
        tfl_type=T, section=S143, sort_key=2,
        population="Safety Population",
        placeholder_columns=H2_EVENTS,
        shell_rows=[
            {"label": "Any TEAE", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "Gastrointestinal disorders", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "  Nausea", "indent": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "  Diarrhoea", "indent": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "  Vomiting", "indent": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "  Constipation", "indent": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "General disorders and administration site conditions", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "  Fatigue", "indent": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "  Pyrexia", "indent": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "  Asthenia", "indent": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "Blood and lymphatic system disorders", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "  Anaemia", "indent": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "  Neutropenia", "indent": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "  Thrombocytopenia", "indent": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "Metabolism and nutrition disorders", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "  Decreased appetite", "indent": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "  Hypokalaemia", "indent": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "Skin and subcutaneous tissue disorders", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "  Rash", "indent": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "  Pruritus", "indent": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "Nervous system disorders", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "  Headache", "indent": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "  Dizziness", "indent": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "Respiratory, thoracic and mediastinal disorders", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "  Cough", "indent": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "  Dyspnoea", "indent": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "Infections and infestations", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "  Upper respiratory tract infection", "indent": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["Sorted alphabetically by SOC; PTs by descending frequency in G1. "
                   "[E]=total events. MedDRA [xx.x]. CTCAE [xx]."],
        dataset_source="ADSL, ADAE", program_ref="t_ae_soc_pt.sas",
        dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.3", title="TEAEs by SOC, PT, and Maximum CTCAE Grade (Group 1)",
        tfl_type=T, section=S143, sort_key=3,
        population="Safety Population",
        placeholder_columns=["System Organ Class\nPreferred Term",
                             "Grade 1\nn (%)", "Grade 2\nn (%)", "Grade 3\nn (%)",
                             "Grade 4\nn (%)", "Grade 5\nn (%)", "Any Grade\nn (%)"],
        shell_rows=[
            ["Gastrointestinal disorders", "", "", "", "", "", "xx (xx.x)"],
            ["  Nausea", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"],
            EROW6,
        ],
        footnotes=["CTCAE [xx]. Table repeated for Group 2 and Overall."],
        dataset_source="ADSL, ADAE", program_ref="t_ae_grade.sas",
        dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.4", title="Drug-Related TEAEs by SOC, PT, and Relationship",
        tfl_type=T, section=S143, sort_key=4,
        population="Safety Population",
        placeholder_columns=H2_SOCPT,
        shell_rows=[
            ["Any Drug-Related TEAE", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Gastrointestinal disorders", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["  Nausea", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["  Diarrhea", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            EROW,
        ],
        dataset_source="ADSL, ADAE", program_ref="t_ae_related.sas",
        dictionary_versions={"MedDRA": "[xx.x]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.5", title="Serious Adverse Events by SOC and PT",
        tfl_type=T, section=S143, sort_key=5,
        population="Safety Population",
        placeholder_columns=H2_EVENTS,
        shell_rows=[
            {"label": "Any SAE", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "Infections and infestations", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "  Pneumonia", "indent": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "  Sepsis", "indent": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "Gastrointestinal disorders", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "  Diarrhoea", "indent": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "  Intestinal Obstruction", "indent": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "Respiratory, thoracic and mediastinal disorders", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "  Pulmonary Embolism", "indent": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["SAE defined per ICH E2A criteria."],
        dataset_source="ADSL, ADAE", program_ref="t_sae_soc_pt.sas",
        dictionary_versions={"MedDRA": "[xx.x]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.6", title="TEAEs Leading to Treatment Discontinuation by SOC and PT",
        tfl_type=T, section=S143, sort_key=6,
        population="Safety Population",
        placeholder_columns=H2_SOCPT,
        shell_rows=[
            {"label": "Any TEAE Leading to Discontinuation", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Gastrointestinal disorders", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Diarrhoea", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Nausea", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "General disorders and administration site conditions", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Asthenia", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Investigations", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  ALT Increased", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  AST Increased", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        dataset_source="ADSL, ADAE", program_ref="t_ae_disc.sas",
        dictionary_versions={"MedDRA": "[xx.x]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.7", title="TEAEs Leading to Dose Reduction or Interruption by SOC and PT",
        tfl_type=T, section=S143, sort_key=7,
        population="Safety Population",
        placeholder_columns=H2_SOCPT,
        shell_rows=[
            ["Any TEAE Leading to Dose Modification", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Gastrointestinal disorders", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["  Diarrhea", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["  Nausea", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            EROW,
        ],
        dataset_source="ADSL, ADAE", program_ref="t_ae_dose_mod.sas",
        dictionary_versions={"MedDRA": "[xx.x]"},
    ))

    items.append(TFLItem(
        id="T14.3.2.1", title="Summary of Deaths",
        tfl_type=T, section=S143, sort_key=8,
        population="Safety Population",
        placeholder_columns=H2_NPCT,
        shell_rows=[
            {"label": "Total Deaths", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Due to Adverse Event", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Due to Progressive Disease", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Due to Other Causes", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "On-treatment Deaths (<=30 days of last dose)", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Post-treatment Deaths (>30 days of last dose)", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        dataset_source="ADSL, ADAE, ADTTE", program_ref="t_deaths.sas",
    ))

    items.append(TFLItem(
        id="T14.3.1.8", title="TEAEs Occurring in >=5% of Subjects by PT",
        tfl_type=T, section=S143, sort_key=9,
        population="Safety Population",
        placeholder_columns=H2_SOCPT,
        shell_rows=[
            ["Fatigue", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Nausea", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Diarrhea", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Asthenia", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            EROW,
        ],
        footnotes=["PTs with incidence >=5% in any arm. Sorted by descending frequency in G1."],
        dataset_source="ADSL, ADAE", program_ref="t_ae_5pct.sas",
        dictionary_versions={"MedDRA": "[xx.x]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.9", title="TEAEs by Cycle / Treatment Period",
        tfl_type=T, section=S143, sort_key=10,
        population="Safety Population",
        placeholder_columns=["Cycle",
                             "N at Risk\n(G1 / G2)",
                             "G1 >=1 TEAE\nn (%)", "G2 >=1 TEAE\nn (%)",
                             "...\n...\nOverall\nn (%)"],
        shell_rows=[
            ["Cycle 1", "xx / xx", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Cycle 2", "xx / xx", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Cycle 3", "xx / xx", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            EROW,
        ],
        dataset_source="ADSL, ADAE, ADEX", program_ref="t_ae_by_cycle.sas",
        dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.10", title="Exposure-Adjusted TEAE Incidence Rates (per 100 Patient-Years)",
        tfl_type=T, section=S143, sort_key=11,
        population="Safety Population",
        placeholder_columns=["Preferred Term",
                             "G1 Rate\n[95% CI]", "G2 Rate\n[95% CI]",
                             "...\n...\nOverall\n[95% CI]"],
        shell_rows=[
            ["Fatigue", "xx.xx [xx.xx, xx.xx]", "xx.xx [xx.xx, xx.xx]", "...", "xx.xx [xx.xx, xx.xx]"],
            ["Nausea", "xx.xx [xx.xx, xx.xx]", "xx.xx [xx.xx, xx.xx]", "...", "xx.xx [xx.xx, xx.xx]"],
            EROW,
        ],
        dataset_source="ADSL, ADAE, ADEX", program_ref="t_ae_adj_rate.sas",
        dictionary_versions={"MedDRA": "[xx.x]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.11", title="TEAEs by Age Group Subgroup",
        tfl_type=T, section=S143, sort_key=12,
        population="Safety Population",
        placeholder_columns=["Preferred Term",
                             "Age <65\n(N=XX) n (%)", "Age >=65\n(N=XX) n (%)",
                             "...\n...\nOverall\n(N=XX) n (%)"],
        shell_rows=[
            ["Fatigue", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Nausea", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            EROW,
        ],
        dataset_source="ADSL, ADAE", program_ref="t_ae_age.sas",
        dictionary_versions={"MedDRA": "[xx.x]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.12", title="TEAEs by Sex Subgroup",
        tfl_type=T, section=S143, sort_key=13,
        population="Safety Population",
        placeholder_columns=["Preferred Term",
                             "Male\n(N=XX) n (%)", "Female\n(N=XX) n (%)",
                             "...\n...\nOverall\n(N=XX) n (%)"],
        shell_rows=[
            ["Fatigue", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Nausea", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            EROW,
        ],
        dataset_source="ADSL, ADAE", program_ref="t_ae_sex.sas",
        dictionary_versions={"MedDRA": "[xx.x]"},
    ))

    items.append(TFLItem(
        id="T14.3.2.2", title="Hy's Law Cases — Liver Chemistry Screening",
        tfl_type=T, section=S143, sort_key=14,
        population="Safety Population with Baseline and Post-Baseline Labs",
        placeholder_columns=["Subject", "Group", "ALT\n(xULN)", "AST\n(xULN)",
                             "TBL\n(xULN)", "ALP\n(xULN)", "Hy's Law\nMet?"],
        shell_rows=[
            ["xxxx/xxx", "Gx", "x.x", "x.x", "x.x", "x.x", "Yes / No"],
            EROW6,
        ],
        footnotes=["Hy's Law: ALT/AST >=3xULN, TBL >=2xULN, ALP <2xULN, no alternative etiology."],
        dataset_source="ADSL, ADLB", program_ref="t_hys_law.sas",
    ))

    items.append(TFLItem(
        id="T14.3.3.1", title="Laboratory Parameters — Shift Table (Baseline to Worst Post-Baseline)",
        tfl_type=T, section=S143, sort_key=15,
        population="Safety Population",
        placeholder_columns=["Parameter\n(Unit)", "Baseline\nGrade",
                             "Worst Post-BL\nGrade",
                             "G1\nn (%)", "G2\nn (%)", "...\n...\nOverall\nn (%)"],
        shell_rows=[
            ["Hemoglobin (g/dL)", "Normal", "Low", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["", "Normal", "Normal", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["", "Low", "Low", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["ALT (U/L)", "Normal", "High (>ULN)", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            EROW6,
        ],
        dataset_source="ADSL, ADLB", program_ref="t_lab_shift.sas",
        dictionary_versions={"CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="T14.3.3.2", title="Hematology Parameters — Summary Statistics by Visit",
        tfl_type=T, section=S143, sort_key=16,
        population="Safety Population",
        placeholder_columns=H2_LAB,
        shell_rows=[
            ["Hemoglobin (g/dL)", "", "", "", "", ""],
            ["  Baseline — n", "xx", "xx", "...", "xx"],
            ["  Baseline — Mean (SD)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            ["  Week 4 — n", "xx", "xx", "...", "xx"],
            ["  Week 4 — Mean (SD)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            ["Platelets (×10⁹/L)", "", "", "", "", ""],
            ["  Baseline — Mean (SD)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            EROW,
        ],
        dataset_source="ADSL, ADLB", program_ref="t_heme_by_visit.sas",
    ))

    items.append(TFLItem(
        id="T14.3.3.3", title="Clinical Chemistry Parameters — Summary Statistics by Visit",
        tfl_type=T, section=S143, sort_key=17,
        population="Safety Population",
        placeholder_columns=H2_LAB,
        shell_rows=[
            ["ALT (U/L)", "", "", "", "", ""],
            ["  Baseline — Mean (SD)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            ["  Week 4 — Mean (SD)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            ["AST (U/L)", "", "", "", "", ""],
            ["  Baseline — Mean (SD)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            ["Total Bilirubin (mg/dL)", "", "", "", "", ""],
            ["  Baseline — Mean (SD)", "x.xx (x.xx)", "x.xx (x.xx)", "...", "x.xx (x.xx)"],
            EROW,
        ],
        dataset_source="ADSL, ADLB", program_ref="t_chem_by_visit.sas",
    ))

    items.append(TFLItem(
        id="T14.3.3.4", title="Laboratory Abnormalities — Grade >=3 Listing",
        tfl_type=T, section=S143, sort_key=18,
        population="Safety Population",
        placeholder_columns=["Subject", "Group", "Visit", "Parameter",
                             "Result", "Unit", "ULN", "CTCAE\nGrade"],
        shell_rows=[
            ["xxxx/xxx", "Gx", "Wk xx", "ALT", "xxx", "U/L", "xx", "x"],
            EROW6,
        ],
        dataset_source="ADSL, ADLB", program_ref="l_lab_grade3.sas",
        dictionary_versions={"CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="T14.3.3.5", title="Laboratory Toxicity Grade Shift Over Time (by Cycle)",
        tfl_type=T, section=S143, sort_key=19,
        population="Safety Population",
        placeholder_columns=["Parameter", "Cycle", "Baseline\nGrade",
                             "Max Post-BL\nGrade",
                             "G1\nn/N (%)", "G2\nn/N (%)", "...\n...\nOverall\nn/N (%)"],
        shell_rows=[
            ["ALT", "Cycle 1", "0-1", "2", "xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
            ["ALT", "Cycle 1", "0-1", "3-4", "xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
            EROW6,
        ],
        dataset_source="ADSL, ADLB", program_ref="t_lab_shift_cycle.sas",
        dictionary_versions={"CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="F14.3.3.1", title="Mean (+/- SD) Change in Laboratory Parameters Over Time",
        tfl_type=F, section=S143, sort_key=20,
        population="Safety Population",
        figure_description="Multi-panel line plot: mean ± SD change in Hgb, Plt, ANC, ALT, AST, Creatinine.",
        dataset_source="ADSL, ADLB", program_ref="f_lab_longitudinal.sas",
        figure_type="longitudinal", figure_width_inches=6, figure_height_inches=4,
    ))

    items.append(TFLItem(
        id="F14.3.3.2", title="Box Plot — Liver Function Tests by Visit",
        tfl_type=F, section=S143, sort_key=21,
        population="Safety Population",
        figure_description="Box plots: ALT, AST, ALP, Total Bilirubin by visit, side-by-side arms, ULN ref lines.",
        dataset_source="ADSL, ADLB", program_ref="f_lft_box.sas",
        figure_type="box_plot", figure_width_inches=6, figure_height_inches=4,
    ))

    items.append(TFLItem(
        id="T14.3.4.1", title="Vital Signs — Summary Statistics by Visit",
        tfl_type=T, section=S143, sort_key=22,
        population="Safety Population",
        placeholder_columns=H2_LAB,
        shell_rows=[
            ["Systolic BP (mmHg)", "", "", "", "", ""],
            ["  Baseline — Mean (SD)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            ["  Week 4 — Mean (SD)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            ["Diastolic BP (mmHg)", "", "", "", "", ""],
            ["  Baseline — Mean (SD)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            ["Heart Rate (bpm)", "", "", "", "", ""],
            ["  Baseline — Mean (SD)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            EROW,
        ],
        dataset_source="ADSL, ADVS", program_ref="t_vs_by_visit.sas",
    ))

    items.append(TFLItem(
        id="T14.3.4.2", title="Vital Signs — Clinically Notable Abnormalities by Visit",
        tfl_type=T, section=S143, sort_key=23,
        population="Safety Population",
        placeholder_columns=["Parameter", "Criterion",
                             "G1\nn (%)", "G2\nn (%)", "...\n...\nOverall\nn (%)"],
        shell_rows=[
            ["SBP", "<=90 mmHg and decrease >=20", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["SBP", ">=180 mmHg and increase >=20", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["DBP", "<=50 mmHg and decrease >=15", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            EROW,
        ],
        dataset_source="ADSL, ADVS", program_ref="t_vs_notable.sas",
    ))

    items.append(TFLItem(
        id="F14.3.4.1", title="Mean (+/- SD) Vital Signs Over Time",
        tfl_type=F, section=S143, sort_key=24,
        population="Safety Population",
        figure_description="Multi-panel: mean ± SD of SBP, DBP, HR, Weight over visits.",
        dataset_source="ADSL, ADVS", program_ref="f_vs_longitudinal.sas",
        figure_type="longitudinal", figure_width_inches=6, figure_height_inches=4,
    ))

    items.append(TFLItem(
        id="F14.3.3.3", title="Liver Function Panel — Mean Over Time with ULN Reference",
        tfl_type=F, section=S143, sort_key=25,
        population="Safety Population",
        figure_description="Line plot: ALT, AST, ALP, TBL means over visits with ULN lines.",
        dataset_source="ADSL, ADLB", program_ref="f_lft_uln.sas",
        figure_type="longitudinal", figure_width_inches=5.5, figure_height_inches=3.5,
    ))

    items.append(TFLItem(
        id="T14.3.4.3", title="ECG Parameters — Summary Statistics by Visit",
        tfl_type=T, section=S143, sort_key=26,
        population="Safety Population with ECG Data",
        placeholder_columns=H2_LAB,
        shell_rows=[
            ["QTcF (ms)", "", "", "", "", ""],
            ["  Baseline — Mean (SD)", "xxx (xx)", "xxx (xx)", "...", "xxx (xx)"],
            ["  Week 4 — Mean (SD)", "xxx (xx)", "xxx (xx)", "...", "xxx (xx)"],
            ["  Change from BL", "xx (xx)", "xx (xx)", "...", "xx (xx)"],
            EROW,
        ],
        footnotes=["QTcF = Fridericia correction. Triplicate ECGs at each visit; mean analyzed."],
        dataset_source="ADSL, ADEG", program_ref="t_ecg_by_visit.sas",
    ))

    items.append(TFLItem(
        id="T14.3.4.4", title="ECG QTcF Categorical Analysis",
        tfl_type=T, section=S143, sort_key=27,
        population="Safety Population with ECG Data",
        placeholder_columns=["QTcF Category",
                             "G1\n(N=XX) n (%)", "G2\n(N=XX) n (%)",
                             "...\n...\nOverall\n(N=XX) n (%)"],
        shell_rows=[
            ["Absolute QTcF <=450 ms", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Absolute QTcF >450-480 ms", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Absolute QTcF >480-500 ms", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Absolute QTcF >500 ms", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Change from BL <=30 ms", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Change from BL >30-60 ms", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Change from BL >60 ms", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            EROW,
        ],
        dataset_source="ADSL, ADEG", program_ref="t_qtcf_cat.sas",
    ))

    items.append(TFLItem(
        id="T14.3.4.5", title="ECG Qualitative Assessment — Shift Table",
        tfl_type=T, section=S143, sort_key=28,
        population="Safety Population with ECG Data",
        placeholder_columns=["Baseline", "Worst\nPost-Baseline",
                             "G1\nn (%)", "G2\nn (%)", "...\n...\nOverall\nn (%)"],
        shell_rows=[
            ["Normal", "Normal", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Normal", "Abnormal NCS", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Normal", "Abnormal CS", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            EROW,
        ],
        footnotes=["NCS = Not Clinically Significant. CS = Clinically Significant."],
        dataset_source="ADSL, ADEG", program_ref="t_ecg_shift.sas",
    ))

    items.append(TFLItem(
        id="T14.3.1.13", title="Infusion-Related Reactions by Preferred Term",
        tfl_type=T, section=S143, sort_key=29,
        population="Safety Population",
        placeholder_columns=H2_SOCPT,
        shell_rows=[
            ["Any Infusion-Related Reaction", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Pyrexia", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Chills", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            EROW,
        ],
        dataset_source="ADSL, ADAE, ADEX", program_ref="t_irr.sas",
        dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="T14.3.2.3", title="ECOG Performance Status Shift Table",
        tfl_type=T, section=S143, sort_key=30,
        population="Safety Population",
        placeholder_columns=["Baseline\nECOG", "Worst Post-BL\nECOG",
                             "G1\nn (%)", "G2\nn (%)", "...\n...\nOverall\nn (%)"],
        shell_rows=[
            ["0", "0", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["0", "1", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["0", ">=2", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["1", "1", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            EROW,
        ],
        dataset_source="ADSL, ADQS", program_ref="t_ecog_shift.sas",
    ))

    items.append(TFLItem(
        id="T14.3.1.14", title="Adverse Events of Special Interest (AESI) — Summary",
        tfl_type=T, section=S143, sort_key=31,
        population="Safety Population",
        placeholder_columns=["AESI Category",
                             "XXX Group 1\n(N=XX)\nn (%) [E]",
                             "XXX Group 2\n(N=XX)\nn (%) [E]",
                             "...", "Overall\n(N=XX)\nn (%) [E]"],
        shell_rows=[
            {"label": "Subjects with Any AESI", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "AESI Category 1: Infusion-Related Reactions", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "  Grade 1-2", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Grade >=3", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Serious AESIs", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Leading to Discontinuation", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "AESI Category 2: Hepatotoxicity", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "  ALT/AST >=3xULN + TBL >=2xULN (Hy's Law)", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  ALT/AST >=5xULN", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  ALT/AST >=10xULN", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "AESI Category 3: Cardiac Events", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "  QTcF Prolongation >500 ms", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Arrhythmia", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Left Ventricular Dysfunction", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "AESI Category 4: Immunogenicity-Related", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "  Hypersensitivity / Anaphylaxis", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Cytokine Release Syndrome", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["AESIs pre-specified in protocol [ref] and SAP [ref]. [E] = number of events.",
                   "MedDRA [xx.x] and CTCAE [xx] used for coding and grading. Groupings based on SMQ/custom MedDRA queries.",
                   "Subjects may have events in more than one AESI category."],
        dataset_source="ADSL, ADAE", program_ref="t_aesi_summary.sas",
        dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.15", title="AESI — Time to First Occurrence",
        tfl_type=T, section=S143, sort_key=32,
        population="Safety Population",
        placeholder_columns=["AESI Category",
                             "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)",
                             "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "Infusion-Related Reactions", "bold": True},
            {"label": "  Events / N (%)", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Median Time to First Onset, days (Range)", "indent": True, "values": ["xx (x-xx)", "xx (x-xx)", "...", "xx (x-xx)"]},
            {"label": "Hepatotoxicity (ALT/AST >=3xULN)", "bold": True},
            {"label": "  Events / N (%)", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Median Time to First Onset, days (Range)", "indent": True, "values": ["xx (x-xx)", "xx (x-xx)", "...", "xx (x-xx)"]},
            {"label": "Cardiac Events", "bold": True},
            {"label": "  Events / N (%)", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Median Time to First Onset, days (Range)", "indent": True, "values": ["xx (x-xx)", "xx (x-xx)", "...", "xx (x-xx)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["Time calculated from first dose of study drug to first AESI occurrence."],
        dataset_source="ADSL, ADAE", program_ref="t_aesi_ttf.sas",
        dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="T14.3.3.6", title="Laboratory Parameters — Descriptive Statistics and Change from Baseline by Visit",
        tfl_type=T, section=S143, sort_key=33,
        population="Safety Population",
        placeholder_columns=["Parameter\nVisit", "Statistic",
                             "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)",
                             "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "HEMATOLOGY", "bold": True},
            {"label": "Hemoglobin (g/L)", "bold": True},
            {"label": "  Baseline — n", "indent": True, "values": ["xx", "xx", "...", "xx"]},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Week 4 — n", "indent": True, "values": ["xx", "xx", "...", "xx"]},
            {"label": "  Week 4 — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Week 4 — Mean Chg from BL (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Week 12 — n", "indent": True, "values": ["xx", "xx", "...", "xx"]},
            {"label": "  Week 12 — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Week 12 — Mean Chg from BL (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  End of Treatment — Mean Chg from BL (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "Platelets (10⁹/L)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Week 4 — Mean Chg from BL (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  End of Treatment — Mean Chg from BL (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "LIVER FUNCTION TESTS", "bold": True},
            {"label": "ALT (U/L)", "bold": True},
            {"label": "  Baseline — n", "indent": True, "values": ["xx", "xx", "...", "xx"]},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Week 4 — Mean Chg from BL (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Week 12 — Mean Chg from BL (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  End of Treatment — Mean Chg from BL (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "AST (U/L)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  End of Treatment — Mean Chg from BL (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "Total Bilirubin (µmol/L)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["x.xx (x.xx)", "x.xx (x.xx)", "...", "x.xx (x.xx)"]},
            {"label": "  End of Treatment — Mean Chg from BL (SD)", "indent": True, "values": ["x.xx (x.xx)", "x.xx (x.xx)", "...", "x.xx (x.xx)"]},
            {"label": "RENAL FUNCTION", "bold": True},
            {"label": "Creatinine (µmol/L)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  End of Treatment — Mean Chg from BL (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "ELECTROLYTES", "bold": True},
            {"label": "Sodium (mmol/L)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "Potassium (mmol/L)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["x.xx (x.xx)", "x.xx (x.xx)", "...", "x.xx (x.xx)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["Baseline = last non-missing assessment on or before first dose date.",
                   "Change from Baseline = Visit value - Baseline value. CTCAE [xx] for grading.",
                   "Full visit schedule: Screening, Baseline, Week 2, 4, 8, 12, 16, 20, 24, End of Treatment, Follow-up."],
        dataset_source="ADSL, ADLB", program_ref="t_lab_chg_bl.sas",
        dictionary_versions={"CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="T14.3.3.7", title="Laboratory Parameters — CTCAE Grade Shift (Baseline to Worst Post-Baseline)",
        tfl_type=T, section=S143, sort_key=34,
        population="Safety Population",
        placeholder_columns=["Parameter\nBaseline Grade", "Worst Post-BL Grade",
                             "G1\nn (%)", "G2\nn (%)",
                             "...", "Overall\nn (%)"],
        shell_rows=[
            {"label": "Hemoglobin (Anemia)", "bold": True},
            {"label": "  Grade 0", "indent": True},
            {"label": "    To Grade 0", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "    To Grade 1", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "    To Grade 2", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "    To Grade 3-4", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Grade 1", "indent": True},
            {"label": "    To Grade 1", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "    To Grade 2", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "    To Grade 3-4", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Neutrophils (Neutropenia)", "bold": True},
            {"label": "  Grade 0", "indent": True},
            {"label": "    To Grade 1-2", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "    To Grade 3", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "    To Grade 4", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Platelets (Thrombocytopenia)", "bold": True},
            {"label": "  Grade 0 to Grade 1-2", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Grade 0 to Grade 3-4", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "ALT", "bold": True},
            {"label": "  Grade 0 to Grade 1", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Grade 0 to Grade 2", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Grade 0 to Grade 3-4", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "AST", "bold": True},
            {"label": "  Grade 0 to Grade 3-4", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Creatinine", "bold": True},
            {"label": "  Grade 0 to Grade 1-2", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Grade 0 to Grade 3-4", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["CTCAE [xx] for grading. Baseline = last assessment before first dose. Worst post-baseline = highest grade on treatment.",
                   "Percentages based on number of subjects with both baseline and at least one post-baseline assessment."],
        dataset_source="ADSL, ADLB", program_ref="t_lab_grade_shift.sas",
        dictionary_versions={"CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.16", title="TEAEs by Worst CTCAE Grade and System Organ Class",
        tfl_type=T, section=S143, sort_key=35,
        population="Safety Population",
        placeholder_columns=["System Organ Class",
                             "Grade 1\nn (%)", "Grade 2\nn (%)",
                             "Grade 3\nn (%)", "Grade 4\nn (%)",
                             "Grade 5\nn (%)", "Any Grade\nn (%)"],
        shell_rows=[
            {"label": "Any TEAE", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"]},
            {"label": "Gastrointestinal disorders", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "0", "xx (xx.x)"]},
            {"label": "  Nausea", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "0", "0", "xx (xx.x)"]},
            {"label": "  Diarrhoea", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "0", "0", "xx (xx.x)"]},
            {"label": "General disorders", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "0", "0", "xx (xx.x)"]},
            {"label": "Blood and lymphatic system disorders", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "0", "xx (xx.x)"]},
            {"label": "Infections and infestations", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "0", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "...", "...", "..."]},
        ],
        footnotes=["CTCAE v[xx]. Each subject counted once per SOC at the maximum grade reported. MedDRA [xx.x].",
                   "Table shown for Group 1; analogous tables generated for Group 2 and Overall."],
        dataset_source="ADSL, ADAE", program_ref="t_ae_worst_grade.sas",
        dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.17", title="TEAEs by Preferred Term — Full Frequency Listing (All PTs)",
        tfl_type=T, section=S143, sort_key=36,
        population="Safety Population",
        placeholder_columns=["Preferred Term", "SOC",
                             "G1\nn (%)", "G2\nn (%)",
                             "...", "Overall\nn (%)"],
        shell_rows=[
            {"label": "Nausea", "values": ["Gastrointestinal disorders", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Diarrhoea", "values": ["Gastrointestinal disorders", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Fatigue", "values": ["General disorders", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Anaemia", "values": ["Blood and lymphatic", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Neutropenia", "values": ["Blood and lymphatic", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Decreased appetite", "values": ["Metabolism and nutrition", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Rash", "values": ["Skin and subcutaneous", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["All PTs reported in any treatment group. Sorted by descending frequency in Group 1.",
                   "MedDRA [xx.x]. CTCAE [xx]. Each subject counted once per preferred term."],
        dataset_source="ADSL, ADAE", program_ref="t_ae_pt_full.sas",
        dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.18", title="TEAEs — Maximum Severity by Relationship to Study Drug",
        tfl_type=T, section=S143, sort_key=37,
        population="Safety Population",
        placeholder_columns=["System Organ Class\nPreferred Term",
                             "Related\nAny Grade / Grade >=3",
                             "Not Related\nAny Grade / Grade >=3",
                             "...", "Overall\nAny Grade / Grade >=3"],
        shell_rows=[
            {"label": "Any TEAE", "bold": True, "values": ["xx (xx.x) / xx (xx.x)", "xx (xx.x) / xx (xx.x)", "...", "xx (xx.x) / xx (xx.x)"]},
            {"label": "Gastrointestinal disorders", "bold": True, "values": ["xx (xx.x) / xx (xx.x)", "xx (xx.x) / xx (xx.x)", "...", "xx (xx.x) / xx (xx.x)"]},
            {"label": "  Nausea", "indent": True, "values": ["xx (xx.x) / xx (xx.x)", "xx (xx.x) / xx (xx.x)", "...", "xx (xx.x) / xx (xx.x)"]},
            {"label": "  Diarrhoea", "indent": True, "values": ["xx (xx.x) / xx (xx.x)", "xx (xx.x) / xx (xx.x)", "...", "xx (xx.x) / xx (xx.x)"]},
            {"label": "Blood and lymphatic system disorders", "bold": True, "values": ["xx (xx.x) / xx (xx.x)", "xx (xx.x) / xx (xx.x)", "...", "xx (xx.x) / xx (xx.x)"]},
            {"label": "  Anaemia", "indent": True, "values": ["xx (xx.x) / xx (xx.x)", "xx (xx.x) / xx (xx.x)", "...", "xx (xx.x) / xx (xx.x)"]},
            {"label": "Skin and subcutaneous tissue disorders", "bold": True, "values": ["xx (xx.x) / xx (xx.x)", "xx (xx.x) / xx (xx.x)", "...", "xx (xx.x) / xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["Related = drug-related per investigator assessment. MedDRA [xx.x]. CTCAE [xx]."],
        dataset_source="ADSL, ADAE", program_ref="t_ae_sev_rel.sas",
        dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.19", title="Time to Onset of TEAEs by System Organ Class",
        tfl_type=T, section=S143, sort_key=38,
        population="Safety Population",
        placeholder_columns=["System Organ Class",
                             "Events\nn", "Median Onset\ndays (Range)",
                             "<=1 day\nn (%)", "2-7 days\nn (%)",
                             "8-30 days\nn (%)", ">30 days\nn (%)"],
        shell_rows=[
            {"label": "Gastrointestinal disorders", "values": ["xx", "xx (x-xx)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"]},
            {"label": "General disorders", "values": ["xx", "xx (x-xx)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"]},
            {"label": "Blood and lymphatic system disorders", "values": ["xx", "xx (x-xx)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"]},
            {"label": "Skin and subcutaneous tissue disorders", "values": ["xx", "xx (x-xx)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"]},
            {"label": "Nervous system disorders", "values": ["xx", "xx (x-xx)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "...", "...", "..."]},
        ],
        footnotes=["Time to onset = (date of first occurrence of TEAE within SOC − date of first dose + 1). MedDRA [xx.x]."],
        dataset_source="ADSL, ADAE", program_ref="t_ae_time_onset.sas",
        dictionary_versions={"MedDRA": "[xx.x]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.20", title="Duration of TEAEs by System Organ Class",
        tfl_type=T, section=S143, sort_key=39,
        population="Safety Population",
        placeholder_columns=["System Organ Class",
                             "Events\nn", "Median Duration\ndays (Range)",
                             "<=7 days\nn (%)", "8-30 days\nn (%)",
                             "31-90 days\nn (%)", ">90 days\nn (%)"],
        shell_rows=[
            {"label": "Gastrointestinal disorders", "values": ["xx", "xx (x-xx)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"]},
            {"label": "General disorders", "values": ["xx", "xx (x-xx)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"]},
            {"label": "Blood and lymphatic system disorders", "values": ["xx", "xx (x-xx)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"]},
            {"label": "Skin and subcutaneous tissue disorders", "values": ["xx", "xx (x-xx)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "...", "...", "..."]},
        ],
        footnotes=["Duration = (end date − start date + 1) for each event. Unresolved events censored at data cutoff.", "MedDRA [xx.x]."],
        dataset_source="ADSL, ADAE", program_ref="t_ae_duration.sas",
        dictionary_versions={"MedDRA": "[xx.x]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.21", title="TEAEs by Preferred Term and Maximum CTCAE Grade — Group 2",
        tfl_type=T, section=S143, sort_key=40,
        population="Safety Population",
        placeholder_columns=["System Organ Class\nPreferred Term",
                             "Any Grade\nn (%)", "Grade 1\nn (%)",
                             "Grade 2\nn (%)", "Grade 3\nn (%)",
                             "Grade 4\nn (%)", "Grade 5\nn (%)"],
        shell_rows=[
            {"label": "Gastrointestinal disorders", "bold": True},
            {"label": "  Nausea", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "0", "0"]},
            {"label": "  Diarrhoea", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "0", "0"]},
            {"label": "  Vomiting", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "0", "0"]},
            {"label": "Blood and lymphatic system disorders", "bold": True},
            {"label": "  Anaemia", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "0", "0"]},
            {"label": "  Neutropenia", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "0"]},
            {"label": "[...]", "values": ["...", "...", "...", "...", "...", "..."]},
        ],
        footnotes=["Table shown for Group 2. Analogous table generated for Group 1 (T14.3.3). CTCAE [xx]. MedDRA [xx.x]."],
        dataset_source="ADSL, ADAE", program_ref="t_ae_grade_g2.sas",
        dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.22", title="TEAEs by Cycle — Detailed On-Treatment Period Analysis",
        tfl_type=T, section=S143, sort_key=41,
        population="Safety Population",
        placeholder_columns=["Cycle", "Subjects\nat Risk",
                             "G1 Any TEAE\nn (%)", "G1 Grade >=3\nn (%)",
                             "G2 Any TEAE\nn (%)", "G2 Grade >=3\nn (%)"],
        shell_rows=[
            {"label": "Cycle 1", "values": ["xx / xx", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"]},
            {"label": "Cycle 2", "values": ["xx / xx", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"]},
            {"label": "Cycle 3", "values": ["xx / xx", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"]},
            {"label": "Cycle 4", "values": ["xx / xx", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"]},
            {"label": "Cycle 5", "values": ["xx / xx", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"]},
            {"label": "Cycle 6", "values": ["xx / xx", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"]},
            {"label": "Cycle >=7", "values": ["xx / xx", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "...", "..."]},
        ],
        footnotes=["Cycle = 21/28-day treatment cycle. Subjects at risk = subjects receiving any dose in the cycle.",
                   "TEAE counted in the cycle of onset. MedDRA [xx.x]. CTCAE [xx]."],
        dataset_source="ADSL, ADAE, ADEX", program_ref="t_ae_by_cycle_detail.sas",
        dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="T14.3.3.8", title="Laboratory Parameters — Clinically Significant Abnormalities Summary",
        tfl_type=T, section=S143, sort_key=42,
        population="Safety Population",
        placeholder_columns=["Parameter (Unit)\nDirection / Criterion",
                             "G1\nn/N1 (%)", "G2\nn/N2 (%)",
                             "...", "Overall\nn/N (%)"],
        shell_rows=[
            {"label": "HEMATOLOGY", "bold": True},
            {"label": "Hemoglobin (g/L)", "bold": True},
            {"label": "  Grade 3-4 (<80 g/L)", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "  Decrease from BL >=20 g/L", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "Neutrophils (10⁹/L)", "bold": True},
            {"label": "  Grade 3-4 (<1.0 ×10⁹/L)", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "Platelets (10⁹/L)", "bold": True},
            {"label": "  Grade 3-4 (<50 ×10⁹/L)", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "LIVER FUNCTION", "bold": True},
            {"label": "ALT (U/L)", "bold": True},
            {"label": "  >=3 × ULN", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "  >=5 × ULN", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "  >=10 × ULN", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "  >=20 × ULN", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "Total Bilirubin (µmol/L)", "bold": True},
            {"label": "  >=2 × ULN", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "RENAL FUNCTION", "bold": True},
            {"label": "Creatinine (µmol/L)", "bold": True},
            {"label": "  >=1.5 × Baseline", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "  >=2 × Baseline", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "eGFR (mL/min/1.73m²)", "bold": True},
            {"label": "  <60 (Grade 2)", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "  <30 (Grade 4)", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["N1/N2 = number of subjects with non-missing baseline and >=1 post-baseline assessment.",
                   "Percentages based on N1/N2 per arm. CTCAE [xx]. Criteria based on protocol-defined thresholds and CTCAE grading."],
        dataset_source="ADSL, ADLB", program_ref="t_lab_cs_abn.sas",
        dictionary_versions={"CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="T14.3.3.9", title="Hematology — Shift Table by CTCAE Grade (Baseline to Worst Post-Baseline) — Detailed",
        tfl_type=T, section=S143, sort_key=43,
        population="Safety Population",
        placeholder_columns=["Parameter\nBaseline Grade", "Worst Post-BL\nGrade",
                             "G1\nn/N (%)", "G2\nn/N (%)",
                             "...", "Overall\nn/N (%)"],
        shell_rows=[
            {"label": "Hemoglobin — Anemia", "bold": True},
            {"label": "  Grade 0", "indent": True},
            {"label": "    Remained Grade 0", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "    Worsened to Grade 1", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "    Worsened to Grade 2", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "    Worsened to Grade 3-4", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "  Grade 1-2 at Baseline", "indent": True},
            {"label": "    Improved to Grade 0", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "    Remained Grade 1-2", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "    Worsened to Grade 3-4", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "Neutrophils — Neutropenia", "bold": True},
            {"label": "  Grade 0 to Grade 1-2", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "  Grade 0 to Grade 3", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "  Grade 0 to Grade 4", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "Platelets — Thrombocytopenia", "bold": True},
            {"label": "  Grade 0 to Grade 1-2", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "  Grade 0 to Grade 3-4", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["N = subjects with both baseline and >=1 post-baseline assessment. CTCAE [xx].",
                   "Worst post-baseline = maximum CTCAE grade on treatment."],
        dataset_source="ADSL, ADLB", program_ref="t_heme_shift_detail.sas",
        dictionary_versions={"CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="T14.3.3.10", title="Clinical Chemistry — Shift Table (Normal Range Based) — Baseline to Worst Post-Baseline",
        tfl_type=T, section=S143, sort_key=44,
        population="Safety Population",
        placeholder_columns=["Parameter (Unit)\nBaseline Category",
                             "Worst Post-BL Category",
                             "G1\nn/N (%)", "G2\nn/N (%)",
                             "...", "Overall\nn/N (%)"],
        shell_rows=[
            {"label": "ALT (U/L)", "bold": True},
            {"label": "  Normal", "indent": True},
            {"label": "    Normal", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "    >1-3 × ULN", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "    >3-5 × ULN", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "    >5 × ULN", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "AST (U/L)", "bold": True},
            {"label": "  Normal → >3 × ULN", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "Total Bilirubin (µmol/L)", "bold": True},
            {"label": "  Normal → >1.5 × ULN", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "  Normal → >2 × ULN", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "Creatinine (µmol/L)", "bold": True},
            {"label": "  Normal → >1.5 × BL", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["Normal range per central laboratory reference ranges. BL = Baseline. ULN = Upper Limit of Normal.",
                   "Percentages based on subjects with non-missing baseline and >=1 post-baseline result."],
        dataset_source="ADSL, ADLB", program_ref="t_chem_shift_nr.sas",
    ))

    items.append(TFLItem(
        id="T14.3.4.6", title="Vital Signs — Shift Table (Normal to Clinically Notable)",
        tfl_type=T, section=S143, sort_key=45,
        population="Safety Population",
        placeholder_columns=["Parameter\nCriterion",
                             "G1\nn/N (%)", "G2\nn/N (%)",
                             "...", "Overall\nn/N (%)"],
        shell_rows=[
            {"label": "Systolic BP", "bold": True},
            {"label": "  Baseline Normal → High (>=160 mmHg)", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "  Baseline Normal → Low (<=90 mmHg)", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "Diastolic BP", "bold": True},
            {"label": "  Baseline Normal → High (>=100 mmHg)", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "  Baseline Normal → Low (<=50 mmHg)", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "Heart Rate", "bold": True},
            {"label": "  Baseline Normal → Tachycardia (>=100 bpm)", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "  Baseline Normal → Bradycardia (<=50 bpm)", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "QTcF Interval", "bold": True},
            {"label": "  Baseline <=450 ms → >450-480 ms", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "  Baseline <=450 ms → >480-500 ms", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "  Baseline <=450 ms → >500 ms", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "  Increase from BL >30 ms", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "  Increase from BL >60 ms", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["N = subjects with both baseline and >=1 post-baseline assessment.",
                   "Clinically notable thresholds per protocol-defined criteria."],
        dataset_source="ADSL, ADVS, ADEG", program_ref="t_vs_shift.sas",
    ))

    items.append(TFLItem(
        id="T14.3.4.7", title="Body Weight — Change from Baseline by Visit",
        tfl_type=T, section=S143, sort_key=46,
        population="Safety Population",
        placeholder_columns=["Visit", "Statistic",
                             "G1\n(N=XX)", "G2\n(N=XX)",
                             "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "Baseline", "bold": True},
            {"label": "  n", "indent": True, "values": ["xx", "xx", "...", "xx"]},
            {"label": "  Mean (SD), kg", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "Week 4", "bold": True},
            {"label": "  n", "indent": True, "values": ["xx", "xx", "...", "xx"]},
            {"label": "  Mean (SD), kg", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Mean Chg from BL (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "Week 12", "bold": True},
            {"label": "  Mean Chg from BL (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "End of Treatment", "bold": True},
            {"label": "  Mean Chg from BL (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "Weight Change Category at EOT", "bold": True},
            {"label": "  >=10% Decrease", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  >=5% to <10% Decrease", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Within ±5%", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  >=5% to <10% Increase", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  >=10% Increase", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["Baseline = last assessment before first dose. Change from BL = visit value − baseline value.",
                   "Percentages based on subjects with non-missing data at each visit."],
        dataset_source="ADSL, ADVS", program_ref="t_weight_chg.sas",
    ))

    items.append(TFLItem(
        id="T14.3.4.8", title="ECG Parameters — Quantitative Change from Baseline by Visit",
        tfl_type=T, section=S143, sort_key=47,
        population="Safety Population with ECG Data",
        placeholder_columns=["Parameter\nVisit", "Statistic",
                             "G1\n(N=XX)", "G2\n(N=XX)",
                             "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "Heart Rate (bpm)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Week 4 — Mean Chg (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  End of Treatment — Mean Chg (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "PR Interval (ms)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Week 4 — Mean Chg (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  End of Treatment — Mean Chg (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "QRS Duration (ms)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  End of Treatment — Mean Chg (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "QTcF Interval (ms)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Week 4 — Mean Chg (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Week 12 — Mean Chg (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  End of Treatment — Mean Chg (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["QTcF = Fridericia correction. Triplicate ECGs averaged per timepoint. Change = post-baseline − baseline."],
        dataset_source="ADSL, ADEG", program_ref="t_ecg_chg_bl.sas",
    ))

    items.append(TFLItem(
        id="T14.3.3.11", title="Laboratory Parameters — Worst Post-Baseline Value by Visit Group",
        tfl_type=T, section=S143, sort_key=48,
        population="Safety Population",
        placeholder_columns=["Parameter (Unit)\nVisit Group", "Statistic",
                             "G1\n(N=XX)", "G2\n(N=XX)",
                             "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "HEMATOLOGY", "bold": True},
            {"label": "Hemoglobin (g/L)", "bold": True},
            {"label": "  Early (Wk 1-4) — Worst, Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Mid (Wk 5-12) — Worst, Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Late (Wk >=13) — Worst, Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "Platelets (10⁹/L)", "bold": True},
            {"label": "  Early (Wk 1-4) — Worst, Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Late (Wk >=13) — Worst, Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "LIVER FUNCTION", "bold": True},
            {"label": "ALT (U/L)", "bold": True},
            {"label": "  Early (Wk 1-4) — Worst, Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Mid (Wk 5-12) — Worst, Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Late (Wk >=13) — Worst, Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "RENAL", "bold": True},
            {"label": "Creatinine (µmol/L)", "bold": True},
            {"label": "  Early (Wk 1-4) — Worst, Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Late (Wk >=13) — Worst, Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["Worst post-baseline = minimum (for Hgb/Plt) or maximum (for ALT/AST/Cr) value in each time window.",
                   "Early = Week 1-4, Mid = Week 5-12, Late = Week >=13."],
        dataset_source="ADSL, ADLB", program_ref="t_lab_worst_visit.sas",
    ))

    items.append(TFLItem(
        id="T14.3.1.23", title="Adverse Events — Summary of Multiple Occurrences per Subject",
        tfl_type=T, section=S143, sort_key=49,
        population="Safety Population",
        placeholder_columns=["Number of TEAEs\nper Subject",
                             "G1\nn (%)", "G2\nn (%)",
                             "...", "Overall\nn (%)"],
        shell_rows=[
            {"label": "Subjects with >=1 TEAE", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  1 Event", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  2 Events", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  3 Events", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  4 Events", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  >=5 Events", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Total number of TEAEs [E]", "bold": True, "values": ["[xx]", "[xx]", "...", "[xx]"]},
            {"label": "Subjects with >=1 Grade >=3 TEAE", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  1 Event", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  2 Events", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  >=3 Events", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["Percentage denominator = number of subjects in the Safety Population per arm. [E] = total event count.",
                   "CTCAE [xx]. MedDRA [xx.x]."],
        dataset_source="ADSL, ADAE", program_ref="t_ae_mult_occ.sas",
        dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
    ))

    # =====================================================================


    # --- 14.3.2 Other Safety Expansion ---
    items.append(TFLItem(
        id="T14.3.2.4", title="Hy's Law — Component Parameters Detail at Peak Value per Subject",
        tfl_type=T, section=S143, sort_key=4,
        population="Safety Population with Baseline and >=1 Post-Baseline Labs",
        placeholder_columns=["Subject", "Group", "Peak ALT\n(xULN)", "Peak AST\n(xULN)",
                             "Peak TBL\n(xULN)", "Peak ALP\n(xULN)", "Hy's Law\nMet?"],
        shell_rows=[
            ["xxxx/xxx", "Gx", "xx.x", "xx.x", "xx.x", "xx.x", "Yes / No"],
            ["xxxx/xxx", "Gx", "xx.x", "xx.x", "xx.x", "xx.x", "Yes / No"],
            {"label": "[...]", "values": ["...", "...", "...", "...", "...", "..."]},
        ],
        footnotes=["Hy's Law: ALT/AST >=3xULN + TBL >=2xULN + ALP <2xULN + no alternative etiology. Listing: L16.2.23."],
        dataset_source="ADSL, ADLB", program_ref="t_hyslaw_detail.sas",
    ))

    items.append(TFLItem(
        id="F14.3.2.1", title="eDISH Plot — Peak ALT vs. Peak Total Bilirubin with Hy's Law Zone",
        tfl_type=F, section=S143, sort_key=5,
        population="Safety Population with Baseline and Post-Baseline Labs",
        figure_description="eDISH: log-log scatter of peak ALT (xULN) vs. peak TBL (xULN). Quadrant at ALT >=3xULN, TBL >=2xULN = Hy's Law zone. Individual subject dots labeled.",
        dataset_source="ADSL, ADLB", program_ref="f_edish.sas",
        figure_type="box_plot", figure_width_inches=5.5, figure_height_inches=5.5,
    ))

    items.append(TFLItem(
        id="T14.3.2.5", title="Deaths — Primary and Secondary Causes with Narrative Cross-Reference",
        tfl_type=T, section=S143, sort_key=6,
        population="All Randomized Subjects",
        placeholder_columns=["Subject", "Group", "Primary Cause\nof Death", "Secondary Cause",
                             "Days from\nFirst Dose", "Days from\nLast Dose", "Narrative ID"],
        shell_rows=[
            ["xxxx/xxx", "Gx", "Disease Progression", "Respiratory Failure", "xxx", "xx", "NAR-xxxx"],
            ["xxxx/xxx", "Gx", "Adverse Event", "Sepsis / Multi-organ Failure", "xxx", "xx", "NAR-xxxx"],
            {"label": "[...]", "values": ["...", "...", "...", "...", "...", "..."]},
        ],
        footnotes=["Primary cause per Investigator assessment. Listing: L16.2.20."],
        dataset_source="ADSL, ADAE, ADTTE", program_ref="t_death_detail.sas",
    ))


    # --- 14.3.3 Lab Expansion (CDISC ADLB) ---
    items.append(TFLItem(
        id="T14.3.3.12", title="Coagulation Panel (PT, INR, aPTT) — Change from Baseline by Visit",
        tfl_type=T, section=S143, sort_key=12,
        population="Safety Population",
        placeholder_columns=["Parameter\nVisit", "Statistic",
                             "G1\n(N=XX)", "G2\n(N=XX)", "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "Prothrombin Time (PT, s)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Week 4 — Mean Chg (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  End of Treatment — Mean Chg (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "INR", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  End of Treatment — Mean Chg (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "aPTT (s)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  End of Treatment — Mean Chg (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["PT/INR/aPTT per central laboratory. Listing: L16.2.26."],
        dataset_source="ADSL, ADLB", program_ref="t_coag_chg.sas",
    ))

    items.append(TFLItem(
        id="T14.3.3.13", title="Coagulation Panel — Shift Table (Normal / Prolonged, Baseline to Worst Post-BL)",
        tfl_type=T, section=S143, sort_key=13,
        population="Safety Population",
        placeholder_columns=["Parameter\nBaseline", "Worst Post-BL",
                             "G1\nn/N (%)", "G2\nn/N (%)", "...", "Overall\nn/N (%)"],
        shell_rows=[
            {"label": "PT", "bold": True},
            {"label": "  Normal", "indent": True},
            {"label": "    Normal", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "    Prolonged (>ULN)", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "aPTT", "bold": True},
            {"label": "  Normal → Prolonged (>ULN)", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        dataset_source="ADSL, ADLB", program_ref="t_coag_shift.sas",
    ))

    items.append(TFLItem(
        id="T14.3.3.14", title="Urinalysis — Dipstick Parameters Shift (Baseline to Worst Post-Baseline)",
        tfl_type=T, section=S143, sort_key=14,
        population="Safety Population",
        placeholder_columns=["Parameter\nBaseline Result", "Worst Post-BL Result",
                             "G1\nn/N (%)", "G2\nn/N (%)", "...", "Overall\nn/N (%)"],
        shell_rows=[
            {"label": "pH", "bold": True},
            {"label": "  Normal (5.0-8.0) → Abnormal", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "Protein", "bold": True},
            {"label": "  Negative → Trace/+", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "  Negative → ++/+++", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "Glucose", "bold": True},
            {"label": "  Negative → Positive", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "Blood", "bold": True},
            {"label": "  Negative → Positive", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "Ketones", "bold": True},
            {"label": "  Negative → Positive", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["Dipstick urinalysis. Listing: L16.2.25."],
        dataset_source="ADSL, ADLB", program_ref="t_ua_dip_shift.sas",
    ))

    items.append(TFLItem(
        id="T14.3.3.15", title="Lipid Panel (TC, HDL-C, LDL-C, TG) — Change from Baseline by Visit",
        tfl_type=T, section=S143, sort_key=15,
        population="Safety Population",
        placeholder_columns=["Parameter\nVisit", "Statistic",
                             "G1\n(N=XX)", "G2\n(N=XX)", "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "Total Cholesterol (mmol/L)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Week 12 — Mean Chg (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  End of Treatment — Mean Chg (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "HDL Cholesterol (mmol/L)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  End of Treatment — Mean Chg (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "LDL Cholesterol (mmol/L)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  End of Treatment — Mean Chg (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "Triglycerides (mmol/L)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["Fasting lipid panel per central laboratory."],
        dataset_source="ADSL, ADLB", program_ref="t_lipid_chg.sas",
    ))

    items.append(TFLItem(
        id="T14.3.3.16", title="Lipid Panel — NCEP ATP III Category Shift (Baseline to Worst Post-BL)",
        tfl_type=T, section=S143, sort_key=16,
        population="Safety Population",
        placeholder_columns=["Parameter\nBaseline Category", "Worst Post-BL Category",
                             "G1\nn/N (%)", "G2\nn/N (%)", "...", "Overall\nn/N (%)"],
        shell_rows=[
            {"label": "LDL-C", "bold": True},
            {"label": "  Optimal (<2.6) → Borderline/High (>=3.4)", "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "HDL-C", "bold": True},
            {"label": "  Normal (>=1.0) → Low (<1.0)", "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "Triglycerides", "bold": True},
            {"label": "  Normal (<1.7) → High (>=2.3)", "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["NCEP ATP III categories. N = subjects with baseline and >=1 post-baseline value."],
        dataset_source="ADSL, ADLB", program_ref="t_lipid_shift.sas",
    ))

    items.append(TFLItem(
        id="T14.3.3.17", title="Thyroid Function (TSH, Free T3, Free T4) — Change from Baseline by Visit",
        tfl_type=T, section=S143, sort_key=17,
        population="Safety Population",
        placeholder_columns=["Parameter\nVisit", "Statistic",
                             "G1\n(N=XX)", "G2\n(N=XX)", "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "TSH (mIU/L)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  End of Treatment — Mean Chg (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "Free T3 (pmol/L)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "Free T4 (pmol/L)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  End of Treatment — Mean Chg (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["Thyroid function panel. TSH reference range: 0.4-4.0 mIU/L."],
        dataset_source="ADSL, ADLB", program_ref="t_thyroid_chg.sas",
    ))

    items.append(TFLItem(
        id="T14.3.3.18", title="Glucose Metabolism — Fasting Glucose and HbA1c Change from Baseline",
        tfl_type=T, section=S143, sort_key=18,
        population="Safety Population",
        placeholder_columns=["Parameter\nVisit", "Statistic",
                             "G1\n(N=XX)", "G2\n(N=XX)", "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "Fasting Glucose (mmol/L)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Week 12 — Mean Chg (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  End of Treatment — Mean Chg (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "HbA1c (%)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  End of Treatment — Mean Chg (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["Fasting >=8 hours for glucose and lipid assessments."],
        dataset_source="ADSL, ADLB", program_ref="t_glucose_chg.sas",
    ))

    items.append(TFLItem(
        id="T14.3.3.19", title="Cardiac Biomarkers (hs-Troponin I/T, CK-MB, NT-proBNP) — Summary at Baseline and Worst Post-BL",
        tfl_type=T, section=S143, sort_key=19,
        population="Safety Population",
        placeholder_columns=["Parameter\n(Unit)", "Timepoint", "Statistic",
                             "G1\n(N=XX)", "G2\n(N=XX)", "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "hs-Troponin I (ng/L)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Worst Post-BL — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  >=ULN, n (%)", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "CK-MB (ng/mL)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "NT-proBNP (pg/mL)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["Cardiac biomarkers collected at Screening, Baseline, and on-treatment timepoints. Listing: L16.2.27."],
        dataset_source="ADSL, ADLB", program_ref="t_cardiac_bio.sas",
    ))

    items.append(TFLItem(
        id="T14.3.3.20", title="Pancreatic Enzymes (Amylase, Lipase) — Change from Baseline",
        tfl_type=T, section=S143, sort_key=20,
        population="Safety Population",
        placeholder_columns=["Parameter\n(Unit)", "Statistic",
                             "G1\n(N=XX)", "G2\n(N=XX)", "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "Amylase (U/L)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Worst Post-BL — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  >=2xULN, n (%)", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Lipase (U/L)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Worst Post-BL — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  >=2xULN, n (%)", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["Pancreatic enzymes per central laboratory. ULN = Upper Limit of Normal."],
        dataset_source="ADSL, ADLB", program_ref="t_pancreas.sas",
    ))

    items.append(TFLItem(
        id="T14.3.3.21", title="Serum Immunoglobulins (IgG, IgA, IgM, IgE) — Change from Baseline",
        tfl_type=T, section=S143, sort_key=21,
        population="Safety Population",
        placeholder_columns=["Parameter\n(Unit)", "Statistic",
                             "G1\n(N=XX)", "G2\n(N=XX)", "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "IgG (g/L)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  End of Treatment — Mean Chg (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "IgA (g/L)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "IgM (g/L)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "IgE (IU/mL)", "bold": True},
            {"label": "  Baseline — Geo Mean (CV%)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["Immunoglobulin panel. Listing: L16.2.27."],
        dataset_source="ADSL, ADLB", program_ref="t_ig_chg.sas",
    ))

    items.append(TFLItem(
        id="T14.3.3.22", title="Lymphocyte Subsets (CD3, CD4, CD8, CD19, CD16+CD56) — Change from Baseline by Visit",
        tfl_type=T, section=S143, sort_key=22,
        population="Safety Population",
        placeholder_columns=["Parameter\n(Unit)", "Statistic",
                             "G1\n(N=XX)", "G2\n(N=XX)", "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "CD3+ T Cells (cells/uL)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx (xx)", "xx (xx)", "...", "xx (xx)"]},
            {"label": "  Week 4 — Mean Chg (SD)", "indent": True, "values": ["xx (xx)", "xx (xx)", "...", "xx (xx)"]},
            {"label": "CD4+ Helper T Cells (cells/uL)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx (xx)", "xx (xx)", "...", "xx (xx)"]},
            {"label": "  End of Treatment — Mean Chg (SD)", "indent": True, "values": ["xx (xx)", "xx (xx)", "...", "xx (xx)"]},
            {"label": "CD8+ Cytotoxic T Cells (cells/uL)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx (xx)", "xx (xx)", "...", "xx (xx)"]},
            {"label": "CD4/CD8 Ratio", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "CD19+ B Cells (cells/uL)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx (xx)", "xx (xx)", "...", "xx (xx)"]},
            {"label": "CD16+CD56+ NK Cells (cells/uL)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx (xx)", "xx (xx)", "...", "xx (xx)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["Lymphocyte subsets by flow cytometry. Listing: L16.2.28."],
        dataset_source="ADSL, ADLB", program_ref="t_lymph_subset.sas",
    ))

    items.append(TFLItem(
        id="T14.3.3.23", title="Inflammatory Cytokine Panel (IL-6, TNF-a, IFN-g, IL-1b, IL-10) — Change from Baseline",
        tfl_type=T, section=S143, sort_key=23,
        population="Safety Population (Subset with Cytokine Data)",
        placeholder_columns=["Cytokine\n(Unit)", "Statistic",
                             "G1\n(N=XX)", "G2\n(N=XX)", "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "IL-6 (pg/mL)", "bold": True},
            {"label": "  Baseline — Geo Mean (CV%)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Cycle 2 — Fold Chg from BL", "indent": True, "values": ["xx.x", "xx.x", "...", "xx.x"]},
            {"label": "TNF-alpha (pg/mL)", "bold": True},
            {"label": "  Baseline — Geo Mean (CV%)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "IFN-gamma (pg/mL)", "bold": True},
            {"label": "  Baseline — Geo Mean (CV%)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "IL-1beta (pg/mL)", "bold": True},
            {"label": "  Baseline — Geo Mean (CV%)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "IL-10 (pg/mL)", "bold": True},
            {"label": "  Baseline — Geo Mean (CV%)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["Cytokine panel by multiplex immunoassay. Listing: L16.2.28."],
        dataset_source="ADSL, ADLB", program_ref="t_cytokine.sas",
    ))

    items.append(TFLItem(
        id="T14.3.3.24", title="Renal Function — AKI Staging per KDIGO Criteria",
        tfl_type=T, section=S143, sort_key=24,
        population="Safety Population",
        placeholder_columns=["KDIGO Stage", "Criterion",
                             "G1\nn/N (%)", "G2\nn/N (%)", "...", "Overall\nn/N (%)"],
        shell_rows=[
            {"label": "Stage 1", "values": ["Cr >=1.5-1.9x BL or >=26.5 umol/L increase", "xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "Stage 2", "values": ["Cr >=2.0-2.9x BL", "xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "Stage 3", "values": ["Cr >=3.0x BL or >=353.6 umol/L or RRT", "xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "Any AKI (Stage 1-3)", "bold": True, "values": ["", "xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
        ],
        footnotes=["KDIGO 2012 criteria. BL = Baseline creatinine. RRT = Renal Replacement Therapy. N = subjects with >=1 post-BL creatinine."],
        dataset_source="ADSL, ADLB", program_ref="t_aki_kdigo.sas",
    ))

    items.append(TFLItem(
        id="T14.3.3.25", title="Urine Chemistry — Protein, Creatinine, and Protein/Creatinine Ratio",
        tfl_type=T, section=S143, sort_key=25,
        population="Safety Population",
        placeholder_columns=["Parameter\n(Unit)", "Visit", "Statistic",
                             "G1\n(N=XX)", "G2\n(N=XX)", "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "Urine Protein (g/24h)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Week 12 — Mean Chg (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "UPCR (mg/mmol)", "bold": True},
            {"label": "  Baseline — Geo Mean (CV%)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Week 12 — Geo Mean (CV%)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "Microalbumin (mg/L)", "bold": True},
            {"label": "  Baseline — Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["UPCR = Urine Protein/Creatinine Ratio. Listing: L16.2.25."],
        dataset_source="ADSL, ADLB", program_ref="t_urine_chem.sas",
    ))

    items.append(TFLItem(
        id="F14.3.3.4", title="Renal Safety Panel — eGFR Trajectory Over Time by Treatment Arm",
        tfl_type=F, section=S143, sort_key=26,
        population="Safety Population",
        figure_description="Line plot: mean (+/-SD) eGFR (CKD-EPI) over visits, individual subject spaghetti lines in background, treatment arms in different colors.",
        dataset_source="ADSL, ADLB", program_ref="f_egfr_traj.sas",
        figure_type="longitudinal", figure_width_inches=5.5, figure_height_inches=3.5,
    ))

    items.append(TFLItem(
        id="F14.3.3.5", title="Laboratory Toxicity Heatmap — CTCAE Grade by Parameter and Subject",
        tfl_type=F, section=S143, sort_key=27,
        population="Safety Population",
        figure_description="Heatmap: subjects (rows) vs. lab parameters (columns), color = worst CTCAE grade. Sidebar: treatment arm. Parameters: Hgb, Plt, Neut, ALT, AST, TBL, Cr.",
        dataset_source="ADSL, ADLB", program_ref="f_lab_heatmap.sas",
        figure_type="box_plot", figure_width_inches=6.5, figure_height_inches=4,
    ))


    # --- 14.3.4 VS/ECG/PE Expansion (CDISC ADVS, ADEG, ADPE) ---
    items.append(TFLItem(
        id="T14.3.4.9", title="Pulse Oximetry (SpO2) — Change from Baseline by Visit",
        tfl_type=T, section=S143, sort_key=9,
        population="Safety Population",
        placeholder_columns=["Visit", "Statistic",
                             "G1\n(N=XX)", "G2\n(N=XX)", "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "Baseline", "bold": True},
            {"label": "  n", "indent": True, "values": ["xx", "xx", "...", "xx"]},
            {"label": "  Mean (SD), %", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "Week 4 — Mean Chg (SD)", "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "End of Treatment — Mean Chg (SD)", "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "SpO2 <92%, n (%)", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
        ],
        dataset_source="ADSL, ADVS", program_ref="t_spo2_chg.sas",
    ))

    items.append(TFLItem(
        id="T14.3.4.10", title="Respiratory Rate — Change from Baseline by Visit",
        tfl_type=T, section=S143, sort_key=10,
        population="Safety Population",
        placeholder_columns=["Visit", "Statistic",
                             "G1\n(N=XX)", "G2\n(N=XX)", "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "Baseline — Mean (SD), breaths/min", "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "Week 4 — Mean Chg (SD)", "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "End of Treatment — Mean Chg (SD)", "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "RR >20 breaths/min, n (%)", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        dataset_source="ADSL, ADVS", program_ref="t_rr_chg.sas",
    ))

    items.append(TFLItem(
        id="T14.3.4.11", title="Body Temperature — Change from Baseline and Fever Incidence",
        tfl_type=T, section=S143, sort_key=11,
        population="Safety Population",
        placeholder_columns=["Visit / Criterion", "Statistic",
                             "G1\n(N=XX)", "G2\n(N=XX)", "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "Baseline — Mean (SD), deg C", "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "End of Treatment — Mean Chg (SD)", "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "Fever (>=38.0 deg C) at Any Visit, n (%)", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Grade 1 (38.0-39.0 deg C)", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Grade >=2 (>39.0 deg C)", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["Temperature measurement method per site SOP. CTCAE [xx]."],
        dataset_source="ADSL, ADVS", program_ref="t_temp_chg.sas",
    ))

    items.append(TFLItem(
        id="T14.3.4.12", title="Vital Signs — Categorical Outlier Summary (All Visits Pooled)",
        tfl_type=T, section=S143, sort_key=12,
        population="Safety Population",
        placeholder_columns=["Parameter\nCriterion",
                             "G1\nn/N (%)", "G2\nn/N (%)", "...", "Overall\nn/N (%)"],
        shell_rows=[
            {"label": "SBP >=160 mmHg", "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "SBP <=90 mmHg (with >=20 mmHg decrease)", "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "DBP >=100 mmHg", "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "DBP <=50 mmHg (with >=15 mmHg decrease)", "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "HR >=120 bpm", "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "HR <=45 bpm", "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "SpO2 <92%", "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "RR >24 breaths/min", "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["N = subjects with >=1 post-baseline assessment for each parameter."],
        dataset_source="ADSL, ADVS", program_ref="t_vs_outlier.sas",
    ))

    items.append(TFLItem(
        id="T14.3.4.13", title="Holter Monitoring Summary — Heart Rate and Arrhythmia Events (Phase 1)",
        tfl_type=T, section=S143, sort_key=13,
        population="Safety Population (Subset with Holter Data)",
        placeholder_columns=["Parameter", "Statistic",
                             "G1\n(N=XX)", "G2\n(N=XX)", "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "HR — Mean (SD), bpm", "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "HR — Minimum, bpm", "values": ["xx", "xx", "...", "xx"]},
            {"label": "HR — Maximum, bpm", "values": ["xx", "xx", "...", "xx"]},
            {"label": "Ventricular Ectopics — Total per 24h, Median (Range)", "values": ["xx (x-xx)", "xx (x-xx)", "...", "xx (x-xx)"]},
            {"label": "Supraventricular Ectopics — Total per 24h, Median (Range)", "values": ["xx (x-xx)", "xx (x-xx)", "...", "xx (x-xx)"]},
            {"label": "Ventricular Tachycardia (>=3 beats), n (%)", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
        ],
        footnotes=["24-hour Holter monitoring at Baseline and post-dose timepoints (Phase 1 only)."],
        dataset_source="ADSL, ADEG", program_ref="t_holter.sas",
    ))

    items.append(TFLItem(
        id="T14.3.4.14", title="ECG — T-Wave and ST-Segment Morphology Findings by Visit",
        tfl_type=T, section=S143, sort_key=14,
        population="Safety Population with ECG Data",
        placeholder_columns=["Visit\nFinding", "G1\nn/N (%)", "G2\nn/N (%)", "...", "Overall\nn/N (%)"],
        shell_rows=[
            {"label": "Baseline", "bold": True},
            {"label": "  Normal", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "  T-wave abnormality", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "  ST-segment abnormality", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "Worst Post-Baseline", "bold": True},
            {"label": "  Normal", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "  New T-wave abnormality", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "  New ST-segment abnormality", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["Morphology findings per central cardiologist over-read. N = subjects with ECG at that timepoint."],
        dataset_source="ADSL, ADEG", program_ref="t_ecg_morph.sas",
    ))

    items.append(TFLItem(
        id="T14.3.4.15", title="Physical Examination — Abnormal Findings by Body System at Baseline and EOT",
        tfl_type=T, section=S143, sort_key=15,
        population="Safety Population",
        placeholder_columns=["Body System\nFinding",
                             "Baseline\nn (%)", "End of Treatment\nn (%)"],
        shell_rows=[
            {"label": "General Appearance", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)"]},
            {"label": "Head/Eyes/Ears/Nose/Throat", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)"]},
            {"label": "Cardiovascular", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)"]},
            {"label": "Respiratory", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)"]},
            {"label": "Abdomen", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)"]},
            {"label": "Musculoskeletal", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)"]},
            {"label": "Neurological", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)"]},
            {"label": "Dermatological", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)"]},
            {"label": "Lymph Nodes", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "..."]},
        ],
        footnotes=["Physical examination per protocol schedule. Listing: L16.2.24."],
        dataset_source="ADSL, ADPE", program_ref="t_pe_findings.sas",
    ))

    items.append(TFLItem(
        id="T14.3.4.16", title="Physical Examination — New or Worsened Findings from Baseline by Body System",
        tfl_type=T, section=S143, sort_key=16,
        population="Safety Population",
        placeholder_columns=["Body System", "G1\nn/N (%)", "G2\nn/N (%)", "...", "Overall\nn/N (%)"],
        shell_rows=[
            {"label": "Any New or Worsened Finding", "bold": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "Cardiovascular", "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "Respiratory", "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "Abdomen", "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "Neurological", "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "Dermatological", "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["New = not present at Baseline. Worsened = increased severity from Baseline. N = subjects with both BL and >=1 post-BL exam."],
        dataset_source="ADSL, ADPE", program_ref="t_pe_new_worse.sas",
    ))

    items.append(TFLItem(
        id="F14.3.4.2", title="QTcF vs. Plasma Drug Concentration Scatter Plot with LOESS Fit",
        tfl_type=F, section=S143, sort_key=17,
        population="Safety Population with Time-Matched PK and ECG",
        figure_description="Scatter: placebo-adjusted change from baseline QTcF vs. plasma concentration, LOESS fit with 90% CI band, ICH E14 reference line at 10 ms.",
        dataset_source="ADSL, ADEG, ADPC", program_ref="f_qtcf_conc.sas",
        figure_type="longitudinal", figure_width_inches=5.5, figure_height_inches=3.5,
    ))

    # 14.4 SPECIAL ASSESSMENTS — Tables + Figures ONLY (no listings)
    # =====================================================================

    items.append(TFLItem(
        id="T14.4.1", title="Summary of Pharmacokinetic Concentrations by Timepoint",
        tfl_type=T, section=S144, sort_key=1,
        population="PK Population",
        placeholder_columns=["Timepoint\n(h)", "Statistic",
                             "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)",
                             "...\n...\nOverall\n(N=XX)"],
        shell_rows=[
            ["Pre-dose (0h)", "Mean (SD), ng/mL", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            ["Cmax (Tmax)", "Mean (SD), ng/mL", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            ["Cmin (24h)", "Mean (SD), ng/mL", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            EROW,
        ],
        dataset_source="ADSL, ADPC", program_ref="t_pk_conc.sas",
    ))

    items.append(TFLItem(
        id="T14.4.2", title="Summary of Pharmacokinetic Parameters",
        tfl_type=T, section=S144, sort_key=2,
        population="PK Population",
        placeholder_columns=["PK Parameter", "Statistic",
                             "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)",
                             "...\n...\nOverall\n(N=XX)"],
        shell_rows=[
            ["Cmax (ng/mL)", "Geo Mean (CV%)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            ["AUC0-tau (ng·h/mL)", "Geo Mean (CV%)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            ["AUC0-inf (ng·h/mL)", "Geo Mean (CV%)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            ["Tmax (h)", "Median (Range)", "x.x (x.x-x.x)", "x.x (x.x-x.x)", "...", "x.x (x.x-x.x)"],
            ["t1/2 (h)", "Mean (SD)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            EROW,
        ],
        dataset_source="ADSL, ADPP", program_ref="t_pk_params.sas",
    ))

    items.append(TFLItem(
        id="T14.4.3", title="Summary of Anti-Drug Antibody (ADA) Incidence",
        tfl_type=T, section=S144, sort_key=3,
        population="Safety Population with ADA Samples",
        placeholder_columns=["ADA Parameter",
                             "XXX Group 1\n(N=XX) n (%)", "XXX Group 2\n(N=XX) n (%)",
                             "...\n...\nOverall\n(N=XX) n (%)"],
        shell_rows=[
            ["ADA Evaluable", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["ADA Positive at Baseline", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["ADA Positive Post-Baseline", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Treatment-Emergent ADA Positive", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Neutralizing Antibody (Nab) Positive", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            EROW,
        ],
        dataset_source="ADSL, ADIS", program_ref="t_ada_incidence.sas",
    ))

    items.append(TFLItem(
        id="T14.4.4", title="Summary of Biomarker Results by Visit",
        tfl_type=T, section=S144, sort_key=4,
        population="ITT Population with Biomarker Data",
        placeholder_columns=["Biomarker", "Visit", "Statistic",
                             "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)",
                             "...\n...\nOverall\n(N=XX)"],
        shell_rows=[
            ["ctDNA (ng/mL)", "Baseline", "Geo Mean (CV%)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            ["ctDNA (ng/mL)", "Cycle 3", "Geo Mean (CV%)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            ["ctDNA (ng/mL)", "EOT", "Geo Mean (CV%)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            EROW,
        ],
        dataset_source="ADSL, ADBM", program_ref="t_biomarker_visit.sas",
    ))

    items.append(TFLItem(
        id="T14.4.5", title="Summary of Patient-Reported Outcomes by Visit",
        tfl_type=T, section=S144, sort_key=5,
        population="ITT Population with PRO Data",
        placeholder_columns=["PRO Scale", "Visit", "Statistic",
                             "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)",
                             "...\n...\nOverall\n(N=XX)"],
        shell_rows=[
            ["EORTC QLQ-C30 GHS", "Baseline", "Mean (SD)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            ["EORTC QLQ-C30 GHS", "Week 12", "Mean (SD)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            ["EORTC QLQ-C30 GHS", "Change from BL", "LS Mean (SE)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            EROW,
        ],
        dataset_source="ADSL, ADPRO", program_ref="t_pro_summary.sas",
    ))

    items.append(TFLItem(
        id="T14.4.6", title="Summary of Pharmacodynamics — Soluble Biomarkers by Visit",
        tfl_type=T, section=S144, sort_key=6,
        population="PD Population",
        placeholder_columns=["Biomarker", "Visit", "Statistic",
                             "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)",
                             "...\n...\nOverall\n(N=XX)"],
        shell_rows=[
            ["Soluble EGFR (pg/mL)", "Baseline", "Geo Mean (CV%)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            ["Soluble EGFR (pg/mL)", "Week 4", "Geo Mean (CV%)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            ["Soluble cMet (ng/mL)", "Baseline", "Geo Mean (CV%)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            EROW,
        ],
        dataset_source="ADSL, ADPD", program_ref="t_pd_summary.sas",
    ))

    items.append(TFLItem(
        id="T14.4.7", title="Summary of Central Molecular Test Results and Gene Aberrations at Baseline",
        tfl_type=T, section=S144, sort_key=7,
        oncology_only=True,
        population="Full Analysis Set",
        placeholder_columns=["Gene", "Alteration Type",
                             "XXX Group 1\n(N=XX) n (%)", "XXX Group 2\n(N=XX) n (%)",
                             "...\n...\nOverall\n(N=XX) n (%)"],
        shell_rows=[
            ["Gene X", "Mutation", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Gene X", "Amplification", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Gene Y", "Mutation", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            EROW,
        ],
        dataset_source="ADSL, ADBM", program_ref="t_gene_aberrations.sas",
    ))

    # 14.4 Figures
    items.append(TFLItem(
        id="F14.4.1", title="Pharmacokinetic (PK) Plot — Mean Serum Concentration-Time Profiles",
        tfl_type=F, section=S144, sort_key=8,
        population="PK Population",
        figure_description="PK plot: Mean (±SD) serum concentration vs. time, linear/log scales.",
        dataset_source="ADSL, ADPC", program_ref="f_pk_profile.sas",
        figure_type="longitudinal", figure_width_inches=6, figure_height_inches=4,
    ))

    items.append(TFLItem(
        id="F14.4.2", title="Overlaying Individual PK Concentration Profiles",
        tfl_type=F, section=S144, sort_key=9,
        population="PK Population",
        figure_description="PK overlay: individual concentration-time profiles by treatment group.",
        dataset_source="ADSL, ADPC", program_ref="f_pk_overlay.sas",
        figure_type="spider", figure_width_inches=6, figure_height_inches=4,
    ))

    items.append(TFLItem(
        id="F14.4.3", title="Mean (SD) Soluble EGFR and cMet Over Time",
        tfl_type=F, section=S144, sort_key=10,
        population="PD Population",
        figure_description="PD plot: Mean (±SD) soluble EGFR/cMet concentrations over time.",
        dataset_source="ADSL, ADPD", program_ref="f_pd_time.sas",
        figure_type="longitudinal", figure_width_inches=6, figure_height_inches=4,
    ))

    items.append(TFLItem(
        id="F14.4.4", title="Boxplot of Biomarkers at Baseline vs. Response Status",
        tfl_type=F, section=S144, sort_key=11,
        oncology_only=True,
        population="Full Analysis Set with Biomarker Data",
        figure_description="Box plot: Biomarker levels at baseline by response status (CR/PR/SD/PD).",
        dataset_source="ADSL, ADBM", program_ref="f_biomarker_box.sas",
        figure_type="box_plot", figure_width_inches=6, figure_height_inches=4,
    ))

    # =====================================================================

    # --- 14.4 Expansion (CDISC ADIS, ADBM, ADPC) ---
    items.append(TFLItem(
        id="T14.4.8", title="ADA Titer Distribution by Visit — Negative, Low, Medium, High",
        tfl_type=T, section=S144, sort_key=8,
        population="Safety Population with ADA Samples",
        placeholder_columns=["Visit\nADA Titer Category",
                             "G1\nn/N (%)", "G2\nn/N (%)", "...", "Overall\nn/N (%)"],
        shell_rows=[
            {"label": "Baseline", "bold": True},
            {"label": "  ADA Negative", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "  Low Titer (1:<xxx)", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "  Medium Titer", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "  High Titer (>=1:xxxx)", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "Post-Baseline (Any)", "bold": True},
            {"label": "  ADA Negative", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "  Low Titer", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "  Medium Titer", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "  High Titer", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "  Treatment-Emergent ADA Positive", "bold": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["ADA assessed by validated bridging immunoassay. Titer categories defined per assay validation report. Listing: L16.2.16."],
        dataset_source="ADSL, ADIS", program_ref="t_ada_titer.sas",
    ))

    items.append(TFLItem(
        id="T14.4.9", title="ADA Impact on Pharmacokinetics — Cmax and AUC in ADA+ vs. ADA- Subjects",
        tfl_type=T, section=S144, sort_key=9,
        population="PK Population with ADA Data",
        placeholder_columns=["PK Parameter\nADA Status", "Statistic",
                             "ADA Positive\n(N=XX)", "ADA Negative\n(N=XX)",
                             "Ratio\n(ADA+/ADA-)"],
        shell_rows=[
            {"label": "Cmax (ng/mL)", "bold": True},
            {"label": "  ADA Positive — Geo Mean (CV%)", "indent": True, "values": ["xx.x (xx.x)", "", ""]},
            {"label": "  ADA Negative — Geo Mean (CV%)", "indent": True, "values": ["", "xx.x (xx.x)", ""]},
            {"label": "  Geometric Mean Ratio (90% CI)", "indent": True, "values": ["", "", "x.xx (x.xx, x.xx)"]},
            {"label": "AUC0-tau (ng*h/mL)", "bold": True},
            {"label": "  ADA Positive — Geo Mean (CV%)", "indent": True, "values": ["xx.x (xx.x)", "", ""]},
            {"label": "  ADA Negative — Geo Mean (CV%)", "indent": True, "values": ["", "xx.x (xx.x)", ""]},
            {"label": "  Geometric Mean Ratio (90% CI)", "indent": True, "values": ["", "", "x.xx (x.xx, x.xx)"]},
        ],
        footnotes=["ADA+ = treatment-emergent ADA positive. ADA- = ADA negative throughout. GMR = geometric mean ratio."],
        dataset_source="ADSL, ADIS, ADPP", program_ref="t_ada_pk_impact.sas",
    ))

    items.append(TFLItem(
        id="T14.4.10", title="Neutralizing Antibody (Nab) — Incidence, Titer, and Cross-Reactivity Status",
        tfl_type=T, section=S144, sort_key=10,
        population="Safety Population with ADA Samples",
        placeholder_columns=["Nab Parameter",
                             "G1\nn/N1 (%)", "G2\nn/N2 (%)", "...", "Overall\nn/N (%)"],
        shell_rows=[
            {"label": "Nab Evaluable Subjects", "bold": True, "values": ["xx", "xx", "...", "xx"]},
            {"label": "Nab Positive, n (%)", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Among ADA Positive Subjects", "indent": True, "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"]},
            {"label": "Nab Titer Distribution", "bold": True},
            {"label": "  Low (<1:xx)", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Medium (1:xx-1:xxx)", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  High (>=1:xxxx)", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Cross-Reactivity to Endogenous Protein", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["Nab = neutralizing antibody. N1/N2 = number of ADA-evaluable subjects. Cross-reactivity assessed by competitive ligand-binding assay."],
        dataset_source="ADSL, ADIS", program_ref="t_nab_detail.sas",
    ))

    items.append(TFLItem(
        id="T14.4.11", title="Soluble Pharmacodynamic Biomarker Change from Baseline Over Time",
        tfl_type=T, section=S144, sort_key=11,
        population="PD Population",
        placeholder_columns=["Biomarker\nVisit", "Statistic",
                             "G1\n(N=XX)", "G2\n(N=XX)", "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "Soluble Target X (ng/mL)", "bold": True},
            {"label": "  Baseline — Geo Mean (CV%)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Cycle 1 Day 8 — Fold Chg from BL", "indent": True, "values": ["x.xx", "x.xx", "...", "x.xx"]},
            {"label": "  Cycle 2 Day 1 — Fold Chg from BL", "indent": True, "values": ["x.xx", "x.xx", "...", "x.xx"]},
            {"label": "  End of Treatment — Fold Chg from BL", "indent": True, "values": ["x.xx", "x.xx", "...", "x.xx"]},
            {"label": "Soluble Biomarker Y (pg/mL)", "bold": True},
            {"label": "  Baseline — Geo Mean (CV%)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  Cycle 2 Day 1 — Fold Chg from BL", "indent": True, "values": ["x.xx", "x.xx", "...", "x.xx"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["PD biomarkers assessed by validated assays. Fold change = post-baseline / baseline."],
        dataset_source="ADSL, ADBM", program_ref="t_pd_bio_chg.sas",
    ))

    items.append(TFLItem(
        id="T14.4.12", title="Trough PK Concentration (Ctrough) by Cycle — Target Attainment",
        tfl_type=T, section=S144, sort_key=12,
        population="PK Population",
        placeholder_columns=["Cycle\nDay", "Statistic",
                             "G1\n(N=XX)", "G2\n(N=XX)", "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "Cycle 1 Day 15 — Mean (SD), ng/mL", "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "Cycle 2 Day 1 — Mean (SD), ng/mL", "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "Cycle 3 Day 1 — Mean (SD), ng/mL", "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "Cycle 4 Day 1 — Mean (SD), ng/mL", "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "Cycle 6 Day 1 — Mean (SD), ng/mL", "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "Ctrough Above Target Threshold, n (%)", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["Ctrough = pre-dose concentration. Target threshold per PK/PD modeling. Listing: L16.2.14."],
        dataset_source="ADSL, ADPC", program_ref="t_ctrough.sas",
    ))

    items.append(TFLItem(
        id="T14.4.13", title="Steady-State Attainment — Trough Concentrations Across Dosing Cycles (ANOVA)",
        tfl_type=T, section=S144, sort_key=13,
        population="PK Population",
        placeholder_columns=["Cycle Comparison",
                             "GMR (90% CI)", "CV%",
                             "Conclusion"],
        shell_rows=[
            {"label": "Cycle 2 vs. Cycle 1 Ctrough", "values": ["x.xx (x.xx, x.xx)", "xx.x", "Steady state / Not yet"]},
            {"label": "Cycle 3 vs. Cycle 2 Ctrough", "values": ["x.xx (x.xx, x.xx)", "xx.x", "Steady state / Not yet"]},
            {"label": "Cycle 4 vs. Cycle 3 Ctrough", "values": ["x.xx (x.xx, x.xx)", "xx.x", "Steady state achieved"]},
            {"label": "Cycle 6 vs. Cycle 4 Ctrough", "values": ["x.xx (x.xx, x.xx)", "xx.x", "Steady state maintained"]},
        ],
        footnotes=["Steady state = no statistically significant increase between consecutive cycles (ANOVA on log-transformed Ctrough, 90% CI of GMR within 0.80-1.25)."],
        dataset_source="ADSL, ADPC", program_ref="t_steady_state.sas",
    ))

    items.append(TFLItem(
        id="T14.4.14", title="Urine Pharmacokinetic Parameters — Renal Excretion and Cumulative Recovery",
        tfl_type=T, section=S144, sort_key=14,
        population="PK Population (Subset with Urine PK)",
        placeholder_columns=["PK Parameter\n(Unit)", "Statistic",
                             "G1\n(N=XX)", "G2\n(N=XX)", "...", "Overall\n(N=XX)"],
        shell_rows=[
            {"label": "Ae (Amount Excreted Unchanged, mg)", "bold": True},
            {"label": "  Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "  % of Dose, Mean (SD)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "Renal Clearance (CLr, L/h)", "bold": True},
            {"label": "  Geo Mean (CV%)", "indent": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "Cumulative Urinary Recovery (% Dose, 0-24h)", "bold": True, "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
        ],
        footnotes=["Urine PK collected over 0-4h, 4-8h, 8-12h, 12-24h intervals post-dose. Ae = cumulative amount excreted unchanged."],
        dataset_source="ADSL, ADPP", program_ref="t_urine_pk.sas",
    ))

    # 16.2 PATIENT DATA LISTINGS (21 items — including PK/ADA/Biomarker from 14.4)
    # =====================================================================

    items.append(TFLItem(
        id="L16.2.1", title="Listing of Subject Disposition",
        tfl_type=L, section=S162, sort_key=1,
        population="All Screened Subjects",
        placeholder_columns=["Site", "Subject", "Group",
                             "Date Screened", "Date Randomized",
                             "Date of First Dose", "Date of Last Dose",
                             "Completed Treatment?", "Reason for Discontinuation"],
        shell_rows=[
            ["xxx", "xxxx/xxx", "Gx", "DDMMMYYYY", "DDMMMYYYY",
             "DDMMMYYYY", "DDMMMYYYY", "Yes/No", "Reason / xxxxxxx"],
            ["[...]", "...", "...", "...", "...", "...", "...", "...", "..."],
        ],
        footnotes=["Sorted by site, subject ID. Refer to EOT/Study Completion CRF pages."],
        dataset_source="ADSL", program_ref="l_disposition.sas",
    ))

    items.append(TFLItem(
        id="L16.2.2", title="Listing of Demographic Data",
        tfl_type=L, section=S162, sort_key=2,
        population="All Randomized Subjects",
        placeholder_columns=["Site", "Subject", "Group", "Age (yrs)", "Sex",
                             "Race", "Height (cm)", "Weight (kg)", "BMI (kg/m²)"],
        shell_rows=[
            ["xxx", "xxxx/xxx", "Gx", "xx", "M/F", "Race", "xxx", "xx.x", "xx.x"],
            ["[...]", "...", "...", "...", "...", "...", "...", "...", "..."],
        ],
        dataset_source="ADSL", program_ref="l_demog.sas",
    ))

    items.append(TFLItem(
        id="L16.2.3", title="Listing of Protocol Deviations",
        tfl_type=L, section=S162, sort_key=3,
        population="All Enrolled Subjects",
        placeholder_columns=["Site", "Subject", "Group", "Deviation Category",
                             "Deviation Description", "Date of Deviation", "Major/Minor"],
        shell_rows=[
            ["xxx", "xxxx/xxx", "Gx", "Category", "Description text xxxxxxx", "DDMMMYYYY", "Major/Minor"],
            ["[...]", "...", "...", "...", "...", "...", "..."],
        ],
        dataset_source="ADSL, DV", program_ref="l_protdev.sas",
    ))

    items.append(TFLItem(
        id="L16.2.4", title="Listing of Adverse Events",
        tfl_type=L, section=S162, sort_key=4,
        population="Safety Population",
        placeholder_columns=["Site", "Subject", "Group", "SOC", "Preferred Term",
                             "Verbatim Term", "Start Date", "End Date",
                             "CTCAE Grade", "Relationship", "SAE?", "Action", "Outcome"],
        shell_rows=[
            ["xxx", "xxxx/xxx", "Gx", "GI disorders", "Nausea",
             "Nausea (Verbatim)", "DDMMMYYYY", "DDMMMYYYY",
             "x", "R/NR", "Y/N", "N/DR/DI/DW", "Recovered/Ongoing"],
            ["[...]", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "..."],
        ],
        footnotes=["R=Related, NR=Not Related. N=None, DR=Dose Reduced, DI=Interrupted, DW=Withdrawn."],
        dataset_source="ADSL, ADAE", program_ref="l_ae.sas",
        dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="L16.2.5", title="Listing of Serious Adverse Events",
        tfl_type=L, section=S162, sort_key=5,
        population="Safety Population",
        placeholder_columns=["Site", "Subject", "Group", "Preferred Term",
                             "SAE Criteria", "Start Date", "End Date",
                             "CTCAE Grade", "Relationship", "Outcome", "Narrative ID"],
        shell_rows=[
            ["xxx", "xxxx/xxx", "Gx", "Pneumonia", "D/L/H/P/C/O", "DDMMMYYYY", "DDMMMYYYY",
             "x", "R/NR", "Recovered/Fatal", "NAR-xxxx"],
            ["[...]", "...", "...", "...", "...", "...", "...", "...", "...", "...", "..."],
        ],
        dataset_source="ADSL, ADAE", program_ref="l_sae.sas",
        dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="L16.2.6", title="Listing of Concomitant Medications",
        tfl_type=L, section=S162, sort_key=6,
        population="Safety Population",
        placeholder_columns=["Site", "Subject", "Group", "ATC Class",
                             "Preferred Name", "Indication",
                             "Dose / Route / Frequency", "Start Date", "End Date"],
        shell_rows=[
            ["xxx", "xxxx/xxx", "Gx", "A02BC", "Omeprazole", "GERD",
             "20 mg / PO / QD", "DDMMMYYYY", "DDMMMYYYY"],
            ["[...]", "...", "...", "...", "...", "...", "...", "...", "..."],
        ],
        dataset_source="ADSL, ADCM", program_ref="l_conmed.sas",
        dictionary_versions={"WHO-DD": "[version]"},
    ))

    items.append(TFLItem(
        id="L16.2.7", title="Listing of Laboratory Data — Hematology and Chemistry",
        tfl_type=L, section=S162, sort_key=7,
        population="Safety Population",
        placeholder_columns=["Site", "Subject", "Group", "Visit", "Parameter",
                             "Result", "Unit", "Normal Range", "Flag"],
        shell_rows=[
            ["xxx", "xxxx/xxx", "Gx", "Screening/Wk xx", "Hemoglobin",
             "xx.x", "g/dL", "xx.x-xx.x", "L/N/H"],
            ["[...]", "...", "...", "...", "...", "...", "...", "...", "..."],
        ],
        dataset_source="ADSL, ADLB", program_ref="l_lab.sas",
    ))

    items.append(TFLItem(
        id="L16.2.8", title="Listing of Vital Signs",
        tfl_type=L, section=S162, sort_key=8,
        population="Safety Population",
        placeholder_columns=["Site", "Subject", "Group", "Visit", "Date",
                             "SBP\n(mmHg)", "DBP\n(mmHg)", "HR\n(bpm)",
                             "Resp Rate", "Temp (°C)", "Weight (kg)"],
        shell_rows=[
            ["xxx", "xxxx/xxx", "Gx", "Screening", "DDMMMYYYY",
             "xxx", "xx", "xx", "xx", "xx.x", "xx.x"],
            ["[...]", "...", "...", "...", "...", "...", "...", "...", "...", "...", "..."],
        ],
        dataset_source="ADSL, ADVS", program_ref="l_vitalsigns.sas",
    ))

    items.append(TFLItem(
        id="L16.2.9", title="Listing of ECG Data",
        tfl_type=L, section=S162, sort_key=9,
        population="Safety Population with ECG Data",
        placeholder_columns=["Site", "Subject", "Group", "Visit", "Date/Time",
                             "HR\n(bpm)", "PR\n(ms)", "QRS\n(ms)",
                             "QT\n(ms)", "QTcF\n(ms)", "Interpretation"],
        shell_rows=[
            ["xxx", "xxxx/xxx", "Gx", "Screening", "DDMMMYYYY HH:MM",
             "xx", "xxx", "xx", "xxx", "xxx", "Normal/Abnormal NCS/Abnormal CS"],
            ["[...]", "...", "...", "...", "...", "...", "...", "...", "...", "...", "..."],
        ],
        dataset_source="ADSL, ADEG", program_ref="l_ecg.sas",
    ))

    items.append(TFLItem(
        id="L16.2.10", title="Listing of Tumor Response Data",
        tfl_type=L, section=S162, sort_key=10, oncology_only=True,
        population="ITT Population",
        placeholder_columns=["Site", "Subject", "Group", "Visit", "Assessment Date",
                             "Target Lesion Sum\n(mm)", "% Change\nfrom BL",
                             "Non-Target Status", "New Lesions?", "Overall Response", "BOR"],
        shell_rows=[
            ["xxx", "xxxx/xxx", "Gx", "Screening/Wk xx", "DDMMMYYYY",
             "xxx.x", "—/xx.x", "Present/Absent", "Y/N", "CR/PR/SD/PD/NE", "CR/PR/SD/PD/NE"],
            ["[...]", "...", "...", "...", "...", "...", "...", "...", "...", "...", "..."],
        ],
        dataset_source="ADSL, ADRS", program_ref="l_tumor_response.sas",
    ))

    items.append(TFLItem(
        id="L16.2.11", title="Listing of Survival Data",
        tfl_type=L, section=S162, sort_key=11, oncology_only=True,
        population="ITT Population",
        placeholder_columns=["Site", "Subject", "Group",
                             "Date of Last Contact", "Vital Status",
                             "Date of Death", "Primary Cause of Death",
                             "PFS Event Date", "PFS Censor", "OS Censor"],
        shell_rows=[
            ["xxx", "xxxx/xxx", "Gx", "DDMMMYYYY", "Alive/Dead/LTFU",
             "DDMMMYYYY", "xxxxxxx", "DDMMMYYYY", "Y/N", "Y/N"],
            ["[...]", "...", "...", "...", "...", "...", "...", "...", "...", "..."],
        ],
        dataset_source="ADSL, ADTTE", program_ref="l_survival.sas",
    ))

    items.append(TFLItem(
        id="L16.2.12", title="Listing of Study Drug Exposure and Dose Modifications",
        tfl_type=L, section=S162, sort_key=12,
        population="Safety Population",
        placeholder_columns=["Site", "Subject", "Group", "Cycle/Day",
                             "Planned Dose", "Actual Dose", "Modification Reason"],
        shell_rows=[
            ["xxx", "xxxx/xxx", "Gx", "CxDx", "xxx mg", "xxx mg", "Reason / None"],
            ["[...]", "...", "...", "...", "...", "...", "..."],
        ],
        dataset_source="ADSL, ADEX", program_ref="l_exposure.sas",
    ))

    items.append(TFLItem(
        id="L16.2.13", title="Listing of Medical History Verbatim vs. Coded Terms",
        tfl_type=L, section=S162, sort_key=13,
        population="Safety Population",
        placeholder_columns=["Site", "Subject", "Group", "SOC", "Preferred Term",
                             "Verbatim Term", "Start Date/Year", "End Date/Year", "Ongoing?"],
        shell_rows=[
            ["xxx", "xxxx/xxx", "Gx", "Vascular disorders", "Hypertension",
             "High Blood Pressure", "YYYY/DDMMMYYYY", "YYYY/DDMMMYYYY", "Y/N"],
            ["[...]", "...", "...", "...", "...", "...", "...", "...", "..."],
        ],
        dataset_source="ADSL, ADMH", program_ref="l_mh_coded.sas",
        dictionary_versions={"MedDRA": "[xx.x]"},
    ))

    items.append(TFLItem(
        id="L16.2.14", title="Listing of PK Concentrations by Subject and Timepoint",
        tfl_type=L, section=S162, sort_key=14,
        population="PK Population",
        placeholder_columns=["Site", "Subject", "Group", "Cycle/Day",
                             "Nominal Time\n(h)", "Actual Time\n(h)",
                             "Concentration\n(ng/mL)", "BQL"],
        shell_rows=[
            ["xxx", "xxxx/xxx", "Gx", "C1D1", "0", "0.00", "xx.x", "Y/N"],
            ["xxx", "xxxx/xxx", "Gx", "C1D1", "2", "2.05", "xx.x", "Y/N"],
            ["[...]", "...", "...", "...", "...", "...", "...", "..."],
        ],
        footnotes=["BQL = Below Quantification Limit (<xx.x ng/mL)."],
        dataset_source="ADSL, ADPC", program_ref="l_pk_conc.sas",
    ))

    items.append(TFLItem(
        id="L16.2.15", title="Listing of PK Parameters by Subject",
        tfl_type=L, section=S162, sort_key=15,
        population="PK Population",
        placeholder_columns=["Site", "Subject", "Group", "Cycle",
                             "Cmax\n(ng/mL)", "AUC0-tau\n(ng·h/mL)",
                             "Tmax\n(h)", "t1/2\n(h)", "CL/F\n(L/h)"],
        shell_rows=[
            ["xxx", "xxxx/xxx", "Gx", "C1", "xx.x", "xxx.x", "x.x", "xx.x", "xx.x"],
            ["[...]", "...", "...", "...", "...", "...", "...", "...", "..."],
        ],
        dataset_source="ADSL, ADPP", program_ref="l_pk_params.sas",
    ))

    items.append(TFLItem(
        id="L16.2.16", title="Listing of ADA and Neutralizing Antibody Results",
        tfl_type=L, section=S162, sort_key=16,
        population="Safety Population with ADA Samples",
        placeholder_columns=["Site", "Subject", "Group", "Visit (Day)",
                             "ADA Result", "ADA Titer", "Nab Result"],
        shell_rows=[
            ["xxx", "xxxx/xxx", "Gx", "Screening (Dxx)", "Neg/Pos", "<LLOQ/1:xxx", "Neg/Pos"],
            ["xxx", "xxxx/xxx", "Gx", "C3D1 (Dxx)", "Neg/Pos", "<LLOQ/1:xxx", "Neg/Pos"],
            ["[...]", "...", "...", "...", "...", "...", "..."],
        ],
        dataset_source="ADSL, ADIS", program_ref="l_ada.sas",
    ))

    items.append(TFLItem(
        id="L16.2.17", title="Listing of Biomarker Results by Subject and Visit",
        tfl_type=L, section=S162, sort_key=17,
        population="ITT with Biomarker Data",
        placeholder_columns=["Site", "Subject", "Group", "Visit", "Biomarker",
                             "Result", "Unit", "Method"],
        shell_rows=[
            ["xxx", "xxxx/xxx", "Gx", "Screening", "ctDNA / PD-L1 / etc.",
             "xx.x", "ng/mL / % / etc.", "NGS / IHC / ddPCR"],
            ["[...]", "...", "...", "...", "...", "...", "...", "..."],
        ],
        dataset_source="ADSL, ADBM", program_ref="l_biomarker.sas",
    ))

    items.append(TFLItem(
        id="L16.2.18", title="Listing of PRO Assessments by Subject and Visit",
        tfl_type=L, section=S162, sort_key=18,
        population="ITT with PRO Data",
        placeholder_columns=["Site", "Subject", "Group", "Visit",
                             "GHS", "PF", "RF", "EF", "CF", "SF"],
        shell_rows=[
            ["xxx", "xxxx/xxx", "Gx", "Screening", "xx", "xx", "xx", "xx", "xx", "xx"],
            ["xxx", "xxxx/xxx", "Gx", "Wk 12", "xx", "xx", "xx", "xx", "xx", "xx"],
            ["[...]", "...", "...", "...", "...", "...", "...", "...", "...", "..."],
        ],
        dataset_source="ADSL, ADPRO", program_ref="l_pro.sas",
    ))

    items.append(TFLItem(
        id="L16.2.19", title="Listing of Subsequent Anti-Cancer Therapies",
        tfl_type=L, section=S162, sort_key=19, oncology_only=True,
        population="ITT Population",
        placeholder_columns=["Site", "Subject", "Group", "Therapy Name",
                             "Therapy Class", "Start Date", "End Date",
                             "Best Response to Subsequent Therapy"],
        shell_rows=[
            ["xxx", "xxxx/xxx", "Gx", "Drug Name", "Chemotherapy/Immunotherapy/Targeted",
             "DDMMMYYYY", "DDMMMYYYY/ongoing", "CR/PR/SD/PD/NE"],
            ["[...]", "...", "...", "...", "...", "...", "...", "..."],
        ],
        dataset_source="ADSL, ADCM", program_ref="l_subsequent_therapy.sas",
    ))

    items.append(TFLItem(
        id="L16.2.20", title="Listing of Deaths — All Subjects",
        tfl_type=L, section=S162, sort_key=20,
        population="All Randomized Subjects",
        placeholder_columns=["Site", "Subject", "Group",
                             "Date of Death", "Days from First Dose",
                             "Days from Last Dose", "Primary Cause of Death",
                             "AE-Related?", "Narrative ID"],
        shell_rows=[
            ["xxx", "xxxx/xxx", "Gx", "DDMMMYYYY", "xx", "xx",
             "xxxxxxx", "Y/N", "NAR-xxxx"],
            ["[...]", "...", "...", "...", "...", "...", "...", "...", "..."],
        ],
        dataset_source="ADSL, ADAE, ADTTE", program_ref="l_deaths.sas",
    ))

    items.append(TFLItem(
        id="L16.2.21", title="Listing of Prior and Subsequent Anti-Cancer Surgery/Radiotherapy",
        tfl_type=L, section=S162, sort_key=21, oncology_only=True,
        population="Full Analysis Set",
        placeholder_columns=["Site", "Subject", "Group", "Procedure",
                             "Target Location", "Intent", "Date"],
        shell_rows=[
            ["xxx", "xxxx/xxx", "Gx", "Surgery/Radiotherapy Name",
             "Location xxxxxxx", "Curative/Palliative/Adjuvant", "DDMMMYYYY"],
            ["[...]", "...", "...", "...", "...", "...", "..."],
        ],
        dataset_source="ADSL, ADCM", program_ref="l_prior_cancer_proc.sas",
    ))

    
    # --- 16.2 Listing Expansion (CDISC Source Data) ---
    items.append(TFLItem(
        id="L16.2.22", title="Listing of Adverse Events of Special Interest (AESI)",
        tfl_type=L, section=S162, sort_key=22,
        population="Safety Population",
        placeholder_columns=["Site", "Subject", "Group", "AESI Category", "Preferred Term",
                             "CTCAE Grade", "Start Date", "End Date",
                             "Outcome", "Serious?", "Relationship", "Narrative ID"],
        shell_rows=[
            ["xxx", "xxxx/xxx", "Gx", "Hepatotoxicity", "ALT Increased",
             "3", "DDMMMYYYY", "DDMMMYYYY", "Recovered", "N", "Related", "NAR-xxxx"],
            ["xxx", "xxxx/xxx", "Gx", "Infusion Reaction", "Anaphylaxis",
             "4", "DDMMMYYYY", "DDMMMYYYY", "Recovered/Resolved with Sequelae", "Y", "Related", "NAR-xxxx"],
            {"label": "[...]", "values": ["...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "..."]},
        ],
        footnotes=["AESI categories per protocol. MedDRA [xx.x]. CTCAE [xx]. Refer to Section 14.3.1 for AESI summary tables."],
        dataset_source="ADSL, ADAE", program_ref="l_aesi.sas",
        dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="L16.2.23", title="Listing of Subjects with Hy's Law Laboratory Criteria",
        tfl_type=L, section=S162, sort_key=23,
        population="Safety Population with Baseline and Post-Baseline Labs",
        placeholder_columns=["Site", "Subject", "Group", "Visit", "ALT (U/L)",
                             "ALT xULN", "AST (U/L)", "AST xULN",
                             "TBL (umol/L)", "TBL xULN", "ALP (U/L)",
                             "ALP xULN", "Hy's Law?", "Alternative Etiology"],
        shell_rows=[
            ["xxx", "xxxx/xxx", "Gx", "Wk 8", "xxx", "x.x", "xxx", "x.x",
             "xx.x", "x.x", "xxx", "x.x", "Yes", "xxxxxxx"],
            {"label": "[...]", "values": ["...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "..."]},
        ],
        footnotes=["Hy's Law: ALT/AST >=3xULN, TBL >=2xULN, ALP <2xULN, no alternative etiology. Refer to T14.3.2.2 and T14.3.2.4."],
        dataset_source="ADSL, ADLB", program_ref="l_hyslaw.sas",
    ))

    items.append(TFLItem(
        id="L16.2.24", title="Listing of Physical Examination Findings",
        tfl_type=L, section=S162, sort_key=24,
        population="Safety Population",
        placeholder_columns=["Site", "Subject", "Group", "Visit",
                             "Body System", "Finding",
                             "Baseline Status", "Current Status"],
        shell_rows=[
            ["xxx", "xxxx/xxx", "Gx", "Screening", "Cardiovascular", "Murmur Grade II/VI",
             "N/A", "Abnormal NCS"],
            ["xxx", "xxxx/xxx", "Gx", "EOT", "Respiratory", "Crackles left base",
             "Normal", "Abnormal CS"],
            {"label": "[...]", "values": ["...", "...", "...", "...", "...", "...", "...", "..."]},
        ],
        footnotes=["NCS = Not Clinically Significant. CS = Clinically Significant. Refer to T14.3.4.15-T14.3.4.16."],
        dataset_source="ADSL, ADPE", program_ref="l_pe.sas",
    ))

    items.append(TFLItem(
        id="L16.2.25", title="Listing of Urinalysis Results — Dipstick and Microscopic",
        tfl_type=L, section=S162, sort_key=25,
        population="Safety Population",
        placeholder_columns=["Site", "Subject", "Group", "Visit",
                             "pH", "Protein", "Glucose", "Blood",
                             "Ketones", "Microscopic Findings"],
        shell_rows=[
            ["xxx", "xxxx/xxx", "Gx", "Baseline", "6.0", "Neg", "Neg", "Neg",
             "Neg", "No casts/crystals"],
            ["xxx", "xxxx/xxx", "Gx", "Wk 12", "7.5", "++", "Neg", "+",
             "Neg", "Hyaline casts: 2-5/LPF"],
            {"label": "[...]", "values": ["...", "...", "...", "...", "...", "...", "...", "...", "...", "..."]},
        ],
        footnotes=["Dipstick: Neg/Trace/+/++/+++. LPF = Low Power Field. Refer to T14.3.3.14."],
        dataset_source="ADSL, ADLB", program_ref="l_ua.sas",
    ))

    items.append(TFLItem(
        id="L16.2.26", title="Listing of Coagulation Panel Results",
        tfl_type=L, section=S162, sort_key=26,
        population="Safety Population",
        placeholder_columns=["Site", "Subject", "Group", "Visit",
                             "PT (s)", "PT Ref Range", "INR",
                             "aPTT (s)", "aPTT Ref Range", "Flag"],
        shell_rows=[
            ["xxx", "xxxx/xxx", "Gx", "Baseline", "xx.x", "xx.x-xx.x", "x.xx",
             "xx.x", "xx.x-xx.x", "N"],
            ["xxx", "xxxx/xxx", "Gx", "Wk 4", "xx.x", "xx.x-xx.x", "x.xx",
             "xx.x", "xx.x-xx.x", "H"],
            {"label": "[...]", "values": ["...", "...", "...", "...", "...", "...", "...", "...", "...", "..."]},
        ],
        footnotes=["Flag: L=Below, N=Within, H=Above reference range. Refer to T14.3.3.12-T14.3.3.13."],
        dataset_source="ADSL, ADLB", program_ref="l_coag.sas",
    ))

    items.append(TFLItem(
        id="L16.2.27", title="Listing of Cardiac Biomarkers and Immunoglobulins",
        tfl_type=L, section=S162, sort_key=27,
        population="Safety Population",
        placeholder_columns=["Site", "Subject", "Group", "Visit",
                             "hs-Troponin I (ng/L)", "CK-MB (ng/mL)",
                             "NT-proBNP (pg/mL)", "IgG (g/L)", "IgM (g/L)"],
        shell_rows=[
            ["xxx", "xxxx/xxx", "Gx", "Baseline", "xx.x", "xx.x", "xxx", "xx.x", "xx.x"],
            ["xxx", "xxxx/xxx", "Gx", "Wk 12", "xx.x", "xx.x", "xxx", "xx.x", "xx.x"],
            {"label": "[...]", "values": ["...", "...", "...", "...", "...", "...", "...", "...", "..."]},
        ],
        footnotes=["Refer to T14.3.3.19 and T14.3.3.21 for summary tables."],
        dataset_source="ADSL, ADLB", program_ref="l_cardiac_bio.sas",
    ))

    items.append(TFLItem(
        id="L16.2.28", title="Listing of Lymphocyte Subsets and Cytokine Panel",
        tfl_type=L, section=S162, sort_key=28,
        population="Safety Population (Subset with Immunophenotyping)",
        placeholder_columns=["Site", "Subject", "Group", "Visit",
                             "CD3 (cells/uL)", "CD4 (cells/uL)", "CD8 (cells/uL)",
                             "CD4/CD8 Ratio", "CD19 (cells/uL)", "CD16+56 (cells/uL)"],
        shell_rows=[
            ["xxx", "xxxx/xxx", "Gx", "Baseline", "xxx", "xxx", "xxx", "x.xx", "xxx", "xxx"],
            ["xxx", "xxxx/xxx", "Gx", "Cycle 2 D1", "xxx", "xxx", "xxx", "x.xx", "xxx", "xxx"],
            {"label": "[...]", "values": ["...", "...", "...", "...", "...", "...", "...", "...", "...", "..."]},
        ],
        footnotes=["Flow cytometry. Refer to T14.3.3.22-T14.3.3.23 for summary tables."],
        dataset_source="ADSL, ADLB", program_ref="l_lymph_cyto.sas",
    ))

    items.append(TFLItem(
        id="L16.2.29", title="Listing of Infusion-Related Reactions — Timing and Management Detail",
        tfl_type=L, section=S162, sort_key=29,
        population="Safety Population",
        placeholder_columns=["Site", "Subject", "Group", "Cycle/Infusion",
                             "IRR PT", "CTCAE Grade", "Onset from Start (min)",
                             "Infusion Rate Change", "Prophylaxis Given",
                             "Completed Infusion?", "Outcome"],
        shell_rows=[
            ["xxx", "xxxx/xxx", "Gx", "C1/Inf1", "Chills", "2", "45",
             "Rate reduced 50%", "Antihistamine", "Y", "Recovered"],
            {"label": "[...]", "values": ["...", "...", "...", "...", "...", "...", "...", "...", "...", "...", "..."]},
        ],
        footnotes=["IRR = infusion-related reaction (onset during or within 24h of infusion). Refer to T14.3.1.13 and T14.3.1.25."],
        dataset_source="ADSL, ADAE, ADEX", program_ref="l_irr.sas",
        dictionary_versions={"CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="L16.2.30", title="Listing of Dose Modifications — Interruptions and Reductions Detail",
        tfl_type=L, section=S162, sort_key=30,
        population="Safety Population",
        placeholder_columns=["Site", "Subject", "Group", "Cycle",
                             "Modification Type", "Reason",
                             "AE-Related PT", "Original Dose",
                             "Modified Dose", "Days Interrupted"],
        shell_rows=[
            ["xxx", "xxxx/xxx", "Gx", "C3", "Interruption", "Neutropenia",
             "Neutropenia Gr3", "xxx mg", "0 mg", "7"],
            ["xxx", "xxxx/xxx", "Gx", "C5", "Reduction", "Fatigue",
             "Fatigue Gr2", "xxx mg", "xx mg", "0"],
            {"label": "[...]", "values": ["...", "...", "...", "...", "...", "...", "...", "...", "...", "..."]},
        ],
        footnotes=["Refer to T14.3.1.7 and T14.3.1.25 for summary tables."],
        dataset_source="ADSL, ADEX", program_ref="l_dose_mod.sas",
    ))

    items.append(TFLItem(
        id="L16.2.31", title="Listing of Reproductive Hormone Panel Results",
        tfl_type=L, section=S162, sort_key=31,
        population="Safety Population (Subset with Hormone Data)",
        placeholder_columns=["Site", "Subject", "Group", "Sex", "Visit",
                             "FSH (IU/L)", "LH (IU/L)", "Estradiol (pmol/L)",
                             "Testosterone (nmol/L)", "AMH (pmol/L)"],
        shell_rows=[
            ["xxx", "xxxx/xxx", "Gx", "F", "Baseline", "xx.x", "xx.x", "xxx", "x.x", "xx.x"],
            ["xxx", "xxxx/xxx", "Gx", "M", "Baseline", "xx.x", "xx.x", "xxx", "xx.x", "N/A"],
            {"label": "[...]", "values": ["...", "...", "...", "...", "...", "...", "...", "...", "...", "..."]},
        ],
        footnotes=["Reproductive hormones collected per protocol. AMH = Anti-Mullerian Hormone (females only where applicable)."],
        dataset_source="ADSL, ADLB", program_ref="l_hormone.sas",
    ))

    return TFLCatalog(items)
