"""Add sections D through G: 14.3.3 Lab, 14.3.4 VS/ECG/PE, 14.4, 16.2"""
DEFS_PATH = r'g:\Workingspace\project-test\TFLshell\src\tflshell\data\definitions.py'

with open(DEFS_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================================
# D. 14.3.3 Lab expansion (16 tables + 2 figures)
# Insert before "# 14.4 SPECIAL ASSESSMENTS"
# ============================================================
new_1433 = r'''
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
            {"label": "", "Baseline — Mean (SD)", "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "", "Worst Post-BL — Mean (SD)", "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "", ">=ULN, n (%)", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "CK-MB (ng/mL)", "bold": True},
            {"label": "", "Baseline — Mean (SD)", "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "NT-proBNP (pg/mL)", "bold": True},
            {"label": "", "Baseline — Mean (SD)", "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
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
            {"label": "", "Baseline — Mean (SD)", "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "", "Week 12 — Mean Chg (SD)", "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "UPCR (mg/mmol)", "bold": True},
            {"label": "", "Baseline — Geo Mean (CV%)", "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "", "Week 12 — Geo Mean (CV%)", "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "Microalbumin (mg/L)", "bold": True},
            {"label": "", "Baseline — Mean (SD)", "values": ["xx.x (xx.x)", "xx.x (xx.x)", "...", "xx.x (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["UPCR = Urine Protein/Creatinine Ratio. Listing: L16.2.25."],
        dataset_source="ADSL, ADLB", program_ref="t_urine_chem.sas",
    ))

    items.append(F14.3.3.4", title="Renal Safety Panel — eGFR Trajectory Over Time by Treatment Arm",
        tfl_type=F, section=S143, sort_key=26,
        population="Safety Population",
        figure_description="Line plot: mean (+/-SD) eGFR (CKD-EPI) over visits, individual subject spaghetti lines in background, treatment arms in different colors.",
        dataset_source="ADSL, ADLB", program_ref="f_egfr_traj.sas",
        figure_type="longitudinal", figure_width_inches=5.5, figure_height_inches=3.5,
    ))

    items.append(F14.3.3.5", title="Laboratory Toxicity Heatmap — CTCAE Grade by Parameter and Subject",
        tfl_type=F, section=S143, sort_key=27,
        population="Safety Population",
        figure_description="Heatmap: subjects (rows) vs. lab parameters (columns), color = worst CTCAE grade. Sidebar: treatment arm. Parameters: Hgb, Plt, Neut, ALT, AST, TBL, Cr.",
        dataset_source="ADSL, ADLB", program_ref="f_lab_heatmap.sas",
        figure_type="box_plot", figure_width_inches=6.5, figure_height_inches=4,
    ))
'''

# Fix the figure ids
new_1433 = new_1433.replace('F14.3.3.4"', 'id="F14.3.3.4"')
new_1433 = new_1433.replace('F14.3.3.5"', 'id="F14.3.3.5"')

# Insert before "# 14.4 SPECIAL ASSESSMENTS"
content = content.replace(
    "    # 14.4 SPECIAL ASSESSMENTS",
    new_1433 + "\n    # 14.4 SPECIAL ASSESSMENTS"
)

with open(DEFS_PATH, 'w', encoding='utf-8') as f:
    f.write(content)
print(f'D section added. Length: {len(content)}')
