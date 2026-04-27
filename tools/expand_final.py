"""Add final sections: E (14.3.4), F (14.4), G (16.2)"""
DEFS_PATH = r'g:\Workingspace\project-test\TFLshell\src\tflshell\data\definitions.py'

with open(DEFS_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================================
# E. 14.3.4 VS/ECG/PE expansion (8 tables + 1 figure)
# ============================================================
new_1434 = r'''
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

    items.append(F14.3.4.2", title="QTcF vs. Plasma Drug Concentration Scatter Plot with LOESS Fit",
        tfl_type=F, section=S143, sort_key=17,
        population="Safety Population with Time-Matched PK and ECG",
        figure_description="Scatter: placebo-adjusted change from baseline QTcF (y-axis) vs. plasma concentration (x-axis). LOESS fit line with 90% CI band. ICH E14 reference line at 10 ms.",
        dataset_source="ADSL, ADEG, ADPC", program_ref="f_qtcf_conc.sas",
        figure_type="longitudinal", figure_width_inches=5.5, figure_height_inches=3.5,
    ))
'''

new_1434 = new_1434.replace('F14.3.4.2"', 'id="F14.3.4.2"')

content = content.replace(
    "    # 14.4 SPECIAL ASSESSMENTS",
    new_1434 + "\n    # 14.4 SPECIAL ASSESSMENTS"
)

# ============================================================
# F. 14.4 expansion (7 tables)
# ============================================================
# Find the last 14.4 item before 16.2
new_144 = r'''
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
'''

content = content.replace(
    "    # 16.2 PATIENT DATA LISTINGS",
    new_144 + "\n    # 16.2 PATIENT DATA LISTINGS"
)

# ============================================================
# G. 16.2 New Listings (9 listings)
# ============================================================
# Find the last listing (L16.2.21) and insert after it
new_162 = r'''
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
'''

# Find the last listing (L16.2.21) and insert after it
# Find "L16.2.21" and insert the new block after its closing ))
last_listing = content.rfind('L16.2.21')
# Find the next )) after it
end_pos = content.find('))', content.find('))', last_listing) + 2)
# Actually, let me find the return statement
return_pos = content.rfind('return TFLCatalog(items)')
content = content[:return_pos] + new_162 + '\n    ' + content[return_pos:]

with open(DEFS_PATH, 'w', encoding='utf-8') as f:
    f.write(content)
print(f'Final content length: {len(content)}')
print('E + F + G sections added')
