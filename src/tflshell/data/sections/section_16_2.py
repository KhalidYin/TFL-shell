"""Section 16.2 catalog definitions: patient listings shells."""

from tflshell.data.common import *


def build_16_2_items() -> list[TFLItem]:
    """Build Section 16.2 catalog items."""
    items: list[TFLItem] = []

    # 16.2 PATIENT DATA LISTINGS (expanded master set including PK/ADA/Biomarker,
    # Phase I dose-escalation review, and non-oncology event review)
    # =====================================================================

    items.append(
        TFLItem(
            id="L16.2.1",
            title="Listing of Subject Disposition",
            tfl_type=L,
            section=S162,
            sort_key=1,
            population="All Screened Subjects",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Date Screened",
                "Date Randomized",
                "Date of First Dose",
                "Date of Last Dose",
                "Completed Treatment?",
                "Reason for Discontinuation",
            ],
            shell_rows=[
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "DDMMMYYYY",
                    "DDMMMYYYY",
                    "DDMMMYYYY",
                    "DDMMMYYYY",
                    "Yes/No",
                    "Reason / xxxxxxx",
                ],
                ["[...]", "...", "...", "...", "...", "...", "...", "...", "..."],
            ],
            footnotes=["Sorted by site, subject ID. Refer to EOT/Study Completion CRF pages."],
            dataset_source="ADSL",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_disposition.sas",
        )
    )

    items.append(
        TFLItem(
            id="L16.2.2",
            title="Listing of Demographic Data",
            tfl_type=L,
            section=S162,
            sort_key=2,
            population="All Randomized Subjects",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Age (yrs)",
                "Sex",
                "Race",
                "Height (cm)",
                "Weight (kg)",
                "BMI (kg/m²)",
            ],
            shell_rows=[
                ["xxx", "xxxx/xxx", "Gx", "xx", "M/F", "Race", "xxx", "xx.x", "xx.x"],
                ["[...]", "...", "...", "...", "...", "...", "...", "...", "..."],
            ],
            dataset_source="ADSL",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_demog.sas",
        )
    )

    items.append(
        TFLItem(
            id="L16.2.3",
            title="Listing of Protocol Deviations",
            tfl_type=L,
            section=S162,
            sort_key=3,
            population="All Enrolled Subjects",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Deviation Category",
                "Deviation Description",
                "Date of Deviation",
                "Major/Minor",
            ],
            shell_rows=[
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "Category",
                    "Description text xxxxxxx",
                    "DDMMMYYYY",
                    "Major/Minor",
                ],
                ["[...]", "...", "...", "...", "...", "...", "..."],
            ],
            dataset_source="ADSL, DV",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_protdev.sas",
        )
    )

    items.append(
        TFLItem(
            id="L16.2.4",
            title="Listing of Adverse Events",
            tfl_type=L,
            section=S162,
            sort_key=4,
            population="Safety Population",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "SOC",
                "Preferred Term",
                "Verbatim Term",
                "Start Date",
                "End Date",
                "CTCAE Grade",
                "Relationship",
                "SAE?",
                "Action",
                "Outcome",
            ],
            shell_rows=[
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "GI disorders",
                    "Nausea",
                    "Nausea (Verbatim)",
                    "DDMMMYYYY",
                    "DDMMMYYYY",
                    "x",
                    "R/NR",
                    "Y/N",
                    "N/DR/DI/DW",
                    "Recovered/Ongoing",
                ],
                [
                    "[...]",
                    "...",
                    "...",
                    "...",
                    "...",
                    "...",
                    "...",
                    "...",
                    "...",
                    "...",
                    "...",
                    "...",
                    "...",
                ],
            ],
            footnotes=[
                "R=Related, NR=Not Related. N=None, DR=Dose Reduced, DI=Interrupted, DW=Withdrawn."
            ],
            dataset_source="ADSL, ADAE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_ae.sas",
            dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
        )
    )

    items.append(
        TFLItem(
            id="L16.2.5",
            title="Listing of Serious Adverse Events",
            tfl_type=L,
            section=S162,
            sort_key=5,
            population="Safety Population",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Preferred Term",
                "SAE Criteria",
                "Start Date",
                "End Date",
                "CTCAE Grade",
                "Relationship",
                "Outcome",
                "Narrative ID",
            ],
            shell_rows=[
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "Pneumonia",
                    "D/L/H/P/C/O",
                    "DDMMMYYYY",
                    "DDMMMYYYY",
                    "x",
                    "R/NR",
                    "Recovered/Fatal",
                    "NAR-xxxx",
                ],
                ["[...]", "...", "...", "...", "...", "...", "...", "...", "...", "...", "..."],
            ],
            dataset_source="ADSL, ADAE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_sae.sas",
            dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
        )
    )

    items.append(
        TFLItem(
            id="L16.2.6",
            title="Listing of Concomitant Medications",
            tfl_type=L,
            section=S162,
            sort_key=6,
            population="Safety Population",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "ATC Class",
                "Preferred Name",
                "Indication",
                "Dose / Route / Frequency",
                "Start Date",
                "End Date",
            ],
            shell_rows=[
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "A02BC",
                    "Omeprazole",
                    "GERD",
                    "20 mg / PO / QD",
                    "DDMMMYYYY",
                    "DDMMMYYYY",
                ],
                ["[...]", "...", "...", "...", "...", "...", "...", "...", "..."],
            ],
            dataset_source="ADSL, ADCM",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_conmed.sas",
            dictionary_versions={"WHO-DD": "[version]"},
        )
    )

    items.append(
        TFLItem(
            id="L16.2.7",
            title="Listing of Laboratory Data — Hematology and Chemistry",
            tfl_type=L,
            section=S162,
            sort_key=7,
            population="Safety Population",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Visit",
                "Parameter",
                "Result",
                "Unit",
                "Normal Range",
                "Flag",
            ],
            shell_rows=[
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "Screening/Wk xx",
                    "Hemoglobin",
                    "xx.x",
                    "g/dL",
                    "xx.x-xx.x",
                    "L/N/H",
                ],
                ["[...]", "...", "...", "...", "...", "...", "...", "...", "..."],
            ],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_lab.sas",
        )
    )

    items.append(
        TFLItem(
            id="L16.2.8",
            title="Listing of Vital Signs",
            tfl_type=L,
            section=S162,
            sort_key=8,
            population="Safety Population",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Visit",
                "Date",
                "SBP\n(mmHg)",
                "DBP\n(mmHg)",
                "HR\n(bpm)",
                "Resp Rate",
                "Temp (°C)",
                "Weight (kg)",
            ],
            shell_rows=[
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "Screening",
                    "DDMMMYYYY",
                    "xxx",
                    "xx",
                    "xx",
                    "xx",
                    "xx.x",
                    "xx.x",
                ],
                ["[...]", "...", "...", "...", "...", "...", "...", "...", "...", "...", "..."],
            ],
            dataset_source="ADSL, ADVS",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_vitalsigns.sas",
        )
    )

    items.append(
        TFLItem(
            id="L16.2.9",
            title="Listing of ECG Data",
            tfl_type=L,
            section=S162,
            sort_key=9,
            population="Safety Population with ECG Data",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Visit",
                "Date/Time",
                "HR\n(bpm)",
                "PR\n(ms)",
                "QRS\n(ms)",
                "QT\n(ms)",
                "QTcF\n(ms)",
                "Interpretation",
            ],
            shell_rows=[
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "Screening",
                    "DDMMMYYYY HH:MM",
                    "xx",
                    "xxx",
                    "xx",
                    "xxx",
                    "xxx",
                    "Normal/Abnormal NCS/Abnormal CS",
                ],
                ["[...]", "...", "...", "...", "...", "...", "...", "...", "...", "...", "..."],
            ],
            dataset_source="ADSL, ADEG",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_ecg.sas",
        )
    )

    items.append(
        TFLItem(
            id="L16.2.10",
            title="Listing of Tumor Response Data",
            tfl_type=L,
            section=S162,
            sort_key=10,
            oncology_only=True,
            population="ITT Population",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Visit",
                "Assessment Date",
                "Target Lesion Sum\n(mm)",
                "% Change\nfrom BL",
                "Non-Target Status",
                "New Lesions?",
                "Overall Response",
                "BOR",
            ],
            shell_rows=[
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "Screening/Wk xx",
                    "DDMMMYYYY",
                    "xxx.x",
                    "—/xx.x",
                    "Present/Absent",
                    "Y/N",
                    "CR/PR/SD/PD/NE",
                    "CR/PR/SD/PD/NE",
                ],
                ["[...]", "...", "...", "...", "...", "...", "...", "...", "...", "...", "..."],
            ],
            dataset_source="ADSL, ADRS",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_tumor_response.sas",
        )
    )

    items.append(
        TFLItem(
            id="L16.2.11",
            title="Listing of Survival Data",
            tfl_type=L,
            section=S162,
            sort_key=11,
            oncology_only=True,
            population="ITT Population",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Date of Last Contact",
                "Vital Status",
                "Date of Death",
                "Primary Cause of Death",
                "PFS Event Date",
                "PFS Censor",
                "OS Censor",
            ],
            shell_rows=[
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "DDMMMYYYY",
                    "Alive/Dead/LTFU",
                    "DDMMMYYYY",
                    "xxxxxxx",
                    "DDMMMYYYY",
                    "Y/N",
                    "Y/N",
                ],
                ["[...]", "...", "...", "...", "...", "...", "...", "...", "...", "..."],
            ],
            dataset_source="ADSL, ADTTE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_survival.sas",
        )
    )

    items.append(
        TFLItem(
            id="L16.2.12",
            title="Listing of Study Drug Exposure and Dose Modifications",
            tfl_type=L,
            section=S162,
            sort_key=12,
            population="Safety Population",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Cycle/Day",
                "Planned Dose",
                "Actual Dose",
                "Modification Reason",
            ],
            shell_rows=[
                ["xxx", "xxxx/xxx", "Gx", "CxDx", "xxx mg", "xxx mg", "Reason / None"],
                ["[...]", "...", "...", "...", "...", "...", "..."],
            ],
            dataset_source="ADSL, ADEX",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_exposure.sas",
        )
    )

    items.append(
        TFLItem(
            id="L16.2.13",
            title="Listing of Medical History Verbatim vs. Coded Terms",
            tfl_type=L,
            section=S162,
            sort_key=13,
            population="Safety Population",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "SOC",
                "Preferred Term",
                "Verbatim Term",
                "Start Date/Year",
                "End Date/Year",
                "Ongoing?",
            ],
            shell_rows=[
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "Vascular disorders",
                    "Hypertension",
                    "High Blood Pressure",
                    "YYYY/DDMMMYYYY",
                    "YYYY/DDMMMYYYY",
                    "Y/N",
                ],
                ["[...]", "...", "...", "...", "...", "...", "...", "...", "..."],
            ],
            dataset_source="ADSL, ADMH",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_mh_coded.sas",
            dictionary_versions={"MedDRA": "[xx.x]"},
        )
    )

    items.append(
        TFLItem(
            id="L16.2.14",
            title="Listing of PK Concentrations by Subject and Timepoint",
            tfl_type=L,
            section=S162,
            sort_key=14,
            population="PK Population",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Cycle/Day",
                "Nominal Time\n(h)",
                "Actual Time\n(h)",
                "Concentration\n(ng/mL)",
                "BQL",
            ],
            shell_rows=[
                ["xxx", "xxxx/xxx", "Gx", "C1D1", "0", "0.00", "xx.x", "Y/N"],
                ["xxx", "xxxx/xxx", "Gx", "C1D1", "2", "2.05", "xx.x", "Y/N"],
                ["[...]", "...", "...", "...", "...", "...", "...", "..."],
            ],
            footnotes=["BQL = Below Quantification Limit (<xx.x ng/mL)."],
            dataset_source="ADSL, ADPC",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_pk_conc.sas",
        )
    )

    items.append(
        TFLItem(
            id="L16.2.15",
            title="Listing of PK Parameters by Subject",
            tfl_type=L,
            section=S162,
            sort_key=15,
            population="PK Population",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Cycle",
                "Cmax\n(ng/mL)",
                "AUC0-tau\n(ng·h/mL)",
                "Tmax\n(h)",
                "t1/2\n(h)",
                "CL/F\n(L/h)",
            ],
            shell_rows=[
                ["xxx", "xxxx/xxx", "Gx", "C1", "xx.x", "xxx.x", "x.x", "xx.x", "xx.x"],
                ["[...]", "...", "...", "...", "...", "...", "...", "...", "..."],
            ],
            dataset_source="ADSL, ADPP",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_pk_params.sas",
        )
    )

    items.append(
        TFLItem(
            id="L16.2.16",
            title="Listing of ADA and Neutralizing Antibody Results",
            tfl_type=L,
            section=S162,
            sort_key=16,
            population="Safety Population with ADA Samples",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Visit (Day)",
                "ADA Result",
                "ADA Titer",
                "Nab Result",
            ],
            shell_rows=[
                ["xxx", "xxxx/xxx", "Gx", "Screening (Dxx)", "Neg/Pos", "<LLOQ/1:xxx", "Neg/Pos"],
                ["xxx", "xxxx/xxx", "Gx", "C3D1 (Dxx)", "Neg/Pos", "<LLOQ/1:xxx", "Neg/Pos"],
                ["[...]", "...", "...", "...", "...", "...", "..."],
            ],
            dataset_source="ADSL, ADIS",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_ada.sas",
        )
    )

    items.append(
        TFLItem(
            id="L16.2.17",
            title="Listing of Biomarker Results by Subject and Visit",
            tfl_type=L,
            section=S162,
            sort_key=17,
            population="ITT with Biomarker Data",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Visit",
                "Biomarker",
                "Result",
                "Unit",
                "Method",
            ],
            shell_rows=[
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "Screening",
                    "ctDNA / PD-L1 / etc.",
                    "xx.x",
                    "ng/mL / % / etc.",
                    "NGS / IHC / ddPCR",
                ],
                ["[...]", "...", "...", "...", "...", "...", "...", "..."],
            ],
            dataset_source="ADSL, ADBM",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_biomarker.sas",
        )
    )

    items.append(
        TFLItem(
            id="L16.2.18",
            title="Listing of PRO Assessments by Subject and Visit",
            tfl_type=L,
            section=S162,
            sort_key=18,
            population="ITT with PRO Data",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Visit",
                "GHS",
                "PF",
                "RF",
                "EF",
                "CF",
                "SF",
            ],
            shell_rows=[
                ["xxx", "xxxx/xxx", "Gx", "Screening", "xx", "xx", "xx", "xx", "xx", "xx"],
                ["xxx", "xxxx/xxx", "Gx", "Wk 12", "xx", "xx", "xx", "xx", "xx", "xx"],
                ["[...]", "...", "...", "...", "...", "...", "...", "...", "...", "..."],
            ],
            dataset_source="ADSL, ADPRO",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_pro.sas",
        )
    )

    items.append(
        TFLItem(
            id="L16.2.19",
            title="Listing of Subsequent Anti-Cancer Therapies",
            tfl_type=L,
            section=S162,
            sort_key=19,
            oncology_only=True,
            population="ITT Population",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Therapy Name",
                "Therapy Class",
                "Start Date",
                "End Date",
                "Best Response to Subsequent Therapy",
            ],
            shell_rows=[
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "Drug Name",
                    "Chemotherapy/Immunotherapy/Targeted",
                    "DDMMMYYYY",
                    "DDMMMYYYY/ongoing",
                    "CR/PR/SD/PD/NE",
                ],
                ["[...]", "...", "...", "...", "...", "...", "...", "..."],
            ],
            dataset_source="ADSL, ADCM",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_subsequent_therapy.sas",
        )
    )

    items.append(
        TFLItem(
            id="L16.2.20",
            title="Listing of Deaths — All Subjects",
            tfl_type=L,
            section=S162,
            sort_key=20,
            population="All Randomized Subjects",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Date of Death",
                "Days from First Dose",
                "Days from Last Dose",
                "Primary Cause of Death",
                "AE-Related?",
                "Narrative ID",
            ],
            shell_rows=[
                ["xxx", "xxxx/xxx", "Gx", "DDMMMYYYY", "xx", "xx", "xxxxxxx", "Y/N", "NAR-xxxx"],
                ["[...]", "...", "...", "...", "...", "...", "...", "...", "..."],
            ],
            dataset_source="ADSL, ADAE, ADTTE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_deaths.sas",
        )
    )

    items.append(
        TFLItem(
            id="L16.2.21",
            title="Listing of Prior and Subsequent Anti-Cancer Surgery/Radiotherapy",
            tfl_type=L,
            section=S162,
            sort_key=21,
            oncology_only=True,
            population="Full Analysis Set",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Procedure",
                "Target Location",
                "Intent",
                "Date",
            ],
            shell_rows=[
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "Surgery/Radiotherapy Name",
                    "Location xxxxxxx",
                    "Curative/Palliative/Adjuvant",
                    "DDMMMYYYY",
                ],
                ["[...]", "...", "...", "...", "...", "...", "..."],
            ],
            dataset_source="ADSL, ADCM",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_prior_cancer_proc.sas",
        )
    )

    # --- 16.2 Listing Expansion (CDISC Source Data) ---
    items.append(
        TFLItem(
            id="L16.2.22",
            title="Listing of Adverse Events of Special Interest (AESI)",
            tfl_type=L,
            section=S162,
            sort_key=22,
            population="Safety Population",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "AESI Category",
                "Preferred Term",
                "CTCAE Grade",
                "Start Date",
                "End Date",
                "Outcome",
                "Serious?",
                "Relationship",
                "Narrative ID",
            ],
            shell_rows=[
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "Hepatotoxicity",
                    "ALT Increased",
                    "3",
                    "DDMMMYYYY",
                    "DDMMMYYYY",
                    "Recovered",
                    "N",
                    "Related",
                    "NAR-xxxx",
                ],
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "Infusion Reaction",
                    "Anaphylaxis",
                    "4",
                    "DDMMMYYYY",
                    "DDMMMYYYY",
                    "Recovered/Resolved with Sequelae",
                    "Y",
                    "Related",
                    "NAR-xxxx",
                ],
                {
                    "label": "[...]",
                    "values": [
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                    ],
                },
            ],
            footnotes=[
                "AESI categories per protocol. MedDRA [xx.x]. CTCAE [xx]. Refer to Section 14.3.1 for AESI summary tables."
            ],
            dataset_source="ADSL, ADAE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_aesi.sas",
            dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
        )
    )

    items.append(
        TFLItem(
            id="L16.2.23",
            title="Listing of Subjects with Hy's Law Laboratory Criteria",
            tfl_type=L,
            section=S162,
            sort_key=23,
            population="Safety Population with Baseline and Post-Baseline Labs",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Visit",
                "ALT (U/L)",
                "ALT xULN",
                "AST (U/L)",
                "AST xULN",
                "TBL (umol/L)",
                "TBL xULN",
                "ALP (U/L)",
                "ALP xULN",
                "Hy's Law?",
                "Alternative Etiology",
            ],
            shell_rows=[
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "Wk 8",
                    "xxx",
                    "x.x",
                    "xxx",
                    "x.x",
                    "xx.x",
                    "x.x",
                    "xxx",
                    "x.x",
                    "Yes",
                    "xxxxxxx",
                ],
                {
                    "label": "[...]",
                    "values": [
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                    ],
                },
            ],
            footnotes=[
                "Hy's Law: ALT/AST >=3xULN, TBL >=2xULN, ALP <2xULN, no alternative etiology. Refer to T14.3.2.2 and T14.3.2.4."
            ],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_hyslaw.sas",
        )
    )

    items.append(
        TFLItem(
            id="L16.2.24",
            title="Listing of Physical Examination Findings",
            tfl_type=L,
            section=S162,
            sort_key=24,
            population="Safety Population",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Visit",
                "Body System",
                "Finding",
                "Baseline Status",
                "Current Status",
            ],
            shell_rows=[
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "Screening",
                    "Cardiovascular",
                    "Murmur Grade II/VI",
                    "N/A",
                    "Abnormal NCS",
                ],
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "EOT",
                    "Respiratory",
                    "Crackles left base",
                    "Normal",
                    "Abnormal CS",
                ],
                {
                    "label": "[...]",
                    "values": ["...", "...", "...", "...", "...", "...", "...", "..."],
                },
            ],
            footnotes=[
                "NCS = Not Clinically Significant. CS = Clinically Significant. Refer to T14.3.4.15-T14.3.4.16."
            ],
            dataset_source="ADSL, ADPE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_pe.sas",
        )
    )

    items.append(
        TFLItem(
            id="L16.2.25",
            title="Listing of Urinalysis Results — Dipstick and Microscopic",
            tfl_type=L,
            section=S162,
            sort_key=25,
            population="Safety Population",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Visit",
                "pH",
                "Protein",
                "Glucose",
                "Blood",
                "Ketones",
                "Microscopic Findings",
            ],
            shell_rows=[
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "Baseline",
                    "6.0",
                    "Neg",
                    "Neg",
                    "Neg",
                    "Neg",
                    "No casts/crystals",
                ],
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "Wk 12",
                    "7.5",
                    "++",
                    "Neg",
                    "+",
                    "Neg",
                    "Hyaline casts: 2-5/LPF",
                ],
                {
                    "label": "[...]",
                    "values": [
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                    ],
                },
            ],
            footnotes=["Dipstick: Neg/Trace/+/++/+++. LPF = Low Power Field. Refer to T14.3.3.14."],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_ua.sas",
        )
    )

    items.append(
        TFLItem(
            id="L16.2.26",
            title="Listing of Coagulation Panel Results",
            tfl_type=L,
            section=S162,
            sort_key=26,
            population="Safety Population",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Visit",
                "PT (s)",
                "PT Ref Range",
                "INR",
                "aPTT (s)",
                "aPTT Ref Range",
                "Flag",
            ],
            shell_rows=[
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "Baseline",
                    "xx.x",
                    "xx.x-xx.x",
                    "x.xx",
                    "xx.x",
                    "xx.x-xx.x",
                    "N",
                ],
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "Wk 4",
                    "xx.x",
                    "xx.x-xx.x",
                    "x.xx",
                    "xx.x",
                    "xx.x-xx.x",
                    "H",
                ],
                {
                    "label": "[...]",
                    "values": [
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                    ],
                },
            ],
            footnotes=[
                "Flag: L=Below, N=Within, H=Above reference range. Refer to T14.3.3.12-T14.3.3.13."
            ],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_coag.sas",
        )
    )

    items.append(
        TFLItem(
            id="L16.2.27",
            title="Listing of Cardiac Biomarkers and Immunoglobulins",
            tfl_type=L,
            section=S162,
            sort_key=27,
            population="Safety Population",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Visit",
                "hs-Troponin I (ng/L)",
                "CK-MB (ng/mL)",
                "NT-proBNP (pg/mL)",
                "IgG (g/L)",
                "IgM (g/L)",
            ],
            shell_rows=[
                ["xxx", "xxxx/xxx", "Gx", "Baseline", "xx.x", "xx.x", "xxx", "xx.x", "xx.x"],
                ["xxx", "xxxx/xxx", "Gx", "Wk 12", "xx.x", "xx.x", "xxx", "xx.x", "xx.x"],
                {
                    "label": "[...]",
                    "values": ["...", "...", "...", "...", "...", "...", "...", "...", "..."],
                },
            ],
            footnotes=["Refer to T14.3.3.19 and T14.3.3.21 for summary tables."],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_cardiac_bio.sas",
        )
    )

    items.append(
        TFLItem(
            id="L16.2.28",
            title="Listing of Lymphocyte Subsets and Cytokine Panel",
            tfl_type=L,
            section=S162,
            sort_key=28,
            population="Safety Population (Subset with Immunophenotyping)",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Visit",
                "CD3 (cells/uL)",
                "CD4 (cells/uL)",
                "CD8 (cells/uL)",
                "CD4/CD8 Ratio",
                "CD19 (cells/uL)",
                "CD16+56 (cells/uL)",
            ],
            shell_rows=[
                ["xxx", "xxxx/xxx", "Gx", "Baseline", "xxx", "xxx", "xxx", "x.xx", "xxx", "xxx"],
                ["xxx", "xxxx/xxx", "Gx", "Cycle 2 D1", "xxx", "xxx", "xxx", "x.xx", "xxx", "xxx"],
                {
                    "label": "[...]",
                    "values": [
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                    ],
                },
            ],
            footnotes=["Flow cytometry. Refer to T14.3.3.22-T14.3.3.23 for summary tables."],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_lymph_cyto.sas",
        )
    )

    items.append(
        TFLItem(
            id="L16.2.29",
            title="Listing of Infusion-Related Reactions — Timing and Management Detail",
            tfl_type=L,
            section=S162,
            sort_key=29,
            population="Safety Population",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Cycle/Infusion",
                "IRR PT",
                "CTCAE Grade",
                "Onset from Start (min)",
                "Infusion Rate Change",
                "Prophylaxis Given",
                "Completed Infusion?",
                "Outcome",
            ],
            shell_rows=[
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "C1/Inf1",
                    "Chills",
                    "2",
                    "45",
                    "Rate reduced 50%",
                    "Antihistamine",
                    "Y",
                    "Recovered",
                ],
                {
                    "label": "[...]",
                    "values": [
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                    ],
                },
            ],
            footnotes=[
                "IRR = infusion-related reaction (onset during or within 24h of infusion). Refer to T14.3.1.13 and T14.3.1.25."
            ],
            dataset_source="ADSL, ADAE, ADEX",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_irr.sas",
            dictionary_versions={"CTCAE": "[xx]"},
        )
    )

    items.append(
        TFLItem(
            id="L16.2.30",
            title="Listing of Dose Modifications — Interruptions and Reductions Detail",
            tfl_type=L,
            section=S162,
            sort_key=30,
            population="Safety Population",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Cycle",
                "Modification Type",
                "Reason",
                "AE-Related PT",
                "Original Dose",
                "Modified Dose",
                "Days Interrupted",
            ],
            shell_rows=[
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "C3",
                    "Interruption",
                    "Neutropenia",
                    "Neutropenia Gr3",
                    "xxx mg",
                    "0 mg",
                    "7",
                ],
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "C5",
                    "Reduction",
                    "Fatigue",
                    "Fatigue Gr2",
                    "xxx mg",
                    "xx mg",
                    "0",
                ],
                {
                    "label": "[...]",
                    "values": [
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                    ],
                },
            ],
            footnotes=["Refer to T14.3.1.7 and T14.3.1.25 for summary tables."],
            dataset_source="ADSL, ADEX",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_dose_mod.sas",
        )
    )

    items.append(
        TFLItem(
            id="L16.2.31",
            title="Listing of Reproductive Hormone Panel Results",
            tfl_type=L,
            section=S162,
            sort_key=31,
            population="Safety Population (Subset with Hormone Data)",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Sex",
                "Visit",
                "FSH (IU/L)",
                "LH (IU/L)",
                "Estradiol (pmol/L)",
                "Testosterone (nmol/L)",
                "AMH (pmol/L)",
            ],
            shell_rows=[
                ["xxx", "xxxx/xxx", "Gx", "F", "Baseline", "xx.x", "xx.x", "xxx", "x.x", "xx.x"],
                ["xxx", "xxxx/xxx", "Gx", "M", "Baseline", "xx.x", "xx.x", "xxx", "xx.x", "N/A"],
                {
                    "label": "[...]",
                    "values": [
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                        "...",
                    ],
                },
            ],
            footnotes=[
                "Reproductive hormones collected per protocol. AMH = Anti-Mullerian Hormone (females only where applicable)."
            ],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_hormone.sas",
        )
    )

    items.append(
        TFLItem(
            id="L16.2.32",
            title="Listing of Dose-Limiting Toxicities and Dose Escalation Review Window",
            tfl_type=L,
            section=S162,
            sort_key=32,
            population="DLT-Evaluable Population",
            placeholder_columns=[
                "Site",
                "Subject",
                "Cohort / Dose Level",
                "DLT Window",
                "DLT Term",
                "Maximum Grade",
                "DLT?",
                "Replacement Subject?",
            ],
            shell_rows=[
                [
                    "xxx",
                    "xxxx/xxx",
                    "Dose Level 1",
                    "Cycle 1 Day 1-28",
                    "ALT Increased",
                    "3",
                    "Y",
                    "N",
                ],
                ["xxx", "xxxx/xxx", "Dose Level 2", "Cycle 1 Day 1-28", "Mucositis", "2", "N", "Y"],
                {
                    "label": "[...]",
                    "values": ["...", "...", "...", "...", "...", "...", "...", "..."],
                },
            ],
            footnotes=[
                "Includes DLT-evaluable and replacement-subject status per protocol-defined dose-escalation rules."
            ],
            dataset_source="ADSL, ADAE, ADEX",
            source_listing="L16.2.32",
            program_ref="l_dlt_review.sas",
            shell_family="Specialized Patient Listings",
            study_phase_scope="Phase I",
            coverage_summary="Core (Phase I)",
        )
    )

    items.append(
        TFLItem(
            id="L16.2.33",
            title="Listing of Food-Effect / Crossover PK Samples by Subject, Period, and Timepoint",
            tfl_type=L,
            section=S162,
            sort_key=33,
            non_oncology_only=True,
            population="PK Population in Food-Effect or Crossover Cohorts",
            placeholder_columns=[
                "Site",
                "Subject",
                "Treatment Sequence",
                "Period",
                "Condition",
                "Nominal Time (h)",
                "Actual Time (h)",
                "Concentration (ng/mL)",
            ],
            shell_rows=[
                ["xxx", "xxxx/xxx", "TR/RT", "1", "Fasted", "0.0", "0.00", "xx.x"],
                ["xxx", "xxxx/xxx", "TR/RT", "1", "Fed", "2.0", "2.05", "xx.x"],
                {
                    "label": "[...]",
                    "values": ["...", "...", "...", "...", "...", "...", "...", "..."],
                },
            ],
            footnotes=[
                "Supports food-effect and crossover PK review by period, condition, and actual sampling time."
            ],
            dataset_source="ADSL, ADPC",
            source_listing="L16.2.33",
            program_ref="l_food_effect_pk.sas",
            shell_family="Non-Oncology Listings",
            study_phase_scope="Phase I",
            coverage_summary="Conditional (Phase I)",
        )
    )

    items.append(
        TFLItem(
            id="L16.2.34",
            title="Listing of Protocol-Defined Clinical Events / Exacerbations",
            tfl_type=L,
            section=S162,
            sort_key=34,
            non_oncology_only=True,
            population="Intent-to-Treat (ITT) Population",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Event Category",
                "Event Term",
                "Start Date",
                "End Date",
                "Hospitalization?",
                "Adjudicated?",
            ],
            shell_rows=[
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "Exacerbation",
                    "Moderate exacerbation",
                    "DDMMMYYYY",
                    "DDMMMYYYY",
                    "N",
                    "Y",
                ],
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "Clinical Event",
                    "Composite endpoint component",
                    "DDMMMYYYY",
                    "DDMMMYYYY",
                    "Y",
                    "Y",
                ],
                {
                    "label": "[...]",
                    "values": ["...", "...", "...", "...", "...", "...", "...", "...", "..."],
                },
            ],
            footnotes=[
                "Event definitions, adjudication rules, and hospitalization criteria per protocol and SAP."
            ],
            dataset_source="ADSL, ADEFF, ADTTE",
            source_listing="L16.2.34",
            program_ref="l_clinical_events.sas",
            shell_family="Non-Oncology Listings",
            study_phase_scope="Phase II-III",
            coverage_summary="Conditional (Phase II-III, Non-Oncology)",
        )
    )

    items.append(
        TFLItem(
            id="L16.2.35",
            title="Listing of Respiratory Exacerbations and Acute Management",
            tfl_type=L,
            section=S162,
            sort_key=35,
            non_oncology_only=True,
            population="Intent-to-Treat (ITT) Population",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Exacerbation Severity",
                "Onset Date",
                "Resolution Date",
                "Systemic Corticosteroids / Antibiotics?",
                "Hospitalization?",
            ],
            shell_rows=[
                ["xxx", "xxxx/xxx", "Gx", "Moderate", "DDMMMYYYY", "DDMMMYYYY", "Y", "N"],
                ["xxx", "xxxx/xxx", "Gx", "Severe", "DDMMMYYYY", "DDMMMYYYY", "Y", "Y"],
                {
                    "label": "[...]",
                    "values": ["...", "...", "...", "...", "...", "...", "...", "..."],
                },
            ],
            footnotes=[
                "Moderate and severe respiratory exacerbations are listed with protocol-defined acute management details."
            ],
            dataset_source="ADSL, ADEFF, ADAE",
            source_listing="L16.2.35",
            program_ref="l_resp_exac.sas",
            shell_family="Respiratory Exacerbation",
            study_phase_scope="Phase II-III",
            coverage_summary="Core (Phase II-III, Non-Oncology)",
        )
    )

    items.append(
        TFLItem(
            id="L16.2.36",
            title="Listing of Adjudicated Cardiovascular Events and Heart Failure Hospitalizations",
            tfl_type=L,
            section=S162,
            sort_key=36,
            non_oncology_only=True,
            population="Intent-to-Treat (ITT) Population",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Adjudicated Event",
                "Event Date",
                "Hospitalization Start",
                "Hospitalization End",
                "Outcome",
            ],
            shell_rows=[
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "Non-fatal Myocardial Infarction",
                    "DDMMMYYYY",
                    "DDMMMYYYY",
                    "DDMMMYYYY",
                    "Recovered",
                ],
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "Heart Failure Hospitalization",
                    "DDMMMYYYY",
                    "DDMMMYYYY",
                    "DDMMMYYYY",
                    "Ongoing / Recovered",
                ],
                {
                    "label": "[...]",
                    "values": ["...", "...", "...", "...", "...", "...", "...", "..."],
                },
            ],
            footnotes=[
                "Events are adjudicated per cardiovascular endpoint charter where applicable."
            ],
            dataset_source="ADSL, ADTTE, ADAE",
            source_listing="L16.2.36",
            program_ref="l_cv_events.sas",
            shell_family="Cardiovascular MACE and HF Hospitalization",
            study_phase_scope="Phase II-III",
            coverage_summary="Core (Phase II-III, Non-Oncology)",
        )
    )

    items.append(
        TFLItem(
            id="L16.2.37",
            title="Listing of Autoimmune Flares, Rescue Therapy, and Corticosteroid Escalation",
            tfl_type=L,
            section=S162,
            sort_key=37,
            non_oncology_only=True,
            population="Intent-to-Treat (ITT) Population",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Flare Category",
                "Flare Date",
                "Rescue Therapy",
                "Steroid Escalation?",
                "Responder Status",
            ],
            shell_rows=[
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "Joint Flare",
                    "DDMMMYYYY",
                    "Methotrexate",
                    "Y",
                    "Non-Responder",
                ],
                [
                    "xxx",
                    "xxxx/xxx",
                    "Gx",
                    "Skin Flare",
                    "DDMMMYYYY",
                    "Topical / Systemic therapy",
                    "N",
                    "Responder",
                ],
                {
                    "label": "[...]",
                    "values": ["...", "...", "...", "...", "...", "...", "...", "..."],
                },
            ],
            footnotes=[
                "Flare and rescue-therapy events reflect protocol-defined autoimmune disease activity rules."
            ],
            dataset_source="ADSL, ADCM, ADEFF",
            source_listing="L16.2.37",
            program_ref="l_autoimmune_flare.sas",
            shell_family="Autoimmune Flare and Responder",
            study_phase_scope="Phase II-III",
            coverage_summary="Core (Phase II-III, Non-Oncology)",
        )
    )

    items.append(
        TFLItem(
            id="L16.2.38",
            title="Listing of Metabolic, Glycemic, and Body Weight Assessments by Subject and Visit",
            tfl_type=L,
            section=S162,
            sort_key=38,
            non_oncology_only=True,
            population="Full Analysis Set (FAS)",
            placeholder_columns=[
                "Site",
                "Subject",
                "Group",
                "Visit",
                "Visit Date",
                "HbA1c (%)",
                "FPG (mg/dL)",
                "Body Weight (kg)",
                "BMI (kg/m2)",
            ],
            shell_rows=[
                ["Subject listing rows omitted", "...", "...", "...", "...", "...", "...", "...", "..."],
            ],
            footnotes=[
                "Metabolic parameters collected per protocol-specified schedule. "
                "Missing assessments are noted as 'M' in the corresponding field."
            ],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.38",
            program_ref="l_metabolic_assess.sas",
            shell_family="Metabolic Endpoint",
            study_phase_scope="Phase II-III",
            coverage_summary="Core (Phase II-III, Non-Oncology)",
        )
    )

    return items
