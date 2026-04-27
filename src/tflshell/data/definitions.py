"""TFL Shell Catalog v2.1 — ~100 TFLs with full clinical practice compliance.

ICH E3 section structure:
  14.1 Demographics and Baseline Characteristics
  14.2 Efficacy Analysis (general + oncology-specific)
  14.3 Safety Analysis
    14.3.1 Adverse Events (AE)
    14.3.2 Deaths
    14.3.3 Clinical Laboratory Evaluations
    14.3.4 Vital Signs and Physical Findings
    14.3.5 ECG
  14.4 Special Assessments (PK, Immunogenicity, Biomarker, PRO)
    16.2 Patient Data Listings (Appendices)
"""

from tflshell.models.enums import TFLType, Section
from tflshell.models.tfl_item import TFLItem
from tflshell.models.catalog import TFLCatalog

T, F, L = TFLType.TABLE, TFLType.FIGURE, TFLType.LISTING
S141, S142, S143, S144 = Section.SEC_14_1, Section.SEC_14_2, Section.SEC_14_3, Section.SEC_14_4
S162 = Section.SEC_16_2


def _rr(n, mean, sd, median, mn, mx, fmt=".1f"):
    """Format a row of descriptive statistics: n, Mean (SD), Median, Min, Max."""
    return [
        str(n),
        f"{mean:{fmt}} ({sd:{fmt}})",
        f"{median:{fmt}}",
        f"{mn:{fmt}}, {mx:{fmt}}",
    ]


