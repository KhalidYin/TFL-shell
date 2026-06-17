"""Section 14.1 catalog definitions: demographics, disposition, baseline, and exposure shells."""

from tflshell.data.common import H2_NPCT, H2_SIMPLE, H2_SOCPT, EROW, S141, T, TFLItem

def build_14_1_items() -> list[TFLItem]:
    """Build Section 14.1 table shells as a self-contained catalog slice."""
    items: list[TFLItem] = []

    items.append(
        TFLItem(
            id="T14.1.1",
            title="Summary of Demographic Characteristics",
            tfl_type=T,
            section=S141,
            sort_key=1,
            population="Intent-to-Treat (ITT) Population",
            placeholder_columns=H2_SIMPLE,
            shell_rows=[
                {"label": "Age (years)", "bold": True},
                {"label": "  n", "indent": True, "values": ["xx", "xx", "...", "xx"]},
                {
                    "label": "  Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Median (Min, Max)",
                    "indent": True,
                    "values": ["xx.x (xx, xx)", "xx.x (xx, xx)", "...", "xx.x (xx, xx)"],
                },
                {"label": "Age Group", "bold": True},
                {
                    "label": "  < 65 years",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  >= 65 years",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "Sex", "bold": True},
                {
                    "label": "  Male",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Female",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "Race", "bold": True},
                {
                    "label": "  White",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Black or African American",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Asian",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Other",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "Ethnicity", "bold": True},
                {
                    "label": "  Hispanic or Latino",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Not Hispanic or Latino",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "Weight (kg)", "bold": True},
                {
                    "label": "  Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "Height (cm)", "bold": True},
                {
                    "label": "  Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "BMI (kg/m²)", "bold": True},
                {
                    "label": "  Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "Percentages based on number of subjects in each treatment group.",
                "Age calculated relative to date of informed consent.",
            ],
            dataset_source="ADSL",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_demog_summary.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.1.2",
            title="Summary of Baseline Oncology Disease Characteristics",
            tfl_type=T,
            section=S141,
            sort_key=2,
            population="Intent-to-Treat (ITT) Population",
            oncology_only=True,
            placeholder_columns=H2_SIMPLE,
            shell_rows=[
                ["ECOG Performance Status, n (%)", "", "", "", ""],
                ["  0 — Fully active", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                [
                    "  1 — Restricted in strenuous activity",
                    "xx (xx.x)",
                    "xx (xx.x)",
                    "...",
                    "xx (xx.x)",
                ],
                ["  2 — Ambulatory, unable to work", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["Disease Stage, n (%)", "", "", "", ""],
                ["  Stage III", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["  Stage IV", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["Time Since Initial Diagnosis (months)", "", "", "", ""],
                ["  Mean (SD)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                EROW,
            ],
            footnotes=[
                "Baseline = last non-missing assessment on/before first dose.",
                "ECOG PS: 0=Fully active, 1=Restricted, 2=Ambulatory, 3=Limited self-care, 4=Completely disabled.",
            ],
            dataset_source="ADSL, ADRS",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_baseline_chars.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.1.3",
            title="Summary of Medical History by System Organ Class and Preferred Term",
            tfl_type=T,
            section=S141,
            sort_key=3,
            population="Safety Population",
            placeholder_columns=H2_SOCPT,
            shell_rows=[
                {
                    "label": "Any Medical History Condition",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Vascular disorders",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Hypertension",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Hypotension",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Cardiac disorders",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Coronary Artery Disease",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Gastrointestinal disorders",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Gastroesophageal reflux disease",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Constipation",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Metabolism and nutrition disorders",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Diabetes mellitus",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Hyperlipidemia",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=["MedDRA version [xx.x] used for coding medical history terms."],
            dataset_source="ADMH",
            source_listing="L16.2.13",
            program_ref="t_mh_soc_pt.sas",
            dictionary_versions={"MedDRA": "[xx.x]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.1.4",
            title="Summary of Prior Medications by ATC Class and Preferred Name",
            tfl_type=T,
            section=S141,
            sort_key=4,
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
            dataset_source="ADCM",
            source_listing="L16.2.6",
            program_ref="t_prior_meds.sas",
            dictionary_versions={"WHO-DD": "[version]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.1.5",
            title="Subject Disposition",
            tfl_type=T,
            section=S141,
            sort_key=5,
            population="All Randomized Subjects",
            placeholder_columns=H2_NPCT,
            shell_rows=[
                {"label": "Subjects Screened", "values": ["xx", "xx", "...", "xx"]},
                {
                    "label": "Subjects Randomized",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Subjects Treated (>=1 dose)",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Completed Treatment",
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Discontinued Treatment",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Adverse Event",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Death",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Progressive Disease",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Withdrawal by Subject",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Physician Decision",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Protocol Violation",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Lost to Follow-up",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "Percentages: N=treated per arm for discontinuation reasons.",
                "Primary reason for discontinuation per CRF EOT page.",
            ],
            dataset_source="ADSL",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_disposition.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.1.6",
            title="Major Protocol Deviations",
            tfl_type=T,
            section=S141,
            sort_key=6,
            population="All Randomized Subjects",
            placeholder_columns=H2_NPCT,
            shell_rows=[
                ["Any Major Protocol Deviation", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                [
                    "Inclusion/Exclusion Criteria Not Met",
                    "xx (xx.x)",
                    "xx (xx.x)",
                    "...",
                    "xx (xx.x)",
                ],
                [
                    "Received Wrong Treatment/Incorrect Dose",
                    "xx (xx.x)",
                    "xx (xx.x)",
                    "...",
                    "xx (xx.x)",
                ],
                [
                    "Missed >=2 Consecutive Efficacy Assessments",
                    "xx (xx.x)",
                    "xx (xx.x)",
                    "...",
                    "xx (xx.x)",
                ],
                EROW,
            ],
            dataset_source="ADSL, DV",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_prot_dev.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.1.7",
            title="Analysis Populations",
            tfl_type=T,
            section=S141,
            sort_key=7,
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
            footnotes=[
                "ITT: All randomized with >=1 dose. Safety: All with >=1 dose. PP: ITT with no major PDs."
            ],
            dataset_source="ADSL",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_populations.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.1.8",
            title="Medical History by SOC/PT — Incidence >=2% in Any Arm",
            tfl_type=T,
            section=S141,
            sort_key=8,
            population="Safety Population",
            placeholder_columns=H2_SOCPT,
            shell_rows=[
                ["Gastrointestinal disorders", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["  Gastroesophageal reflux disease", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["Musculoskeletal disorders", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["  Back pain", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                EROW,
            ],
            dataset_source="ADMH",
            source_listing="L16.2.13",
            program_ref="t_mh_2pct.sas",
            dictionary_versions={"MedDRA": "[xx.x]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.1.9",
            title="Prior and Concomitant Medications by ATC Level 2 and Preferred Name",
            tfl_type=T,
            section=S141,
            sort_key=9,
            population="Safety Population",
            placeholder_columns=H2_SOCPT,
            shell_rows=[
                ["Prior Medications — Any", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["Concomitant Medications — Any", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["Drugs for acid-related disorders", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["Analgesics", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                EROW,
            ],
            dataset_source="ADCM",
            source_listing="L16.2.6",
            program_ref="t_conmed_atc.sas",
            dictionary_versions={"WHO-DD": "[version]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.1.10",
            title="Summary of Study Drug Exposure — Duration, Cycles, Dose Intensity",
            tfl_type=T,
            section=S141,
            sort_key=10,
            population="Safety Population",
            placeholder_columns=H2_SIMPLE,
            shell_rows=[
                {"label": "Duration of Exposure (weeks)", "bold": True},
                {"label": "  n", "indent": True, "values": ["xx", "xx", "...", "xx"]},
                {
                    "label": "  Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Median (Min, Max)",
                    "indent": True,
                    "values": ["xx.x (xx, xx)", "xx.x (xx, xx)", "...", "xx.x (xx, xx)"],
                },
                {"label": "Number of Cycles Administered", "bold": True},
                {"label": "  n", "indent": True, "values": ["xx", "xx", "...", "xx"]},
                {
                    "label": "  Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Median (Min, Max)",
                    "indent": True,
                    "values": ["xx.x (xx, xx)", "xx.x (xx, xx)", "...", "xx.x (xx, xx)"],
                },
                {"label": "Cumulative Dose (mg)", "bold": True},
                {
                    "label": "  Mean (SD)",
                    "indent": True,
                    "values": ["xxxx.x (xxx.x)", "xxxx.x (xxx.x)", "...", "xxxx.x (xxx.x)"],
                },
                {
                    "label": "  Median (Min, Max)",
                    "indent": True,
                    "values": [
                        "xxxx.x (xx, xxxx)",
                        "xxxx.x (xx, xxxx)",
                        "...",
                        "xxxx.x (xx, xxxx)",
                    ],
                },
                {"label": "Relative Dose Intensity (%)", "bold": True},
                {"label": "  n", "indent": True, "values": ["xx", "xx", "...", "xx"]},
                {
                    "label": "  Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Median (Min, Max)",
                    "indent": True,
                    "values": ["xx.x (xx, xx)", "xx.x (xx, xx)", "...", "xx.x (xx, xx)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            dataset_source="ADEX",
            source_listing="L16.2.12",
            program_ref="t_exposure_summary.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.1.11",
            title="Summary of Genomic/Biomarker Baseline Characteristics",
            tfl_type=T,
            section=S141,
            sort_key=11,
            oncology_only=True,
            population="ITT Population with Biomarker Data",
            placeholder_columns=H2_SIMPLE,
            shell_rows=[
                ["PD-L1 TPS >=50%", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["PD-L1 TPS 1-49%", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["EGFR Mutation Positive", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                EROW,
            ],
            dataset_source="ADSL, ADBM",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_biomarker_baseline.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.1.12",
            title="Subject Disposition by Country and Site",
            tfl_type=T,
            section=S141,
            sort_key=12,
            population="All Randomized Subjects",
            placeholder_columns=[
                "Country\nSite",
                "Screened\nn",
                "Randomized\nn",
                "Treated\nn (%)",
                "Completed\nn (%)",
                "Discontinued\nn (%)",
            ],
            shell_rows=[
                {"label": "Country A", "bold": True},
                {
                    "label": "  Site 001",
                    "indent": True,
                    "values": ["xx", "xx", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"],
                },
                {
                    "label": "  Site 002",
                    "indent": True,
                    "values": ["xx", "xx", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"],
                },
                {"label": "Country B", "bold": True},
                {
                    "label": "  Site 003",
                    "indent": True,
                    "values": ["xx", "xx", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "...", "..."]},
            ],
            dataset_source="ADSL",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_disp_site.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.1.13",
            title="Screening Summary — Screen Failure Reasons by Eligibility Criterion",
            tfl_type=T,
            section=S141,
            sort_key=13,
            population="All Screened Subjects",
            placeholder_columns=["Eligibility Criterion", "Screen Failures\nn", "Reason\nCategory"],
            shell_rows=[
                {"label": "Inclusion Criterion 1: Age >=18", "values": ["xx", "Age <18"]},
                {"label": "Inclusion Criterion 2: ECOG 0-1", "values": ["xx", "ECOG >=2"]},
                {
                    "label": "Exclusion Criterion 1: Prior malignancy",
                    "values": ["xx", "History of prior cancer"],
                },
                {
                    "label": "Exclusion Criterion 2: Active infection",
                    "values": ["xx", "Active HBV/HCV/HIV"],
                },
                {"label": "Total Screen Failures", "bold": True, "values": ["xx", ""]},
                {"label": "[...]", "values": ["...", "..."]},
            ],
            dataset_source="ADSL",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_screen_fail.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.1.14",
            title="Major Protocol Deviations — by Category and Subcategory",
            tfl_type=T,
            section=S141,
            sort_key=14,
            population="All Randomized Subjects",
            placeholder_columns=[
                "Deviation Category\nSubcategory",
                "G1\nn (%)",
                "G2\nn (%)",
                "...",
                "Overall\nn (%)",
            ],
            shell_rows=[
                {"label": "Eligibility Criteria", "bold": True},
                {
                    "label": "  Inclusion criteria not met",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Exclusion criteria not met",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "Study Procedure", "bold": True},
                {
                    "label": "  Missed efficacy assessment",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Out-of-window visit",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "Study Treatment", "bold": True},
                {
                    "label": "  Wrong dose administered",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Non-compliance <80%",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "Concomitant Medication", "bold": True},
                {
                    "label": "  Prohibited medication taken",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            dataset_source="ADSL, DV",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_protdev_cat.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.1.15",
            title="Surgical and Procedure History by Body System",
            tfl_type=T,
            section=S141,
            sort_key=15,
            population="Safety Population",
            placeholder_columns=[
                "Body System\nProcedure",
                "G1\nn (%)",
                "G2\nn (%)",
                "...",
                "Overall\nn (%)",
            ],
            shell_rows=[
                {
                    "label": "Any Surgical/Procedure History",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Cardiovascular",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Coronary artery bypass graft",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Pacemaker insertion",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Gastrointestinal",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Cholecystectomy",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Appendectomy",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Musculoskeletal",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Joint replacement",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            dataset_source="ADSL, ADMH",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_surg_hist.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.1.16",
            title="Prior and Concomitant Medications by WHO ATC Level 3 — >=5% in Any Arm",
            tfl_type=T,
            section=S141,
            sort_key=16,
            population="Safety Population",
            placeholder_columns=[
                "ATC Level 3\nPreferred Name",
                "Prior\nn (%)",
                "Concomitant\nn (%)",
                "...",
                "Overall\nn (%)",
            ],
            shell_rows=[
                {"label": "A02BC — Proton Pump Inhibitors", "bold": True},
                {
                    "label": "  Omeprazole",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Pantoprazole",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "N02BE — Anilides (Paracetamol)", "bold": True},
                {
                    "label": "  Paracetamol",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "C10AA — HMG-CoA Reductase Inhibitors", "bold": True},
                {
                    "label": "  Atorvastatin",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "WHO Drug Global [version]. Prior = stopped before first dose. Concomitant = any use on/after first dose."
            ],
            dataset_source="ADSL, ADCM",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_conmed_atc3.sas",
            dictionary_versions={"WHO-DD": "[version]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.1.17",
            title="Study Drug Exposure by Duration Category",
            tfl_type=T,
            section=S141,
            sort_key=17,
            population="Safety Population",
            placeholder_columns=[
                "Exposure Duration",
                "G1\nn (%)",
                "G2\nn (%)",
                "...",
                "Overall\nn (%)",
            ],
            shell_rows=[
                {"label": "Duration of Exposure", "bold": True},
                {
                    "label": "  Mean (SD), weeks",
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Median (Min, Max), weeks",
                    "values": ["xx.x (xx, xx)", "xx.x (xx, xx)", "...", "xx.x (xx, xx)"],
                },
                {"label": "Exposure by Duration Category", "bold": True},
                {
                    "label": "  >=1 month (<30 days)",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  >=3 months (>=90 days)",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  >=6 months (>=180 days)",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  >=12 months (>=360 days)",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            dataset_source="ADSL, ADEX",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_expo_durcat.sas",
        )
    )

    return items

