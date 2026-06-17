"""Section 14.4 catalog definitions: special assessments shells."""

from tflshell.data.common import *


def build_14_4_items() -> list[TFLItem]:
    """Build Section 14.4 catalog items."""
    items: list[TFLItem] = []

    # 14.4 SPECIAL ASSESSMENTS — Tables + Figures ONLY (no listings)
    # =====================================================================

    items.append(
        TFLItem(
            id="T14.4.1",
            title="Summary of Pharmacokinetic Concentrations by Timepoint",
            tfl_type=T,
            section=S144,
            sort_key=1,
            population="PK Population",
            placeholder_columns=[
                "Timepoint\n(h)",
                "Statistic",
                "XXX Group 1\n(N=XX)",
                "XXX Group 2\n(N=XX)",
                "...\n...\nOverall\n(N=XX)",
            ],
            shell_rows=[
                [
                    "Pre-dose (0h)",
                    "Mean (SD), ng/mL",
                    "xx.x (xx.x)",
                    "xx.x (xx.x)",
                    "...",
                    "xx.x (xx.x)",
                ],
                [
                    "Cmax (Tmax)",
                    "Mean (SD), ng/mL",
                    "xx.x (xx.x)",
                    "xx.x (xx.x)",
                    "...",
                    "xx.x (xx.x)",
                ],
                [
                    "Cmin (24h)",
                    "Mean (SD), ng/mL",
                    "xx.x (xx.x)",
                    "xx.x (xx.x)",
                    "...",
                    "xx.x (xx.x)",
                ],
                EROW,
            ],
            dataset_source="ADSL, ADPC",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_pk_conc.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.4.2",
            title="Summary of Pharmacokinetic Parameters",
            tfl_type=T,
            section=S144,
            sort_key=2,
            population="PK Population",
            placeholder_columns=[
                "PK Parameter",
                "Statistic",
                "XXX Group 1\n(N=XX)",
                "XXX Group 2\n(N=XX)",
                "...\n...\nOverall\n(N=XX)",
            ],
            shell_rows=[
                [
                    "Cmax (ng/mL)",
                    "Geo Mean (CV%)",
                    "xx.x (xx.x)",
                    "xx.x (xx.x)",
                    "...",
                    "xx.x (xx.x)",
                ],
                [
                    "AUC0-tau (ng·h/mL)",
                    "Geo Mean (CV%)",
                    "xx.x (xx.x)",
                    "xx.x (xx.x)",
                    "...",
                    "xx.x (xx.x)",
                ],
                [
                    "AUC0-inf (ng·h/mL)",
                    "Geo Mean (CV%)",
                    "xx.x (xx.x)",
                    "xx.x (xx.x)",
                    "...",
                    "xx.x (xx.x)",
                ],
                [
                    "Tmax (h)",
                    "Median (Range)",
                    "x.x (x.x-x.x)",
                    "x.x (x.x-x.x)",
                    "...",
                    "x.x (x.x-x.x)",
                ],
                ["t1/2 (h)", "Mean (SD)", "xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                EROW,
            ],
            dataset_source="ADSL, ADPP",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_pk_params.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.4.3",
            title="Summary of Anti-Drug Antibody (ADA) Incidence",
            tfl_type=T,
            section=S144,
            sort_key=3,
            population="Safety Population with ADA Samples",
            placeholder_columns=[
                "ADA Parameter",
                "XXX Group 1\n(N=XX) n (%)",
                "XXX Group 2\n(N=XX) n (%)",
                "...\n...\nOverall\n(N=XX) n (%)",
            ],
            shell_rows=[
                ["ADA Evaluable", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["ADA Positive at Baseline", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["ADA Positive Post-Baseline", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["Treatment-Emergent ADA Positive", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                [
                    "Neutralizing Antibody (Nab) Positive",
                    "xx (xx.x)",
                    "xx (xx.x)",
                    "...",
                    "xx (xx.x)",
                ],
                EROW,
            ],
            dataset_source="ADSL, ADIS",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ada_incidence.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.4.4",
            title="Summary of Biomarker Results by Visit",
            tfl_type=T,
            section=S144,
            sort_key=4,
            population="ITT Population with Biomarker Data",
            placeholder_columns=[
                "Biomarker",
                "Visit",
                "Statistic",
                "XXX Group 1\n(N=XX)",
                "XXX Group 2\n(N=XX)",
                "...\n...\nOverall\n(N=XX)",
            ],
            shell_rows=[
                [
                    "ctDNA (ng/mL)",
                    "Baseline",
                    "Geo Mean (CV%)",
                    "xx.x (xx.x)",
                    "xx.x (xx.x)",
                    "...",
                    "xx.x (xx.x)",
                ],
                [
                    "ctDNA (ng/mL)",
                    "Cycle 3",
                    "Geo Mean (CV%)",
                    "xx.x (xx.x)",
                    "xx.x (xx.x)",
                    "...",
                    "xx.x (xx.x)",
                ],
                [
                    "ctDNA (ng/mL)",
                    "EOT",
                    "Geo Mean (CV%)",
                    "xx.x (xx.x)",
                    "xx.x (xx.x)",
                    "...",
                    "xx.x (xx.x)",
                ],
                EROW,
            ],
            dataset_source="ADSL, ADBM",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_biomarker_visit.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.4.5",
            title="Summary of Patient-Reported Outcomes by Visit",
            tfl_type=T,
            section=S144,
            sort_key=5,
            population="ITT Population with PRO Data",
            placeholder_columns=[
                "PRO Scale",
                "Visit",
                "Statistic",
                "XXX Group 1\n(N=XX)",
                "XXX Group 2\n(N=XX)",
                "...\n...\nOverall\n(N=XX)",
            ],
            shell_rows=[
                [
                    "EORTC QLQ-C30 GHS",
                    "Baseline",
                    "Mean (SD)",
                    "xx.x (xx.x)",
                    "xx.x (xx.x)",
                    "...",
                    "xx.x (xx.x)",
                ],
                [
                    "EORTC QLQ-C30 GHS",
                    "Week 12",
                    "Mean (SD)",
                    "xx.x (xx.x)",
                    "xx.x (xx.x)",
                    "...",
                    "xx.x (xx.x)",
                ],
                [
                    "EORTC QLQ-C30 GHS",
                    "Change from BL",
                    "LS Mean (SE)",
                    "xx.x (xx.x)",
                    "xx.x (xx.x)",
                    "...",
                    "xx.x (xx.x)",
                ],
                EROW,
            ],
            dataset_source="ADSL, ADPRO",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_pro_summary.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.4.6",
            title="Summary of Pharmacodynamics — Soluble Biomarkers by Visit",
            tfl_type=T,
            section=S144,
            sort_key=6,
            population="PD Population",
            placeholder_columns=[
                "Biomarker",
                "Visit",
                "Statistic",
                "XXX Group 1\n(N=XX)",
                "XXX Group 2\n(N=XX)",
                "...\n...\nOverall\n(N=XX)",
            ],
            shell_rows=[
                [
                    "Soluble EGFR (pg/mL)",
                    "Baseline",
                    "Geo Mean (CV%)",
                    "xx.x (xx.x)",
                    "xx.x (xx.x)",
                    "...",
                    "xx.x (xx.x)",
                ],
                [
                    "Soluble EGFR (pg/mL)",
                    "Week 4",
                    "Geo Mean (CV%)",
                    "xx.x (xx.x)",
                    "xx.x (xx.x)",
                    "...",
                    "xx.x (xx.x)",
                ],
                [
                    "Soluble cMet (ng/mL)",
                    "Baseline",
                    "Geo Mean (CV%)",
                    "xx.x (xx.x)",
                    "xx.x (xx.x)",
                    "...",
                    "xx.x (xx.x)",
                ],
                EROW,
            ],
            dataset_source="ADSL, ADPD",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_pd_summary.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.4.7",
            title="Summary of Central Molecular Test Results and Gene Aberrations at Baseline",
            tfl_type=T,
            section=S144,
            sort_key=7,
            oncology_only=True,
            population="Full Analysis Set",
            placeholder_columns=[
                "Gene",
                "Alteration Type",
                "XXX Group 1\n(N=XX) n (%)",
                "XXX Group 2\n(N=XX) n (%)",
                "...\n...\nOverall\n(N=XX) n (%)",
            ],
            shell_rows=[
                ["Gene X", "Mutation", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["Gene X", "Amplification", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                ["Gene Y", "Mutation", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                EROW,
            ],
            dataset_source="ADSL, ADBM",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_gene_aberrations.sas",
        )
    )

    # 14.4 Figures
    items.append(
        TFLItem(
            id="F14.4.1",
            title="Pharmacokinetic (PK) Plot — Mean Serum Concentration-Time Profiles",
            tfl_type=F,
            section=S144,
            sort_key=15,
            population="PK Population",
            figure_description="PK plot: Mean (±SD) serum concentration vs. time, linear/log scales.",
            dataset_source="ADSL, ADPC",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="f_pk_profile.sas",
            figure_type="longitudinal",
            figure_width_inches=6,
            figure_height_inches=4,
        )
    )

    items.append(
        TFLItem(
            id="F14.4.2",
            title="Overlaying Individual PK Concentration Profiles",
            tfl_type=F,
            section=S144,
            sort_key=16,
            population="PK Population",
            figure_description="PK overlay: individual concentration-time profiles by treatment group.",
            dataset_source="ADSL, ADPC",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="f_pk_overlay.sas",
            figure_type="spider",
            figure_width_inches=6,
            figure_height_inches=4,
        )
    )

    items.append(
        TFLItem(
            id="F14.4.3",
            title="Mean (SD) Soluble EGFR and cMet Over Time",
            tfl_type=F,
            section=S144,
            sort_key=17,
            population="PD Population",
            figure_description="PD plot: Mean (±SD) soluble EGFR/cMet concentrations over time.",
            dataset_source="ADSL, ADPD",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="f_pd_time.sas",
            figure_type="longitudinal",
            figure_width_inches=6,
            figure_height_inches=4,
        )
    )

    items.append(
        TFLItem(
            id="F14.4.4",
            title="Boxplot of Biomarkers at Baseline vs. Response Status",
            tfl_type=F,
            section=S144,
            sort_key=18,
            oncology_only=True,
            population="Full Analysis Set with Biomarker Data",
            figure_description="Box plot: Biomarker levels at baseline by response status (CR/PR/SD/PD).",
            dataset_source="ADSL, ADBM",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="f_biomarker_box.sas",
            figure_type="box_plot",
            figure_width_inches=6,
            figure_height_inches=4,
        )
    )

    # =====================================================================

    # --- 14.4 Expansion (CDISC ADIS, ADBM, ADPC) ---
    items.append(
        TFLItem(
            id="T14.4.8",
            title="ADA Titer Distribution by Visit — Negative, Low, Medium, High",
            tfl_type=T,
            section=S144,
            sort_key=8,
            population="Safety Population with ADA Samples",
            placeholder_columns=[
                "Visit\nADA Titer Category",
                "G1\nn/N (%)",
                "G2\nn/N (%)",
                "...",
                "Overall\nn/N (%)",
            ],
            shell_rows=[
                {"label": "Baseline", "bold": True},
                {
                    "label": "  ADA Negative",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "  Low Titer (1:<xxx)",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "  Medium Titer",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "  High Titer (>=1:xxxx)",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "Post-Baseline (Any)", "bold": True},
                {
                    "label": "  ADA Negative",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "  Low Titer",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "  Medium Titer",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "  High Titer",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {
                    "label": "  Treatment-Emergent ADA Positive",
                    "bold": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "ADA assessed by validated bridging immunoassay. Titer categories defined per assay validation report. Listing: L16.2.16."
            ],
            dataset_source="ADSL, ADIS",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ada_titer.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.4.9",
            title="ADA Impact on Pharmacokinetics — Cmax and AUC in ADA+ vs. ADA- Subjects",
            tfl_type=T,
            section=S144,
            sort_key=9,
            population="PK Population with ADA Data",
            placeholder_columns=[
                "PK Parameter\nADA Status",
                "Statistic",
                "ADA Positive\n(N=XX)",
                "ADA Negative\n(N=XX)",
                "Ratio\n(ADA+/ADA-)",
            ],
            shell_rows=[
                {"label": "Cmax (ng/mL)", "bold": True},
                {
                    "label": "  ADA Positive — Geo Mean (CV%)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "", ""],
                },
                {
                    "label": "  ADA Negative — Geo Mean (CV%)",
                    "indent": True,
                    "values": ["", "xx.x (xx.x)", ""],
                },
                {
                    "label": "  Geometric Mean Ratio (90% CI)",
                    "indent": True,
                    "values": ["", "", "x.xx (x.xx, x.xx)"],
                },
                {"label": "AUC0-tau (ng*h/mL)", "bold": True},
                {
                    "label": "  ADA Positive — Geo Mean (CV%)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "", ""],
                },
                {
                    "label": "  ADA Negative — Geo Mean (CV%)",
                    "indent": True,
                    "values": ["", "xx.x (xx.x)", ""],
                },
                {
                    "label": "  Geometric Mean Ratio (90% CI)",
                    "indent": True,
                    "values": ["", "", "x.xx (x.xx, x.xx)"],
                },
            ],
            footnotes=[
                "ADA+ = treatment-emergent ADA positive. ADA- = ADA negative throughout. GMR = geometric mean ratio."
            ],
            dataset_source="ADSL, ADIS, ADPP",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ada_pk_impact.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.4.10",
            title="Neutralizing Antibody (Nab) — Incidence, Titer, and Cross-Reactivity Status",
            tfl_type=T,
            section=S144,
            sort_key=10,
            population="Safety Population with ADA Samples",
            placeholder_columns=[
                "Nab Parameter",
                "G1\nn/N1 (%)",
                "G2\nn/N2 (%)",
                "...",
                "Overall\nn/N (%)",
            ],
            shell_rows=[
                {
                    "label": "Nab Evaluable Subjects",
                    "bold": True,
                    "values": ["xx", "xx", "...", "xx"],
                },
                {
                    "label": "Nab Positive, n (%)",
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Among ADA Positive Subjects",
                    "indent": True,
                    "values": ["xx/xx (xx.x)", "xx/xx (xx.x)", "...", "xx/xx (xx.x)"],
                },
                {"label": "Nab Titer Distribution", "bold": True},
                {
                    "label": "  Low (<1:xx)",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Medium (1:xx-1:xxx)",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  High (>=1:xxxx)",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Cross-Reactivity to Endogenous Protein",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "Nab = neutralizing antibody. N1/N2 = number of ADA-evaluable subjects. Cross-reactivity assessed by competitive ligand-binding assay."
            ],
            dataset_source="ADSL, ADIS",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_nab_detail.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.4.11",
            title="Soluble Pharmacodynamic Biomarker Change from Baseline Over Time",
            tfl_type=T,
            section=S144,
            sort_key=11,
            population="PD Population",
            placeholder_columns=[
                "Biomarker\nVisit",
                "Statistic",
                "G1\n(N=XX)",
                "G2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {"label": "Soluble Target X (ng/mL)", "bold": True},
                {
                    "label": "  Baseline — Geo Mean (CV%)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Cycle 1 Day 8 — Fold Chg from BL",
                    "indent": True,
                    "values": ["x.xx", "x.xx", "...", "x.xx"],
                },
                {
                    "label": "  Cycle 2 Day 1 — Fold Chg from BL",
                    "indent": True,
                    "values": ["x.xx", "x.xx", "...", "x.xx"],
                },
                {
                    "label": "  End of Treatment — Fold Chg from BL",
                    "indent": True,
                    "values": ["x.xx", "x.xx", "...", "x.xx"],
                },
                {"label": "Soluble Biomarker Y (pg/mL)", "bold": True},
                {
                    "label": "  Baseline — Geo Mean (CV%)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  Cycle 2 Day 1 — Fold Chg from BL",
                    "indent": True,
                    "values": ["x.xx", "x.xx", "...", "x.xx"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "PD biomarkers assessed by validated assays. Fold change = post-baseline / baseline."
            ],
            dataset_source="ADSL, ADBM",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_pd_bio_chg.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.4.12",
            title="Trough PK Concentration (Ctrough) by Cycle — Target Attainment",
            tfl_type=T,
            section=S144,
            sort_key=12,
            population="PK Population",
            placeholder_columns=[
                "Cycle\nDay",
                "Statistic",
                "G1\n(N=XX)",
                "G2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {
                    "label": "Cycle 1 Day 15 — Mean (SD), ng/mL",
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "Cycle 2 Day 1 — Mean (SD), ng/mL",
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "Cycle 3 Day 1 — Mean (SD), ng/mL",
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "Cycle 4 Day 1 — Mean (SD), ng/mL",
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "Cycle 6 Day 1 — Mean (SD), ng/mL",
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "Ctrough Above Target Threshold, n (%)",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "Ctrough = pre-dose concentration. Target threshold per PK/PD modeling. Listing: L16.2.14."
            ],
            dataset_source="ADSL, ADPC",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ctrough.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.4.13",
            title="Steady-State Attainment — Trough Concentrations Across Dosing Cycles (ANOVA)",
            tfl_type=T,
            section=S144,
            sort_key=13,
            population="PK Population",
            placeholder_columns=["Cycle Comparison", "GMR (90% CI)", "CV%", "Conclusion"],
            shell_rows=[
                {
                    "label": "Cycle 2 vs. Cycle 1 Ctrough",
                    "values": ["x.xx (x.xx, x.xx)", "xx.x", "Steady state / Not yet"],
                },
                {
                    "label": "Cycle 3 vs. Cycle 2 Ctrough",
                    "values": ["x.xx (x.xx, x.xx)", "xx.x", "Steady state / Not yet"],
                },
                {
                    "label": "Cycle 4 vs. Cycle 3 Ctrough",
                    "values": ["x.xx (x.xx, x.xx)", "xx.x", "Steady state achieved"],
                },
                {
                    "label": "Cycle 6 vs. Cycle 4 Ctrough",
                    "values": ["x.xx (x.xx, x.xx)", "xx.x", "Steady state maintained"],
                },
            ],
            footnotes=[
                "Steady state = no statistically significant increase between consecutive cycles (ANOVA on log-transformed Ctrough, 90% CI of GMR within 0.80-1.25)."
            ],
            dataset_source="ADSL, ADPC",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_steady_state.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.4.14",
            title="Urine Pharmacokinetic Parameters — Renal Excretion and Cumulative Recovery",
            tfl_type=T,
            section=S144,
            sort_key=14,
            population="PK Population (Subset with Urine PK)",
            placeholder_columns=[
                "PK Parameter\n(Unit)",
                "Statistic",
                "G1\n(N=XX)",
                "G2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {"label": "Ae (Amount Excreted Unchanged, mg)", "bold": True},
                {
                    "label": "  Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  % of Dose, Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "Renal Clearance (CLr, L/h)", "bold": True},
                {
                    "label": "  Geo Mean (CV%)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "Cumulative Urinary Recovery (% Dose, 0-24h)",
                    "bold": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
            ],
            footnotes=[
                "Urine PK collected over 0-4h, 4-8h, 8-12h, 12-24h intervals post-dose. Ae = cumulative amount excreted unchanged."
            ],
            dataset_source="ADSL, ADPP",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_urine_pk.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.4.15",
            title="Food Effect on Pharmacokinetic Parameters — Fed vs Fasted Comparison",
            tfl_type=T,
            section=S144,
            sort_key=15,
            non_oncology_only=True,
            population="PK Population in Food-Effect Cohorts",
            placeholder_columns=[
                "PK Parameter",
                "Fasted\nGeo Mean",
                "Fed\nGeo Mean",
                "Fed/Fasted GMR",
                "90% CI",
            ],
            shell_rows=[
                ["Cmax", "xx.x", "xx.x", "x.xx", "[x.xx, x.xx]"],
                ["AUC0-t", "xx.x", "xx.x", "x.xx", "[x.xx, x.xx]"],
                ["AUC0-inf", "xx.x", "xx.x", "x.xx", "[x.xx, x.xx]"],
                ["Tmax", "x.x", "x.x", "", ""],
            ],
            footnotes=[
                "Food-effect comparison based on log-transformed PK parameters in protocol-defined fed and fasted periods."
            ],
            dataset_source="ADSL, ADPP",
            source_listing="L16.2.33",
            program_ref="t_food_effect_pk.sas",
            shell_family="Phase I Clinical Pharmacology",
            study_phase_scope="Phase I",
            coverage_summary="Conditional (Phase I)",
        )
    )

    items.append(
        TFLItem(
            id="T14.4.16",
            title="Relative Bioavailability / Crossover PK Comparison by Treatment Period",
            tfl_type=T,
            section=S144,
            sort_key=16,
            non_oncology_only=True,
            population="PK Population in Crossover / Relative Bioavailability Cohorts",
            placeholder_columns=[
                "PK Parameter",
                "Reference Treatment",
                "Test Treatment",
                "Test/Reference GMR",
                "90% CI",
            ],
            shell_rows=[
                ["Cmax", "xx.x", "xx.x", "x.xx", "[x.xx, x.xx]"],
                ["AUC0-t", "xx.x", "xx.x", "x.xx", "[x.xx, x.xx]"],
                ["AUC0-inf", "xx.x", "xx.x", "x.xx", "[x.xx, x.xx]"],
                ["t1/2", "xx.x", "xx.x", "x.xx", "[x.xx, x.xx]"],
            ],
            footnotes=[
                "Relative bioavailability or crossover comparison per protocol-defined mixed-effects model with sequence, period, and treatment effects where applicable."
            ],
            dataset_source="ADSL, ADPP",
            source_listing="L16.2.33",
            program_ref="t_crossover_pk.sas",
            shell_family="Phase I Clinical Pharmacology",
            study_phase_scope="Phase I",
            coverage_summary="Conditional (Phase I)",
        )
    )

    items.append(
        TFLItem(
            id="F14.4.5",
            title="Mean Concentration-Time Profiles — Fed vs Fasted",
            tfl_type=F,
            section=S144,
            sort_key=19,
            non_oncology_only=True,
            population="PK Population in Food-Effect Cohorts",
            figure_description="Mean concentration-time profiles under fed and fasted conditions with linear and semilog interpretation support.",
            dataset_source="ADSL, ADPC",
            source_listing="L16.2.33",
            program_ref="f_food_effect_pk.sas",
            figure_type="longitudinal",
            figure_width_inches=6,
            figure_height_inches=4,
            shell_family="Phase I Clinical Pharmacology",
            study_phase_scope="Phase I",
            coverage_summary="Conditional (Phase I)",
        )
    )

    return items
