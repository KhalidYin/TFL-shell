"""Section 14.2 catalog definitions: efficacy shells."""

from tflshell.data.common import *


def build_14_2_items() -> list[TFLItem]:
    """Build Section 14.2 catalog items."""
    items: list[TFLItem] = []

    # 14.2 EFFICACY (32 items: 11 general + 21 oncology)
    # =====================================================================

    items.append(
        TFLItem(
            id="T14.2.1",
            title="Primary Efficacy Endpoint — Primary Analysis",
            tfl_type=T,
            section=S142,
            sort_key=1,
            population="Intent-to-Treat (ITT) Population",
            placeholder_columns=[
                "Parameter",
                "XXX Group 1\n(N=XX)",
                "XXX Group 2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {
                    "label": "Subjects in Analysis",
                    "bold": True,
                    "values": ["xx", "xx", "...", "xx"],
                },
                {"label": "Baseline", "bold": True},
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
                {"label": "End of Study (Week 24)", "bold": True},
                {
                    "label": "  Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "Change from Baseline at Week 24", "bold": True},
                {
                    "label": "  LS Mean (SE)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  LS Mean Difference vs. Control",
                    "indent": True,
                    "values": ["", "xx.x", "...", ""],
                },
                {"label": "  95% CI", "indent": True, "values": ["", "[xx.x, xx.x]", "...", ""]},
                {"label": "  p-value", "indent": True, "values": ["", "x.xxx", "...", ""]},
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "ANCOVA with treatment as fixed effect, baseline as covariate, stratified by [stratification factors].",
                "MMRM under MAR for missing data. Two-sided 95% CI. Multiplicity adjustment per hierarchical testing procedure.",
            ],
            dataset_source="ADSL, ADEFF",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_primary_eff.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.2.2",
            title="Secondary Efficacy Endpoints — Summary",
            tfl_type=T,
            section=S142,
            sort_key=2,
            population="Intent-to-Treat (ITT) Population",
            placeholder_columns=[
                "Endpoint\nStatistic",
                "XXX Group 1\n(N=XX)",
                "XXX Group 2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {"label": "Key Secondary Endpoint 1 — Change from BL at Week 24", "bold": True},
                {
                    "label": "  LS Mean (SE)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "  LS Mean Difference (95% CI)",
                    "indent": True,
                    "values": ["xx.x [xx.x, xx.x]", "", "...", ""],
                },
                {
                    "label": "  p-value (adjusted)",
                    "indent": True,
                    "values": ["x.xxx", "", "...", ""],
                },
                {"label": "Key Secondary Endpoint 2 — Response Rate", "bold": True},
                {
                    "label": "  n (%)",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Odds Ratio (95% CI)",
                    "indent": True,
                    "values": ["x.xx [x.xx, x.xx]", "", "...", ""],
                },
                {
                    "label": "  p-value (adjusted)",
                    "indent": True,
                    "values": ["x.xxx", "", "...", ""],
                },
                {"label": "Key Secondary Endpoint 3 — Time to Event", "bold": True},
                {
                    "label": "  Events / N (%)",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Median, months (95% CI)",
                    "indent": True,
                    "values": [
                        "xx.x (xx.x, xx.x)",
                        "xx.x (xx.x, xx.x)",
                        "...",
                        "xx.x (xx.x, xx.x)",
                    ],
                },
                {
                    "label": "  HR (95% CI)",
                    "indent": True,
                    "values": ["x.xx [x.xx, x.xx]", "", "...", ""],
                },
                {
                    "label": "  p-value (adjusted)",
                    "indent": True,
                    "values": ["x.xxx", "", "...", ""],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "Endpoints tested per hierarchical fixed-sequence procedure. Adjusted p-values shown.",
                "Response defined per protocol SAP [ref]. ANCOVA/CMH/Cox models as appropriate per endpoint type.",
            ],
            dataset_source="ADSL, ADEFF, ADTTE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_secondary_eff.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.2.3",
            title="Subgroup Analysis of Primary Endpoint",
            tfl_type=T,
            section=S142,
            sort_key=3,
            population="Intent-to-Treat (ITT) Population",
            placeholder_columns=[
                "Subgroup\nLevel",
                "XXX Group 1\nn / Estimate",
                "XXX Group 2\nn / Estimate",
                "...\n...\nEffect [95% CI]",
                "Interaction\np-value",
            ],
            shell_rows=[
                ["Overall", "xx / xx.x", "xx / xx.x", "...", "xx.x [xx.x, xx.x]", "—"],
                ["Age <65", "xx / xx.x", "xx / xx.x", "...", "xx.x [xx.x, xx.x]", "x.xxx"],
                ["Age >=65", "xx / xx.x", "xx / xx.x", "...", "xx.x [xx.x, xx.x]", ""],
                ["Male", "xx / xx.x", "xx / xx.x", "...", "xx.x [xx.x, xx.x]", "x.xxx"],
                ["Female", "xx / xx.x", "xx / xx.x", "...", "xx.x [xx.x, xx.x]", ""],
                EROW5,
            ],
            footnotes=["Subgroup analyses are exploratory."],
            dataset_source="ADSL, ADEFF",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_subgroup_primary.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.2.4",
            title="Sensitivity Analysis of Primary Endpoint",
            tfl_type=T,
            section=S142,
            sort_key=4,
            population="ITT and PP Populations",
            placeholder_columns=[
                "Analysis\nPopulation / Missing Data",
                "XXX Group 1\nLS Mean",
                "XXX Group 2\nLS Mean",
                "...\n...\nDifference",
                "95% CI",
            ],
            shell_rows=[
                ["Primary (MMRM / ITT / MAR)", "xx.x", "xx.x", "...", "xx.x", "[xx.x, xx.x]"],
                ["PP Analysis (Completers)", "xx.x", "xx.x", "...", "xx.x", "[xx.x, xx.x]"],
                [
                    "Multiple Imputation (100 imputations)",
                    "xx.x",
                    "xx.x",
                    "...",
                    "xx.x",
                    "[xx.x, xx.x]",
                ],
                ["Tipping Point (δ=1.0)", "xx.x", "xx.x", "...", "xx.x", "[xx.x, xx.x]"],
                EROW5,
            ],
            dataset_source="ADSL, ADEFF",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_sensitivity_eff.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.2.5",
            title="Non-Inferiority Analysis of Primary Endpoint",
            tfl_type=T,
            section=S142,
            sort_key=5,
            population="Per-Protocol (PP) Population",
            placeholder_columns=[
                "Parameter",
                "XXX Group 1\n(N=XX)",
                "Control\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {
                    "label": "Primary Endpoint — LS Mean (SE)",
                    "bold": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {
                    "label": "Difference vs. Control (95% CI)",
                    "values": ["xx.x [xx.x, xx.x]", "", "...", ""],
                },
                {"label": "Non-Inferiority Margin (Δ)", "values": ["xx.x", "", "...", ""]},
                {"label": "Lower Bound of 95% CI > −Δ?", "values": ["Yes / No", "", "...", ""]},
                {
                    "label": "NI Conclusion",
                    "bold": True,
                    "values": ["Non-inferiority met / not met", "", "...", ""],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "NI margin per regulatory guidance. Analysis population: PP (primary), ITT (supportive)."
            ],
            dataset_source="ADSL, ADEFF",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ni_analysis.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.2.6",
            title="Tipping Point Analysis for Primary Endpoint",
            tfl_type=T,
            section=S142,
            sort_key=6,
            population="ITT Population",
            placeholder_columns=["Tipping Point Parameter\nShift Value", "p-value", "Conclusion"],
            shell_rows=[
                ["Tipping Point Analysis", "", ""],
                ["  Placebo-arm shift (delta) = 0.0", "x.xxx", "Statistically significant"],
                ["  Placebo-arm shift (delta) = 0.5", "x.xxx", "Remains significant"],
                ["  Placebo-arm shift (delta) = 1.0", "x.xxx", "Borderline"],
                [
                    "  Placebo-arm shift (delta) = 1.5",
                    "x.xxx",
                    "Not significant — tipping point reached",
                ],
                ["[...]", "...", "..."],
            ],
            dataset_source="ADSL, ADEFF",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_tipping_point.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.2.7",
            title="Sensitivity Analysis by Estimand Strategy",
            tfl_type=T,
            section=S142,
            sort_key=7,
            population="ITT Population",
            placeholder_columns=[
                "Estimand Strategy\nIntercurrent Event Handling",
                "Difference",
                "95% CI",
                "p-value",
            ],
            shell_rows=[
                ["Treatment Policy — Ignore rescue therapy", "xx.x", "[xx.x, xx.x]", "x.xxx"],
                ["Composite — Rescue = treatment failure", "xx.x", "[xx.x, xx.x]", "x.xxx"],
                ["Hypothetical — Rescue subjects censored", "xx.x", "[xx.x, xx.x]", "x.xxx"],
                EROW,
            ],
            dataset_source="ADSL, ADEFF",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_estimand_sens.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.2.8",
            title="Time to Deterioration (TTD) — Quality of Life",
            tfl_type=T,
            section=S142,
            sort_key=8,
            population="ITT Population with PRO Data",
            placeholder_columns=[
                "Parameter",
                "XXX Group 1\n(N=XX)",
                "XXX Group 2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {"label": "Number of Subjects", "bold": True, "values": ["xx", "xx", "...", "xx"]},
                {
                    "label": "Events, n (%)",
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Censored, n (%)",
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Median TTD, months (95% CI)",
                    "bold": True,
                    "values": [
                        "xx.x (xx.x, xx.x)",
                        "xx.x (xx.x, xx.x)",
                        "...",
                        "xx.x (xx.x, xx.x)",
                    ],
                },
                {
                    "label": "TTD Rate at 6 months, % (95% CI)",
                    "values": [
                        "xx.x (xx.x, xx.x)",
                        "xx.x (xx.x, xx.x)",
                        "...",
                        "xx.x (xx.x, xx.x)",
                    ],
                },
                {
                    "label": "TTD Rate at 12 months, % (95% CI)",
                    "values": [
                        "xx.x (xx.x, xx.x)",
                        "xx.x (xx.x, xx.x)",
                        "...",
                        "xx.x (xx.x, xx.x)",
                    ],
                },
                {
                    "label": "Hazard Ratio (95% CI)",
                    "bold": True,
                    "values": ["x.xx [x.xx, x.xx]", "", "...", ""],
                },
                {"label": "p-value (stratified log-rank)", "values": ["x.xxx", "", "...", ""]},
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "TTD defined as time from randomization to first deterioration in [PRO instrument] score >= [threshold] points.",
                "KM estimates; Brookmeyer-Crowley CI for median. Stratified Cox/log-rank by baseline factors.",
            ],
            dataset_source="ADSL, ADPRO",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ttd_qol.sas",
        )
    )

    # General efficacy figures
    items.append(
        TFLItem(
            id="F14.2.1",
            title="Forest Plot — Primary Endpoint by Subgroup",
            tfl_type=F,
            section=S142,
            sort_key=23,
            population="Intent-to-Treat (ITT) Population",
            figure_description="Forest plot: treatment effect [95% CI] per subgroup, overall diamond, ref line at null.",
            dataset_source="ADSL, ADEFF",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="f_forest_primary.sas",
            figure_type="forest",
            figure_width_inches=6,
            figure_height_inches=3.5,
        )
    )

    items.append(
        TFLItem(
            id="F14.2.2",
            title="Longitudinal Plot — Primary Endpoint Over Time",
            tfl_type=F,
            section=S142,
            sort_key=24,
            population="Intent-to-Treat (ITT) Population",
            figure_description="Line plot: Mean (±SE) primary endpoint by visit, two arms.",
            dataset_source="ADSL, ADEFF",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="f_longitudinal_eff.sas",
            figure_type="longitudinal",
            figure_width_inches=5.5,
            figure_height_inches=3.2,
        )
    )

    items.append(
        TFLItem(
            id="F14.2.3",
            title="Cumulative Distribution Function Plot of Primary Endpoint",
            tfl_type=F,
            section=S142,
            sort_key=25,
            population="Intent-to-Treat (ITT) Population",
            figure_description="CDF plot: X=Change from Baseline, Y=Cumulative Proportion, two arms.",
            dataset_source="ADSL, ADEFF",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="f_cdf_eff.sas",
            figure_type="cdf",
            figure_width_inches=5.5,
            figure_height_inches=3.2,
        )
    )

    # --- Oncology-Specific Efficacy (13 tables + 7 figures) ---

    items.append(
        TFLItem(
            id="T14.2.9",
            title="Tumor Response — Best Overall Response (BOR)",
            tfl_type=T,
            section=S142,
            sort_key=9,
            oncology_only=True,
            population="Intent-to-Treat (ITT) Population",
            placeholder_columns=H2_NPCT,
            shell_rows=[
                {"label": "Best Overall Response (BOR)", "bold": True},
                {
                    "label": "  Complete Response (CR)",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Partial Response (PR)",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Stable Disease (SD)",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Progressive Disease (PD)",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Not Evaluable (NE)",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Objective Response Rate (ORR = CR+PR)",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  95% CI (Clopper-Pearson)",
                    "indent": True,
                    "values": ["[xx.x, xx.x]", "[xx.x, xx.x]", "...", "[xx.x, xx.x]"],
                },
                {
                    "label": "Disease Control Rate (DCR = CR+PR+SD)",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  95% CI (Clopper-Pearson)",
                    "indent": True,
                    "values": ["[xx.x, xx.x]", "[xx.x, xx.x]", "...", "[xx.x, xx.x]"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "RECIST v1.1 by Independent Central Review (ICR). Confirmed responses only (repeat assessment >=4 weeks after initial response).",
                "CR = Disappearance of all target and non-target lesions. PR = >=30% decrease in sum of diameters.",
                "95% CI calculated using Clopper-Pearson exact method.",
            ],
            dataset_source="ADSL, ADRS",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_bor.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.2.10",
            title="Tumor Response — Objective Response Rate (ORR)",
            tfl_type=T,
            section=S142,
            sort_key=10,
            oncology_only=True,
            population="Intent-to-Treat (ITT) Population",
            placeholder_columns=[
                "Parameter",
                "XXX Group 1\n(N=XX)",
                "XXX Group 2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {
                    "label": "Responders (CR+PR), n (%)",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  95% CI (Clopper-Pearson)",
                    "indent": True,
                    "values": ["[xx.x, xx.x]", "[xx.x, xx.x]", "...", "[xx.x, xx.x]"],
                },
                {"label": "Stratified Analysis", "bold": True},
                {
                    "label": "  Odds Ratio (95% CI)",
                    "indent": True,
                    "values": ["x.xx [x.xx, x.xx]", "", "...", ""],
                },
                {
                    "label": "  p-value (CMH, stratified)",
                    "indent": True,
                    "values": ["x.xxx", "", "...", ""],
                },
                {
                    "label": "  Risk Difference, % (95% CI)",
                    "indent": True,
                    "values": ["xx.x [xx.x, xx.x]", "", "...", ""],
                },
                {
                    "label": "Sensitivity: Unconfirmed Responses",
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "ORR = CR + PR per RECIST v1.1 (ICR). Confirmed responses only (>=4 weeks after initial response).",
                "CMH test stratified by randomization stratification factors.",
            ],
            dataset_source="ADSL, ADRS",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_orr.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.2.11",
            title="Tumor Response — Disease Control Rate (DCR)",
            tfl_type=T,
            section=S142,
            sort_key=11,
            oncology_only=True,
            population="Intent-to-Treat (ITT) Population",
            placeholder_columns=[
                "Parameter",
                "XXX Group 1\n(N=XX)",
                "XXX Group 2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {
                    "label": "DCR (CR+PR+SD), n (%)",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  95% CI (Clopper-Pearson)",
                    "indent": True,
                    "values": ["[xx.x, xx.x]", "[xx.x, xx.x]", "...", "[xx.x, xx.x]"],
                },
                {
                    "label": "Clinical Benefit Rate (CR+PR+SD>=24 wks)",
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  95% CI (Clopper-Pearson)",
                    "indent": True,
                    "values": ["[xx.x, xx.x]", "[xx.x, xx.x]", "...", "[xx.x, xx.x]"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "DCR = CR + PR + SD (SD must be maintained for >=6 weeks after first dose).",
                "Clinical Benefit Rate defined as CR + PR + SD lasting >=24 weeks.",
            ],
            dataset_source="ADSL, ADRS",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_dcr.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.2.12",
            title="Tumor Response — Duration of Response (DOR)",
            tfl_type=T,
            section=S142,
            sort_key=12,
            oncology_only=True,
            population="Responders (Confirmed CR or PR)",
            placeholder_columns=[
                "Parameter",
                "XXX Group 1\n(N=XX)",
                "XXX Group 2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {
                    "label": "Number of Responders",
                    "bold": True,
                    "values": ["xx", "xx", "...", "xx"],
                },
                {
                    "label": "Events (Progression or Death), n (%)",
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Censored, n (%)",
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Median DOR, months (95% CI)",
                    "bold": True,
                    "values": [
                        "xx.x (xx.x, xx.x)",
                        "xx.x (xx.x, xx.x)",
                        "...",
                        "xx.x (xx.x, xx.x)",
                    ],
                },
                {
                    "label": "DOR Rate at 6 months, % (95% CI)",
                    "values": [
                        "xx.x (xx.x, xx.x)",
                        "xx.x (xx.x, xx.x)",
                        "...",
                        "xx.x (xx.x, xx.x)",
                    ],
                },
                {
                    "label": "DOR Rate at 12 months, % (95% CI)",
                    "values": [
                        "xx.x (xx.x, xx.x)",
                        "xx.x (xx.x, xx.x)",
                        "...",
                        "xx.x (xx.x, xx.x)",
                    ],
                },
                {
                    "label": "Hazard Ratio (95% CI)",
                    "bold": True,
                    "values": ["x.xx [x.xx, x.xx]", "", "...", ""],
                },
                {"label": "p-value (stratified log-rank)", "values": ["x.xxx", "", "...", ""]},
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "DOR: time from first documented CR/PR to first PD (RECIST 1.1, ICR) or death.",
                "KM estimates; Brookmeyer-Crowley CI for median. Stratified Cox/log-rank by baseline factors.",
            ],
            dataset_source="ADSL, ADRS, ADTTE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_dor.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.2.13",
            title="Tumor Response — Time to Response (TTR)",
            tfl_type=T,
            section=S142,
            sort_key=13,
            oncology_only=True,
            population="Responders (Confirmed CR or PR)",
            placeholder_columns=[
                "Parameter",
                "XXX Group 1\n(N=XX)",
                "XXX Group 2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {
                    "label": "Number of Responders",
                    "bold": True,
                    "values": ["xx", "xx", "...", "xx"],
                },
                {
                    "label": "Mean (SD), months",
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "Median, months", "values": ["xx.x", "xx.x", "...", "xx.x"]},
                {"label": "Min, Max", "values": ["xx.x, xx.x", "xx.x, xx.x", "...", "xx.x, xx.x"]},
                {
                    "label": "<=12 weeks, n (%)",
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": ">12 to 24 weeks, n (%)",
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": ">24 weeks, n (%)",
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=["TTR: time from randomization to first documented CR or PR (confirmed)."],
            dataset_source="ADSL, ADRS",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ttr.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.2.14",
            title="Progression-Free Survival (PFS) — Primary Analysis",
            tfl_type=T,
            section=S142,
            sort_key=14,
            oncology_only=True,
            population="Intent-to-Treat (ITT) Population",
            placeholder_columns=[
                "Parameter",
                "XXX Group 1\n(N=XX)",
                "XXX Group 2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {"label": "Number of Subjects", "bold": True, "values": ["xx", "xx", "...", "xx"]},
                {
                    "label": "Events (Progression or Death), n (%)",
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Censored, n (%)",
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Median PFS, months (95% CI)",
                    "bold": True,
                    "values": [
                        "xx.x (xx.x, xx.x)",
                        "xx.x (xx.x, xx.x)",
                        "...",
                        "xx.x (xx.x, xx.x)",
                    ],
                },
                {"label": "Stratified Cox Model", "bold": True},
                {
                    "label": "  Hazard Ratio (95% CI)",
                    "indent": True,
                    "values": ["x.xx [x.xx, x.xx]", "", "...", ""],
                },
                {
                    "label": "  p-value (stratified log-rank)",
                    "indent": True,
                    "values": ["x.xxx", "", "...", ""],
                },
                {"label": "PFS Rate (KM Estimate)", "bold": True},
                {
                    "label": "  6-month PFS Rate, % (95% CI)",
                    "indent": True,
                    "values": [
                        "xx.x (xx.x, xx.x)",
                        "xx.x (xx.x, xx.x)",
                        "...",
                        "xx.x (xx.x, xx.x)",
                    ],
                },
                {
                    "label": "  12-month PFS Rate, % (95% CI)",
                    "indent": True,
                    "values": [
                        "xx.x (xx.x, xx.x)",
                        "xx.x (xx.x, xx.x)",
                        "...",
                        "xx.x (xx.x, xx.x)",
                    ],
                },
                {
                    "label": "  18-month PFS Rate, % (95% CI)",
                    "indent": True,
                    "values": [
                        "xx.x (xx.x, xx.x)",
                        "xx.x (xx.x, xx.x)",
                        "...",
                        "xx.x (xx.x, xx.x)",
                    ],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "PFS: time from randomization to first documented PD (RECIST 1.1, ICR) or death from any cause.",
                "KM estimates. Brookmeyer-Crowley CI for median. Greenwood CI for landmark rates.",
                "Stratified Cox/log-rank by baseline stratification factors (ECOG PS, disease stage, prior lines).",
            ],
            dataset_source="ADSL, ADTTE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_pfs_primary.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.2.15",
            title="Overall Survival (OS) — Primary Analysis",
            tfl_type=T,
            section=S142,
            sort_key=15,
            oncology_only=True,
            population="Intent-to-Treat (ITT) Population",
            placeholder_columns=[
                "Parameter",
                "XXX Group 1\n(N=XX)",
                "XXX Group 2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {"label": "Number of Subjects", "bold": True, "values": ["xx", "xx", "...", "xx"]},
                {
                    "label": "Deaths, n (%)",
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Censored, n (%)",
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Median OS, months (95% CI)",
                    "bold": True,
                    "values": ["xx.x (xx.x, NR)", "xx.x (xx.x, NR)", "...", "xx.x (xx.x, NR)"],
                },
                {"label": "Stratified Cox Model", "bold": True},
                {
                    "label": "  Hazard Ratio (95% CI)",
                    "indent": True,
                    "values": ["x.xx [x.xx, x.xx]", "", "...", ""],
                },
                {
                    "label": "  p-value (stratified log-rank)",
                    "indent": True,
                    "values": ["x.xxx", "", "...", ""],
                },
                {"label": "OS Rate (KM Estimate)", "bold": True},
                {
                    "label": "  6-month OS Rate, % (95% CI)",
                    "indent": True,
                    "values": [
                        "xx.x (xx.x, xx.x)",
                        "xx.x (xx.x, xx.x)",
                        "...",
                        "xx.x (xx.x, xx.x)",
                    ],
                },
                {
                    "label": "  12-month OS Rate, % (95% CI)",
                    "indent": True,
                    "values": [
                        "xx.x (xx.x, xx.x)",
                        "xx.x (xx.x, xx.x)",
                        "...",
                        "xx.x (xx.x, xx.x)",
                    ],
                },
                {
                    "label": "  24-month OS Rate, % (95% CI)",
                    "indent": True,
                    "values": [
                        "xx.x (xx.x, xx.x)",
                        "xx.x (xx.x, xx.x)",
                        "...",
                        "xx.x (xx.x, xx.x)",
                    ],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "OS: time from randomization to death from any cause. NR = Not Reached.",
                "KM estimates. Brookmeyer-Crowley CI for median. Greenwood CI for landmark rates.",
                "Stratified Cox/log-rank by baseline stratification factors.",
            ],
            dataset_source="ADSL, ADTTE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_os_primary.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.2.16",
            title="PFS — Sensitivity Analysis",
            tfl_type=T,
            section=S142,
            sort_key=16,
            oncology_only=True,
            population="Intent-to-Treat (ITT) Population",
            placeholder_columns=[
                "Analysis",
                "Med PFS G1\n(months)",
                "Med PFS G2\n(months)",
                "...\n...\nHR [95% CI]",
                "p-value",
            ],
            shell_rows=[
                ["Primary (ICR, RECIST 1.1)", "xx.x", "xx.x", "...", "x.xx [x.xx, x.xx]", "x.xxx"],
                ["Investigator Assessment", "xx.x", "xx.x", "...", "x.xx [x.xx, x.xx]", "x.xxx"],
                ["PP Population", "xx.x", "xx.x", "...", "x.xx [x.xx, x.xx]", "x.xxx"],
                EROW5,
            ],
            dataset_source="ADSL, ADTTE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_pfs_sensitivity.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.2.17",
            title="PFS — Subgroup Analysis",
            tfl_type=T,
            section=S142,
            sort_key=17,
            oncology_only=True,
            population="Intent-to-Treat (ITT) Population",
            placeholder_columns=[
                "Subgroup\nLevel",
                "G1 n/N\nMed PFS",
                "G2 n/N\nMed PFS",
                "...\n...\nHR [95% CI]",
                "Interaction\np-value",
            ],
            shell_rows=[
                ["Overall", "xx/xx, xx.x", "xx/xx, xx.x", "...", "x.xx [x.xx, x.xx]", "—"],
                ["Age <65", "xx/xx, xx.x", "xx/xx, xx.x", "...", "x.xx [x.xx, x.xx]", "x.xxx"],
                ["Age >=65", "xx/xx, xx.x", "xx/xx, xx.x", "...", "x.xx [x.xx, x.xx]", ""],
                EROW5,
            ],
            dataset_source="ADSL, ADTTE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_pfs_subgroup.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.2.18",
            title="OS — Subgroup Analysis",
            tfl_type=T,
            section=S142,
            sort_key=18,
            oncology_only=True,
            population="Intent-to-Treat (ITT) Population",
            placeholder_columns=[
                "Subgroup\nLevel",
                "G1 n/N\nMed OS",
                "G2 n/N\nMed OS",
                "...\n...\nHR [95% CI]",
                "Interaction\np-value",
            ],
            shell_rows=[
                ["Overall", "xx/xx, xx.x", "xx/xx, xx.x", "...", "x.xx [x.xx, x.xx]", "—"],
                ["Age <65", "xx/xx, xx.x", "xx/xx, xx.x", "...", "x.xx [x.xx, x.xx]", "x.xxx"],
                EROW5,
            ],
            dataset_source="ADSL, ADTTE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_os_subgroup.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.2.19",
            title="Summary of Target Lesion Changes from Baseline",
            tfl_type=T,
            section=S142,
            sort_key=19,
            oncology_only=True,
            population="ITT with Measurable Disease and Post-Baseline Assessment",
            placeholder_columns=[
                "Parameter",
                "XXX Group 1\n(N=XX)",
                "XXX Group 2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {
                    "label": "Subjects with Baseline and >=1 Post-BL Assessment",
                    "bold": True,
                    "values": ["xx", "xx", "...", "xx"],
                },
                {"label": "Best % Change from Baseline in Target Lesion Sum", "bold": True},
                {
                    "label": "  Mean (SD)",
                    "indent": True,
                    "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"],
                },
                {"label": "  Median", "indent": True, "values": ["xx.x", "xx.x", "...", "xx.x"]},
                {
                    "label": "  Min, Max",
                    "indent": True,
                    "values": ["xx.x, xx.x", "xx.x, xx.x", "...", "xx.x, xx.x"],
                },
                {"label": "Best % Change Category", "bold": True},
                {
                    "label": "  >=20% Increase (PD)",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  -30% to +20% (SD)",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  >= -30% Decrease (PR/CR)",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  >= -100% (CR)",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "Target lesion sum per RECIST 1.1. Best % change = min(post-baseline sum) - baseline sum / baseline sum * 100."
            ],
            dataset_source="ADSL, ADRS",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_target_lesion.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.2.20",
            title="Landmark Analysis of OS by 6-Month PFS Status",
            tfl_type=T,
            section=S142,
            sort_key=20,
            oncology_only=True,
            population="ITT Alive and On-Study at 6 Months",
            placeholder_columns=[
                "PFS Status at 6M",
                "G1 n/N\nMed OS",
                "G2 n/N\nMed OS",
                "...\n...\nHR [95% CI]",
            ],
            shell_rows=[
                ["Progression-Free at 6M", "xx/xx, NR", "xx/xx, NR", "...", "x.xx [x.xx, x.xx]"],
                ["Progressed by 6M", "xx/xx, xx.x", "xx/xx, xx.x", "...", "x.xx [x.xx, x.xx]"],
                EROW,
            ],
            dataset_source="ADSL, ADTTE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_landmark_os.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.2.21",
            title="Time to First Subsequent Therapy (TFST)",
            tfl_type=T,
            section=S142,
            sort_key=21,
            oncology_only=True,
            population="ITT Population",
            placeholder_columns=[
                "Parameter",
                "XXX Group 1\n(N=XX)",
                "XXX Group 2\n(N=XX)",
                "...",
                "Overall\n(N=XX)",
            ],
            shell_rows=[
                {"label": "Number of Subjects", "bold": True, "values": ["xx", "xx", "...", "xx"]},
                {
                    "label": "Subjects with Subsequent Therapy, n (%)",
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Censored, n (%)",
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Median TFST, months (95% CI)",
                    "bold": True,
                    "values": [
                        "xx.x (xx.x, xx.x)",
                        "xx.x (xx.x, xx.x)",
                        "...",
                        "xx.x (xx.x, xx.x)",
                    ],
                },
                {
                    "label": "Hazard Ratio (95% CI)",
                    "bold": True,
                    "values": ["x.xx [x.xx, x.xx]", "", "...", ""],
                },
                {"label": "p-value (stratified log-rank)", "values": ["x.xxx", "", "...", ""]},
                {"label": "Subsequent Therapy Type", "bold": True},
                {
                    "label": "  Chemotherapy",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Targeted Therapy",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Immunotherapy",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "TFST: time from randomization to first subsequent anti-cancer therapy or death.",
                "KM estimates. Brookmeyer-Crowley CI for median.",
            ],
            dataset_source="ADSL, ADTTE, ADCM",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_tfst.sas",
        )
    )

    # Oncology figures
    items.append(
        TFLItem(
            id="F14.2.4",
            title="Waterfall Plot — Best Percentage Change in Target Lesions",
            tfl_type=F,
            section=S142,
            sort_key=26,
            oncology_only=True,
            population="ITT with Measurable Disease and Post-Baseline Assessment",
            figure_description="Waterfall: best % change per subject, BOR-colored bars, ref lines +20%/-30%.",
            dataset_source="ADSL, ADRS",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="f_waterfall.sas",
            figure_type="waterfall",
            figure_width_inches=6.5,
            figure_height_inches=3.5,
        )
    )

    items.append(
        TFLItem(
            id="F14.2.5",
            title="Spider Plot — Percentage Change in Tumor Burden Over Time",
            tfl_type=F,
            section=S142,
            sort_key=27,
            oncology_only=True,
            population="ITT with Measurable Disease",
            figure_description="Spider: % change trajectories, BOR-colored lines, PD/death terminal markers.",
            dataset_source="ADSL, ADRS",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="f_spider.sas",
            figure_type="spider",
            figure_width_inches=6,
            figure_height_inches=3.5,
        )
    )

    items.append(
        TFLItem(
            id="F14.2.6",
            title="Swimmer Plot — Duration of Treatment and Response",
            tfl_type=F,
            section=S142,
            sort_key=28,
            oncology_only=True,
            population="Safety Population",
            figure_description="Swimmer: horizontal bars showing treatment duration, response/progression/ongoing markers.",
            dataset_source="ADSL, ADEX, ADRS",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="f_swimmer.sas",
            figure_type="swimmer",
            figure_width_inches=6.5,
            figure_height_inches=4,
        )
    )

    items.append(
        TFLItem(
            id="F14.2.7",
            title="Kaplan-Meier Plot — Progression-Free Survival",
            tfl_type=F,
            section=S142,
            sort_key=29,
            oncology_only=True,
            population="Intent-to-Treat (ITT) Population",
            figure_description="KM PFS: step-function curves, + censoring, number-at-risk table, HR/p-value annotation.",
            dataset_source="ADSL, ADTTE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="f_km_pfs.sas",
            figure_type="km_curve",
            figure_width_inches=6,
            figure_height_inches=3.5,
        )
    )

    items.append(
        TFLItem(
            id="F14.2.8",
            title="Kaplan-Meier Plot — Overall Survival",
            tfl_type=F,
            section=S142,
            sort_key=30,
            oncology_only=True,
            population="Intent-to-Treat (ITT) Population",
            figure_description="KM OS: step-function curves, + censoring, number-at-risk table, HR/p-value annotation.",
            dataset_source="ADSL, ADTTE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="f_km_os.sas",
            figure_type="km_curve",
            figure_width_inches=6,
            figure_height_inches=3.5,
        )
    )

    items.append(
        TFLItem(
            id="F14.2.9",
            title="Forest Plot — PFS by Subgroup",
            tfl_type=F,
            section=S142,
            sort_key=31,
            oncology_only=True,
            population="Intent-to-Treat (ITT) Population",
            figure_description="Forest PFS: HR [95% CI] per subgroup, overall diamond at bottom.",
            dataset_source="ADSL, ADTTE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="f_forest_pfs.sas",
            figure_type="forest",
            figure_width_inches=6,
            figure_height_inches=3.5,
        )
    )

    items.append(
        TFLItem(
            id="F14.2.10",
            title="Forest Plot — OS by Subgroup",
            tfl_type=F,
            section=S142,
            sort_key=32,
            oncology_only=True,
            population="Intent-to-Treat (ITT) Population",
            figure_description="Forest OS: HR [95% CI] per subgroup, overall diamond at bottom.",
            dataset_source="ADSL, ADTTE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="f_forest_os.sas",
            figure_type="forest",
            figure_width_inches=6,
            figure_height_inches=3.5,
        )
    )

    items.append(
        TFLItem(
            id="T14.2.22",
            title="PK/PD Exposure-Response Correlation Analysis",
            tfl_type=T,
            section=S142,
            sort_key=22,
            population="PK/PD Evaluable Population",
            placeholder_columns=["PK Parameter\nQuartile", "N", "Response Rate (%)", "95% CI"],
            shell_rows=[
                ["AUC0-tau — Q1 (lowest)", "xx", "xx.x%", "[xx.x, xx.x]"],
                ["AUC0-tau — Q2", "xx", "xx.x%", "[xx.x, xx.x]"],
                ["AUC0-tau — Q3", "xx", "xx.x%", "[xx.x, xx.x]"],
                ["AUC0-tau — Q4 (highest)", "xx", "xx.x%", "[xx.x, xx.x]"],
                EROW,
            ],
            dataset_source="ADSL, ADPK, ADEFF",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_pkpd_corr.sas",
        )
    )

    items.append(
        TFLItem(
            id="T14.2.23",
            title="Responder Analysis of Primary Clinical Endpoint",
            tfl_type=T,
            section=S142,
            sort_key=23,
            non_oncology_only=True,
            population="Intent-to-Treat (ITT) Population",
            placeholder_columns=[
                "Responder Analysis",
                "XXX Group 1\n(N=XX)",
                "XXX Group 2\n(N=XX)",
                "Difference / Effect",
                "95% CI / p-value",
            ],
            shell_rows=[
                ["Responders, n (%)", "xx (xx.x)", "xx (xx.x)", "xx.x", "[xx.x, xx.x]"],
                ["Non-Responders, n (%)", "xx (xx.x)", "xx (xx.x)", "", ""],
                ["Risk Difference (%)", "", "", "xx.x", "[xx.x, xx.x]"],
                ["Odds Ratio", "", "", "x.xx", "[x.xx, x.xx]"],
                ["p-value", "", "", "", "x.xxx"],
            ],
            footnotes=[
                "Responder definition per protocol and SAP. Stratified CMH / logistic model as applicable."
            ],
            dataset_source="ADSL, ADEFF",
            source_listing="L16.2.34",
            program_ref="t_responder_primary.sas",
            shell_family="Non-Oncology Efficacy",
            study_phase_scope="Phase II-III",
            coverage_summary="Core (Phase II-III, Non-Oncology)",
        )
    )

    items.append(
        TFLItem(
            id="T14.2.24",
            title="Annualized Clinically Significant Event / Exacerbation Rate Analysis",
            tfl_type=T,
            section=S142,
            sort_key=24,
            non_oncology_only=True,
            population="Intent-to-Treat (ITT) Population",
            placeholder_columns=[
                "Event Rate Analysis",
                "XXX Group 1\n(N=XX)",
                "XXX Group 2\n(N=XX)",
                "Rate Ratio",
                "95% CI / p-value",
            ],
            shell_rows=[
                ["Subjects with >=1 Event, n (%)", "xx (xx.x)", "xx (xx.x)", "", ""],
                ["Total Number of Events", "xx", "xx", "", ""],
                ["Exposure Time (Patient-Years)", "xx.x", "xx.x", "", ""],
                ["Annualized Event Rate", "x.xx", "x.xx", "x.xx", "[x.xx, x.xx]"],
                ["Negative Binomial Model p-value", "", "", "", "x.xxx"],
            ],
            footnotes=[
                "Event/exacerbation definitions and over-dispersion model settings per SAP."
            ],
            dataset_source="ADSL, ADEFF, ADTTE",
            source_listing="L16.2.34",
            program_ref="t_event_rate.sas",
            shell_family="Non-Oncology Efficacy",
            study_phase_scope="Phase II-III",
            coverage_summary="Core (Phase II-III, Non-Oncology)",
        )
    )

    items.append(
        TFLItem(
            id="T14.2.25",
            title="Time to First Clinically Significant Event",
            tfl_type=T,
            section=S142,
            sort_key=25,
            non_oncology_only=True,
            population="Intent-to-Treat (ITT) Population",
            placeholder_columns=[
                "Time-to-Event Statistic",
                "XXX Group 1\n(N=XX)",
                "XXX Group 2\n(N=XX)",
                "Hazard Ratio",
                "95% CI / p-value",
            ],
            shell_rows=[
                ["Subjects with Event, n (%)", "xx (xx.x)", "xx (xx.x)", "", ""],
                ["Median Time to First Event (days)", "xx.x", "xx.x", "", ""],
                ["25th, 75th Percentile", "xx.x, xx.x", "xx.x, xx.x", "", ""],
                ["Stratified Cox Model", "", "", "x.xx", "[x.xx, x.xx]"],
                ["Stratified Log-Rank p-value", "", "", "", "x.xxx"],
            ],
            footnotes=[
                "Clinically significant event defined per adjudication or protocol rules. KM estimates and Cox model per SAP."
            ],
            dataset_source="ADSL, ADTTE",
            source_listing="L16.2.34",
            program_ref="t_time_to_event_nononc.sas",
            shell_family="Non-Oncology Efficacy",
            study_phase_scope="Phase II-III",
            coverage_summary="Core (Phase II-III, Non-Oncology)",
        )
    )

    items.append(
        TFLItem(
            id="F14.2.11",
            title="Kaplan-Meier Plot — Time to First Clinically Significant Event",
            tfl_type=F,
            section=S142,
            sort_key=33,
            non_oncology_only=True,
            population="Intent-to-Treat (ITT) Population",
            figure_description="KM curve for time to first protocol-defined clinically significant event with censoring marks and number-at-risk table.",
            dataset_source="ADSL, ADTTE",
            source_listing="L16.2.34",
            program_ref="f_km_event_nononc.sas",
            figure_type="km_curve",
            figure_width_inches=6,
            figure_height_inches=3.5,
            shell_family="Non-Oncology Efficacy",
            study_phase_scope="Phase II-III",
            coverage_summary="Core (Phase II-III, Non-Oncology)",
        )
    )

    items.append(
        TFLItem(
            id="T14.2.26",
            title="Annualized Moderate or Severe Respiratory Exacerbation Rate",
            tfl_type=T,
            section=S142,
            sort_key=26,
            non_oncology_only=True,
            population="Intent-to-Treat (ITT) Population",
            placeholder_columns=[
                "Respiratory Exacerbation Analysis",
                "XXX Group 1\n(N=XX)",
                "XXX Group 2\n(N=XX)",
                "Rate Ratio",
                "95% CI / p-value",
            ],
            shell_rows=[
                [
                    "Subjects with >=1 Moderate or Severe Exacerbation, n (%)",
                    "xx (xx.x)",
                    "xx (xx.x)",
                    "",
                    "",
                ],
                ["Total Moderate or Severe Exacerbations", "xx", "xx", "", ""],
                ["Exposure Time (Patient-Years)", "xx.x", "xx.x", "", ""],
                ["Annualized Exacerbation Rate", "x.xx", "x.xx", "x.xx", "[x.xx, x.xx]"],
                ["Negative Binomial Model p-value", "", "", "", "x.xxx"],
            ],
            footnotes=[
                "Moderate and severe exacerbations defined per protocol, including systemic corticosteroid, antibiotic, emergency visit, or hospitalization criteria as applicable."
            ],
            dataset_source="ADSL, ADEFF, ADTTE",
            source_listing="L16.2.35",
            program_ref="t_resp_exac_rate.sas",
            shell_family="Respiratory Exacerbation",
            study_phase_scope="Phase II-III",
            coverage_summary="Core (Phase II-III, Non-Oncology)",
        )
    )

    items.append(
        TFLItem(
            id="T14.2.27",
            title="Time to First Moderate or Severe Respiratory Exacerbation",
            tfl_type=T,
            section=S142,
            sort_key=27,
            non_oncology_only=True,
            population="Intent-to-Treat (ITT) Population",
            placeholder_columns=[
                "Time-to-First Exacerbation Statistic",
                "XXX Group 1\n(N=XX)",
                "XXX Group 2\n(N=XX)",
                "Hazard Ratio",
                "95% CI / p-value",
            ],
            shell_rows=[
                ["Subjects with Event, n (%)", "xx (xx.x)", "xx (xx.x)", "", ""],
                ["Median Time to First Exacerbation (days)", "xx.x", "xx.x", "", ""],
                ["Event-Free Rate at Week 24, %", "xx.x", "xx.x", "", ""],
                ["Stratified Cox Model", "", "", "x.xx", "[x.xx, x.xx]"],
                ["Stratified Log-Rank p-value", "", "", "", "x.xxx"],
            ],
            footnotes=[
                "Event timing is based on protocol-defined onset date of the first moderate or severe respiratory exacerbation."
            ],
            dataset_source="ADSL, ADTTE",
            source_listing="L16.2.35",
            program_ref="t_resp_exac_tte.sas",
            shell_family="Respiratory Exacerbation",
            study_phase_scope="Phase II-III",
            coverage_summary="Core (Phase II-III, Non-Oncology)",
        )
    )

    items.append(
        TFLItem(
            id="F14.2.12",
            title="Kaplan-Meier Plot — Time to First Moderate or Severe Respiratory Exacerbation",
            tfl_type=F,
            section=S142,
            sort_key=34,
            non_oncology_only=True,
            population="Intent-to-Treat (ITT) Population",
            figure_description="KM curve for time to first moderate or severe respiratory exacerbation with censoring marks and number-at-risk table.",
            dataset_source="ADSL, ADTTE",
            source_listing="L16.2.35",
            program_ref="f_resp_exac_km.sas",
            figure_type="km_curve",
            figure_width_inches=6,
            figure_height_inches=3.5,
            shell_family="Respiratory Exacerbation",
            study_phase_scope="Phase II-III",
            coverage_summary="Core (Phase II-III, Non-Oncology)",
        )
    )

    items.append(
        TFLItem(
            id="T14.2.28",
            title="Adjudicated Major Adverse Cardiovascular Events (MACE) Summary",
            tfl_type=T,
            section=S142,
            sort_key=28,
            non_oncology_only=True,
            population="Intent-to-Treat (ITT) Population",
            placeholder_columns=[
                "Cardiovascular Event Summary",
                "XXX Group 1\n(N=XX)",
                "XXX Group 2\n(N=XX)",
                "Hazard Ratio / Risk Difference",
                "95% CI / p-value",
            ],
            shell_rows=[
                [
                    "Subjects with >=1 Adjudicated MACE, n (%)",
                    "xx (xx.x)",
                    "xx (xx.x)",
                    "x.xx",
                    "[x.xx, x.xx]",
                ],
                ["Cardiovascular Death, n (%)", "xx (xx.x)", "xx (xx.x)", "", ""],
                ["Non-fatal Myocardial Infarction, n (%)", "xx (xx.x)", "xx (xx.x)", "", ""],
                ["Non-fatal Stroke, n (%)", "xx (xx.x)", "xx (xx.x)", "", ""],
                ["Urgent Coronary Revascularization, n (%)", "xx (xx.x)", "xx (xx.x)", "", ""],
            ],
            footnotes=[
                "MACE components are adjudicated per charter. Composite definition and censoring rules per SAP."
            ],
            dataset_source="ADSL, ADEFF, ADTTE",
            source_listing="L16.2.36",
            program_ref="t_mace_summary.sas",
            shell_family="Cardiovascular MACE and HF Hospitalization",
            study_phase_scope="Phase II-III",
            coverage_summary="Core (Phase II-III, Non-Oncology)",
        )
    )

    items.append(
        TFLItem(
            id="T14.2.29",
            title="Time to First MACE or Heart Failure Hospitalization",
            tfl_type=T,
            section=S142,
            sort_key=29,
            non_oncology_only=True,
            population="Intent-to-Treat (ITT) Population",
            placeholder_columns=[
                "Time-to-Cardiovascular Event Statistic",
                "XXX Group 1\n(N=XX)",
                "XXX Group 2\n(N=XX)",
                "Hazard Ratio",
                "95% CI / p-value",
            ],
            shell_rows=[
                ["Subjects with Event, n (%)", "xx (xx.x)", "xx (xx.x)", "", ""],
                ["Median Time to First Event (days)", "xx.x", "xx.x", "", ""],
                ["Event-Free Rate at Month 12, %", "xx.x", "xx.x", "", ""],
                ["Stratified Cox Model", "", "", "x.xx", "[x.xx, x.xx]"],
                ["Stratified Log-Rank p-value", "", "", "", "x.xxx"],
            ],
            footnotes=[
                "Event includes first adjudicated MACE component or first hospitalization for worsening heart failure, whichever occurs first."
            ],
            dataset_source="ADSL, ADTTE",
            source_listing="L16.2.36",
            program_ref="t_mace_hf_tte.sas",
            shell_family="Cardiovascular MACE and HF Hospitalization",
            study_phase_scope="Phase II-III",
            coverage_summary="Core (Phase II-III, Non-Oncology)",
        )
    )

    items.append(
        TFLItem(
            id="F14.2.13",
            title="Kaplan-Meier Plot — Time to First MACE or Heart Failure Hospitalization",
            tfl_type=F,
            section=S142,
            sort_key=35,
            non_oncology_only=True,
            population="Intent-to-Treat (ITT) Population",
            figure_description="KM curve for time to first adjudicated MACE or worsening-heart-failure hospitalization with censoring marks and number-at-risk table.",
            dataset_source="ADSL, ADTTE",
            source_listing="L16.2.36",
            program_ref="f_mace_hf_km.sas",
            figure_type="km_curve",
            figure_width_inches=6,
            figure_height_inches=3.5,
            shell_family="Cardiovascular MACE and HF Hospitalization",
            study_phase_scope="Phase II-III",
            coverage_summary="Core (Phase II-III, Non-Oncology)",
        )
    )

    items.append(
        TFLItem(
            id="T14.2.30",
            title="Autoimmune Disease Flare and Clinical Responder Analysis",
            tfl_type=T,
            section=S142,
            sort_key=30,
            non_oncology_only=True,
            population="Intent-to-Treat (ITT) Population",
            placeholder_columns=[
                "Autoimmune Disease Activity Analysis",
                "XXX Group 1\n(N=XX)",
                "XXX Group 2\n(N=XX)",
                "Difference / Effect",
                "95% CI / p-value",
            ],
            shell_rows=[
                [
                    "Clinical Responders at Week 24, n (%)",
                    "xx (xx.x)",
                    "xx (xx.x)",
                    "xx.x",
                    "[xx.x, xx.x]",
                ],
                [
                    "Subjects with >=1 Disease Flare, n (%)",
                    "xx (xx.x)",
                    "xx (xx.x)",
                    "xx.x",
                    "[xx.x, xx.x]",
                ],
                ["Mean Change in Disease Activity Score", "xx.x", "xx.x", "xx.x", "[xx.x, xx.x]"],
                ["Odds Ratio for Response", "", "", "x.xx", "[x.xx, x.xx]"],
                ["p-value", "", "", "", "x.xxx"],
            ],
            footnotes=[
                "Responder and flare definitions are protocol-specific and may be based on composite disease activity criteria, rescue medication, or physician global assessment."
            ],
            dataset_source="ADSL, ADEFF",
            source_listing="L16.2.37",
            program_ref="t_autoimmune_resp_flare.sas",
            shell_family="Autoimmune Flare and Responder",
            study_phase_scope="Phase II-III",
            coverage_summary="Core (Phase II-III, Non-Oncology)",
        )
    )

    items.append(
        TFLItem(
            id="T14.2.31",
            title="Time to First Autoimmune Flare or Rescue Therapy",
            tfl_type=T,
            section=S142,
            sort_key=31,
            non_oncology_only=True,
            population="Intent-to-Treat (ITT) Population",
            placeholder_columns=[
                "Time-to-Flare Statistic",
                "XXX Group 1\n(N=XX)",
                "XXX Group 2\n(N=XX)",
                "Hazard Ratio",
                "95% CI / p-value",
            ],
            shell_rows=[
                ["Subjects with Event, n (%)", "xx (xx.x)", "xx (xx.x)", "", ""],
                ["Median Time to First Flare / Rescue Therapy (days)", "xx.x", "xx.x", "", ""],
                ["Flare-Free Rate at Week 52, %", "xx.x", "xx.x", "", ""],
                ["Stratified Cox Model", "", "", "x.xx", "[x.xx, x.xx]"],
                ["Stratified Log-Rank p-value", "", "", "", "x.xxx"],
            ],
            footnotes=[
                "Event is the earliest protocol-defined flare or initiation/escalation of rescue therapy."
            ],
            dataset_source="ADSL, ADTTE, ADCM",
            source_listing="L16.2.37",
            program_ref="t_autoimmune_ttf.sas",
            shell_family="Autoimmune Flare and Responder",
            study_phase_scope="Phase II-III",
            coverage_summary="Core (Phase II-III, Non-Oncology)",
        )
    )

    items.append(
        TFLItem(
            id="F14.2.14",
            title="Kaplan-Meier Plot — Time to First Autoimmune Flare or Rescue Therapy",
            tfl_type=F,
            section=S142,
            sort_key=36,
            non_oncology_only=True,
            population="Intent-to-Treat (ITT) Population",
            figure_description="KM curve for time to first autoimmune flare or rescue therapy with censoring marks and number-at-risk table.",
            dataset_source="ADSL, ADTTE, ADCM",
            source_listing="L16.2.37",
            program_ref="f_autoimmune_flare_km.sas",
            figure_type="km_curve",
            figure_width_inches=6,
            figure_height_inches=3.5,
            shell_family="Autoimmune Flare and Responder",
            study_phase_scope="Phase II-III",
            coverage_summary="Core (Phase II-III, Non-Oncology)",
        )
    )

    # --- Metabolic Endpoint (Non-Oncology) ---
    items.append(
        TFLItem(
            id="T14.2.32",
            title="Change from Baseline in Glycemic and Metabolic Parameters",
            tfl_type=T,
            section=S142,
            sort_key=32,
            non_oncology_only=True,
            population="Full Analysis Set (FAS)",
            placeholder_columns=[
                "Metabolic Parameter",
                "XXX Group 1\n(N=XX)",
                "XXX Group 2\n(N=XX)",
                "...",
            ],
            shell_rows=[
                ["HbA1c (%)", "", "", ""],
                ["  Baseline, Mean (SD)", "xx.x (xx.x)", "xx.x (xx.x)", ""],
                ["  Change at Week 24, LS Mean (SE)", "xx.x (xx.x)", "xx.x (xx.x)", ""],
                ["  LS Mean Difference [95% CI]", "xx.x [xx.x, xx.x]", "", ""],
                ["  p-value", "x.xxx", "", ""],
                ["", "", "", ""],
                ["Fasting Plasma Glucose (mg/dL)", "", "", ""],
                ["  Baseline, Mean (SD)", "xx.x (xx.x)", "xx.x (xx.x)", ""],
                ["  Change at Week 24, LS Mean (SE)", "xx.x (xx.x)", "xx.x (xx.x)", ""],
                ["  LS Mean Difference [95% CI]", "xx.x [xx.x, xx.x]", "", ""],
                ["  p-value", "x.xxx", "", ""],
                ["", "", "", ""],
                ["Body Weight (kg)", "", "", ""],
                ["  Baseline, Mean (SD)", "xx.x (xx.x)", "xx.x (xx.x)", ""],
                ["  Percent Change at Week 24", "xx.x (xx.x)", "xx.x (xx.x)", ""],
                ["  LS Mean Difference [95% CI]", "xx.x [xx.x, xx.x]", "", ""],
                ["  p-value", "x.xxx", "", ""],
            ],
            dataset_source="ADLB, ADSL",
            source_listing="L16.2.38",
            program_ref="t_metabolic_chg.sas",
            shell_family="Metabolic Endpoint",
            study_phase_scope="Phase II-III",
            coverage_summary="Core (Phase II-III, Non-Oncology)",
        )
    )
    items.append(
        TFLItem(
            id="T14.2.33",
            title="Responder Analysis for Clinically Meaningful Glycemic and Weight Targets",
            tfl_type=T,
            section=S142,
            sort_key=33,
            non_oncology_only=True,
            population="Full Analysis Set (FAS)",
            placeholder_columns=[
                "Responder Criterion",
                "XXX Group 1\n(N=XX)",
                "XXX Group 2\n(N=XX)",
                "...",
            ],
            shell_rows=[
                ["HbA1c and Body Weight Composite", "", "", ""],
                ["  HbA1c < 7.0% AND WL >= 5%, n (%)", "xx (xx.x)", "xx (xx.x)", ""],
                ["  HbA1c < 7.0% AND WL >= 10%, n (%)", "xx (xx.x)", "xx (xx.x)", ""],
                ["", "", "", ""],
                ["HbA1c Target Only", "", "", ""],
                ["  HbA1c < 7.0%, n (%)", "xx (xx.x)", "xx (xx.x)", ""],
                ["  HbA1c reduction >= 1.0%, n (%)", "xx (xx.x)", "xx (xx.x)", ""],
                ["", "", "", ""],
                ["Body Weight Target Only", "", "", ""],
                ["  Weight loss >= 5%, n (%)", "xx (xx.x)", "xx (xx.x)", ""],
                ["  Weight loss >= 10%, n (%)", "xx (xx.x)", "xx (xx.x)", ""],
                ["", "", "", ""],
                ["Odds Ratio [95% CI]", "x.xx [x.xx, x.xx]", "", ""],
                ["p-value", "x.xxx", "", ""],
            ],
            dataset_source="ADLB, ADSL",
            source_listing="L16.2.38",
            program_ref="t_metabolic_resp.sas",
            shell_family="Metabolic Endpoint",
            study_phase_scope="Phase II-III",
            coverage_summary="Core (Phase II-III, Non-Oncology)",
        )
    )
    items.append(
        TFLItem(
            id="F14.2.15",
            title="Mean Change from Baseline in HbA1c Over Time by Treatment Group",
            tfl_type=F,
            section=S142,
            sort_key=37,
            non_oncology_only=True,
            population="Full Analysis Set (FAS)",
            dataset_source="ADLB, ADSL",
            source_listing="L16.2.38",
            program_ref="f_hba1c_longitudinal.sas",
            figure_type="longitudinal",
            figure_width_inches=6,
            figure_height_inches=3.5,
            shell_family="Metabolic Endpoint",
            study_phase_scope="Phase II-III",
            coverage_summary="Core (Phase II-III, Non-Oncology)",
        )
    )

    # =====================================================================

    # --- 14.3.1 AE Expansion (CDISC ADAE) ---
    items.append(
        TFLItem(
            id="T14.3.1.24",
            title="Immune-Related Adverse Events (irAEs) by Preferred Term",
            tfl_type=T,
            section=S143,
            sort_key=24,
            oncology_only=True,
            population="Safety Population",
            placeholder_columns=[
                "Preferred Term",
                "G1\nn (%)",
                "G2\nn (%)",
                "...",
                "Overall\nn (%)",
            ],
            shell_rows=[
                {
                    "label": "Any irAE",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "Pneumonitis", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
                {"label": "Colitis", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
                {"label": "Hepatitis", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
                {
                    "label": "Dermatitis / Rash",
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "Thyroiditis", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
                {"label": "Nephritis", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "irAEs per protocol-defined list (MedDRA SMQ). Confirmed by adjudication. CTCAE [xx]."
            ],
            dataset_source="ADSL, ADAE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_irae_pt.sas",
            dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.1.25",
            title="Infusion-Related Reactions — Onset Timing, Maximum Grade, and Management",
            tfl_type=T,
            section=S143,
            sort_key=25,
            population="Safety Population",
            placeholder_columns=[
                "IRR Characteristic",
                "G1\nn (%)",
                "G2\nn (%)",
                "...",
                "Overall\nn (%)",
            ],
            shell_rows=[
                {
                    "label": "Subjects with Any IRR",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "Maximum CTCAE Grade", "bold": True},
                {
                    "label": "  Grade 1",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Grade 2",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Grade >=3",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "Onset Timing", "bold": True},
                {
                    "label": "  First infusion (Cycle 1)",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Subsequent infusions",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "Management", "bold": True},
                {
                    "label": "  Infusion rate slowed",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Infusion interrupted",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Prophylaxis in subsequent cycles",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=["IRR = any AE during or within 24h of infusion start. CTCAE [xx]."],
            dataset_source="ADSL, ADAE, ADEX",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_irr_detail.sas",
            dictionary_versions={"CTCAE": "[xx]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.1.26",
            title="TEAE Outcomes by System Organ Class — Resolved / Recovering / Not Recovered",
            tfl_type=T,
            section=S143,
            sort_key=26,
            population="Safety Population",
            placeholder_columns=[
                "System Organ Class",
                "Recovered\nn (%)",
                "Recovering\nn (%)",
                "Not Recovered\nn (%)",
                "Fatal\nn (%)",
                "Unknown\nn (%)",
            ],
            shell_rows=[
                {
                    "label": "Gastrointestinal disorders",
                    "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"],
                },
                {
                    "label": "General disorders",
                    "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"],
                },
                {
                    "label": "Blood and lymphatic system disorders",
                    "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"],
                },
                {
                    "label": "Skin and subcutaneous tissue disorders",
                    "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"],
                },
                {
                    "label": "Nervous system disorders",
                    "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "...", "..."]},
            ],
            footnotes=[
                "Outcome at last follow-up. Recovered = resolved no sequelae. MedDRA [xx.x]."
            ],
            dataset_source="ADSL, ADAE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ae_outcome.sas",
            dictionary_versions={"MedDRA": "[xx.x]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.1.27",
            title="Late-Onset TEAEs (>90 Days from First Dose) by SOC and PT",
            tfl_type=T,
            section=S143,
            sort_key=27,
            population="Safety Population with >90 Days Exposure",
            placeholder_columns=[
                "System Organ Class\nPreferred Term",
                "G1\nn (%)",
                "G2\nn (%)",
                "...",
                "Overall\nn (%)",
            ],
            shell_rows=[
                {
                    "label": "Any Late-Onset TEAE",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Blood and lymphatic system disorders",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Anaemia",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Neutropenia",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Skin disorders",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Rash",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Gastrointestinal disorders",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "Late-onset = AE start >90 days after first dose in subjects with >90 days on treatment. MedDRA [xx.x]."
            ],
            dataset_source="ADSL, ADAE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ae_late.sas",
            dictionary_versions={"MedDRA": "[xx.x]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.1.28",
            title="TEAEs by Post-Baseline Time Window — Onset Distribution",
            tfl_type=T,
            section=S143,
            sort_key=28,
            population="Safety Population",
            placeholder_columns=[
                "Time Window",
                "G1\nn (%) [E]",
                "G2\nn (%) [E]",
                "...",
                "Overall\nn (%) [E]",
            ],
            shell_rows=[
                {
                    "label": "0-30 Days",
                    "bold": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "31-90 Days",
                    "bold": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "91-180 Days",
                    "bold": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": ">180 Days",
                    "bold": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {
                    "label": "Follow-up (>30d post-last-dose)",
                    "bold": True,
                    "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "TEAEs assigned to window by onset date. [E] = total events. MedDRA [xx.x]."
            ],
            dataset_source="ADSL, ADAE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ae_timewindow.sas",
            dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.1.29",
            title="Treatment-Emergent SAEs by PT and ICH E2A Criterion — Group 1",
            tfl_type=T,
            section=S143,
            sort_key=29,
            population="Safety Population",
            placeholder_columns=[
                "Preferred Term",
                "Death\nn",
                "Life-Threat\nn",
                "Hospital\nn",
                "Disability\nn",
                "Cong. Anom.\nn",
                "Other\nn",
                "Total\nn (%)",
            ],
            shell_rows=[
                {"label": "Pneumonia", "values": ["xx", "xx", "xx", "0", "0", "xx", "xx (xx.x)"]},
                {
                    "label": "Febrile Neutropenia",
                    "values": ["xx", "xx", "xx", "0", "0", "0", "xx (xx.x)"],
                },
                {"label": "Sepsis", "values": ["xx", "xx", "xx", "0", "0", "xx", "xx (xx.x)"]},
                {
                    "label": "Pulmonary Embolism",
                    "values": ["xx", "xx", "xx", "0", "0", "0", "xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "...", "...", "...", "..."]},
            ],
            footnotes=[
                "SAE per ICH E2A. Multiple criteria per event possible. SAE listing: L16.2.5. MedDRA [xx.x]."
            ],
            dataset_source="ADSL, ADAE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_sae_crit.sas",
            dictionary_versions={"MedDRA": "[xx.x]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.1.30",
            title="Recurrent TEAEs — Subjects with Same PT >=2 Occurrences",
            tfl_type=T,
            section=S143,
            sort_key=30,
            population="Safety Population",
            placeholder_columns=[
                "System Organ Class\nPreferred Term",
                "Subjects >=2\nEvents\nn (%)",
                "Median Events\nper Subject",
                "G1 [E]",
                "G2 [E]",
            ],
            shell_rows=[
                {
                    "label": "Gastrointestinal disorders",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx", "[xx]", "[xx]"],
                },
                {
                    "label": "  Nausea",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx", "[xx]", "[xx]"],
                },
                {
                    "label": "  Diarrhoea",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx", "[xx]", "[xx]"],
                },
                {
                    "label": "Blood and lymphatic system disorders",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx", "[xx]", "[xx]"],
                },
                {
                    "label": "  Anaemia",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx", "[xx]", "[xx]"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "[E] = total number of events. Recurrence = same PT >=2 separate occurrences."
            ],
            dataset_source="ADSL, ADAE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ae_recur.sas",
            dictionary_versions={"MedDRA": "[xx.x]"},
        )
    )

    items.append(
        TFLItem(
            id="T14.3.1.31",
            title="TEAEs During Follow-up Period (>30 Days Post Last Dose)",
            tfl_type=T,
            section=S143,
            sort_key=31,
            population="Safety Population with Follow-up Data",
            placeholder_columns=[
                "System Organ Class\nPreferred Term",
                "G1\nn (%)",
                "G2\nn (%)",
                "...",
                "Overall\nn (%)",
            ],
            shell_rows=[
                {
                    "label": "Any TEAE During Follow-up",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Blood and lymphatic system disorders",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "  Anaemia",
                    "indent": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Gastrointestinal disorders",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {
                    "label": "Neoplasms benign, malignant",
                    "bold": True,
                    "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"],
                },
                {"label": "[...]", "values": ["...", "...", "...", "..."]},
            ],
            footnotes=[
                "Follow-up period = >30 days after last dose through end of study. MedDRA [xx.x]."
            ],
            dataset_source="ADSL, ADAE",
            source_listing="L16.2.1 / L16.2.2",
            program_ref="t_ae_followup.sas",
            dictionary_versions={"MedDRA": "[xx.x]"},
        )
    )

    return items
