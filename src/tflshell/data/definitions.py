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

# Standard 4-column header templates
H2_SIMPLE = ["Parameter\nCategory / Statistic",
             "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)", "...\n...\nOverall\n(N=XX)"]
H2_NPCT = ["Parameter\nCategory",
            "XXX Group 1\n(N=XX)\nn (%)", "XXX Group 2\n(N=XX)\nn (%)",
            "...\n...\nOverall\n(N=XX)\nn (%)"]
H2_SOCPT = ["System Organ Class\nPreferred Term",
             "XXX Group 1\n(N=XX)\nn (%)", "XXX Group 2\n(N=XX)\nn (%)",
             "...\n...\nOverall\n(N=XX)\nn (%)"]
H2_EVENTS = ["Parameter\nCategory",
              "XXX Group 1\n(N=XX)\nn (%) [E]", "XXX Group 2\n(N=XX)\nn (%) [E]",
              "...\n...\nOverall\n(N=XX)\nn (%) [E]"]
H2_EFF = ["Endpoint\nStatistic",
           "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)",
           "...\n...\nOverall\n(N=XX)"]
H2_LAB = ["Parameter\nVisit", "Statistic",
           "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)", "...\n...\nOverall\n(N=XX)"]

# Shared ellipsis row
EROW = ["[...]", "...", "...", "..."]
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
            ["Age (years)", "xx", "xx", "...", "xx"],
            ["  n", "xx", "xx", "...", "xx"],
            ["  Mean (SD)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            ["  Median", "xx.x", "xx.x", "...", "xx.x"],
            ["  Min, Max", "xx, xx", "xx, xx", "...", "xx, xx"],
            ["Sex, n (%)", "", "", "", ""],
            ["  Male", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["  Female", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Race, n (%)", "", "", "", ""],
            ["  White", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["  Black or African American", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["  Asian", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            EROW,
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
            ["Any Medical History Condition", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Vascular disorders", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["  Hypertension", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["  Hypotension", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Metabolism and nutrition disorders", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["  Diabetes mellitus", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            EROW,
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
            ["Randomized", "xx", "xx", "...", "xx"],
            ["Treated (>=1 dose)", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Completed Treatment", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Discontinued Treatment", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["  Disease Progression", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["  Adverse Event", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["  Withdrawal by Subject", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            EROW,
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
        id="T14.1.10", title="COVID-19 Medical History, Vaccination, and Testing Status",
        tfl_type=T, section=S141, sort_key=10,
        population="Safety Population",
        placeholder_columns=H2_SIMPLE,
        shell_rows=[
            ["Prior COVID-19 Diagnosis — Yes", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["COVID-19 Vaccinated — Yes", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Baseline COVID-19 Test — Negative", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            EROW,
        ],
        dataset_source="ADSL, ADMH", program_ref="t_covid19_status.sas",
    ))

    items.append(TFLItem(
        id="T14.1.11", title="Summary of Study Drug Exposure — Duration, Cycles, Dose Intensity",
        tfl_type=T, section=S141, sort_key=11,
        population="Safety Population",
        placeholder_columns=H2_SIMPLE,
        shell_rows=[
            ["Duration of exposure (days)", "", "", "", ""],
            ["  Mean (SD)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            ["  Median", "xx.x", "xx.x", "...", "xx.x"],
            ["Number of cycles started", "", "", "", ""],
            ["  Mean (SD)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            ["Dose intensity (mg/day)", "", "", "", ""],
            ["  Mean (SD)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            EROW,
        ],
        dataset_source="ADEX", program_ref="t_exposure_summary.sas",
    ))

    items.append(TFLItem(
        id="T14.1.12", title="Summary of Genomic/Biomarker Baseline Characteristics",
        tfl_type=T, section=S141, sort_key=12,
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

    # =====================================================================
    # 14.2 EFFICACY (32 items: 11 general + 21 oncology)
    # =====================================================================

    items.append(TFLItem(
        id="T14.2.1", title="Primary Efficacy Endpoint — Primary Analysis",
        tfl_type=T, section=S142, sort_key=1,
        population="Intent-to-Treat (ITT) Population",
        placeholder_columns=["Parameter",
                             "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)", "...\n...\nOverall\n(N=XX)"],
        shell_rows=[
            ["Primary Endpoint — Change from Baseline at Week 24", "", "", "", ""],
            ["  Least Squares Mean (SE)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            ["  LS Mean Difference", "", "xx.x", "", ""],
            ["  95% CI", "", "[xx.x, xx.x]", "", ""],
            ["  p-value", "", "x.xxx", "", ""],
            EROW,
        ],
        footnotes=["ANCOVA: baseline as covariate, treatment + stratification as fixed effects.",
                   "Missing data via MMRM under MAR. Two-sided 95% CI and p-value."],
        dataset_source="ADSL, ADEFF", program_ref="t_primary_eff.sas",
    ))

    items.append(TFLItem(
        id="T14.2.2", title="Secondary Efficacy Endpoints — Summary",
        tfl_type=T, section=S142, sort_key=2,
        population="Intent-to-Treat (ITT) Population",
        placeholder_columns=["Endpoint\nStatistic",
                             "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)", "...\n...\nOverall\n(N=XX)"],
        shell_rows=[
            ["Secondary Endpoint 1 — Change from BL", "", "", "", ""],
            ["  LS Mean (SE)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            ["  LS Mean Difference (95% CI)", "xx.x [xx.x, xx.x]", "", "", ""],
            ["  p-value", "x.xxx", "", "", ""],
            ["Secondary Endpoint 2 — Response Rate, n (%)", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["  p-value", "x.xxx", "", "", ""],
            EROW,
        ],
        dataset_source="ADSL, ADEFF", program_ref="t_secondary_eff.sas",
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
                             "XXX Group 1\n(N=XX)", "Control\n(N=XX)", "...\n...\nOverall\n(N=XX)"],
        shell_rows=[
            ["Primary Endpoint — LS Mean (SE)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            ["Difference (95% CI)", "xx.x [xx.x, xx.x]", "", "", ""],
            ["NI Margin", "xx.x", "", "", ""],
            ["NI Met?", "Yes / No", "", "", ""],
            EROW,
        ],
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
                             "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)", "...\n...\nOverall\n(N=XX)"],
        shell_rows=[
            ["Median TTD (months)", "xx.x", "xx.x", "...", "xx.x"],
            ["Events / N", "xx / xx", "xx / xx", "...", "xx / xx"],
            ["Hazard Ratio (95% CI)", "x.xx [x.xx, x.xx]", "", "", ""],
            ["p-value", "x.xxx", "", "", ""],
            EROW,
        ],
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
            ["Complete Response (CR)", "xx ( xx.x)", "xx ( xx.x)", "...", "xx ( xx.x)"],
            ["Partial Response (PR)", "xx ( xx.x)", "xx ( xx.x)", "...", "xx ( xx.x)"],
            ["Stable Disease (SD)", "xx ( xx.x)", "xx ( xx.x)", "...", "xx ( xx.x)"],
            ["Progressive Disease (PD)", "xx ( xx.x)", "xx ( xx.x)", "...", "xx ( xx.x)"],
            ["Not Evaluable (NE)", "xx ( xx.x)", "xx ( xx.x)", "...", "xx ( xx.x)"],
            EROW,
        ],
        footnotes=["RECIST v1.1 by Independent Central Review (ICR). Confirmed responses only.",
                   "CR = Disappearance of all lesions. PR = >=30% decrease in sum of diameters."],
        dataset_source="ADSL, ADRS", program_ref="t_bor.sas",
    ))

    items.append(TFLItem(
        id="T14.2.10", title="Tumor Response — Objective Response Rate (ORR)",
        tfl_type=T, section=S142, sort_key=13, oncology_only=True,
        population="Intent-to-Treat (ITT) Population",
        placeholder_columns=["Parameter",
                             "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)", "...\n...\nOverall\n(N=XX)"],
        shell_rows=[
            ["ORR (CR+PR), n (%)", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["95% CI (Clopper-Pearson)", "[xx.x, xx.x]", "[xx.x, xx.x]", "", "[xx.x, xx.x]"],
            ["Odds Ratio (95% CI)", "x.xx [x.xx, x.xx]", "", "", ""],
            ["p-value (CMH, stratified)", "x.xxx", "", "", ""],
            EROW,
        ],
        dataset_source="ADSL, ADRS", program_ref="t_orr.sas",
    ))

    items.append(TFLItem(
        id="T14.2.11", title="Tumor Response — Disease Control Rate (DCR)",
        tfl_type=T, section=S142, sort_key=14, oncology_only=True,
        population="Intent-to-Treat (ITT) Population",
        placeholder_columns=["Parameter",
                             "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)", "...\n...\nOverall\n(N=XX)"],
        shell_rows=[
            ["DCR (CR+PR+SD), n (%)", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["95% CI (Clopper-Pearson)", "[xx.x, xx.x]", "[xx.x, xx.x]", "", "[xx.x, xx.x]"],
            EROW,
        ],
        dataset_source="ADSL, ADRS", program_ref="t_dcr.sas",
    ))

    items.append(TFLItem(
        id="T14.2.12", title="Tumor Response — Duration of Response (DOR)",
        tfl_type=T, section=S142, sort_key=15, oncology_only=True,
        population="Responders (Confirmed CR or PR)",
        placeholder_columns=["Parameter",
                             "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)", "...\n...\nOverall\n(N=XX)"],
        shell_rows=[
            ["Events / N (%)", "xx / xx (xx.x)", "xx / xx (xx.x)", "...", "xx / xx (xx.x)"],
            ["Median DOR (months)", "xx.x", "xx.x", "...", "xx.x"],
            ["95% CI (Brookmeyer-Crowley)", "[xx.x, xx.x]", "[xx.x, xx.x]", "", "[xx.x, xx.x]"],
            EROW,
        ],
        dataset_source="ADSL, ADRS, ADTTE", program_ref="t_dor.sas",
    ))

    items.append(TFLItem(
        id="T14.2.13", title="Tumor Response — Time to Response (TTR)",
        tfl_type=T, section=S142, sort_key=16, oncology_only=True,
        population="Responders (Confirmed CR or PR)",
        placeholder_columns=["Parameter",
                             "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)", "...\n...\nOverall\n(N=XX)"],
        shell_rows=[
            ["Mean (SD), months", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            ["Median (Min, Max)", "xx.x (xx.x, xx.x)", "xx.x (xx.x, xx.x)", "...", "xx.x (xx.x, xx.x)"],
            EROW,
        ],
        dataset_source="ADSL, ADRS", program_ref="t_ttr.sas",
    ))

    items.append(TFLItem(
        id="T14.2.14", title="Progression-Free Survival (PFS) — Primary Analysis",
        tfl_type=T, section=S142, sort_key=17, oncology_only=True,
        population="Intent-to-Treat (ITT) Population",
        placeholder_columns=["Parameter",
                             "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)", "...\n...\nOverall\n(N=XX)"],
        shell_rows=[
            ["Events / N (%)", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Median PFS (months)", "xx.x", "xx.x", "...", "xx.x"],
            ["95% CI", "[xx.x, xx.x]", "[xx.x, xx.x]", "", "[xx.x, xx.x]"],
            ["Hazard Ratio (95% CI)", "x.xx [x.xx, x.xx]", "", "", ""],
            ["p-value (stratified log-rank)", "x.xxx", "", "", ""],
            ["PFS Rate at 6 months", "xx.x%", "xx.x%", "", ""],
            ["PFS Rate at 12 months", "xx.x%", "xx.x%", "", ""],
            EROW,
        ],
        footnotes=["PFS: time from randomization to PD (RECIST 1.1, ICR) or death.",
                   "Stratified Cox/log-rank by baseline stratification factors."],
        dataset_source="ADSL, ADTTE", program_ref="t_pfs_primary.sas",
    ))

    items.append(TFLItem(
        id="T14.2.15", title="Overall Survival (OS) — Primary Analysis",
        tfl_type=T, section=S142, sort_key=18, oncology_only=True,
        population="Intent-to-Treat (ITT) Population",
        placeholder_columns=["Parameter",
                             "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)", "...\n...\nOverall\n(N=XX)"],
        shell_rows=[
            ["Events / N (%)", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Median OS (months)", "xx.x / NR", "xx.x / NR", "...", "xx.x / NR"],
            ["95% CI", "[xx.x, NR]", "[xx.x, NR]", "", ""],
            ["Hazard Ratio (95% CI)", "x.xx [x.xx, x.xx]", "", "", ""],
            ["p-value (stratified log-rank)", "x.xxx", "", "", ""],
            ["OS Rate at 12 months", "xx.x%", "xx.x%", "", ""],
            EROW,
        ],
        footnotes=["OS: time from randomization to death from any cause. NR=Not Reached."],
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
                             "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)", "...\n...\nOverall\n(N=XX)"],
        shell_rows=[
            ["Best % Change from Baseline", "", "", "", ""],
            ["  Mean (SD)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
            ["  Median (Range)", "xx.x (xx.x, xx.x)", "xx.x (xx.x, xx.x)", "...", "xx.x (xx.x, xx.x)"],
            EROW,
        ],
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
                             "XXX Group 1\n(N=XX)", "XXX Group 2\n(N=XX)", "...\n...\nOverall\n(N=XX)"],
        shell_rows=[
            ["Events / N (%)", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Median TFST (months)", "xx.x", "xx.x", "...", "xx.x"],
            ["HR (95% CI)", "x.xx [x.xx, x.xx]", "", "", ""],
            EROW,
        ],
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
    # 14.3 SAFETY — 30 items (AE → Deaths → Labs → VS → ECG)
    # =====================================================================

    items.append(TFLItem(
        id="T14.3.1", title="Overall Summary of Treatment-Emergent Adverse Events",
        tfl_type=T, section=S143, sort_key=1,
        population="Safety Population",
        placeholder_columns=["Adverse Event Category",
                             "XXX Group 1\n(N=XX)\nn (%) [E]",
                             "XXX Group 2\n(N=XX)\nn (%) [E]",
                             "...\n...\nOverall\n(N=XX)\nn (%) [E]"],
        shell_rows=[
            ["Any TEAE", "xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
            ["Drug-Related TEAE", "xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
            ["CTCAE Grade >=3 TEAE", "xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
            ["Serious TEAE (SAE)", "xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
            ["TEAE Leading to Discontinuation", "xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
            ["TEAE Leading to Dose Reduction/Interruption", "xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
            ["Fatal TEAE (Grade 5)", "xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
            EROW,
        ],
        footnotes=["TEAE: onset on/after first dose through 30 days after last dose. CTCAE v[xx]. MedDRA [xx.x]."],
        dataset_source="ADSL, ADAE", program_ref="t_ae_overview.sas",
        dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="T14.3.2", title="TEAEs by System Organ Class and Preferred Term (>=5% in Any Arm)",
        tfl_type=T, section=S143, sort_key=2,
        population="Safety Population",
        placeholder_columns=H2_EVENTS,
        shell_rows=[
            ["Any TEAE", "xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
            ["Gastrointestinal disorders", "xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
            ["  Nausea", "xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
            ["  Diarrhea", "xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
            ["  Vomiting", "xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
            ["General disorders", "xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
            ["  Fatigue", "xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
            EROW,
        ],
        footnotes=["Sorted alphabetically by SOC; PTs by descending frequency in G1. "
                   "[E]=total events. MedDRA [xx.x]. CTCAE [xx]."],
        dataset_source="ADSL, ADAE", program_ref="t_ae_soc_pt.sas",
        dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="T14.3.3", title="TEAEs by SOC, PT, and Maximum CTCAE Grade (Group 1)",
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
        id="T14.3.4", title="Drug-Related TEAEs by SOC, PT, and Relationship",
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
        id="T14.3.5", title="Serious Adverse Events by SOC and PT",
        tfl_type=T, section=S143, sort_key=5,
        population="Safety Population",
        placeholder_columns=H2_EVENTS,
        shell_rows=[
            ["Any SAE", "xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
            ["Infections and infestations", "xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
            ["  Pneumonia", "xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
            EROW,
        ],
        footnotes=["SAE defined per ICH E2A criteria."],
        dataset_source="ADSL, ADAE", program_ref="t_sae_soc_pt.sas",
        dictionary_versions={"MedDRA": "[xx.x]"},
    ))

    items.append(TFLItem(
        id="T14.3.6", title="TEAEs Leading to Treatment Discontinuation by SOC and PT",
        tfl_type=T, section=S143, sort_key=6,
        population="Safety Population",
        placeholder_columns=H2_SOCPT,
        shell_rows=[
            ["Any TEAE Leading to Discontinuation", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["Gastrointestinal disorders", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["  Nausea", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            EROW,
        ],
        dataset_source="ADSL, ADAE", program_ref="t_ae_disc.sas",
        dictionary_versions={"MedDRA": "[xx.x]"},
    ))

    items.append(TFLItem(
        id="T14.3.7", title="TEAEs Leading to Dose Reduction or Interruption by SOC and PT",
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
        id="T14.3.8", title="Summary of Deaths",
        tfl_type=T, section=S143, sort_key=8,
        population="Safety Population",
        placeholder_columns=H2_SOCPT,
        shell_rows=[
            ["All Deaths", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["  Disease Progression", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["  Adverse Event", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            ["  Other", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
            EROW,
        ],
        dataset_source="ADSL, ADAE, ADTTE", program_ref="t_deaths.sas",
    ))

    items.append(TFLItem(
        id="T14.3.9", title="TEAEs Occurring in >=5% of Subjects by PT",
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
        id="T14.3.10", title="TEAEs by Cycle / Treatment Period",
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
        id="T14.3.11", title="Exposure-Adjusted TEAE Incidence Rates (per 100 Patient-Years)",
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
        id="T14.3.12", title="TEAEs by Age Group Subgroup",
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
        id="T14.3.13", title="TEAEs by Sex Subgroup",
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
        id="T14.3.14", title="Hy's Law Cases — Liver Chemistry Screening",
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
        id="T14.3.15", title="Laboratory Parameters — Shift Table (Baseline to Worst Post-Baseline)",
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
        id="T14.3.16", title="Hematology Parameters — Summary Statistics by Visit",
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
        id="T14.3.17", title="Clinical Chemistry Parameters — Summary Statistics by Visit",
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
        id="T14.3.18", title="Laboratory Abnormalities — Grade >=3 Listing",
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
        id="T14.3.19", title="Laboratory Toxicity Grade Shift Over Time (by Cycle)",
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
        id="F14.3.1", title="Mean (+/- SD) Change in Laboratory Parameters Over Time",
        tfl_type=F, section=S143, sort_key=20,
        population="Safety Population",
        figure_description="Multi-panel line plot: mean ± SD change in Hgb, Plt, ANC, ALT, AST, Creatinine.",
        dataset_source="ADSL, ADLB", program_ref="f_lab_longitudinal.sas",
        figure_type="longitudinal", figure_width_inches=6, figure_height_inches=4,
    ))

    items.append(TFLItem(
        id="F14.3.2", title="Box Plot — Liver Function Tests by Visit",
        tfl_type=F, section=S143, sort_key=21,
        population="Safety Population",
        figure_description="Box plots: ALT, AST, ALP, Total Bilirubin by visit, side-by-side arms, ULN ref lines.",
        dataset_source="ADSL, ADLB", program_ref="f_lft_box.sas",
        figure_type="box_plot", figure_width_inches=6, figure_height_inches=4,
    ))

    items.append(TFLItem(
        id="T14.3.20", title="Vital Signs — Summary Statistics by Visit",
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
        id="T14.3.21", title="Vital Signs — Clinically Notable Abnormalities by Visit",
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
        id="F14.3.3", title="Mean (+/- SD) Vital Signs Over Time",
        tfl_type=F, section=S143, sort_key=24,
        population="Safety Population",
        figure_description="Multi-panel: mean ± SD of SBP, DBP, HR, Weight over visits.",
        dataset_source="ADSL, ADVS", program_ref="f_vs_longitudinal.sas",
        figure_type="longitudinal", figure_width_inches=6, figure_height_inches=4,
    ))

    items.append(TFLItem(
        id="F14.3.4", title="Liver Function Panel — Mean Over Time with ULN Reference",
        tfl_type=F, section=S143, sort_key=25,
        population="Safety Population",
        figure_description="Line plot: ALT, AST, ALP, TBL means over visits with ULN lines.",
        dataset_source="ADSL, ADLB", program_ref="f_lft_uln.sas",
        figure_type="longitudinal", figure_width_inches=5.5, figure_height_inches=3.5,
    ))

    items.append(TFLItem(
        id="T14.3.22", title="ECG Parameters — Summary Statistics by Visit",
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
        id="T14.3.23", title="ECG QTcF Categorical Analysis",
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
        id="T14.3.24", title="ECG Qualitative Assessment — Shift Table",
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
        id="T14.3.25", title="Infusion-Related Reactions by Preferred Term",
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
        id="T14.3.26", title="ECOG Performance Status Shift Table",
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

    # =====================================================================
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

    return TFLCatalog(items)
