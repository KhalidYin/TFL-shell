"""Section 14.3 catalog definitions: safety shells."""

from tflshell.data.common import *


def build_14_3_items() -> list[TFLItem]:
    """Build Section 14.3 catalog items."""
    items: list[TFLItem] = []

    # 14.3 SAFETY — 30 items (AE → Deaths → Labs → VS → ECG)
    # =====================================================================

    items.append(
        TFLItem(
            id="T14.3.1.1",
            title="Overall Summary of Treatment-Emergent Adverse Events",
            tfl_type=T,
            section=S143,
            sort_key=1,
            population="Safety Population",
            placeholder_columns=[
                "Adverse Event Category",
                "XXX Group 1\n(N=XX)\nn (%) [E]",
                "XXX Group 2\n(N=XX)\nn (%) [E]",
                "...",
                "Overall\n(N=XX)\nn (%) [E]",
            ],
            shell_rows=[
                {
                    "label": "Any TEAE",
                    "bold": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "Drug-Related TEAE",
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "CTCAE Grade >=3 TEAE",
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "Drug-Related Grade >=3 TEAE",
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "Serious TEAE (SAE)",
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "Drug-Related SAE",
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "TEAE Leading to Treatment Discontinuation",
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "TEAE Leading to Dose Interruption",
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "TEAE Leading to Dose Reduction",
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "Fatal TEAE (Grade 5)",
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "TEAE: onset on/after first dose through 30 days after last dose. CTCAE v[xx]. MedDRA [xx.x]."
            ],
            dataset_source="ADSL, ADAE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ae_overview.sas",
            dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.1.2",
            title="TEAEs by System Organ Class and Preferred Term (>=5% in Any Arm)",
            tfl_type=T,
            section=S143,
            sort_key=2,
            population="Safety Population",
            placeholder_columns=H2_EVENTS,
            shell_rows=[
                {
                    "label": "Any TEAE",
                    "bold": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "Gastrointestinal disorders",
                    "bold": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "  Nausea",
                    "indent": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "  Diarrhoea",
                    "indent": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "  Vomiting",
                    "indent": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "  Constipation",
                    "indent": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "General disorders and administration site conditions",
                    "bold": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "  Fatigue",
                    "indent": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "  Pyrexia",
                    "indent": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "  Asthenia",
                    "indent": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "Blood and lymphatic system disorders",
                    "bold": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "  Anaemia",
                    "indent": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "  Neutropenia",
                    "indent": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "  Thrombocytopenia",
                    "indent": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "Metabolism and nutrition disorders",
                    "bold": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "  Decreased appetite",
                    "indent": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "  Hypokalaemia",
                    "indent": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "Skin and subcutaneous tissue disorders",
                    "bold": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "  Rash",
                    "indent": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "  Pruritus",
                    "indent": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "Nervous system disorders",
                    "bold": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "  Headache",
                    "indent": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "  Dizziness",
                    "indent": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "Respiratory, thoracic and mediastinal disorders",
                    "bold": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "  Cough",
                    "indent": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "  Dyspnoea",
                    "indent": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "Infections and infestations",
                    "bold": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "  Upper respiratory tract infection",
                    "indent": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "Sorted alphabetically by SOC; PTs by descending frequency in G1. "
                "[E]=total events. MedDRA [xx.x]. CTCAE [xx]."
            ],
            dataset_source="ADSL, ADAE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ae_soc_pt.sas",
            dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.1.3",
            title="TEAEs by SOC, PT, and Maximum CTCAE Grade (Group 1)",
            tfl_type=T,
            section=S143,
            sort_key=3,
            population="Safety Population",
            placeholder_columns=[
                "System Organ Class\nPreferred Term",
                "Grade 1\nn (%)",
                "Grade 2\nn (%)",
                "Grade 3\nn (%)",
                "Grade 4\nn (%)",
                "Grade 5\nn (%)",
                "Any Grade\nn (%)",
            ],
            shell_rows=[
                ["Gastrointestinal disorders", "", "", "", "", "", "xx (xx.x)"],
                [
                    "  Nausea",
                    "xx (xx.x)",
                    "xx (xx.x)",
                    "xx (xx.x)",
                    "xx (xx.x)",
                    "xx (xx.x)",
                    "xx (xx.x)",
                ],
                EROW6,
            ],
            footnotes=["CTCAE [xx]. Table repeated for Group 2 and Overall."],
            dataset_source="ADSL, ADAE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ae_grade.sas",
            dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.1.4",
            title="Drug-Related TEAEs by SOC, PT, and Relationship",
            tfl_type=T,
            section=S143,
            sort_key=4,
            population="Safety Population",
            placeholder_columns=H2_SOCPT,
            shell_rows=[
                ["Any Drug-Related TEAE", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["Gastrointestinal disorders", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["  Nausea", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["  Diarrhea", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                EROW,
            ],
            dataset_source="ADSL, ADAE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ae_related.sas",
            dictionary_versions={"MedDRA": "[xx.x]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.1.5",
            title="Serious Adverse Events by SOC and PT",
            tfl_type=T,
            section=S143,
            sort_key=5,
            population="Safety Population",
            placeholder_columns=H2_EVENTS,
            shell_rows=[
                {
                    "label": "Any SAE",
                    "bold": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "Infections and infestations",
                    "bold": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "  Pneumonia",
                    "indent": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "  Sepsis",
                    "indent": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "Gastrointestinal disorders",
                    "bold": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "  Diarrhoea",
                    "indent": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "  Intestinal Obstruction",
                    "indent": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "Respiratory, thoracic and mediastinal disorders",
                    "bold": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "  Pulmonary Embolism",
                    "indent": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=["SAE defined per ICH E2A criteria."],
            dataset_source="ADSL, ADAE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_sae_soc_pt.sas",
            dictionary_versions={"MedDRA": "[xx.x]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.1.6",
            title="TEAEs Leading to Treatment Discontinuation by SOC and PT",
            tfl_type=T,
            section=S143,
            sort_key=6,
            population="Safety Population",
            placeholder_columns=H2_SOCPT,
            shell_rows=[
                {
                    "label": "Any TEAE Leading to Discontinuation",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Gastrointestinal disorders",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Diarrhoea",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Nausea",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "General disorders and administration site conditions",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Asthenia",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Investigations",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  ALT Increased",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  AST Increased",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            dataset_source="ADSL, ADAE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ae_disc.sas",
            dictionary_versions={"MedDRA": "[xx.x]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.1.7",
            title="TEAEs Leading to Dose Reduction or Interruption by SOC and PT",
            tfl_type=T,
            section=S143,
            sort_key=7,
            population="Safety Population",
            placeholder_columns=H2_SOCPT,
            shell_rows=[
                [
                    "Any TEAE Leading to Dose Modification",
                    "xx (xx.x)",
                    "xx (xx.x)",
                    "...",
                    "xx (xx.x)",
                ],
                ["Gastrointestinal disorders", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["  Diarrhea", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["  Nausea", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                EROW,
            ],
            dataset_source="ADSL, ADAE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ae_dose_mod.sas",
            dictionary_versions={"MedDRA": "[xx.x]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.2.1",
            title="Summary of Deaths",
            tfl_type=T,
            section=S143,
            sort_key=1,
            population="Safety Population",
            placeholder_columns=H2_NPCT,
            shell_rows=[
                {
                    "label": "Total Deaths",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Due to Adverse Event",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Due to Progressive Disease",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Due to Other Causes",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "On-treatment Deaths (<=30 days of last dose)",
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Post-treatment Deaths (>30 days of last dose)",
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            dataset_source="ADSL, ADAE, ADTTE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_deaths.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.1.8",
            title="TEAEs Occurring in >=5% of Subjects by PT",
            tfl_type=T,
            section=S143,
            sort_key=8,
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
            dataset_source="ADSL, ADAE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ae_5pct.sas",
            dictionary_versions={"MedDRA": "[xx.x]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.1.9",
            title="TEAEs by Cycle / Treatment Period",
            tfl_type=T,
            section=S143,
            sort_key=9,
            population="Safety Population",
            placeholder_columns=[
                "Cycle",
                "N at Risk\n(G1 / G2)",
                "G1 >=1 TEAE\nn (%)",
                "G2 >=1 TEAE\nn (%)",
                "...\n...\nOverall\nn (%)",
            ],
            shell_rows=[
                ["Cycle 1", "xx / xx", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["Cycle 2", "xx / xx", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["Cycle 3", "xx / xx", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                EROW,
            ],
            dataset_source="ADSL, ADAE, ADEX",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ae_by_cycle.sas",
            dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.1.10",
            title="Exposure-Adjusted TEAE Incidence Rates (per 100 Patient-Years)",
            tfl_type=T,
            section=S143,
            sort_key=10,
            population="Safety Population",
            placeholder_columns=[
                "Preferred Term",
                "G1 Rate\n[95% CI]",
                "G2 Rate\n[95% CI]",
                "...\n...\nOverall\n[95% CI]",
            ],
            shell_rows=[
                [
                    "Fatigue",
                    "xx.xx [xx.xx, xx.xx]",
                    "xx.xx [xx.xx, xx.xx]",
                    "...",
                    "xx.xx [xx.xx, xx.xx]",
                ],
                [
                    "Nausea",
                    "xx.xx [xx.xx, xx.xx]",
                    "xx.xx [xx.xx, xx.xx]",
                    "...",
                    "xx.xx [xx.xx, xx.xx]",
                ],
                EROW,
            ],
            dataset_source="ADSL, ADAE, ADEX",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ae_adj_rate.sas",
            dictionary_versions={"MedDRA": "[xx.x]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.1.11",
            title="TEAEs by Age Group Subgroup",
            tfl_type=T,
            section=S143,
            sort_key=11,
            population="Safety Population",
            placeholder_columns=[
                "Preferred Term",
                "Age <65\n(N=XX) n (%)",
                "Age >=65\n(N=XX) n (%)",
                "...\n...\nOverall\n(N=XX) n (%)",
            ],
            shell_rows=[
                ["Fatigue", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["Nausea", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                EROW,
            ],
            dataset_source="ADSL, ADAE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ae_age.sas",
            dictionary_versions={"MedDRA": "[xx.x]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.1.12",
            title="TEAEs by Sex Subgroup",
            tfl_type=T,
            section=S143,
            sort_key=12,
            population="Safety Population",
            placeholder_columns=[
                "Preferred Term",
                "Male\n(N=XX) n (%)",
                "Female\n(N=XX) n (%)",
                "...\n...\nOverall\n(N=XX) n (%)",
            ],
            shell_rows=[
                ["Fatigue", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["Nausea", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                EROW,
            ],
            dataset_source="ADSL, ADAE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ae_sex.sas",
            dictionary_versions={"MedDRA": "[xx.x]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.2.2",
            title="Hy's Law Cases — Liver Chemistry Screening",
            tfl_type=T,
            section=S143,
            sort_key=2,
            population="Safety Population with Baseline and Post-Baseline Labs",
            placeholder_columns=[
                "Subject",
                "Group",
                "ALT\n(xULN)",
                "AST\n(xULN)",
                "TBL\n(xULN)",
                "ALP\n(xULN)",
                "Hy's Law\nMet?",
            ],
            shell_rows=[
                ["xxxx/xxx", "Gx", "x.x", "x.x", "x.x", "x.x", "Yes / No"],
                EROW6,
            ],
            footnotes=[
                "Hy's Law: ALT/AST >=3xULN, TBL >=2xULN, ALP <2xULN, no alternative etiology."
            ],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_hys_law.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.3.1",
            title="Laboratory Parameters — Shift Table (Baseline to Worst Post-Baseline)",
            tfl_type=T,
            section=S143,
            sort_key=1,
            population="Safety Population",
            placeholder_columns=[
                "Parameter\n(Unit)",
                "Baseline\nGrade",
                "Worst Post-BL\nGrade",
                "G1\nn (%)",
                "G2\nn (%)",
                "...\n...\nOverall\nn (%)",
            ],
            shell_rows=[
                [
                    "Hemoglobin (g/dL)",
                    "Normal",
                    "Low",
                    "xx (xx.x)",
                    "xx (xx.x)",
                    "...",
                    "xx (xx.x)",
                ],
                ["", "Normal", "Normal", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["", "Low", "Low", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                [
                    "ALT (U/L)",
                    "Normal",
                    "High (>ULN)",
                    "xx (xx.x)",
                    "xx (xx.x)",
                    "...",
                    "xx (xx.x)",
                ],
                EROW6,
            ],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_lab_shift.sas",
            dictionary_versions={"CTCAE": "[xx]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.3.2",
            title="Hematology Parameters — Summary Statistics by Visit",
            tfl_type=T,
            section=S143,
            sort_key=2,
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
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_heme_by_visit.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.3.3",
            title="Clinical Chemistry Parameters — Summary Statistics by Visit",
            tfl_type=T,
            section=S143,
            sort_key=3,
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
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_chem_by_visit.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.3.4",
            title="Laboratory Abnormalities — Grade >=3 Listing",
            tfl_type=T,
            section=S143,
            sort_key=4,
            population="Safety Population",
            placeholder_columns=[
                "Subject",
                "Group",
                "Visit",
                "Parameter",
                "Result",
                "Unit",
                "ULN",
                "CTCAE\nGrade",
            ],
            shell_rows=[
                ["xxxx/xxx", "Gx", "Wk xx", "ALT", "xxx", "U/L", "xx", "x"],
                EROW6,
            ],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="l_lab_grade3.sas",
            dictionary_versions={"CTCAE": "[xx]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.3.5",
            title="Laboratory Toxicity Grade Shift Over Time (by Cycle)",
            tfl_type=T,
            section=S143,
            sort_key=5,
            population="Safety Population",
            placeholder_columns=[
                "Parameter",
                "Cycle",
                "Baseline\nGrade",
                "Max Post-BL\nGrade",
                "G1\nn/N (%)",
                "G2\nn/N (%)",
                "...\n...\nOverall\nn/N (%)",
            ],
            shell_rows=[
                [
                    "ALT",
                    "Cycle 1",
                    "0-1",
                    "2",
                    "xx/xx (xx.x)",
                    "xx/xx (xx.x)",
                    "...",
                    "xx/xx (xx.x)",
                ],
                [
                    "ALT",
                    "Cycle 1",
                    "0-1",
                    "3-4",
                    "xx/xx (xx.x)",
                    "xx/xx (xx.x)",
                    "...",
                    "xx/xx (xx.x)",
                ],
                EROW6,
            ],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_lab_shift_cycle.sas",
            dictionary_versions={"CTCAE": "[xx]"},
        )
    )

    items.append(
        TFLItem(
            id="F14.3.3.1",
            title="Mean (+/- SD) Change in Laboratory Parameters Over Time",
            tfl_type=F,
            section=S143,
            sort_key=26,
            population="Safety Population",
            figure_description="Multi-panel line plot: mean ± SD change in Hgb, Plt, ANC, ALT, AST, Creatinine.",
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="f_lab_longitudinal.sas",
            figure_type="longitudinal",
            figure_width_inches=6,
            figure_height_inches=4,
        )
    )

    items.append(
        TFLItem(
            id="F14.3.3.2",
            title="Box Plot — Liver Function Tests by Visit",
            tfl_type=F,
            section=S143,
            sort_key=27,
            population="Safety Population",
            figure_description="Box plots: ALT, AST, ALP, Total Bilirubin by visit, side-by-side arms, ULN ref lines.",
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="f_lft_box.sas",
            figure_type="box_plot",
            figure_width_inches=6,
            figure_height_inches=4,
        )
    )

    items.append(
        TFLItem(
            id="T14.3.4.1",
            title="Vital Signs — Summary Statistics by Visit",
            tfl_type=T,
            section=S143,
            sort_key=1,
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
            dataset_source="ADSL, ADVS",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_vs_by_visit.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.4.2",
            title="Vital Signs — Clinically Notable Abnormalities by Visit",
            tfl_type=T,
            section=S143,
            sort_key=2,
            population="Safety Population",
            placeholder_columns=[
                "Parameter",
                "Criterion",
                "G1\nn (%)",
                "G2\nn (%)",
                "...\n...\nOverall\nn (%)",
            ],
            shell_rows=[
                [
                    "SBP",
                    "<=90 mmHg and decrease >=20",
                    "xx (xx.x)",
                    "xx (xx.x)",
                    "...",
                    "xx (xx.x)",
                ],
                [
                    "SBP",
                    ">=180 mmHg and increase >=20",
                    "xx (xx.x)",
                    "xx (xx.x)",
                    "...",
                    "xx (xx.x)",
                ],
                [
                    "DBP",
                    "<=50 mmHg and decrease >=15",
                    "xx (xx.x)",
                    "xx (xx.x)",
                    "...",
                    "xx (xx.x)",
                ],
                EROW,
            ],
            dataset_source="ADSL, ADVS",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_vs_notable.sas",
        )
    )

    items.append(
        TFLItem(
            id="F14.3.4.1",
            title="Mean (+/- SD) Vital Signs Over Time",
            tfl_type=F,
            section=S143,
            sort_key=17,
            population="Safety Population",
            figure_description="Multi-panel: mean ± SD of SBP, DBP, HR, Weight over visits.",
            dataset_source="ADSL, ADVS",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="f_vs_longitudinal.sas",
            figure_type="longitudinal",
            figure_width_inches=6,
            figure_height_inches=4,
        )
    )

    items.append(
        TFLItem(
            id="F14.3.3.3",
            title="Liver Function Panel — Mean Over Time with ULN Reference",
            tfl_type=F,
            section=S143,
            sort_key=28,
            population="Safety Population",
            figure_description="Line plot: ALT, AST, ALP, TBL means over visits with ULN lines.",
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="f_lft_uln.sas",
            figure_type="longitudinal",
            figure_width_inches=5.5,
            figure_height_inches=3.5,
        )
    )

    items.append(
        TFLItem(
            id="T14.3.4.3",
            title="ECG Parameters — Summary Statistics by Visit",
            tfl_type=T,
            section=S143,
            sort_key=3,
            population="Safety Population with ECG Data",
            placeholder_columns=H2_LAB,
            shell_rows=[
                ["QTcF (ms)", "", "", "", "", ""],
                ["  Baseline — Mean (SD)", "xxx (xx)", "xxx (xx)", "...", "xxx (xx)"],
                ["  Week 4 — Mean (SD)", "xxx (xx)", "xxx (xx)", "...", "xxx (xx)"],
                ["  Change from BL", "xx (xx)", "xx (xx)", "...", "xx (xx)"],
                EROW,
            ],
            footnotes=[
                "QTcF = Fridericia correction. Triplicate ECGs at each visit; mean analyzed."
            ],
            dataset_source="ADSL, ADEG",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ecg_by_visit.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.4.4",
            title="ECG QTcF Categorical Analysis",
            tfl_type=T,
            section=S143,
            sort_key=4,
            population="Safety Population with ECG Data",
            placeholder_columns=[
                "QTcF Category",
                "G1\n(N=XX) n (%)",
                "G2\n(N=XX) n (%)",
                "...\n...\nOverall\n(N=XX) n (%)",
            ],
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
            dataset_source="ADSL, ADEG",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_qtcf_cat.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.4.5",
            title="ECG Qualitative Assessment — Shift Table",
            tfl_type=T,
            section=S143,
            sort_key=5,
            population="Safety Population with ECG Data",
            placeholder_columns=[
                "Baseline",
                "Worst\nPost-Baseline",
                "G1\nn (%)",
                "G2\nn (%)",
                "...\n...\nOverall\nn (%)",
            ],
            shell_rows=[
                ["Normal", "Normal", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["Normal", "Abnormal NCS", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["Normal", "Abnormal CS", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                EROW,
            ],
            footnotes=["NCS = Not Clinically Significant. CS = Clinically Significant."],
            dataset_source="ADSL, ADEG",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ecg_shift.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.1.13",
            title="Infusion-Related Reactions by Preferred Term",
            tfl_type=T,
            section=S143,
            sort_key=13,
            population="Safety Population",
            placeholder_columns=H2_SOCPT,
            shell_rows=[
                ["Any Infusion-Related Reaction", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["Pyrexia", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["Chills", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                EROW,
            ],
            dataset_source="ADSL, ADAE, ADEX",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_irr.sas",
            dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.2.3",
            title="ECOG Performance Status Shift Table",
            tfl_type=T,
            section=S143,
            sort_key=3,
            population="Safety Population",
            placeholder_columns=[
                "Baseline\nECOG",
                "Worst Post-BL\nECOG",
                "G1\nn (%)",
                "G2\nn (%)",
                "...\n...\nOverall\nn (%)",
            ],
            shell_rows=[
                ["0", "0", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["0", "1", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["0", ">=2", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["1", "1", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                EROW,
            ],
            dataset_source="ADSL, ADQS",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ecog_shift.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.1.14",
            title="Adverse Events of Special Interest (AESI) — Summary",
            tfl_type=T,
            section=S143,
            sort_key=14,
            population="Safety Population",
            placeholder_columns=[
                "AESI Category",
                "XXX Group 1\n(N=XX)\nn (%) [E]",
                "XXX Group 2\n(N=XX)\nn (%) [E]",
                "...",
                "Overall\n(N=XX)\nn (%) [E]",
            ],
            shell_rows=[
                {
                    "label": "Subjects with Any AESI",
                    "bold": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "AESI Category 1: Infusion-Related Reactions",
                    "bold": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "  Grade 1-2",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Grade >=3",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Serious AESIs",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Leading to Discontinuation",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "AESI Category 2: Hepatotoxicity",
                    "bold": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "  ALT/AST >=3xULN + TBL >=2xULN (Hy's Law)",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  ALT/AST >=5xULN",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  ALT/AST >=10xULN",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "AESI Category 3: Cardiac Events",
                    "bold": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "  QTcF Prolongation >500 ms",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Arrhythmia",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Left Ventricular Dysfunction",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "AESI Category 4: Immunogenicity-Related",
                    "bold": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "  Hypersensitivity / Anaphylaxis",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Cytokine Release Syndrome",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "AESIs pre-specified in protocol [ref] and SAP [ref]. [E] = number of events.",
                "MedDRA [xx.x] and CTCAE [xx] used for coding and grading. Groupings based on SMQ/custom MedDRA queries.",
                "Subjects may have events in more than one AESI category.",
            ],
            dataset_source="ADSL, ADAE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_aesi_summary.sas",
            dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.1.15",
            title="AESI — Time to First Occurrence",
            tfl_type=T,
            section=S143,
            sort_key=15,
            population="Safety Population",
            placeholder_columns=[
                "AESI Category",
                "XXX Group 1\n(N=XX)",
                "XXX Group 2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {"label": "Infusion-Related Reactions", "bold": True},
                {
                    "label": "  Events / N (%)",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Median Time to First Onset, days (Range)",
                    "indent": True,
                    "values": ["xx (x-xx)", "xx (x-xx)", "...", "xx (x-xx)"],
                },
                {"label": "Hepatotoxicity (ALT/AST >=3xULN)", "bold": True},
                {
                    "label": "  Events / N (%)",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Median Time to First Onset, days (Range)",
                    "indent": True,
                    "values": ["xx (x-xx)", "xx (x-xx)", "...", "xx (x-xx)"],
                },
                {"label": "Cardiac Events", "bold": True},
                {
                    "label": "  Events / N (%)",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Median Time to First Onset, days (Range)",
                    "indent": True,
                    "values": ["xx (x-xx)", "xx (x-xx)", "...", "xx (x-xx)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=["Time calculated from first dose of study drug to first AESI occurrence."],
            dataset_source="ADSL, ADAE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_aesi_ttf.sas",
            dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.3.6",
            title="Laboratory Parameters — Descriptive Statistics and Change from Baseline by Visit",
            tfl_type=T,
            section=S143,
            sort_key=6,
            population="Safety Population",
            placeholder_columns=[
                "Parameter\nVisit",
                "Statistic",
                "XXX Group 1\n(N=XX)",
                "XXX Group 2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {"label": "HEMATOLOGY", "bold": True},
                {"label": "Hemoglobin (g/L)", "bold": True},
                {"label": "  Baseline — n", "indent": True, "values": ["xx", "xx", "...", "xx"]},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "  Week 4 — n", "indent": True, "values": ["xx", "xx", "...", "xx"]},
                {
                    "label": "  Week 4 — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Week 4 — Mean Chg from BL (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "  Week 12 — n", "indent": True, "values": ["xx", "xx", "...", "xx"]},
                {
                    "label": "  Week 12 — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Week 12 — Mean Chg from BL (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  End of Treatment — Mean Chg from BL (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "Platelets (10⁹/L)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Week 4 — Mean Chg from BL (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  End of Treatment — Mean Chg from BL (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "LIVER FUNCTION TESTS", "bold": True},
                {"label": "ALT (U/L)", "bold": True},
                {"label": "  Baseline — n", "indent": True, "values": ["xx", "xx", "...", "xx"]},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Week 4 — Mean Chg from BL (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Week 12 — Mean Chg from BL (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  End of Treatment — Mean Chg from BL (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "AST (U/L)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  End of Treatment — Mean Chg from BL (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "Total Bilirubin (µmol/L)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["x.xx (x.xx)", "x.xx (x.xx)", "...", "x.xx (x.xx)"],
                },
                {
                    "label": "  End of Treatment — Mean Chg from BL (SD)",
                    "indent": True,
                    "values": ["x.xx (x.xx)", "x.xx (x.xx)", "...", "x.xx (x.xx)"],
                },
                {"label": "RENAL FUNCTION", "bold": True},
                {"label": "Creatinine (µmol/L)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  End of Treatment — Mean Chg from BL (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "ELECTROLYTES", "bold": True},
                {"label": "Sodium (mmol/L)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "Potassium (mmol/L)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["x.xx (x.xx)", "x.xx (x.xx)", "...", "x.xx (x.xx)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "Baseline = last non-missing assessment on or before first dose date.",
                "Change from Baseline = Visit value - Baseline value. CTCAE [xx] for grading.",
                "Full visit schedule: Screening, Baseline, Week 2, 4, 8, 12, 16, 20, 24, End of Treatment, Follow-up.",
            ],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_lab_chg_bl.sas",
            dictionary_versions={"CTCAE": "[xx]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.3.7",
            title="Laboratory Parameters — CTCAE Grade Shift (Baseline to Worst Post-Baseline)",
            tfl_type=T,
            section=S143,
            sort_key=7,
            population="Safety Population",
            placeholder_columns=[
                "Parameter\nBaseline Grade",
                "Worst Post-BL Grade",
                "G1\nn (%)",
                "G2\nn (%)",
                "...",
                "Overall\nn (%)",
            ],
            shell_rows=[
                {"label": "Hemoglobin (Anemia)", "bold": True},
                {"label": "  Grade 0", "indent": True},
                {
                    "label": "    To Grade 0",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "    To Grade 1",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "    To Grade 2",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "    To Grade 3-4",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "  Grade 1", "indent": True},
                {
                    "label": "    To Grade 1",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "    To Grade 2",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "    To Grade 3-4",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "Neutrophils (Neutropenia)", "bold": True},
                {"label": "  Grade 0", "indent": True},
                {
                    "label": "    To Grade 1-2",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "    To Grade 3",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "    To Grade 4",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "Platelets (Thrombocytopenia)", "bold": True},
                {
                    "label": "  Grade 0 to Grade 1-2",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Grade 0 to Grade 3-4",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "ALT", "bold": True},
                {
                    "label": "  Grade 0 to Grade 1",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Grade 0 to Grade 2",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Grade 0 to Grade 3-4",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "AST", "bold": True},
                {
                    "label": "  Grade 0 to Grade 3-4",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "Creatinine", "bold": True},
                {
                    "label": "  Grade 0 to Grade 1-2",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Grade 0 to Grade 3-4",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "CTCAE [xx] for grading. Baseline = last assessment before first dose. Worst post-baseline = highest grade on treatment.",
                "Percentages based on number of subjects with both baseline and at least one post-baseline assessment.",
            ],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_lab_grade_shift.sas",
            dictionary_versions={"CTCAE": "[xx]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.1.16",
            title="TEAEs by Worst CTCAE Grade and System Organ Class",
            tfl_type=T,
            section=S143,
            sort_key=16,
            population="Safety Population",
            placeholder_columns=[
                "System Organ Class",
                "Grade 1\nn (%)",
                "Grade 2\nn (%)",
                "Grade 3\nn (%)",
                "Grade 4\nn (%)",
                "Grade 5\nn (%)",
                "Any Grade\nn (%)",
            ],
            shell_rows=[
                {
                    "label": "Any TEAE",
                    "bold": True,
                    "values": [
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                    ],
                },
                {
                    "label": "Gastrointestinal disorders",
                    "bold": True,
                    "values": [
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "0",
                        "xx (xx.x)",
                    ],
                },
                {
                    "label": "  Nausea",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "0", "0", "xx (xx.x)"],
                },
                {
                    "label": "  Diarrhoea",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "0", "0", "xx (xx.x)"],
                },
                {
                    "label": "General disorders",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "0", "0", "xx (xx.x)"],
                },
                {
                    "label": "Blood and lymphatic system disorders",
                    "bold": True,
                    "values": [
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "0",
                        "xx (xx.x)",
                    ],
                },
                {
                    "label": "Infections and infestations",
                    "bold": True,
                    "values": [
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "0",
                        "xx (xx.x)",
                    ],
                },
                {"label": "[...]", "values": ["...", "...", "...", "...", "...", "..."]},
            ],
            footnotes=[
                "CTCAE v[xx]. Each subject counted once per SOC at the maximum grade reported. MedDRA [xx.x].",
                "Table shown for Group 1; analogous tables generated for Group 2 and Overall.",
            ],
            dataset_source="ADSL, ADAE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ae_worst_grade.sas",
            dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.1.17",
            title="TEAEs by Preferred Term — Full Frequency Listing (All PTs)",
            tfl_type=T,
            section=S143,
            sort_key=17,
            population="Safety Population",
            placeholder_columns=[
                "Preferred Term",
                "SOC",
                "G1\nn (%)",
                "G2\nn (%)",
                "...",
                "Overall\nn (%)",
            ],
            shell_rows=[
                {
                    "label": "Nausea",
                    "values": [
                        "Gastrointestinal disorders",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "...",
                        "xx (xx.x)",
                    ],
                },
                {
                    "label": "Diarrhoea",
                    "values": [
                        "Gastrointestinal disorders",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "...",
                        "xx (xx.x)",
                    ],
                },
                {
                    "label": "Fatigue",
                    "values": ["General disorders", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Anaemia",
                    "values": ["Blood and lymphatic", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Neutropenia",
                    "values": ["Blood and lymphatic", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Decreased appetite",
                    "values": [
                        "Metabolism and nutrition",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "...",
                        "xx (xx.x)",
                    ],
                },
                {
                    "label": "Rash",
                    "values": [
                        "Skin and subcutaneous",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "...",
                        "xx (xx.x)",
                    ],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "All PTs reported in any treatment group. Sorted by descending frequency in Group 1.",
                "MedDRA [xx.x]. CTCAE [xx]. Each subject counted once per preferred term.",
            ],
            dataset_source="ADSL, ADAE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ae_pt_full.sas",
            dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.1.18",
            title="TEAEs — Maximum Severity by Relationship to Study Drug",
            tfl_type=T,
            section=S143,
            sort_key=18,
            population="Safety Population",
            placeholder_columns=[
                "System Organ Class\nPreferred Term",
                "Related\nAny Grade / Grade >=3",
                "Not Related\nAny Grade / Grade >=3",
                "...",
                "Overall\nAny Grade / Grade >=3",
            ],
            shell_rows=[
                {
                    "label": "Any TEAE",
                    "bold": True,
                    "values": [
                        "xx (xx.x) / xx (xx.x)",
                        "xx (xx.x) / xx (xx.x)",
                        "...",
                        "xx (xx.x) / xx (xx.x)",
                    ],
                },
                {
                    "label": "Gastrointestinal disorders",
                    "bold": True,
                    "values": [
                        "xx (xx.x) / xx (xx.x)",
                        "xx (xx.x) / xx (xx.x)",
                        "...",
                        "xx (xx.x) / xx (xx.x)",
                    ],
                },
                {
                    "label": "  Nausea",
                    "indent": True,
                    "values": [
                        "xx (xx.x) / xx (xx.x)",
                        "xx (xx.x) / xx (xx.x)",
                        "...",
                        "xx (xx.x) / xx (xx.x)",
                    ],
                },
                {
                    "label": "  Diarrhoea",
                    "indent": True,
                    "values": [
                        "xx (xx.x) / xx (xx.x)",
                        "xx (xx.x) / xx (xx.x)",
                        "...",
                        "xx (xx.x) / xx (xx.x)",
                    ],
                },
                {
                    "label": "Blood and lymphatic system disorders",
                    "bold": True,
                    "values": [
                        "xx (xx.x) / xx (xx.x)",
                        "xx (xx.x) / xx (xx.x)",
                        "...",
                        "xx (xx.x) / xx (xx.x)",
                    ],
                },
                {
                    "label": "  Anaemia",
                    "indent": True,
                    "values": [
                        "xx (xx.x) / xx (xx.x)",
                        "xx (xx.x) / xx (xx.x)",
                        "...",
                        "xx (xx.x) / xx (xx.x)",
                    ],
                },
                {
                    "label": "Skin and subcutaneous tissue disorders",
                    "bold": True,
                    "values": [
                        "xx (xx.x) / xx (xx.x)",
                        "xx (xx.x) / xx (xx.x)",
                        "...",
                        "xx (xx.x) / xx (xx.x)",
                    ],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "Related = drug-related per investigator assessment. MedDRA [xx.x]. CTCAE [xx]."
            ],
            dataset_source="ADSL, ADAE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ae_sev_rel.sas",
            dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.1.19",
            title="Time to Onset of TEAEs by System Organ Class",
            tfl_type=T,
            section=S143,
            sort_key=19,
            population="Safety Population",
            placeholder_columns=[
                "System Organ Class",
                "Events\nn",
                "Median Onset\ndays (Range)",
                "<=1 day\nn (%)",
                "2-7 days\nn (%)",
                "8-30 days\nn (%)",
                ">30 days\nn (%)",
            ],
            shell_rows=[
                {
                    "label": "Gastrointestinal disorders",
                    "values": [
                        "xx",
                        "xx (x-xx)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                    ],
                },
                {
                    "label": "General disorders",
                    "values": [
                        "xx",
                        "xx (x-xx)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                    ],
                },
                {
                    "label": "Blood and lymphatic system disorders",
                    "values": [
                        "xx",
                        "xx (x-xx)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                    ],
                },
                {
                    "label": "Skin and subcutaneous tissue disorders",
                    "values": [
                        "xx",
                        "xx (x-xx)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                    ],
                },
                {
                    "label": "Nervous system disorders",
                    "values": [
                        "xx",
                        "xx (x-xx)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                    ],
                },
                {"label": "[...]", "values": ["...", "...", "...", "...", "...", "..."]},
            ],
            footnotes=[
                "Time to onset = (date of first occurrence of TEAE within SOC − date of first dose + 1). MedDRA [xx.x]."
            ],
            dataset_source="ADSL, ADAE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ae_time_onset.sas",
            dictionary_versions={"MedDRA": "[xx.x]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.1.20",
            title="Duration of TEAEs by System Organ Class",
            tfl_type=T,
            section=S143,
            sort_key=20,
            population="Safety Population",
            placeholder_columns=[
                "System Organ Class",
                "Events\nn",
                "Median Duration\ndays (Range)",
                "<=7 days\nn (%)",
                "8-30 days\nn (%)",
                "31-90 days\nn (%)",
                ">90 days\nn (%)",
            ],
            shell_rows=[
                {
                    "label": "Gastrointestinal disorders",
                    "values": [
                        "xx",
                        "xx (x-xx)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                    ],
                },
                {
                    "label": "General disorders",
                    "values": [
                        "xx",
                        "xx (x-xx)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                    ],
                },
                {
                    "label": "Blood and lymphatic system disorders",
                    "values": [
                        "xx",
                        "xx (x-xx)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                    ],
                },
                {
                    "label": "Skin and subcutaneous tissue disorders",
                    "values": [
                        "xx",
                        "xx (x-xx)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                    ],
                },
                {"label": "[...]", "values": ["...", "...", "...", "...", "...", "..."]},
            ],
            footnotes=[
                "Duration = (end date − start date + 1) for each event. Unresolved events censored at data cutoff.",
                "MedDRA [xx.x].",
            ],
            dataset_source="ADSL, ADAE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ae_duration.sas",
            dictionary_versions={"MedDRA": "[xx.x]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.1.21",
            title="TEAEs by Preferred Term and Maximum CTCAE Grade — Group 2",
            tfl_type=T,
            section=S143,
            sort_key=21,
            population="Safety Population",
            placeholder_columns=[
                "System Organ Class\nPreferred Term",
                "Any Grade\nn (%)",
                "Grade 1\nn (%)",
                "Grade 2\nn (%)",
                "Grade 3\nn (%)",
                "Grade 4\nn (%)",
                "Grade 5\nn (%)",
            ],
            shell_rows=[
                {"label": "Gastrointestinal disorders", "bold": True},
                {
                    "label": "  Nausea",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "0", "0"],
                },
                {
                    "label": "  Diarrhoea",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "0", "0"],
                },
                {
                    "label": "  Vomiting",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "0", "0"],
                },
                {"label": "Blood and lymphatic system disorders", "bold": True},
                {
                    "label": "  Anaemia",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "0", "0"],
                },
                {
                    "label": "  Neutropenia",
                    "indent": True,
                    "values": [
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "xx (xx.x)",
                        "0",
                    ],
                },
                {"label": "[...]", "values": ["...", "...", "...", "...", "...", "..."]},
            ],
            footnotes=[
                "Table shown for Group 2. Analogous table generated for Group 1 (T14.3.3). CTCAE [xx]. MedDRA [xx.x]."
            ],
            dataset_source="ADSL, ADAE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ae_grade_g2.sas",
            dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.1.22",
            title="TEAEs by Cycle — Detailed On-Treatment Period Analysis",
            tfl_type=T,
            section=S143,
            sort_key=22,
            population="Safety Population",
            placeholder_columns=[
                "Cycle",
                "Subjects\nat Risk",
                "G1 Any TEAE\nn (%)",
                "G1 Grade >=3\nn (%)",
                "G2 Any TEAE\nn (%)",
                "G2 Grade >=3\nn (%)",
            ],
            shell_rows=[
                {
                    "label": "Cycle 1",
                    "values": ["xx / xx", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"],
                },
                {
                    "label": "Cycle 2",
                    "values": ["xx / xx", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"],
                },
                {
                    "label": "Cycle 3",
                    "values": ["xx / xx", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"],
                },
                {
                    "label": "Cycle 4",
                    "values": ["xx / xx", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"],
                },
                {
                    "label": "Cycle 5",
                    "values": ["xx / xx", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"],
                },
                {
                    "label": "Cycle 6",
                    "values": ["xx / xx", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"],
                },
                {
                    "label": "Cycle >=7",
                    "values": ["xx / xx", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "...", "..."]},
            ],
            footnotes=[
                "Cycle = 21/28-day treatment cycle. Subjects at risk = subjects receiving any dose in the cycle.",
                "TEAE counted in the cycle of onset. MedDRA [xx.x]. CTCAE [xx].",
            ],
            dataset_source="ADSL, ADAE, ADEX",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ae_by_cycle_detail.sas",
            dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.3.8",
            title="Laboratory Parameters — Clinically Significant Abnormalities Summary",
            tfl_type=T,
            section=S143,
            sort_key=8,
            population="Safety Population",
            placeholder_columns=[
                "Parameter (Unit)\nDirection / Criterion",
                "G1\nn/N1 (%)",
                "G2\nn/N2 (%)",
                "...",
                "Overall\nn/N (%)",
            ],
            shell_rows=[
                {"label": "HEMATOLOGY", "bold": True},
                {"label": "Hemoglobin (g/L)", "bold": True},
                {
                    "label": "  Grade 3-4 (<80 g/L)",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "  Decrease from BL >=20 g/L",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "Neutrophils (10⁹/L)", "bold": True},
                {
                    "label": "  Grade 3-4 (<1.0 ×10⁹/L)",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "Platelets (10⁹/L)", "bold": True},
                {
                    "label": "  Grade 3-4 (<50 ×10⁹/L)",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "LIVER FUNCTION", "bold": True},
                {"label": "ALT (U/L)", "bold": True},
                {
                    "label": "  >=3 × ULN",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "  >=5 × ULN",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "  >=10 × ULN",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "  >=20 × ULN",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "Total Bilirubin (µmol/L)", "bold": True},
                {
                    "label": "  >=2 × ULN",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "RENAL FUNCTION", "bold": True},
                {"label": "Creatinine (µmol/L)", "bold": True},
                {
                    "label": "  >=1.5 × Baseline",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "  >=2 × Baseline",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "eGFR (mL/min/1.73m²)", "bold": True},
                {
                    "label": "  <60 (Grade 2)",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "  <30 (Grade 4)",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "N1/N2 = number of subjects with non-missing baseline and >=1 post-baseline assessment.",
                "Percentages based on N1/N2 per arm. CTCAE [xx]. Criteria based on protocol-defined thresholds and CTCAE grading.",
            ],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_lab_cs_abn.sas",
            dictionary_versions={"CTCAE": "[xx]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.3.9",
            title="Hematology — Shift Table by CTCAE Grade (Baseline to Worst Post-Baseline) — Detailed",
            tfl_type=T,
            section=S143,
            sort_key=9,
            population="Safety Population",
            placeholder_columns=[
                "Parameter\nBaseline Grade",
                "Worst Post-BL\nGrade",
                "G1\nn/N (%)",
                "G2\nn/N (%)",
                "...",
                "Overall\nn/N (%)",
            ],
            shell_rows=[
                {"label": "Hemoglobin — Anemia", "bold": True},
                {"label": "  Grade 0", "indent": True},
                {
                    "label": "    Remained Grade 0",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "    Worsened to Grade 1",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "    Worsened to Grade 2",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "    Worsened to Grade 3-4",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "  Grade 1-2 at Baseline", "indent": True},
                {
                    "label": "    Improved to Grade 0",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "    Remained Grade 1-2",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "    Worsened to Grade 3-4",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "Neutrophils — Neutropenia", "bold": True},
                {
                    "label": "  Grade 0 to Grade 1-2",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "  Grade 0 to Grade 3",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "  Grade 0 to Grade 4",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "Platelets — Thrombocytopenia", "bold": True},
                {
                    "label": "  Grade 0 to Grade 1-2",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "  Grade 0 to Grade 3-4",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "N = subjects with both baseline and >=1 post-baseline assessment. CTCAE [xx].",
                "Worst post-baseline = maximum CTCAE grade on treatment.",
            ],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_heme_shift_detail.sas",
            dictionary_versions={"CTCAE": "[xx]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.3.10",
            title="Clinical Chemistry — Shift Table (Normal Range Based) — Baseline to Worst Post-Baseline",
            tfl_type=T,
            section=S143,
            sort_key=10,
            population="Safety Population",
            placeholder_columns=[
                "Parameter (Unit)\nBaseline Category",
                "Worst Post-BL Category",
                "G1\nn/N (%)",
                "G2\nn/N (%)",
                "...",
                "Overall\nn/N (%)",
            ],
            shell_rows=[
                {"label": "ALT (U/L)", "bold": True},
                {"label": "  Normal", "indent": True},
                {
                    "label": "    Normal",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "    >1-3 × ULN",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "    >3-5 × ULN",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "    >5 × ULN",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "AST (U/L)", "bold": True},
                {
                    "label": "  Normal → >3 × ULN",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "Total Bilirubin (µmol/L)", "bold": True},
                {
                    "label": "  Normal → >1.5 × ULN",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "  Normal → >2 × ULN",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "Creatinine (µmol/L)", "bold": True},
                {
                    "label": "  Normal → >1.5 × BL",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "Normal range per central laboratory reference ranges. BL = Baseline. ULN = Upper Limit of Normal.",
                "Percentages based on subjects with non-missing baseline and >=1 post-baseline result.",
            ],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_chem_shift_nr.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.4.6",
            title="Vital Signs — Shift Table (Normal to Clinically Notable)",
            tfl_type=T,
            section=S143,
            sort_key=6,
            population="Safety Population",
            placeholder_columns=[
                "Parameter\nCriterion",
                "G1\nn/N (%)",
                "G2\nn/N (%)",
                "...",
                "Overall\nn/N (%)",
            ],
            shell_rows=[
                {"label": "Systolic BP", "bold": True},
                {
                    "label": "  Baseline Normal → High (>=160 mmHg)",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "  Baseline Normal → Low (<=90 mmHg)",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "Diastolic BP", "bold": True},
                {
                    "label": "  Baseline Normal → High (>=100 mmHg)",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "  Baseline Normal → Low (<=50 mmHg)",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "Heart Rate", "bold": True},
                {
                    "label": "  Baseline Normal → Tachycardia (>=100 bpm)",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "  Baseline Normal → Bradycardia (<=50 bpm)",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "QTcF Interval", "bold": True},
                {
                    "label": "  Baseline <=450 ms → >450-480 ms",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "  Baseline <=450 ms → >480-500 ms",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "  Baseline <=450 ms → >500 ms",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "  Increase from BL >30 ms",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "  Increase from BL >60 ms",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "N = subjects with both baseline and >=1 post-baseline assessment.",
                "Clinically notable thresholds per protocol-defined criteria.",
            ],
            dataset_source="ADSL, ADVS, ADEG",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_vs_shift.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.4.7",
            title="Body Weight — Change from Baseline by Visit",
            tfl_type=T,
            section=S143,
            sort_key=7,
            population="Safety Population",
            placeholder_columns=[
                "Visit",
                "Statistic",
                "G1\n(N=XX)",
                "G2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {"label": "Baseline", "bold": True},
                {"label": "  n", "indent": True, "values": ["xx", "xx", "...", "xx"]},
                {
                    "label": "  Mean (SD), kg",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "Week 4", "bold": True},
                {"label": "  n", "indent": True, "values": ["xx", "xx", "...", "xx"]},
                {
                    "label": "  Mean (SD), kg",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Mean Chg from BL (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "Week 12", "bold": True},
                {
                    "label": "  Mean Chg from BL (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "End of Treatment", "bold": True},
                {
                    "label": "  Mean Chg from BL (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "Weight Change Category at EOT", "bold": True},
                {
                    "label": "  >=10% Decrease",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  >=5% to <10% Decrease",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Within ±5%",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  >=5% to <10% Increase",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  >=10% Increase",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "Baseline = last assessment before first dose. Change from BL = visit value − baseline value.",
                "Percentages based on subjects with non-missing data at each visit.",
            ],
            dataset_source="ADSL, ADVS",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_weight_chg.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.4.8",
            title="ECG Parameters — Quantitative Change from Baseline by Visit",
            tfl_type=T,
            section=S143,
            sort_key=8,
            population="Safety Population with ECG Data",
            placeholder_columns=[
                "Parameter\nVisit",
                "Statistic",
                "G1\n(N=XX)",
                "G2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {"label": "Heart Rate (bpm)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Week 4 — Mean Chg (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  End of Treatment — Mean Chg (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "PR Interval (ms)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Week 4 — Mean Chg (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  End of Treatment — Mean Chg (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "QRS Duration (ms)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  End of Treatment — Mean Chg (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "QTcF Interval (ms)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Week 4 — Mean Chg (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Week 12 — Mean Chg (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  End of Treatment — Mean Chg (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "QTcF = Fridericia correction. Triplicate ECGs averaged per timepoint. Change = post-baseline − baseline."
            ],
            dataset_source="ADSL, ADEG",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ecg_chg_bl.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.3.11",
            title="Laboratory Parameters — Worst Post-Baseline Value by Visit Group",
            tfl_type=T,
            section=S143,
            sort_key=11,
            population="Safety Population",
            placeholder_columns=[
                "Parameter (Unit)\nVisit Group",
                "Statistic",
                "G1\n(N=XX)",
                "G2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {"label": "HEMATOLOGY", "bold": True},
                {"label": "Hemoglobin (g/L)", "bold": True},
                {
                    "label": "  Early (Wk 1-4) — Worst, Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Mid (Wk 5-12) — Worst, Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Late (Wk >=13) — Worst, Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "Platelets (10⁹/L)", "bold": True},
                {
                    "label": "  Early (Wk 1-4) — Worst, Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Late (Wk >=13) — Worst, Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "LIVER FUNCTION", "bold": True},
                {"label": "ALT (U/L)", "bold": True},
                {
                    "label": "  Early (Wk 1-4) — Worst, Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Mid (Wk 5-12) — Worst, Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Late (Wk >=13) — Worst, Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "RENAL", "bold": True},
                {"label": "Creatinine (µmol/L)", "bold": True},
                {
                    "label": "  Early (Wk 1-4) — Worst, Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Late (Wk >=13) — Worst, Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "Worst post-baseline = minimum (for Hgb/Plt) or maximum (for ALT/AST/Cr) value in each time window.",
                "Early = Week 1-4, Mid = Week 5-12, Late = Week >=13.",
            ],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_lab_worst_visit.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.1.23",
            title="Adverse Events — Summary of Multiple Occurrences per Subject",
            tfl_type=T,
            section=S143,
            sort_key=23,
            population="Safety Population",
            placeholder_columns=[
                "Number of TEAEs\nper Subject",
                "G1\nn (%)",
                "G2\nn (%)",
                "...",
                "Overall\nn (%)",
            ],
            shell_rows=[
                {
                    "label": "Subjects with >=1 TEAE",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  1 Event",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  2 Events",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  3 Events",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  4 Events",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  >=5 Events",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Total number of TEAEs [E]",
                    "bold": True,
                    "values": ["[xx]", "[xx]", "...", "[xx]"],
                },
                {
                    "label": "Subjects with >=1 Grade >=3 TEAE",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  1 Event",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  2 Events",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  >=3 Events",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "Percentage denominator = number of subjects in the Safety Population per arm. [E] = total event count.",
                "CTCAE [xx]. MedDRA [xx.x].",
            ],
            dataset_source="ADSL, ADAE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ae_mult_occ.sas",
            dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
        )
    )

    # =====================================================================

    # --- 14.3.2 Other Safety Expansion ---
    items.append(
        TFLItem(
            id="T14.3.2.4",
            title="Hy's Law — Component Parameters Detail at Peak Value per Subject",
            tfl_type=T,
            section=S143,
            sort_key=4,
            population="Safety Population with Baseline and >=1 Post-Baseline Labs",
            placeholder_columns=[
                "Subject",
                "Group",
                "Peak ALT\n(xULN)",
                "Peak AST\n(xULN)",
                "Peak TBL\n(xULN)",
                "Peak ALP\n(xULN)",
                "Hy's Law\nMet?",
            ],
            shell_rows=[
                ["xxxx/xxx", "Gx", "xx.x", "xx.x", "xx.x", "xx.x", "Yes / No"],
                ["xxxx/xxx", "Gx", "xx.x", "xx.x", "xx.x", "xx.x", "Yes / No"],
                {"label": "[...]", "values": ["...", "...", "...", "...", "...", "..."]},
            ],
            footnotes=[
                "Hy's Law: ALT/AST >=3xULN + TBL >=2xULN + ALP <2xULN + no alternative etiology. Listing: L16.2.23."
            ],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_hyslaw_detail.sas",
        )
    )

    items.append(
        TFLItem(
            id="F14.3.2.1",
            title="eDISH Plot — Peak ALT vs. Peak Total Bilirubin with Hy's Law Zone",
            tfl_type=F,
            section=S143,
            sort_key=6,
            population="Safety Population with Baseline and Post-Baseline Labs",
            figure_description="eDISH: log-log scatter of peak ALT (xULN) vs. peak TBL (xULN). Quadrant at ALT >=3xULN, TBL >=2xULN = Hy's Law zone. Individual subject dots labeled.",
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="f_edish.sas",
            figure_type="box_plot",
            figure_width_inches=5.5,
            figure_height_inches=5.5,
        )
    )

    items.append(
        TFLItem(
            id="T14.3.2.5",
            title="Deaths — Primary and Secondary Causes with Narrative Cross-Reference",
            tfl_type=T,
            section=S143,
            sort_key=5,
            population="All Randomized Subjects",
            placeholder_columns=[
                "Subject",
                "Group",
                "Primary Cause\nof Death",
                "Secondary Cause",
                "Days from\nFirst Dose",
                "Days from\nLast Dose",
                "Narrative ID",
            ],
            shell_rows=[
                [
                    "xxxx/xxx",
                    "Gx",
                    "Disease Progression",
                    "Respiratory Failure",
                    "xxx",
                    "xx",
                    "NAR-xxxx",
                ],
                [
                    "xxxx/xxx",
                    "Gx",
                    "Adverse Event",
                    "Sepsis / Multi-organ Failure",
                    "xxx",
                    "xx",
                    "NAR-xxxx",
                ],
                {"label": "[...]", "values": ["...", "...", "...", "...", "...", "..."]},
            ],
            footnotes=["Primary cause per Investigator assessment. Listing: L16.2.20."],
            dataset_source="ADSL, ADAE, ADTTE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_death_detail.sas",
        )
    )

    # --- 14.3.3 Lab Expansion (CDISC ADLB) ---
    items.append(
        TFLItem(
            id="T14.3.3.12",
            title="Coagulation Panel (PT, INR, aPTT) — Change from Baseline by Visit",
            tfl_type=T,
            section=S143,
            sort_key=12,
            population="Safety Population",
            placeholder_columns=[
                "Parameter\nVisit",
                "Statistic",
                "G1\n(N=XX)",
                "G2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {"label": "Prothrombin Time (PT, s)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Week 4 — Mean Chg (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  End of Treatment — Mean Chg (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "INR", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  End of Treatment — Mean Chg (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "aPTT (s)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  End of Treatment — Mean Chg (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=["PT/INR/aPTT per central laboratory. Listing: L16.2.26."],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_coag_chg.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.3.13",
            title="Coagulation Panel — Shift Table (Normal / Prolonged, Baseline to Worst Post-BL)",
            tfl_type=T,
            section=S143,
            sort_key=13,
            population="Safety Population",
            placeholder_columns=[
                "Parameter\nBaseline",
                "Worst Post-BL",
                "G1\nn/N (%)",
                "G2\nn/N (%)",
                "...",
                "Overall\nn/N (%)",
            ],
            shell_rows=[
                {"label": "PT", "bold": True},
                {"label": "  Normal", "indent": True},
                {
                    "label": "    Normal",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "    Prolonged (>ULN)",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "aPTT", "bold": True},
                {
                    "label": "  Normal → Prolonged (>ULN)",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_coag_shift.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.3.14",
            title="Urinalysis — Dipstick Parameters Shift (Baseline to Worst Post-Baseline)",
            tfl_type=T,
            section=S143,
            sort_key=14,
            population="Safety Population",
            placeholder_columns=[
                "Parameter\nBaseline Result",
                "Worst Post-BL Result",
                "G1\nn/N (%)",
                "G2\nn/N (%)",
                "...",
                "Overall\nn/N (%)",
            ],
            shell_rows=[
                {"label": "pH", "bold": True},
                {
                    "label": "  Normal (5.0-8.0) → Abnormal",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "Protein", "bold": True},
                {
                    "label": "  Negative → Trace/+",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "  Negative → ++/+++",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "Glucose", "bold": True},
                {
                    "label": "  Negative → Positive",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "Blood", "bold": True},
                {
                    "label": "  Negative → Positive",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "Ketones", "bold": True},
                {
                    "label": "  Negative → Positive",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=["Dipstick urinalysis. Listing: L16.2.25."],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ua_dip_shift.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.3.15",
            title="Lipid Panel (TC, HDL-C, LDL-C, TG) — Change from Baseline by Visit",
            tfl_type=T,
            section=S143,
            sort_key=15,
            population="Safety Population",
            placeholder_columns=[
                "Parameter\nVisit",
                "Statistic",
                "G1\n(N=XX)",
                "G2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {"label": "Total Cholesterol (mmol/L)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Week 12 — Mean Chg (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  End of Treatment — Mean Chg (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "HDL Cholesterol (mmol/L)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  End of Treatment — Mean Chg (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "LDL Cholesterol (mmol/L)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  End of Treatment — Mean Chg (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "Triglycerides (mmol/L)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=["Fasting lipid panel per central laboratory."],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_lipid_chg.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.3.16",
            title="Lipid Panel — NCEP ATP III Category Shift (Baseline to Worst Post-BL)",
            tfl_type=T,
            section=S143,
            sort_key=16,
            population="Safety Population",
            placeholder_columns=[
                "Parameter\nBaseline Category",
                "Worst Post-BL Category",
                "G1\nn/N (%)",
                "G2\nn/N (%)",
                "...",
                "Overall\nn/N (%)",
            ],
            shell_rows=[
                {"label": "LDL-C", "bold": True},
                {
                    "label": "  Optimal (<2.6) → Borderline/High (>=3.4)",
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "HDL-C", "bold": True},
                {
                    "label": "  Normal (>=1.0) → Low (<1.0)",
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "Triglycerides", "bold": True},
                {
                    "label": "  Normal (<1.7) → High (>=2.3)",
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "NCEP ATP III categories. N = subjects with baseline and >=1 post-baseline value."
            ],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_lipid_shift.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.3.17",
            title="Thyroid Function (TSH, Free T3, Free T4) — Change from Baseline by Visit",
            tfl_type=T,
            section=S143,
            sort_key=17,
            population="Safety Population",
            placeholder_columns=[
                "Parameter\nVisit",
                "Statistic",
                "G1\n(N=XX)",
                "G2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {"label": "TSH (mIU/L)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  End of Treatment — Mean Chg (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "Free T3 (pmol/L)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "Free T4 (pmol/L)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  End of Treatment — Mean Chg (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=["Thyroid function panel. TSH reference range: 0.4-4.0 mIU/L."],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_thyroid_chg.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.3.18",
            title="Glucose Metabolism — Fasting Glucose and HbA1c Change from Baseline",
            tfl_type=T,
            section=S143,
            sort_key=18,
            population="Safety Population",
            placeholder_columns=[
                "Parameter\nVisit",
                "Statistic",
                "G1\n(N=XX)",
                "G2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {"label": "Fasting Glucose (mmol/L)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Week 12 — Mean Chg (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  End of Treatment — Mean Chg (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "HbA1c (%)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  End of Treatment — Mean Chg (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=["Fasting >=8 hours for glucose and lipid assessments."],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_glucose_chg.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.3.19",
            title="Cardiac Biomarkers (hs-Troponin I/T, CK-MB, NT-proBNP) — Summary at Baseline and Worst Post-BL",
            tfl_type=T,
            section=S143,
            sort_key=19,
            population="Safety Population",
            placeholder_columns=[
                "Parameter\n(Unit)",
                "Timepoint",
                "Statistic",
                "G1\n(N=XX)",
                "G2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {"label": "hs-Troponin I (ng/L)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Worst Post-BL — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  >=ULN, n (%)",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "CK-MB (ng/mL)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "NT-proBNP (pg/mL)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "Cardiac biomarkers collected at Screening, Baseline, and on-treatment timepoints. Listing: L16.2.27."
            ],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_cardiac_bio.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.3.20",
            title="Pancreatic Enzymes (Amylase, Lipase) — Change from Baseline",
            tfl_type=T,
            section=S143,
            sort_key=20,
            population="Safety Population",
            placeholder_columns=[
                "Parameter\n(Unit)",
                "Statistic",
                "G1\n(N=XX)",
                "G2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {"label": "Amylase (U/L)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Worst Post-BL — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  >=2xULN, n (%)",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "Lipase (U/L)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Worst Post-BL — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  >=2xULN, n (%)",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=["Pancreatic enzymes per central laboratory. ULN = Upper Limit of Normal."],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_pancreas.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.3.21",
            title="Serum Immunoglobulins (IgG, IgA, IgM, IgE) — Change from Baseline",
            tfl_type=T,
            section=S143,
            sort_key=21,
            population="Safety Population",
            placeholder_columns=[
                "Parameter\n(Unit)",
                "Statistic",
                "G1\n(N=XX)",
                "G2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {"label": "IgG (g/L)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  End of Treatment — Mean Chg (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "IgA (g/L)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "IgM (g/L)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "IgE (IU/mL)", "bold": True},
                {
                    "label": "  Baseline — Geo Mean (CV%)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=["Immunoglobulin panel. Listing: L16.2.27."],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ig_chg.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.3.22",
            title="Lymphocyte Subsets (CD3, CD4, CD8, CD19, CD16+CD56) — Change from Baseline by Visit",
            tfl_type=T,
            section=S143,
            sort_key=22,
            population="Safety Population",
            placeholder_columns=[
                "Parameter\n(Unit)",
                "Statistic",
                "G1\n(N=XX)",
                "G2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {"label": "CD3+ T Cells (cells/uL)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx (xx)", "xx (xx)", "...", "xx (xx)"],
                },
                {
                    "label": "  Week 4 — Mean Chg (SD)",
                    "indent": True,
                    "values": ["xx (xx)", "xx (xx)", "...", "xx (xx)"],
                },
                {"label": "CD4+ Helper T Cells (cells/uL)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx (xx)", "xx (xx)", "...", "xx (xx)"],
                },
                {
                    "label": "  End of Treatment — Mean Chg (SD)",
                    "indent": True,
                    "values": ["xx (xx)", "xx (xx)", "...", "xx (xx)"],
                },
                {"label": "CD8+ Cytotoxic T Cells (cells/uL)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx (xx)", "xx (xx)", "...", "xx (xx)"],
                },
                {"label": "CD4/CD8 Ratio", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "CD19+ B Cells (cells/uL)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx (xx)", "xx (xx)", "...", "xx (xx)"],
                },
                {"label": "CD16+CD56+ NK Cells (cells/uL)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx (xx)", "xx (xx)", "...", "xx (xx)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=["Lymphocyte subsets by flow cytometry. Listing: L16.2.28."],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_lymph_subset.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.3.23",
            title="Inflammatory Cytokine Panel (IL-6, TNF-a, IFN-g, IL-1b, IL-10) — Change from Baseline",
            tfl_type=T,
            section=S143,
            sort_key=23,
            population="Safety Population (Subset with Cytokine Data)",
            placeholder_columns=[
                "Cytokine\n(Unit)",
                "Statistic",
                "G1\n(N=XX)",
                "G2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {"label": "IL-6 (pg/mL)", "bold": True},
                {
                    "label": "  Baseline — Geo Mean (CV%)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Cycle 2 — Fold Chg from BL",
                    "indent": True,
                    "values": ["xx.x", "xx.x", "...", "xx.x"],
                },
                {"label": "TNF-alpha (pg/mL)", "bold": True},
                {
                    "label": "  Baseline — Geo Mean (CV%)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "IFN-gamma (pg/mL)", "bold": True},
                {
                    "label": "  Baseline — Geo Mean (CV%)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "IL-1beta (pg/mL)", "bold": True},
                {
                    "label": "  Baseline — Geo Mean (CV%)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "IL-10 (pg/mL)", "bold": True},
                {
                    "label": "  Baseline — Geo Mean (CV%)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=["Cytokine panel by multiplex immunoassay. Listing: L16.2.28."],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_cytokine.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.3.24",
            title="Renal Function — AKI Staging per KDIGO Criteria",
            tfl_type=T,
            section=S143,
            sort_key=24,
            population="Safety Population",
            placeholder_columns=[
                "KDIGO Stage",
                "Criterion",
                "G1\nn/N (%)",
                "G2\nn/N (%)",
                "...",
                "Overall\nn/N (%)",
            ],
            shell_rows=[
                {
                    "label": "Stage 1",
                    "values": [
                        "Cr >=1.5-1.9x BL or >=26.5 umol/L increase",
                        "xx/xx (xx.x)",
                        "xx/xx (xx.x)",
                        "...",
                        "xx/xx (xx.x)",
                    ],
                },
                {
                    "label": "Stage 2",
                    "values": [
                        "Cr >=2.0-2.9x BL",
                        "xx/xx (xx.x)",
                        "xx/xx (xx.x)",
                        "...",
                        "xx/xx (xx.x)",
                    ],
                },
                {
                    "label": "Stage 3",
                    "values": [
                        "Cr >=3.0x BL or >=353.6 umol/L or RRT",
                        "xx/xx (xx.x)",
                        "xx/xx (xx.x)",
                        "...",
                        "xx/xx (xx.x)",
                    ],
                },
                {
                    "label": "Any AKI (Stage 1-3)",
                    "bold": True,
                    "values": ["", "xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
            ],
            footnotes=[
                "KDIGO 2012 criteria. BL = Baseline creatinine. RRT = Renal Replacement Therapy. N = subjects with >=1 post-BL creatinine."
            ],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_aki_kdigo.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.3.25",
            title="Urine Chemistry — Protein, Creatinine, and Protein/Creatinine Ratio",
            tfl_type=T,
            section=S143,
            sort_key=25,
            population="Safety Population",
            placeholder_columns=[
                "Parameter\n(Unit)",
                "Visit",
                "Statistic",
                "G1\n(N=XX)",
                "G2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {"label": "Urine Protein (g/24h)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Week 12 — Mean Chg (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "UPCR (mg/mmol)", "bold": True},
                {
                    "label": "  Baseline — Geo Mean (CV%)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Week 12 — Geo Mean (CV%)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "Microalbumin (mg/L)", "bold": True},
                {
                    "label": "  Baseline — Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=["UPCR = Urine Protein/Creatinine Ratio. Listing: L16.2.25."],
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_urine_chem.sas",
        )
    )

    items.append(
        TFLItem(
            id="F14.3.3.4",
            title="Renal Safety Panel — eGFR Trajectory Over Time by Treatment Arm",
            tfl_type=F,
            section=S143,
            sort_key=29,
            population="Safety Population",
            figure_description="Line plot: mean (+/-SD) eGFR (CKD-EPI) over visits, individual subject spaghetti lines in background, treatment arms in different colors.",
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="f_egfr_traj.sas",
            figure_type="longitudinal",
            figure_width_inches=5.5,
            figure_height_inches=3.5,
        )
    )

    items.append(
        TFLItem(
            id="F14.3.3.5",
            title="Laboratory Toxicity Heatmap — CTCAE Grade by Parameter and Subject",
            tfl_type=F,
            section=S143,
            sort_key=30,
            population="Safety Population",
            figure_description="Heatmap: subjects (rows) vs. lab parameters (columns), color = worst CTCAE grade. Sidebar: treatment arm. Parameters: Hgb, Plt, Neut, ALT, AST, TBL, Cr.",
            dataset_source="ADSL, ADLB",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="f_lab_heatmap.sas",
            figure_type="box_plot",
            figure_width_inches=6.5,
            figure_height_inches=4,
        )
    )

    # --- 14.3.4 VS/ECG/PE Expansion (CDISC ADVS, ADEG, ADPE) ---
    items.append(
        TFLItem(
            id="T14.3.4.9",
            title="Pulse Oximetry (SpO2) — Change from Baseline by Visit",
            tfl_type=T,
            section=S143,
            sort_key=9,
            population="Safety Population",
            placeholder_columns=[
                "Visit",
                "Statistic",
                "G1\n(N=XX)",
                "G2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {"label": "Baseline", "bold": True},
                {"label": "  n", "indent": True, "values": ["xx", "xx", "...", "xx"]},
                {
                    "label": "  Mean (SD), %",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "Week 4 — Mean Chg (SD)",
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "End of Treatment — Mean Chg (SD)",
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "SpO2 <92%, n (%)",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
            ],
            dataset_source="ADSL, ADVS",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_spo2_chg.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.4.10",
            title="Respiratory Rate — Change from Baseline by Visit",
            tfl_type=T,
            section=S143,
            sort_key=10,
            population="Safety Population",
            placeholder_columns=[
                "Visit",
                "Statistic",
                "G1\n(N=XX)",
                "G2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {
                    "label": "Baseline — Mean (SD), breaths/min",
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "Week 4 — Mean Chg (SD)",
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "End of Treatment — Mean Chg (SD)",
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "RR >20 breaths/min, n (%)",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            dataset_source="ADSL, ADVS",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_rr_chg.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.4.11",
            title="Body Temperature — Change from Baseline and Fever Incidence",
            tfl_type=T,
            section=S143,
            sort_key=11,
            population="Safety Population",
            placeholder_columns=[
                "Visit / Criterion",
                "Statistic",
                "G1\n(N=XX)",
                "G2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {
                    "label": "Baseline — Mean (SD), deg C",
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "End of Treatment — Mean Chg (SD)",
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "Fever (>=38.0 deg C) at Any Visit, n (%)",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Grade 1 (38.0-39.0 deg C)",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Grade >=2 (>39.0 deg C)",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=["Temperature measurement method per site SOP. CTCAE [xx]."],
            dataset_source="ADSL, ADVS",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_temp_chg.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.4.12",
            title="Vital Signs — Categorical Outlier Summary (All Visits Pooled)",
            tfl_type=T,
            section=S143,
            sort_key=12,
            population="Safety Population",
            placeholder_columns=[
                "Parameter\nCriterion",
                "G1\nn/N (%)",
                "G2\nn/N (%)",
                "...",
                "Overall\nn/N (%)",
            ],
            shell_rows=[
                {
                    "label": "SBP >=160 mmHg",
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "SBP <=90 mmHg (with >=20 mmHg decrease)",
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "DBP >=100 mmHg",
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "DBP <=50 mmHg (with >=15 mmHg decrease)",
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "HR >=120 bpm",
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "HR <=45 bpm",
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "SpO2 <92%",
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "RR >24 breaths/min",
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=["N = subjects with >=1 post-baseline assessment for each parameter."],
            dataset_source="ADSL, ADVS",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_vs_outlier.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.4.13",
            title="Holter Monitoring Summary — Heart Rate and Arrhythmia Events (Phase 1)",
            tfl_type=T,
            section=S143,
            sort_key=13,
            population="Safety Population (Subset with Holter Data)",
            placeholder_columns=[
                "Parameter",
                "Statistic",
                "G1\n(N=XX)",
                "G2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {
                    "label": "HR — Mean (SD), bpm",
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "HR — Minimum, bpm", "values": ["xx", "xx", "...", "xx"]},
                {"label": "HR — Maximum, bpm", "values": ["xx", "xx", "...", "xx"]},
                {
                    "label": "Ventricular Ectopics — Total per 24h, Median (Range)",
                    "values": ["xx (x-xx)", "xx (x-xx)", "...", "xx (x-xx)"],
                },
                {
                    "label": "Supraventricular Ectopics — Total per 24h, Median (Range)",
                    "values": ["xx (x-xx)", "xx (x-xx)", "...", "xx (x-xx)"],
                },
                {
                    "label": "Ventricular Tachycardia (>=3 beats), n (%)",
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
            ],
            footnotes=[
                "24-hour Holter monitoring at Baseline and post-dose timepoints (Phase 1 only)."
            ],
            dataset_source="ADSL, ADEG",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_holter.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.4.14",
            title="ECG — T-Wave and ST-Segment Morphology Findings by Visit",
            tfl_type=T,
            section=S143,
            sort_key=14,
            population="Safety Population with ECG Data",
            placeholder_columns=[
                "Visit\nFinding",
                "G1\nn/N (%)",
                "G2\nn/N (%)",
                "...",
                "Overall\nn/N (%)",
            ],
            shell_rows=[
                {"label": "Baseline", "bold": True},
                {
                    "label": "  Normal",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "  T-wave abnormality",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "  ST-segment abnormality",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "Worst Post-Baseline", "bold": True},
                {
                    "label": "  Normal",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "  New T-wave abnormality",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "  New ST-segment abnormality",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "Morphology findings per central cardiologist over-read. N = subjects with ECG at that timepoint."
            ],
            dataset_source="ADSL, ADEG",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ecg_morph.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.4.15",
            title="Physical Examination — Abnormal Findings by Body System at Baseline and EOT",
            tfl_type=T,
            section=S143,
            sort_key=15,
            population="Safety Population",
            placeholder_columns=[
                "Body System\nFinding",
                "Baseline\nn (%)",
                "End of Treatment\nn (%)",
            ],
            shell_rows=[
                {"label": "General Appearance", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)"]},
                {
                    "label": "Head/Eyes/Ears/Nose/Throat",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)"],
                },
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
            dataset_source="ADSL, ADPE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_pe_findings.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.4.16",
            title="Physical Examination — New or Worsened Findings from Baseline by Body System",
            tfl_type=T,
            section=S143,
            sort_key=16,
            population="Safety Population",
            placeholder_columns=[
                "Body System",
                "G1\nn/N (%)",
                "G2\nn/N (%)",
                "...",
                "Overall\nn/N (%)",
            ],
            shell_rows=[
                {
                    "label": "Any New or Worsened Finding",
                    "bold": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "Cardiovascular",
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "Respiratory",
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "Abdomen",
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "Neurological",
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "Dermatological",
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "New = not present at Baseline. Worsened = increased severity from Baseline. N = subjects with both BL and >=1 post-BL exam."
            ],
            dataset_source="ADSL, ADPE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_pe_new_worse.sas",
        )
    )

    items.append(
        TFLItem(
            id="F14.3.4.2",
            title="QTcF vs. Plasma Drug Concentration Scatter Plot with LOESS Fit",
            tfl_type=F,
            section=S143,
            sort_key=18,
            population="Safety Population with Time-Matched PK and ECG",
            figure_description="Scatter: placebo-adjusted change from baseline QTcF vs. plasma concentration, LOESS fit with 90% CI band, ICH E14 reference line at 10 ms.",
            dataset_source="ADSL, ADEG, ADPC",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="f_qtcf_conc.sas",
            figure_type="longitudinal",
            figure_width_inches=5.5,
            figure_height_inches=3.5,
        )
    )

    items.append(
        TFLItem(
            id="T14.3.4.17",
            title="Dose-Limiting Toxicities by Dose Level and Cycle 1 Evaluation Window",
            tfl_type=T,
            section=S143,
            sort_key=32,
            population="DLT-Evaluable Population",
            placeholder_columns=[
                "Dose Level / Cohort",
                "Subjects Treated\n(N)",
                "Subjects DLT-Evaluable\n(n)",
                "Subjects with DLT\nn (%)",
                "DLT Terms / Maximum Grade",
            ],
            shell_rows=[
                ["Dose Level 1", "xx", "xx", "xx (xx.x)", "DLT term x / Gr x"],
                ["Dose Level 2", "xx", "xx", "xx (xx.x)", "DLT term x / Gr x"],
                ["Dose Level 3", "xx", "xx", "xx (xx.x)", "DLT term x / Gr x"],
                ["Expansion Cohort", "xx", "xx", "xx (xx.x)", "DLT term x / Gr x"],
                ["[...]", "...", "...", "...", "..."],
            ],
            footnotes=[
                "DLT window and evaluability criteria per dose-escalation section of protocol/SAP. Multiple DLT terms may be summarized per subject."
            ],
            dataset_source="ADSL, ADAE, ADEX",
            source_listing="L16.2.32",
            program_ref="t_dlt_by_dose.sas",
            shell_family="Phase I Safety and Dose Escalation",
            study_phase_scope="Phase I",
            coverage_summary="Core (Phase I)",
        )
    )

    items.append(
        TFLItem(
            id="T14.3.4.18",
            title="Maximum Tolerated Dose / RP2D Determination Summary by Dose Level and Cohort",
            tfl_type=T,
            section=S143,
            sort_key=33,
            population="All Treated Subjects in Dose Escalation",
            placeholder_columns=[
                "Dose Level Decision Summary",
                "Subjects Treated",
                "Observed DLT Rate",
                "Review Committee Decision",
                "Rationale",
            ],
            shell_rows=[
                [
                    "Dose Level 1",
                    "xx",
                    "xx.x%",
                    "Escalate / Expand / Stop",
                    "No protocol-defined DLT threshold met",
                ],
                [
                    "Dose Level 2",
                    "xx",
                    "xx.x%",
                    "Escalate / Expand / Stop",
                    "Observed DLTs within acceptable boundary",
                ],
                [
                    "Dose Level 3",
                    "xx",
                    "xx.x%",
                    "MTD Exceeded / RP2D Selected",
                    "DLT frequency exceeded decision rule",
                ],
                [
                    "Recommended Phase II Dose",
                    "xx",
                    "N/A",
                    "RP2D",
                    "Integrated safety, PK, and target-exposure review",
                ],
            ],
            footnotes=[
                "Review decision rules per protocol-defined escalation algorithm or SRC charter. RP2D may differ from formal MTD."
            ],
            dataset_source="ADSL, ADAE, ADEX, ADPC",
            source_listing="L16.2.32",
            program_ref="t_mtd_rp2d.sas",
            shell_family="Phase I Safety and Dose Escalation",
            study_phase_scope="Phase I",
            coverage_summary="Core (Phase I)",
        )
    )

    return items