def build_catalog() -> TFLCatalog:
    items: list[TFLItem] = []

    # =====================================================================
    # 14.1 DEMOGRAPHICS AND BASELINE (12 items)
    # =====================================================================

    items.append(TFLItem(
        id="T14.1.1", title="Summary of Demographic Characteristics",
        tfl_type=T, section=S141, sort_key=1,
        population="Intent-to-Treat (ITT) Population",
        description="Summary statistics of demographic variables by treatment arm.",
        placeholder_columns=["Demographic Variable\nCategory / Statistic",
                             "Treatment Group 1\n(N=xx)", "Treatment Group 2\n(N=xx)", "...\n...\nTotal\n(N=xx)"],
        shell_rows=[
            ['Age (years)', 'XX', 'XX', 'XX'],
            ['  n', 'XX', 'XX', 'XX'],
            ['  Mean (SD)', 'XX', 'XX', 'XX'],
            ['Sex', 'XX', 'XX', 'XX', 'XX'],
            ['Race', 'XX', 'XX', 'XX', 'XX'],
            ['Weight (kg)', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX']
        ],
        footnotes=["Percentages based on number of subjects in each treatment group.",
                   "Age calculated relative to date of informed consent."],
        dataset_source="ADSL", program_ref="t_demog_summary.sas",
        table_notes="Continuous: n, Mean, SD, Median, Min, Max. Categorical: n (%).",
    ))

    items.append(TFLItem(
        id="T14.1.2", title="Summary of Baseline Disease Characteristics",
        tfl_type=T, section=S141, sort_key=2,
        population="Intent-to-Treat (ITT) Population",
        placeholder_columns=["Characteristic\nCategory / Statistic",
                             "Treatment Group 1\n(N=xx)", "Treatment Group 2\n(N=xx)", "...\n...\nTotal\n(N=xx)"],
        shell_rows=[
            ['ECOG Performance Status', 'XX', 'XX', 'XX'],
            ['Primary Tumor Type', 'XX', 'XX', 'XX'],
            ['Disease Stage', 'XX', 'XX', 'XX', 'XX'],
            ['Time Since Initial Diagnosis (months)', 'XX', 'XX', 'XX'],
            ['Disease Duration (mo)', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX']
        ],
        footnotes=["ECOG: 0=Fully active, 1=Restricted, 2=Ambulatory but unable to work, "
                   "3=Limited self-care, 4=Completely disabled.",
                   "Baseline = last non-missing assessment on/before first dose."],
        dataset_source="ADSL, ADRS", program_ref="t_baseline_chars.sas",
    ))

    items.append(TFLItem(
        id="T14.1.3", title="Summary of Medical History by System Organ Class and Preferred Term",
        tfl_type=T, section=S141, sort_key=3,
        population="Safety Population",
        placeholder_columns=["System Organ Class\nPreferred Term",
                             "Treatment Group 1\n(N=xx) n (%)", "Treatment Group 2\n(N=xx) n (%)",
                             "...\n...\nTotal\n(N=xx) n (%)"],
        shell_rows=[
            ['Vascular disorders', 'XX', 'XX', 'XX'],
            ['  Hypertension', 'XX', 'XX', 'XX'],
            ['  Hypotension', 'XX', 'XX', 'XX'],
            ['Metabolism and nutrition disorders', 'XX', 'XX', 'XX'],
            ['  Diabetes mellitus', 'XX', 'XX', 'XX'],
            ['  Hyperlipidemia', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX']
        ],
        footnotes=["MedDRA version 26.0 used for coding medical history terms."],
        dataset_source="ADMH", program_ref="t_mh_soc_pt.sas",
        dictionary_versions={"MedDRA": "26.0"},
    ))

    items.append(TFLItem(
        id="T14.1.4", title="Summary of Prior Medications by ATC Class and Preferred Name",
        tfl_type=T, section=S141, sort_key=4,
        population="Safety Population",
        placeholder_columns=["ATC Class Level 2\nPreferred Name",
                             "Treatment Group 1\n(N=xx) n (%)", "Treatment Group 2\n(N=xx) n (%)",
                             "...\n...\nTotal\n(N=xx) n (%)"],
        shell_rows=[
            ['Drugs for acid-related disorders', 'XX', 'XX', 'XX'],
            ['  Omeprazole', 'XX', 'XX', 'XX'],
            ['  Pantoprazole', 'XX', 'XX', 'XX'],
            ['Antibacterials for systemic use', 'XX', 'XX', 'XX'],
            ['  Amoxicillin', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX']
        ],
        footnotes=["WHO Drug Dictionary Global 2024Q1 used for medication coding."],
        dataset_source="ADCM", program_ref="t_prior_meds.sas",
        dictionary_versions={"WHO-DD": "2024Q1"},
    ))

    items.append(TFLItem(
        id="T14.1.5", title="Subject Disposition",
        tfl_type=T, section=S141, sort_key=5,
        population="All Randomized Subjects",
        placeholder_columns=["Disposition Category",
                             "Treatment Group 1\nn (%)", "Treatment Group 2\nn (%)", "Total\nn (%)"],
        shell_rows=[
            ['Treated (>=1 dose)', 'XX', 'XX', 'XX'],
            ['Completed Treatment', 'XX', 'XX', 'XX'],
            ['Discontinued Treatment', 'XX', 'XX', 'XX'],
            ['  Disease Progression', 'XX', 'XX', 'XX'],
            ['  Adverse Event', 'XX', 'XX', 'XX'],
            ['  Withdrawal by Subject', 'XX', 'XX', 'XX'],
            ['  Other', 'XX', 'XX', 'XX']
        ],
        footnotes=["Percentages for discontinued: N=treated per arm.",
                   "Primary reason for discontinuation per CRF EOT page."],
        dataset_source="ADSL", program_ref="t_disposition.sas",
    ))

    items.append(TFLItem(
        id="T14.1.6", title="Major Protocol Deviations",
        tfl_type=T, section=S141, sort_key=6,
        population="All Randomized Subjects",
        placeholder_columns=["Deviation Category / Description",
                             "Treatment Group 1\nn (%)", "Treatment Group 2\nn (%)", "Total\nn (%)"],
        shell_rows=[
            ['Inclusion/Exclusion Criteria Not Met', 'XX', 'XX', 'XX'],
            ['Received Wrong Treatment/Incorrect Dose', 'XX', 'XX', 'XX'],
            ['Missed >=2 Consecutive Efficacy Assessments', 'XX', 'XX', 'XX'],
            ['Concomitant Prohibited Medication', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX']
        ],
        footnotes=["Major PDs defined per Protocol Deviation Plan, determined prior to unblinding."],
        dataset_source="ADSL, DV", program_ref="t_prot_dev.sas",
    ))

    items.append(TFLItem(
        id="T14.1.7", title="Analysis Populations",
        tfl_type=T, section=S141, sort_key=7,
        population="All Subjects",
        placeholder_columns=["Analysis Population",
                             "Treatment Group 1\nn (%)", "Treatment Group 2\nn (%)", "Total\nn (%)"],
        shell_rows=[
            ['Randomized', 'XX', 'XX', 'XX'],
            ['Intent-to-Treat (ITT)', 'XX', 'XX', 'XX'],
            ['Safety Population', 'XX', 'XX', 'XX'],
            ['Per-Protocol (PP)', 'XX', 'XX', 'XX'],
            ['PK Population', 'XX', 'XX', 'XX']
        ],
        footnotes=["ITT: All randomized subjects who received >=1 dose of study treatment.",
                   "Safety: All subjects who received >=1 dose of study treatment."],
        dataset_source="ADSL", program_ref="t_populations.sas",
    ))

    items.append(TFLItem(
        id="T14.1.8", title="Medical History by SOC/PT — Incidence >=2% in Any Arm",
        tfl_type=T, section=S141, sort_key=8,
        population="Safety Population",
        placeholder_columns=["SOC / Preferred Term",
                             "Treatment Group 1\n(N=xx) n (%)", "Treatment Group 2\n(N=xx) n (%)"],
        shell_rows=[
            ['  Gastroesophageal reflux disease', 'XX', 'XX'],
            ['  Hiatus hernia', 'XX', 'XX'],
            ['Musculoskeletal disorders', 'XX', 'XX'],
            ['  Back pain', 'XX', 'XX'],
            ['  Osteoarthritis', 'XX', 'XX'],
            ['XX', 'XX', 'XX']
        ],
        footnotes=["MedDRA 26.0. Only PTs with >=2% incidence in any arm displayed."],
        dataset_source="ADMH", program_ref="t_mh_2pct.sas",
        dictionary_versions={"MedDRA": "26.0"},
    ))

    items.append(TFLItem(
        id="T14.1.9", title="Prior and Concomitant Medications by ATC Level 2 and Preferred Name",
        tfl_type=T, section=S141, sort_key=9,
        population="Safety Population",
        placeholder_columns=["ATC Level 2 / Preferred Name",
                             "Treatment Group 1\n(N=xx) n (%)", "Treatment Group 2\n(N=xx) n (%)"],
        shell_rows=[
            ['Concomitant Medications — Any', 'XX', 'XX'],
            ['Drugs for acid-related disorders', 'XX', 'XX'],
            ['Analgesics', 'XX', 'XX'],
            ['Antihypertensives', 'XX', 'XX'],
            ['XX', 'XX', 'XX']
        ],
        footnotes=["WHO Drug Dictionary 2024Q1. Concomitant: any medication after first dose "
                   "or within 30 days prior and continuing."],
        dataset_source="ADCM", program_ref="t_conmed_atc.sas",
        dictionary_versions={"WHO-DD": "2024Q1"},
    ))

    items.append(TFLItem(
        id="T14.1.10", title="COVID-19 Medical History, Vaccination, and Testing Status",
        tfl_type=T, section=S141, sort_key=10,
        population="Safety Population",
        placeholder_columns=["COVID-19 Parameter", "Category",
                             "Treatment Group 1\n(N=xx) n (%)", "Treatment Group 2\n(N=xx) n (%)"],
        shell_rows=[
            ['COVID-19 Vaccinated', 'XX', 'XX', 'XX'],
            ['Baseline COVID-19 Test', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADMH", program_ref="t_covid19_status.sas",
    ))

    items.append(TFLItem(
        id="T14.1.11", title="Summary of Study Drug Exposure",
        tfl_type=T, section=S141, sort_key=11,
        population="Safety Population",
        placeholder_columns=["Exposure Parameter", "Statistic",
                             "Treatment Group 1\n(N=xx)", "Treatment Group 2\n(N=xx)"],
        shell_rows=[
            ['Duration of Exposure (days)', 'XX', 'XX', 'XX'],
            ['Number of cycles started', 'XX', 'XX', 'XX'],
            ['Cumulative dose (mg)', 'XX', 'XX', 'XX'],
            ['Dose intensity (mg/day)', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADEX", program_ref="t_exposure_summary.sas",
    ))

    items.append(TFLItem(
        id="T14.1.12", title="Summary of Genomic/Biomarker Baseline Characteristics",
        tfl_type=T, section=S141, sort_key=12,
        oncology_only=True,
        population="ITT Population with Biomarker Data",
        placeholder_columns=["Biomarker", "Category / Statistic",
                             "Treatment A\n(N=xx)", "Treatment B\n(N=xx)"],
        shell_rows=[
            ['PD-L1 Expression', 'XX', 'XX', 'XX'],
            ['Tumor Mutation Burden', 'XX', 'XX', 'XX'],
            ['EGFR Mutation', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADBM", program_ref="t_biomarker_baseline.sas",
    ))

    # =====================================================================
    # 14.2 EFFICACY ANALYSIS (33 items: 11 general + 22 oncology)
    # =====================================================================

    items.append(TFLItem(
        id="T14.2.1", title="Primary Efficacy Endpoint — Primary Analysis",
        tfl_type=T, section=S142, sort_key=1,
        population="Intent-to-Treat (ITT) Population",
        placeholder_columns=["Parameter", "Treatment Group 1\n(N=xx)", "Treatment Group 2\n(N=xx)",
                             "Difference", "95% CI", "p-value"],
        shell_rows=[
            ['  Least Squares Mean (SE)', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['  ANCOVA Model: treatment + baseline + stratification factors', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        footnotes=["ANCOVA with baseline value as covariate and treatment, stratification as fixed effects.",
                   "Missing data handled by MMRM under MAR assumption.",
                   "Two-sided 95% CI and p-value reported."],
        dataset_source="ADSL, ADEFF", program_ref="t_primary_eff.sas",
    ))

    items.append(TFLItem(
        id="T14.2.2", title="Secondary Efficacy Endpoints — Summary",
        tfl_type=T, section=S142, sort_key=2,
        population="Intent-to-Treat (ITT) Population",
        placeholder_columns=["Endpoint", "Statistic",
                             "Treatment Group 1\n(N=xx)", "Treatment Group 2\n(N=xx)",
                             "Difference", "95% CI", "p-value"],
        shell_rows=[
            ['Secondary Endpoint 2 — Response Rate', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        footnotes=["Hierarchical testing per SAP; nominal p-values shown.",
                   "Multiplicity-adjusted p-values for the primary family."],
        dataset_source="ADSL, ADEFF", program_ref="t_secondary_eff.sas",
    ))

    items.append(TFLItem(
        id="T14.2.3", title="Subgroup Analysis of Primary Endpoint",
        tfl_type=T, section=S142, sort_key=3,
        population="Intent-to-Treat (ITT) Population",
        placeholder_columns=["Subgroup", "Level", "Treatment Group 1\nn/N [stat]",
                             "Treatment Group 2\nn/N [stat]", "Effect [95% CI]", "Interaction p"],
        shell_rows=[
            ['Age', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['Sex', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        footnotes=["Subgroup analyses are exploratory.",
                   "Interaction p-value from model with treatment-by-subgroup term."],
        dataset_source="ADSL, ADEFF", program_ref="t_subgroup_primary.sas",
    ))

    items.append(TFLItem(
        id="T14.2.4", title="Sensitivity Analysis of Primary Endpoint",
        tfl_type=T, section=S142, sort_key=4,
        population="ITT and Per-Protocol (PP) Populations",
        placeholder_columns=["Analysis", "Population", "Missing Data",
                             "Treatment Group 1\nLS Mean", "Treatment Group 2\nLS Mean",
                             "Difference", "95% CI"],
        shell_rows=[
            ['PP Analysis', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['Multiple Imputation', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['Tipping Point (δ=1.0)', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        footnotes=["Sensitivity analyses assess robustness to MAR deviations."],
        dataset_source="ADSL, ADEFF", program_ref="t_sensitivity_eff.sas",
    ))

    items.append(TFLItem(
        id="T14.2.5", title="Non-Inferiority Analysis of Primary Endpoint",
        tfl_type=T, section=S142, sort_key=5,
        population="Per-Protocol (PP) Population",
        placeholder_columns=["Parameter", "Treatment Group 1\n(N=xx)", "Control Group\n(N=xx)",
                             "Difference", "95% CI", "NI Margin", "NI Met?"],
        shell_rows=[
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        footnotes=["NI margin = [X] per regulatory agreement.",
                   "NI demonstrated if upper bound of 95% CI < NI margin."],
        dataset_source="ADSL, ADEFF", program_ref="t_ni_analysis.sas",
    ))

    items.append(TFLItem(
        id="T14.2.6", title="Tipping Point Analysis for Primary Endpoint",
        tfl_type=T, section=S142, sort_key=6,
        population="ITT Population",
        placeholder_columns=["Tipping Point Parameter", "Shift Value",
                             "p-value", "Conclusion"],
        shell_rows=[
            ['', 'XX', 'XX', 'XX'],
            ['', 'XX', 'XX', 'XX'],
            ['', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX']
        ],
        footnotes=["Tipping point analysis per ICH E9(R1). Assesses departures from MAR."],
        dataset_source="ADSL, ADEFF", program_ref="t_tipping_point.sas",
    ))

    items.append(TFLItem(
        id="T14.2.7", title="Sensitivity Analysis by Estimand Strategy",
        tfl_type=T, section=S142, sort_key=7,
        population="ITT Population",
        placeholder_columns=["Estimand Strategy", "Intercurrent Event Handling",
                             "Difference", "95% CI", "p-value"],
        shell_rows=[
            ['Composite', 'XX', 'XX', 'XX', 'XX'],
            ['Hypothetical', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX']
        ],
        footnotes=["Estimand strategies per ICH E9(R1)."],
        dataset_source="ADSL, ADEFF", program_ref="t_estimand_sens.sas",
    ))

    items.append(TFLItem(
        id="T14.2.8", title="Time to Deterioration (TTD) — Quality of Life",
        tfl_type=T, section=S142, sort_key=8,
        population="ITT Population with PRO Data",
        placeholder_columns=["Parameter", "Treatment Group 1\n(N=xx)", "Treatment Group 2\n(N=xx)",
                             "HR [95% CI]", "p-value"],
        shell_rows=[
            ['Events / N', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX']
        ],
        footnotes=["TTD: time to first >=10-point decrease in EORTC QLQ-C30 GHS, "
                   "confirmed at next visit, or death."],
        dataset_source="ADSL, ADPRO", program_ref="t_ttd_qol.sas",
    ))

    # General efficacy figures
    items.append(TFLItem(
        id="F14.2.1", title="Forest Plot — Primary Endpoint by Subgroup",
        tfl_type=F, section=S142, sort_key=9,
        population="Intent-to-Treat (ITT) Population",
        figure_description="Forest plot: treatment effect [95% CI] per subgroup, overall diamond.",
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
        id="F14.2.3", title="Cumulative Distribution Function Plot",
        tfl_type=F, section=S142, sort_key=11,
        population="Intent-to-Treat (ITT) Population",
        figure_description="CDF plot: X=Change from Baseline, Y=Cumulative Proportion.",
        dataset_source="ADSL, ADEFF", program_ref="f_cdf_eff.sas",
        figure_type="cdf", figure_width_inches=5.5, figure_height_inches=3.2,
    ))

    # --- Oncology-Specific Efficacy ---
    items.append(TFLItem(
        id="T14.2.9", title="Tumor Response — Best Overall Response (BOR)",
        tfl_type=T, section=S142, sort_key=12, oncology_only=True,
        population="Intent-to-Treat (ITT) Population",
        placeholder_columns=["Best Overall Response",
                             "Treatment Group 1\n(N=xx) n (%)", "Treatment Group 2\n(N=xx) n (%)"],
        shell_rows=[
            ['Complete Response (CR)', 'XX', 'XX'],
            ['Partial Response (PR)', 'XX', 'XX'],
            ['Stable Disease (SD)', 'XX', 'XX'],
            ['Progressive Disease (PD)', 'XX', 'XX'],
            ['Not Evaluable (NE)', 'XX', 'XX']
        ],
        footnotes=["RECIST v1.1 by Independent Central Review (ICR). Confirmed responses only."],
        dataset_source="ADSL, ADRS", program_ref="t_bor.sas",
    ))

    items.append(TFLItem(
        id="T14.2.10", title="Tumor Response — Objective Response Rate (ORR)",
        tfl_type=T, section=S142, sort_key=13, oncology_only=True,
        population="Intent-to-Treat (ITT) Population",
        placeholder_columns=["Parameter", "Treatment Group 1\n(N=xx)", "Treatment Group 2\n(N=xx)",
                             "Odds Ratio [95% CI]", "p-value"],
        shell_rows=[
            ['95% CI', 'XX', 'XX', 'XX', 'XX'],
            ['Stratified CMH Test', 'XX', 'XX', 'XX', 'XX']
        ],
        footnotes=["95% CI via Clopper-Pearson exact method.",
                   "OR from stratified logistic regression."],
        dataset_source="ADSL, ADRS", program_ref="t_orr.sas",
    ))

    items.append(TFLItem(
        id="T14.2.11", title="Tumor Response — Disease Control Rate (DCR)",
        tfl_type=T, section=S142, sort_key=14, oncology_only=True,
        population="Intent-to-Treat (ITT) Population",
        placeholder_columns=["Parameter", "Treatment Group 1\n(N=xx)", "Treatment Group 2\n(N=xx)"],
        shell_rows=[
            ['95% CI', 'XX', 'XX']
        ],
        footnotes=["SD must be maintained for >=6 weeks from first dose."],
        dataset_source="ADSL, ADRS", program_ref="t_dcr.sas",
    ))

    items.append(TFLItem(
        id="T14.2.12", title="Tumor Response — Duration of Response (DOR)",
        tfl_type=T, section=S142, sort_key=15, oncology_only=True,
        population="Responders (Confirmed CR or PR)",
        placeholder_columns=["Parameter", "Treatment Group 1\n(N=xx)", "Treatment Group 2\n(N=xx)"],
        shell_rows=[
            ['Median DOR (months)', 'XX', 'XX', 'XX'],
            ['95% CI', 'XX', 'XX', 'XX'],
            ['KM rate at 12 months', 'XX', 'XX', 'XX']
        ],
        footnotes=["KM method; median via Brookmeyer-Crowley. Censored at last "
                   "adequate tumor assessment for alive+progression-free responders."],
        dataset_source="ADSL, ADRS, ADTTE", program_ref="t_dor.sas",
    ))

    items.append(TFLItem(
        id="T14.2.13", title="Tumor Response — Time to Response (TTR)",
        tfl_type=T, section=S142, sort_key=16, oncology_only=True,
        population="Responders (Confirmed CR or PR)",
        placeholder_columns=["Parameter", "Treatment Group 1\n(N=xx)", "Treatment Group 2\n(N=xx)"],
        shell_rows=[
            ['Median (Min, Max)', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADRS", program_ref="t_ttr.sas",
    ))

    items.append(TFLItem(
        id="T14.2.14", title="Progression-Free Survival (PFS) — Primary Analysis",
        tfl_type=T, section=S142, sort_key=17, oncology_only=True,
        population="Intent-to-Treat (ITT) Population",
        placeholder_columns=["Parameter", "Treatment Group 1\n(N=xx)", "Treatment Group 2\n(N=xx)"],
        shell_rows=[
            ['Median PFS (months)', 'XX', 'XX', 'XX'],
            ['95% CI', 'XX', 'XX', 'XX'],
            ['Hazard Ratio (95% CI)', 'XX', 'XX', 'XX'],
            ['p-value (stratified log-rank)', 'XX', 'XX', 'XX']
        ],
        footnotes=["PFS: time from randomization to PD (RECIST 1.1, ICR) or death.",
                   "Stratified Cox model and log-rank test by baseline stratification factors."],
        dataset_source="ADSL, ADTTE", program_ref="t_pfs_primary.sas",
    ))

    items.append(TFLItem(
        id="T14.2.15", title="Overall Survival (OS) — Primary Analysis",
        tfl_type=T, section=S142, sort_key=18, oncology_only=True,
        population="Intent-to-Treat (ITT) Population",
        placeholder_columns=["Parameter", "Treatment Group 1\n(N=xx)", "Treatment Group 2\n(N=xx)"],
        shell_rows=[
            ['Median OS (months)', 'XX', 'XX', 'XX'],
            ['95% CI', 'XX', 'XX', 'XX'],
            ['Hazard Ratio (95% CI)', 'XX', 'XX', 'XX'],
            ['p-value (stratified log-rank)', 'XX', 'XX', 'XX']
        ],
        footnotes=["OS: time from randomization to death from any cause. NR=Not Reached."],
        dataset_source="ADSL, ADTTE", program_ref="t_os_primary.sas",
    ))

    items.append(TFLItem(
        id="T14.2.16", title="PFS — Sensitivity Analysis",
        tfl_type=T, section=S142, sort_key=19, oncology_only=True,
        population="Intent-to-Treat (ITT) Population",
        placeholder_columns=["Analysis", "Med PFS A\n(mo)", "Med PFS B\n(mo)",
                             "HR [95% CI]", "p-value"],
        shell_rows=[
            ['Investigator Assessment', 'XX', 'XX', 'XX', 'XX'],
            ['PP Population', 'XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADTTE", program_ref="t_pfs_sensitivity.sas",
    ))

    items.append(TFLItem(
        id="T14.2.17", title="PFS — Subgroup Analysis",
        tfl_type=T, section=S142, sort_key=20, oncology_only=True,
        population="Intent-to-Treat (ITT) Population",
        placeholder_columns=["Subgroup", "Level", "Treatment A\nn/N, Med PFS",
                             "Treatment B\nn/N, Med PFS", "HR [95% CI]", "Interaction p"],
        shell_rows=[
            ['PD-L1 TPS', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADTTE", program_ref="t_pfs_subgroup.sas",
    ))

    items.append(TFLItem(
        id="T14.2.18", title="OS — Subgroup Analysis",
        tfl_type=T, section=S142, sort_key=21, oncology_only=True,
        population="Intent-to-Treat (ITT) Population",
        placeholder_columns=["Subgroup", "Level", "Treatment A\nn/N, Med OS",
                             "Treatment B\nn/N, Med OS", "HR [95% CI]", "Interaction p"],
        shell_rows=[
            ['Age <65', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['Male', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADTTE", program_ref="t_os_subgroup.sas",
    ))

    items.append(TFLItem(
        id="T14.2.19", title="Summary of Target Lesion Changes from Baseline",
        tfl_type=T, section=S142, sort_key=22, oncology_only=True,
        population="ITT with Measurable Disease and Post-Baseline Assessment",
        placeholder_columns=["Parameter", "Treatment A\n(N=145)", "Treatment B\n(N=145)"],
        shell_rows=[
            ['Median (Range)', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADRS", program_ref="t_target_lesion.sas",
    ))

    # Oncology figures — reduced sizes
    items.append(TFLItem(
        id="F14.2.4", title="Waterfall Plot — Best Percentage Change in Target Lesions",
        tfl_type=F, section=S142, sort_key=23, oncology_only=True,
        population="ITT with Measurable Disease and Post-Baseline Assessment",
        figure_description="Waterfall: best % change per subject, BOR-colored, ref lines at +20%/-30%.",
        dataset_source="ADSL, ADRS", program_ref="f_waterfall.sas",
        figure_type="waterfall", figure_width_inches=6.5, figure_height_inches=3.5,
    ))

    items.append(TFLItem(
        id="F14.2.5", title="Spider Plot — Percentage Change in Tumor Burden Over Time",
        tfl_type=F, section=S142, sort_key=24, oncology_only=True,
        population="ITT with Measurable Disease",
        figure_description="Spider plot: % change trajectories, BOR-colored, PD/death markers.",
        dataset_source="ADSL, ADRS", program_ref="f_spider.sas",
        figure_type="spider", figure_width_inches=6, figure_height_inches=3.5,
    ))

    items.append(TFLItem(
        id="F14.2.6", title="Swimmer Plot — Duration of Treatment and Response",
        tfl_type=F, section=S142, sort_key=25, oncology_only=True,
        population="Safety Population",
        figure_description="Swimmer: treatment duration bars, response/progression/ongoing markers.",
        dataset_source="ADSL, ADEX, ADRS", program_ref="f_swimmer.sas",
        figure_type="swimmer", figure_width_inches=6.5, figure_height_inches=4,
    ))

    items.append(TFLItem(
        id="F14.2.7", title="Kaplan-Meier Plot — Progression-Free Survival",
        tfl_type=F, section=S142, sort_key=26, oncology_only=True,
        population="Intent-to-Treat (ITT) Population",
        figure_description="KM PFS: step-function curves, + censoring, number-at-risk table, HR annotation.",
        dataset_source="ADSL, ADTTE", program_ref="f_km_pfs.sas",
        figure_type="km_curve", figure_width_inches=6, figure_height_inches=3.5,
    ))

    items.append(TFLItem(
        id="F14.2.8", title="Kaplan-Meier Plot — Overall Survival",
        tfl_type=F, section=S142, sort_key=27, oncology_only=True,
        population="Intent-to-Treat (ITT) Population",
        figure_description="KM OS: step-function curves, + censoring, number-at-risk table, HR annotation.",
        dataset_source="ADSL, ADTTE", program_ref="f_km_os.sas",
        figure_type="km_curve", figure_width_inches=6, figure_height_inches=3.5,
    ))

    items.append(TFLItem(
        id="F14.2.9", title="Forest Plot — PFS by Subgroup",
        tfl_type=F, section=S142, sort_key=28, oncology_only=True,
        population="Intent-to-Treat (ITT) Population",
        figure_description="Forest PFS: HR [95% CI] per subgroup, overall diamond.",
        dataset_source="ADSL, ADTTE", program_ref="f_forest_pfs.sas",
        figure_type="forest", figure_width_inches=6, figure_height_inches=3.5,
    ))

    items.append(TFLItem(
        id="F14.2.10", title="Forest Plot — OS by Subgroup",
        tfl_type=F, section=S142, sort_key=29, oncology_only=True,
        population="Intent-to-Treat (ITT) Population",
        figure_description="Forest OS: HR [95% CI] per subgroup, overall diamond.",
        dataset_source="ADSL, ADTTE", program_ref="f_forest_os.sas",
        figure_type="forest", figure_width_inches=6, figure_height_inches=3.5,
    ))

    items.append(TFLItem(
        id="T14.2.20", title="Landmark Analysis of OS by 6-Month PFS Status",
        tfl_type=T, section=S142, sort_key=30, oncology_only=True,
        population="ITT Alive and On-Study at 6 Months",
        placeholder_columns=["PFS Status at 6M", "Treatment A\nn/N, Med OS",
                             "Treatment B\nn/N, Med OS", "HR [95% CI]"],
        shell_rows=[
            ['Progression-Free at 6M', 'XX', 'XX', 'XX'],
            ['Progressed by 6M', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADTTE", program_ref="t_landmark_os.sas",
    ))

    items.append(TFLItem(
        id="T14.2.21", title="PK/PD Exposure-Response Correlation",
        tfl_type=T, section=S142, sort_key=31,
        population="PK/PD Evaluable Population",
        placeholder_columns=["PK Parameter", "Quartile", "N",
                             "Response Rate (%)", "95% CI"],
        shell_rows=[
            ['', 'XX', 'XX', 'XX', 'XX'],
            ['', 'XX', 'XX', 'XX', 'XX'],
            ['', 'XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADPK, ADEFF", program_ref="t_pkpd_corr.sas",
    ))

    items.append(TFLItem(
        id="T14.2.22", title="Time to First Subsequent Therapy (TFST)",
        tfl_type=T, section=S142, sort_key=32, oncology_only=True,
        population="ITT Population",
        placeholder_columns=["Parameter", "Treatment Group 1\n(N=xx)", "Treatment Group 2\n(N=xx)",
                             "HR [95% CI]", "p-value"],
        shell_rows=[
            ['Median TFST (months)', 'XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADTTE, ADCM", program_ref="t_tfst.sas",
    ))

    # =====================================================================
    # 14.3 SAFETY ANALYSIS — Restructured per clinical practice
    # =====================================================================
    # Subsection markers in sort_key ranges:
    #   14.3.1 AE: sort_key 1-13
    #   14.3.2 Deaths: sort_key 14-15
    #   14.3.3 Labs: sort_key 16-22
    #   14.3.4 Vital Signs: sort_key 23-26
    #   14.3.5 ECG: sort_key 27-30

    AE_SOC_PT_COLS = ["System Organ Class\nPreferred Term",
                       "Treatment Group 1\n(N=xx) n (%) [E]",
                       "Treatment Group 2\n(N=xx) n (%) [E]"]
    AE_GRADE_COLS = ["System Organ Class\nPreferred Term",
                      "Grade 1\nn (%)", "Grade 2\nn (%)", "Grade 3\nn (%)",
                      "Grade 4\nn (%)", "Grade 5\nn (%)", "Any Grade\nn (%)"]

    items.append(TFLItem(
        id="T14.3.1", title="Overall Summary of Treatment-Emergent Adverse Events",
        tfl_type=T, section=S143, sort_key=1,
        population="Safety Population",
        placeholder_columns=["Adverse Event Category",
                             "Treatment Group 1\n(N=xx) n (%) [E]",
                             "Treatment Group 2\n(N=xx) n (%) [E]"],
        shell_rows=[
            ['Any TEAE', 'XX', 'XX'],
            ['Drug-Related TEAE', 'XX', 'XX'],
            ['CTCAE Grade >=3 TEAE', 'XX', 'XX'],
            ['Serious TEAE (SAE)', 'XX', 'XX'],
            ['TEAE Leading to Discontinuation', 'XX', 'XX'],
            ['TEAE Leading to Dose Reduction/Interruption', 'XX', 'XX'],
            ['Fatal TEAE (Grade 5)', 'XX', 'XX']
        ],
        footnotes=["TEAE: AE with onset on/after first dose through 30 days after last dose.",
                   "CTCAE v5.0. MedDRA 26.0."],
        dataset_source="ADSL, ADAE", program_ref="t_ae_overview.sas",
        dictionary_versions={"MedDRA": "26.0", "CTCAE": "5.0"},
    ))

    items.append(TFLItem(
        id="T14.3.2", title="TEAEs by System Organ Class and Preferred Term (>=5% in Any Arm)",
        tfl_type=T, section=S143, sort_key=2,
        population="Safety Population",
        placeholder_columns=[c.replace(" [E]", "\n[Events]") if " [E]" in c else c for c in AE_SOC_PT_COLS],
        shell_rows=[
            ['Any TEAE', 'XX', 'XX'],
            ['Gastrointestinal disorders', 'XX', 'XX'],
            ['  Nausea', 'XX', 'XX'],
            ['  Diarrhea', 'XX', 'XX'],
            ['  Vomiting', 'XX', 'XX'],
            ['  Constipation', 'XX', 'XX'],
            ['General disorders', 'XX', 'XX'],
            ['  Fatigue', 'XX', 'XX'],
            ['  Asthenia', 'XX', 'XX'],
            ['XX', 'XX', 'XX']
        ],
        footnotes=["Sorted alphabetically by SOC; PTs by descending frequency in Treatment A.",
                   "[E]=total events. MedDRA 26.0. CTCAE v5.0."],
        dataset_source="ADSL, ADAE", program_ref="t_ae_soc_pt.sas",
        dictionary_versions={"MedDRA": "26.0", "CTCAE": "5.0"},
    ))

    items.append(TFLItem(
        id="T14.3.3", title="TEAEs by SOC, PT, and Maximum CTCAE Grade (Treatment A)",
        tfl_type=T, section=S143, sort_key=3,
        population="Safety Population",
        placeholder_columns=AE_GRADE_COLS,
        shell_rows=[
            ['Any TEAE (N=xx)', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['Gastrointestinal disorders', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['  Nausea', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['  Diarrhea', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['  Vomiting', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        footnotes=["CTCAE v5.0. Each subject counted once per PT at highest grade experienced.",
                   "Table repeated for Treatment B."],
        dataset_source="ADSL, ADAE", program_ref="t_ae_grade.sas",
        dictionary_versions={"MedDRA": "26.0", "CTCAE": "5.0"},
    ))

    items.append(TFLItem(
        id="T14.3.4", title="Drug-Related TEAEs by SOC, PT, and Relationship",
        tfl_type=T, section=S143, sort_key=4,
        population="Safety Population",
        placeholder_columns=["System Organ Class\nPreferred Term",
                             "Treatment Group 1\n(N=xx) n (%)", "Treatment Group 2\n(N=xx) n (%)"],
        shell_rows=[
            ['Gastrointestinal disorders', 'XX', 'XX'],
            ['  Nausea', 'XX', 'XX'],
            ['  Diarrhea', 'XX', 'XX'],
            ['  Vomiting', 'XX', 'XX'],
            ['General disorders', 'XX', 'XX'],
            ['  Fatigue', 'XX', 'XX'],
            ['XX', 'XX', 'XX']
        ],
        footnotes=["Drug-related = investigator-assessed 'Related' or 'Reasonably Possible'."],
        dataset_source="ADSL, ADAE", program_ref="t_ae_related.sas",
        dictionary_versions={"MedDRA": "26.0"},
    ))

    items.append(TFLItem(
        id="T14.3.5", title="Serious Adverse Events by SOC and PT",
        tfl_type=T, section=S143, sort_key=5,
        population="Safety Population",
        placeholder_columns=["System Organ Class\nPreferred Term",
                             "Treatment Group 1\n(N=xx) n (%) [E]",
                             "Treatment Group 2\n(N=xx) n (%) [E]"],
        shell_rows=[
            ['Any SAE', 'XX', 'XX'],
            ['Infections and infestations', 'XX', 'XX'],
            ['  Pneumonia', 'XX', 'XX'],
            ['  Sepsis', 'XX', 'XX'],
            ['Respiratory disorders', 'XX', 'XX'],
            ['XX', 'XX', 'XX']
        ],
        footnotes=["SAE defined per ICH E2A criteria. [E]=total events."],
        dataset_source="ADSL, ADAE", program_ref="t_sae_soc_pt.sas",
        dictionary_versions={"MedDRA": "26.0"},
    ))

    items.append(TFLItem(
        id="T14.3.6", title="TEAEs Leading to Treatment Discontinuation by SOC and PT",
        tfl_type=T, section=S143, sort_key=6,
        population="Safety Population",
        placeholder_columns=["System Organ Class\nPreferred Term",
                             "Treatment Group 1\n(N=xx) n (%)", "Treatment Group 2\n(N=xx) n (%)"],
        shell_rows=[
            ['Gastrointestinal disorders', 'XX', 'XX'],
            ['  Nausea', 'XX', 'XX'],
            ['  Diarrhea', 'XX', 'XX'],
            ['Skin disorders', 'XX', 'XX'],
            ['  Rash', 'XX', 'XX'],
            ['XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADAE", program_ref="t_ae_disc.sas",
        dictionary_versions={"MedDRA": "26.0"},
    ))

    items.append(TFLItem(
        id="T14.3.7", title="TEAEs Leading to Dose Reduction or Interruption by SOC and PT",
        tfl_type=T, section=S143, sort_key=7,
        population="Safety Population",
        placeholder_columns=["System Organ Class\nPreferred Term",
                             "Treatment Group 1\n(N=xx) n (%)", "Treatment Group 2\n(N=xx) n (%)"],
        shell_rows=[
            ['Gastrointestinal disorders', 'XX', 'XX'],
            ['  Diarrhea', 'XX', 'XX'],
            ['  Nausea', 'XX', 'XX'],
            ['General disorders', 'XX', 'XX'],
            ['  Fatigue', 'XX', 'XX'],
            ['XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADAE", program_ref="t_ae_dose_mod.sas",
        dictionary_versions={"MedDRA": "26.0"},
    ))

    items.append(TFLItem(
        id="T14.3.8", title="TEAEs Leading to Death (Grade 5)",
        tfl_type=T, section=S143, sort_key=8,
        population="Safety Population",
        placeholder_columns=["Subject ID", "Arm", "Preferred Term\n(Cause of Death)",
                             "Days from\nFirst Dose", "Relationship\nto Study Drug"],
        shell_rows=[
            ['02005', 'XX', 'XX', 'XX', 'XX'],
            ['01015', 'XX', 'XX', 'XX', 'XX'],
            ['02012', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX']
        ],
        footnotes=["All Grade 5 TEAEs. Relationship assessed by investigator."],
        dataset_source="ADSL, ADAE", program_ref="l_ae_death.sas",
        dictionary_versions={"MedDRA": "26.0", "CTCAE": "5.0"},
    ))

    items.append(TFLItem(
        id="T14.3.9", title="TEAEs Occurring in >=5% of Subjects by PT",
        tfl_type=T, section=S143, sort_key=9,
        population="Safety Population",
        placeholder_columns=["Preferred Term",
                             "Treatment Group 1\n(N=xx) n (%)", "Treatment Group 2\n(N=xx) n (%)"],
        shell_rows=[
            ['Nausea', 'XX', 'XX'],
            ['Diarrhea', 'XX', 'XX'],
            ['Asthenia', 'XX', 'XX'],
            ['Vomiting', 'XX', 'XX'],
            ['Rash', 'XX', 'XX'],
            ['Headache', 'XX', 'XX'],
            ['Constipation', 'XX', 'XX'],
            ['XX', 'XX', 'XX']
        ],
        footnotes=["Sorted by descending frequency in Treatment A. MedDRA 26.0."],
        dataset_source="ADSL, ADAE", program_ref="t_ae_5pct.sas",
        dictionary_versions={"MedDRA": "26.0"},
    ))

    items.append(TFLItem(
        id="T14.3.10", title="TEAEs by Cycle / Treatment Period",
        tfl_type=T, section=S143, sort_key=10,
        population="Safety Population",
        placeholder_columns=["Cycle", "N at Risk\n(A / B)",
                             "Treatment A\n>=1 TEAE n (%)", "Treatment B\n>=1 TEAE n (%)"],
        shell_rows=[
            ['Cycle 2', 'XX', 'XX', 'XX'],
            ['Cycle 3', 'XX', 'XX', 'XX'],
            ['Cycle 4', 'XX', 'XX', 'XX'],
            ['Cycle 5', 'XX', 'XX', 'XX'],
            ['Cycle 6+', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADAE, ADEX", program_ref="t_ae_by_cycle.sas",
        dictionary_versions={"MedDRA": "26.0", "CTCAE": "5.0"},
    ))

    items.append(TFLItem(
        id="T14.3.11", title="Exposure-Adjusted TEAE Incidence Rates (per 100 Patient-Years)",
        tfl_type=T, section=S143, sort_key=11,
        population="Safety Population",
        placeholder_columns=["Preferred Term",
                             "Treatment A\nRate [95% CI]",
                             "Treatment B\nRate [95% CI]"],
        shell_rows=[
            ['Fatigue', 'XX', 'XX'],
            ['Nausea', 'XX', 'XX'],
            ['Diarrhea', 'XX', 'XX'],
            ['XX', 'XX', 'XX']
        ],
        footnotes=["Exposure-adjusted rate = (n subjects with event / total PY exposure) × 100.",
                   "95% CI via exact method based on Poisson distribution."],
        dataset_source="ADSL, ADAE, ADEX", program_ref="t_ae_adj_rate.sas",
        dictionary_versions={"MedDRA": "26.0"},
    ))

    items.append(TFLItem(
        id="T14.3.12", title="TEAEs by Age Group Subgroup (>=5% in Any Arm)",
        tfl_type=T, section=S143, sort_key=12,
        population="Safety Population",
        placeholder_columns=["Preferred Term",
                             "Age <65\n(N=xx) n (%)", "Age >=65\n(N=xx) n (%)",
                             "Age >=75\n(N=xx) n (%)"],
        shell_rows=[
            ['Nausea', 'XX', 'XX', 'XX'],
            ['Diarrhea', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADAE", program_ref="t_ae_age.sas",
        dictionary_versions={"MedDRA": "26.0"},
    ))

    items.append(TFLItem(
        id="T14.3.13", title="TEAEs by Sex Subgroup (>=5% in Any Arm)",
        tfl_type=T, section=S143, sort_key=13,
        population="Safety Population",
        placeholder_columns=["Preferred Term",
                             "Male\n(N=xx) n (%)", "Female\n(N=xx) n (%)"],
        shell_rows=[
            ['Nausea', 'XX', 'XX'],
            ['XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADAE", program_ref="t_ae_sex.sas",
        dictionary_versions={"MedDRA": "26.0"},
    ))

    items.append(TFLItem(
        id="T14.3.14", title="Listing of All Deaths with Narrative Reference",
        tfl_type=T, section=S143, sort_key=14,
        population="All Randomized Subjects",
        placeholder_columns=["Subject", "Arm", "Date of\nDeath",
                             "Days from\nFirst Dose", "Days from\nLast Dose",
                             "Primary Cause\nof Death", "Narrative\nID"],
        shell_rows=[
            ['02005', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['01015', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        footnotes=["All deaths regardless of causality. Narrative cross-references Section 12.2."],
        dataset_source="ADSL, ADAE, ADTTE", program_ref="l_deaths.sas",
    ))

    items.append(TFLItem(
        id="T14.3.15", title="Hy's Law Cases — Liver Chemistry Screening",
        tfl_type=T, section=S143, sort_key=15,
        population="Safety Population with Baseline and Post-Baseline Labs",
        placeholder_columns=["Subject", "Arm", "ALT\n(xULN)", "AST\n(xULN)",
                             "TBL\n(xULN)", "ALP\n(xULN)", "Hy's Law\nMet?"],
        shell_rows=[
            ['02015', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        footnotes=["Hy's Law: ALT/AST >=3xULN, TBL >=2xULN, ALP <2xULN, no alternative cause."],
        dataset_source="ADSL, ADLB", program_ref="t_hys_law.sas",
    ))

    items.append(TFLItem(
        id="T14.3.16", title="Laboratory Parameters — Shift Table (Baseline to Worst Post-Baseline)",
        tfl_type=T, section=S143, sort_key=16,
        population="Safety Population",
        placeholder_columns=["Parameter\n(Unit)", "Baseline\nGrade",
                             "Worst Post-BL\nGrade", "Treatment Group 1\nn (%)",
                             "Treatment Group 2\nn (%)"],
        shell_rows=[
            ['', 'XX', 'XX', 'XX', 'XX'],
            ['', 'XX', 'XX', 'XX', 'XX'],
            ['ALT (U/L)', 'XX', 'XX', 'XX', 'XX'],
            ['', 'XX', 'XX', 'XX', 'XX'],
            ['', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX']
        ],
        footnotes=["CTCAE v5.0 grading. Baseline = last value on/before first dose.",
                   "Worst post-baseline = furthest from normal range."],
        dataset_source="ADSL, ADLB", program_ref="t_lab_shift.sas",
        dictionary_versions={"CTCAE": "5.0"},
    ))

    items.append(TFLItem(
        id="T14.3.17", title="Hematology Parameters — Summary Statistics by Visit",
        tfl_type=T, section=S143, sort_key=17,
        population="Safety Population",
        placeholder_columns=["Parameter\nVisit", "Statistic",
                             "Treatment Group 1\n(N=xx)", "Treatment Group 2\n(N=xx)"],
        shell_rows=[
            ['  Baseline', 'XX', 'XX', 'XX'],
            ['', 'XX', 'XX', 'XX'],
            ['  Week 4', 'XX', 'XX', 'XX'],
            ['', 'XX', 'XX', 'XX'],
            ['Platelets (×10⁹/L)', 'XX', 'XX', 'XX'],
            ['  Baseline', 'XX', 'XX', 'XX'],
            ['  Week 4', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADLB", program_ref="t_heme_by_visit.sas",
    ))

    items.append(TFLItem(
        id="T14.3.18", title="Clinical Chemistry Parameters — Summary Statistics by Visit",
        tfl_type=T, section=S143, sort_key=18,
        population="Safety Population",
        placeholder_columns=["Parameter\nVisit", "Statistic",
                             "Treatment Group 1\n(N=xx)", "Treatment Group 2\n(N=xx)"],
        shell_rows=[
            ['  Baseline', 'XX', 'XX', 'XX'],
            ['  Week 4', 'XX', 'XX', 'XX'],
            ['AST (U/L)', 'XX', 'XX', 'XX'],
            ['  Baseline', 'XX', 'XX', 'XX'],
            ['  Week 4', 'XX', 'XX', 'XX'],
            ['Total Bilirubin (mg/dL)', 'XX', 'XX', 'XX'],
            ['  Baseline', 'XX', 'XX', 'XX'],
            ['Creatinine (mg/dL)', 'XX', 'XX', 'XX'],
            ['  Baseline', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADLB", program_ref="t_chem_by_visit.sas",
    ))

    items.append(TFLItem(
        id="T14.3.19", title="Laboratory Abnormalities — Grade >=3 Listing",
        tfl_type=T, section=S143, sort_key=19,
        population="Safety Population",
        placeholder_columns=["Subject", "Arm", "Visit", "Parameter",
                             "Result", "Unit", "ULN", "CTCAE\nGrade"],
        shell_rows=[
            ['01012', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['02005', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADLB", program_ref="l_lab_grade3.sas",
        dictionary_versions={"CTCAE": "5.0"},
    ))

    items.append(TFLItem(
        id="T14.3.20", title="Laboratory Toxicity Grade Shift Over Time (by Cycle)",
        tfl_type=T, section=S143, sort_key=20,
        population="Safety Population",
        placeholder_columns=["Parameter", "Cycle", "Baseline\nGrade",
                             "Max Post-BL\nGrade", "Treatment A\nn/N (%)",
                             "Treatment B\nn/N (%)"],
        shell_rows=[
            ['', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['ALT', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADLB", program_ref="t_lab_shift_cycle.sas",
        dictionary_versions={"CTCAE": "5.0"},
    ))

    items.append(TFLItem(
        id="F14.3.1", title="Mean (+/- SD) Change in Laboratory Parameters Over Time",
        tfl_type=F, section=S143, sort_key=21,
        population="Safety Population",
        figure_description="Multi-panel line plot: mean ± SD change in Hgb, Plt, ANC, ALT, AST, Creatinine.",
        dataset_source="ADSL, ADLB", program_ref="f_lab_longitudinal.sas",
        figure_type="longitudinal", figure_width_inches=6, figure_height_inches=4,
    ))

    items.append(TFLItem(
        id="F14.3.2", title="Box Plot — Liver Function Tests by Visit",
        tfl_type=F, section=S143, sort_key=22,
        population="Safety Population",
        figure_description="Box plots: ALT, AST, ALP, TBL by visit, side-by-side arms, ULN reference.",
        dataset_source="ADSL, ADLB", program_ref="f_lft_box.sas",
        figure_type="box_plot", figure_width_inches=6, figure_height_inches=4,
    ))

    items.append(TFLItem(
        id="T14.3.21", title="Vital Signs — Summary Statistics by Visit",
        tfl_type=T, section=S143, sort_key=23,
        population="Safety Population",
        placeholder_columns=["Parameter\nVisit", "Statistic",
                             "Treatment Group 1\n(N=xx)", "Treatment Group 2\n(N=xx)"],
        shell_rows=[
            ['Systolic BP (mmHg)', 'XX', 'XX', 'XX'],
            ['  Baseline', 'XX', 'XX', 'XX'],
            ['  Week 4', 'XX', 'XX', 'XX'],
            ['Diastolic BP (mmHg)', 'XX', 'XX', 'XX'],
            ['  Baseline', 'XX', 'XX', 'XX'],
            ['Heart Rate (bpm)', 'XX', 'XX', 'XX'],
            ['  Baseline', 'XX', 'XX', 'XX'],
            ['Temperature (°C)', 'XX', 'XX', 'XX'],
            ['  Baseline', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADVS", program_ref="t_vs_by_visit.sas",
    ))

    items.append(TFLItem(
        id="T14.3.22", title="Vital Signs — Clinically Notable Abnormalities by Visit",
        tfl_type=T, section=S143, sort_key=24,
        population="Safety Population",
        placeholder_columns=["Parameter", "Criterion", "Visit",
                             "Treatment Group 1\nn (%)", "Treatment Group 2\nn (%)"],
        shell_rows=[
            ['SBP', 'XX', 'XX', 'XX', 'XX'],
            ['DBP', 'XX', 'XX', 'XX', 'XX'],
            ['HR', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADVS", program_ref="t_vs_notable.sas",
    ))

    items.append(TFLItem(
        id="F14.3.3", title="Mean (+/- SD) Vital Signs Over Time",
        tfl_type=F, section=S143, sort_key=25,
        population="Safety Population",
        figure_description="Multi-panel: mean ± SD of SBP, DBP, HR, Weight over visits.",
        dataset_source="ADSL, ADVS", program_ref="f_vs_longitudinal.sas",
        figure_type="longitudinal", figure_width_inches=6, figure_height_inches=4,
    ))

    items.append(TFLItem(
        id="F14.3.4", title="Liver Function Panel — Mean Over Time with ULN Reference",
        tfl_type=F, section=S143, sort_key=26,
        population="Safety Population",
        figure_description="Line plot: ALT, AST, ALP, TBL means over visits with ULN lines.",
        dataset_source="ADSL, ADLB", program_ref="f_lft_uln.sas",
        figure_type="longitudinal", figure_width_inches=5.5, figure_height_inches=3.5,
    ))

    items.append(TFLItem(
        id="T14.3.23", title="ECG Parameters — Summary Statistics by Visit",
        tfl_type=T, section=S143, sort_key=27,
        population="Safety Population with ECG Data",
        placeholder_columns=["Parameter\nVisit", "Statistic",
                             "Treatment Group 1\n(N=xx)", "Treatment Group 2\n(N=xx)"],
        shell_rows=[
            ['QTcF (ms)', 'XX', 'XX', 'XX'],
            ['  Baseline', 'XX', 'XX', 'XX'],
            ['  Week 4', 'XX', 'XX', 'XX'],
            ['', 'XX', 'XX', 'XX'],
            ['QRS Duration (ms)', 'XX', 'XX', 'XX'],
            ['  Baseline', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX']
        ],
        footnotes=["QTcF = Fridericia correction. Triplicate ECGs at each visit; mean analyzed."],
        dataset_source="ADSL, ADEG", program_ref="t_ecg_by_visit.sas",
    ))

    items.append(TFLItem(
        id="T14.3.24", title="ECG QTcF Categorical Analysis",
        tfl_type=T, section=S143, sort_key=28,
        population="Safety Population with ECG Data",
        placeholder_columns=["QTcF Category", "Treatment Group 1\n(N=xx) n (%)",
                             "Treatment Group 2\n(N=xx) n (%)"],
        shell_rows=[
            ['  <=450 ms', 'XX', 'XX'],
            ['  >450-480 ms', 'XX', 'XX'],
            ['  >480-500 ms', 'XX', 'XX'],
            ['  >500 ms', 'XX', 'XX'],
            ['Change from Baseline', 'XX', 'XX'],
            ['  <=30 ms increase', 'XX', 'XX'],
            ['  >30-60 ms increase', 'XX', 'XX'],
            ['  >60 ms increase', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADEG", program_ref="t_qtcf_cat.sas",
    ))

    items.append(TFLItem(
        id="T14.3.25", title="ECG Qualitative Assessment — Shift Table",
        tfl_type=T, section=S143, sort_key=29,
        population="Safety Population with ECG Data",
        placeholder_columns=["Baseline", "Worst\nPost-Baseline",
                             "Treatment Group 1\nn (%)", "Treatment Group 2\nn (%)"],
        shell_rows=[
            ['Normal', 'XX', 'XX', 'XX'],
            ['Normal', 'XX', 'XX', 'XX'],
            ['Abnormal NCS', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX']
        ],
        footnotes=["NCS = Not Clinically Significant. CS = Clinically Significant."],
        dataset_source="ADSL, ADEG", program_ref="t_ecg_shift.sas",
    ))

    items.append(TFLItem(
        id="T14.3.26", title="Infusion-Related Reactions by Preferred Term",
        tfl_type=T, section=S143, sort_key=30,
        population="Safety Population",
        placeholder_columns=["Preferred Term",
                             "Treatment Group 1\n(N=xx) n (%)", "Treatment Group 2\n(N=xx) n (%)"],
        shell_rows=[
            ['Pyrexia', 'XX', 'XX'],
            ['Chills', 'XX', 'XX'],
            ['Flushing', 'XX', 'XX'],
            ['XX', 'XX', 'XX']
        ],
        dictionary_versions={"MedDRA": "26.0", "CTCAE": "5.0"},
        dataset_source="ADSL, ADAE, ADEX", program_ref="t_irr.sas",
    ))

    # =====================================================================
    # 14.4 SPECIAL ASSESSMENTS (PK, Immuno, Biomarker, PRO)
    # =====================================================================

    items.append(TFLItem(
        id="T14.4.1", title="Summary of Pharmacokinetic Concentrations by Timepoint",
        tfl_type=T, section=S144, sort_key=1,
        population="PK Population",
        placeholder_columns=["Timepoint\n(h)", "Statistic",
                             "Treatment A\n(N=30)", "Treatment B\n(N=32)"],
        shell_rows=[
            ['Cmax (2h)', 'XX', 'XX', 'XX'],
            ['Cmin (24h)', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADPC", program_ref="t_pk_conc.sas",
    ))

    items.append(TFLItem(
        id="T14.4.2", title="Summary of PK Parameters by Subject",
        tfl_type=T, section=S144, sort_key=2,
        population="PK Population",
        placeholder_columns=["PK Parameter", "Statistic",
                             "Treatment A\n(N=30)", "Treatment B\n(N=32)"],
        shell_rows=[
            ['AUC0-tau (ng·h/mL)', 'XX', 'XX', 'XX'],
            ['AUC0-inf', 'XX', 'XX', 'XX'],
            ['Tmax (h)', 'XX', 'XX', 'XX'],
            ['t1/2 (h)', 'XX', 'XX', 'XX'],
            ['CL/F (L/h)', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADPP", program_ref="t_pk_params.sas",
    ))

    items.append(TFLItem(
        id="L14.4.1", title="Listing of Pharmacokinetic Concentrations by Subject and Timepoint",
        tfl_type=L, section=S144, sort_key=3,
        population="PK Population",
        placeholder_columns=["Subject", "Arm", "Cycle\nDay",
                             "Nominal\nTime (h)", "Actual\nTime (h)",
                             "Conc\n(ng/mL)", "BQL"],
        shell_rows=[
            ['01001', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['01001', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADPC", program_ref="l_pk_conc.sas",
    ))

    items.append(TFLItem(
        id="T14.4.3", title="Immunogenicity Summary — Anti-Drug Antibody (ADA) Incidence",
        tfl_type=T, section=S144, sort_key=4,
        population="Safety Population with ADA Samples",
        placeholder_columns=["ADA Parameter",
                             "Treatment Group 1\n(N=xx) n (%)", "Treatment Group 2\n(N=xx) n (%)"],
        shell_rows=[
            ['ADA Positive at Baseline', 'XX', 'XX'],
            ['ADA Positive Post-Baseline', 'XX', 'XX'],
            ['Treatment-Emergent ADA Positive', 'XX', 'XX'],
            ['Neutralizing Antibody Positive', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADIS", program_ref="t_ada_incidence.sas",
    ))

    items.append(TFLItem(
        id="L14.4.2", title="Listing of Immunogenicity Results by Subject and Visit",
        tfl_type=L, section=S144, sort_key=5,
        population="Safety Population with ADA Samples",
        placeholder_columns=["Subject", "Arm", "Visit", "ADA\nResult",
                             "ADA\nTiter", "Nab\nResult", "TE-ADA?"],
        shell_rows=[
            ['01005', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['01005', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADIS", program_ref="l_immuno.sas",
    ))

    items.append(TFLItem(
        id="T14.4.4", title="Summary of Biomarker Results by Visit",
        tfl_type=T, section=S144, sort_key=6,
        population="ITT Population with Biomarker Data",
        placeholder_columns=["Biomarker", "Visit", "Statistic",
                             "Treatment A\n(N=xx)", "Treatment B\n(N=xx)"],
        shell_rows=[
            ['', 'XX', 'XX', 'XX', 'XX'],
            ['', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADBM", program_ref="t_biomarker_visit.sas",
    ))

    items.append(TFLItem(
        id="L14.4.3", title="Listing of Biomarker Results by Subject and Visit",
        tfl_type=L, section=S144, sort_key=7,
        population="ITT with Biomarker Data",
        placeholder_columns=["Subject", "Arm", "Visit", "Biomarker",
                             "Result", "Unit", "Method"],
        shell_rows=[
            ['01001', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADBM", program_ref="l_biomarker.sas",
    ))

    items.append(TFLItem(
        id="T14.4.5", title="Summary of Patient-Reported Outcomes by Visit",
        tfl_type=T, section=S144, sort_key=8,
        population="ITT Population with PRO Data",
        placeholder_columns=["PRO Scale", "Visit", "Statistic",
                             "Treatment Group 1\n(N=xx)", "Treatment Group 2\n(N=xx)"],
        shell_rows=[
            ['', 'XX', 'XX', 'XX', 'XX'],
            ['', 'XX', 'XX', 'XX', 'XX'],
            ['EORTC QLQ-C30 PF', 'XX', 'XX', 'XX', 'XX'],
            ['', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADPRO", program_ref="t_pro_summary.sas",
    ))

    items.append(TFLItem(
        id="L14.4.4", title="Listing of Patient-Reported Outcomes by Subject and Visit",
        tfl_type=L, section=S144, sort_key=9,
        population="ITT with PRO Data",
        placeholder_columns=["Subject", "Arm", "Visit",
                             "GHS", "PF", "RF", "EF", "CF", "SF"],
        shell_rows=[
            ['01001', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADPRO", program_ref="l_pro.sas",
    ))
    # =====================================================================
    # 16.2 PATIENT DATA LISTINGS (APPENDICES)
    # ===================================================================== PATIENT DATA LISTINGS (Appendices) — 17 items
    # =====================================================================

    items.append(TFLItem(
        id="L16.2.1", title="Listing of Subject Disposition",
        tfl_type=L, section=S162, sort_key=1,
        population="All Randomized Subjects",
        placeholder_columns=["Site/\nSubject", "Arm", "Date\nRandomized",
                             "Date of\nFirst Dose", "Date of\nLast Dose",
                             "Completed\nTreatment?", "Reason for\nDiscontinuation",
                             "Completed\nStudy?"],
        shell_rows=[
            ['01/002', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL", program_ref="l_disposition.sas",
    ))

    items.append(TFLItem(
        id="L16.2.2", title="Listing of Demographic Data",
        tfl_type=L, section=S162, sort_key=2,
        population="All Randomized Subjects",
        placeholder_columns=["Site/\nSubject", "Arm", "Age\n(yrs)", "Sex",
                             "Race", "Ethnicity", "Height\n(cm)", "Weight\n(kg)", "BMI"],
        shell_rows=[
            ['01/002', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL", program_ref="l_demog.sas",
    ))

    items.append(TFLItem(
        id="L16.2.3", title="Listing of Protocol Deviations",
        tfl_type=L, section=S162, sort_key=3,
        population="All Randomized Subjects",
        placeholder_columns=["Site/\nSubject", "Arm", "Deviation\nCategory",
                             "Deviation Description", "Date of\nDeviation", "Major/\nMinor"],
        shell_rows=[
            ['02/015', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, DV", program_ref="l_protdev.sas",
    ))

    items.append(TFLItem(
        id="L16.2.4", title="Listing of Adverse Events",
        tfl_type=L, section=S162, sort_key=4,
        population="Safety Population",
        placeholder_columns=["Site/\nSubject", "Arm", "SOC", "Preferred\nTerm",
                             "Start\nDate", "End\nDate", "Grade",
                             "Rel", "SAE?", "Action", "Outcome"],
        shell_rows=[
            ['01/001', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADAE", program_ref="l_ae.sas",
        dictionary_versions={"MedDRA": "26.0", "CTCAE": "5.0"},
    ))

    items.append(TFLItem(
        id="L16.2.5", title="Listing of Serious Adverse Events",
        tfl_type=L, section=S162, sort_key=5,
        population="Safety Population",
        placeholder_columns=["Site/\nSubject", "Arm", "Preferred\nTerm",
                             "SAE\nCriteria", "Start\nDate", "End\nDate",
                             "Grade", "Rel", "Outcome", "Narrative\nRef"],
        shell_rows=[
            ['02/012', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADAE", program_ref="l_sae.sas",
        dictionary_versions={"MedDRA": "26.0", "CTCAE": "5.0"},
    ))

    items.append(TFLItem(
        id="L16.2.6", title="Listing of Concomitant Medications",
        tfl_type=L, section=S162, sort_key=6,
        population="Safety Population",
        placeholder_columns=["Site/\nSubject", "Arm", "ATC\nClass",
                             "Preferred\nName", "Indication",
                             "Dose / Route /\nFrequency", "Start\nDate", "End\nDate"],
        shell_rows=[
            ['01/003', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADCM", program_ref="l_conmed.sas",
        dictionary_versions={"WHO-DD": "2024Q1"},
    ))

    items.append(TFLItem(
        id="L16.2.7", title="Listing of Laboratory Data — Hematology and Chemistry",
        tfl_type=L, section=S162, sort_key=7,
        population="Safety Population",
        placeholder_columns=["Site/\nSubject", "Arm", "Visit", "Parameter",
                             "Result", "Unit", "Normal\nRange", "Flag"],
        shell_rows=[
            ['01/001', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['01/001', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADLB", program_ref="l_lab.sas",
    ))

    items.append(TFLItem(
        id="L16.2.8", title="Listing of Vital Signs",
        tfl_type=L, section=S162, sort_key=8,
        population="Safety Population",
        placeholder_columns=["Site/\nSubject", "Arm", "Visit", "Date",
                             "SBP\n(mmHg)", "DBP\n(mmHg)", "HR\n(bpm)",
                             "Resp\nRate", "Temp\n(°C)", "Weight\n(kg)"],
        shell_rows=[
            ['01/001', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADVS", program_ref="l_vitalsigns.sas",
    ))

    items.append(TFLItem(
        id="L16.2.9", title="Listing of ECG Data",
        tfl_type=L, section=S162, sort_key=9,
        population="Safety Population with ECG Data",
        placeholder_columns=["Site/\nSubject", "Arm", "Visit", "Date/\nTime",
                             "HR\n(bpm)", "PR\n(ms)", "QRS\n(ms)",
                             "QT\n(ms)", "QTcF\n(ms)", "Interpretation"],
        shell_rows=[
            ['01/001', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADEG", program_ref="l_ecg.sas",
    ))

    items.append(TFLItem(
        id="L16.2.10", title="Listing of Tumor Response Data",
        tfl_type=L, section=S162, sort_key=10, oncology_only=True,
        population="ITT Population",
        placeholder_columns=["Site/\nSubject", "Arm", "Visit", "Assessment\nDate",
                             "Target Sum\n(mm)", "% Change\nfrom BL",
                             "Non-Target\nStatus", "New\nLesions?", "Overall\nResponse", "BOR"],
        shell_rows=[
            ['01/001', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['01/001', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADRS", program_ref="l_tumor_response.sas",
    ))

    items.append(TFLItem(
        id="L16.2.11", title="Listing of Survival Data",
        tfl_type=L, section=S162, sort_key=11, oncology_only=True,
        population="ITT Population",
        placeholder_columns=["Site/\nSubject", "Arm", "Last\nContact",
                             "Vital\nStatus", "Death\nDate", "Primary Cause\nof Death",
                             "PFS Event\nDate", "PFS\nCensor"],
        shell_rows=[
            ['01/005', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADTTE", program_ref="l_survival.sas",
    ))

    items.append(TFLItem(
        id="L16.2.12", title="Listing of Study Drug Exposure and Dose Modifications",
        tfl_type=L, section=S162, sort_key=12,
        population="Safety Population",
        placeholder_columns=["Site/\nSubject", "Arm", "Cycle/\nDay",
                             "Planned\nDose", "Actual\nDose", "Modification\nReason"],
        shell_rows=[
            ['01/001', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADEX", program_ref="l_exposure.sas",
    ))

    items.append(TFLItem(
        id="L16.2.13", title="Listing of Medical History Verbatim vs. Coded Terms",
        tfl_type=L, section=S162, sort_key=13,
        population="Safety Population",
        placeholder_columns=["Site/\nSubject", "Arm", "SOC", "Preferred\nTerm",
                             "Verbatim\nTerm", "Start\nDate", "End\nDate", "Ongoing?"],
        shell_rows=[
            ['01/003', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADMH", program_ref="l_mh_coded.sas",
        dictionary_versions={"MedDRA": "26.0"},
    ))

    items.append(TFLItem(
        id="L16.2.14", title="Listing of PK Parameters by Subject",
        tfl_type=L, section=S162, sort_key=14,
        population="PK Population",
        placeholder_columns=["Site/\nSubject", "Arm", "Cycle",
                             "Cmax\n(ng/mL)", "AUC0-tau\n(ng·h/mL)",
                             "Tmax\n(h)", "t1/2\n(h)", "CL/F\n(L/h)"],
        shell_rows=[
            ['02/020', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADPP", program_ref="l_pk_params.sas",
    ))

    items.append(TFLItem(
        id="L16.2.15", title="Listing of ADA and Neutralizing Antibody Results",
        tfl_type=L, section=S162, sort_key=15,
        population="Safety Population with ADA Samples",
        placeholder_columns=["Site/\nSubject", "Arm", "Visit\n(Day)",
                             "ADA\nResult", "ADA\nTiter", "Nab\nResult"],
        shell_rows=[
            ['01/005', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['01/005', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADIS", program_ref="l_ada.sas",
    ))

    items.append(TFLItem(
        id="L16.2.16", title="Listing of Subsequent Anti-Cancer Therapies",
        tfl_type=L, section=S162, sort_key=16, oncology_only=True,
        population="ITT Population",
        placeholder_columns=["Site/\nSubject", "Arm", "Therapy\nName",
                             "Therapy\nClass", "Start\nDate", "End\nDate",
                             "Best Response\nto Subsequent Therapy"],
        shell_rows=[
            ['02/010', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADCM", program_ref="l_subsequent_therapy.sas",
    ))

    items.append(TFLItem(
        id="L16.2.17", title="Listing of PRO Assessments by Subject and Visit",
        tfl_type=L, section=S162, sort_key=17,
        population="ITT with PRO Data",
        placeholder_columns=["Site/\nSubject", "Arm", "Visit",
                             "GHS", "PF", "RF", "EF", "CF", "SF"],
        shell_rows=[
            ['01/001', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'],
            ['XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX']
        ],
        dataset_source="ADSL, ADPRO", program_ref="l_pro.sas",
    ))

    return TFLCatalog(items)
