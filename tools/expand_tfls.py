"""Add 60+ new TFLs to definitions.py — CDISC data-domain driven expansion."""
import re

DEFS_PATH = r'g:\Workingspace\project-test\TFLshell\src\tflshell\data\definitions.py'

with open(DEFS_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================================
# A. 14.1 expansion (6 tables)
# ============================================================
new_141 = '''
    items.append(TFLItem(
        id="T14.1.12", title="Subject Disposition by Country and Site",
        tfl_type=T, section=S141, sort_key=12,
        population="All Randomized Subjects",
        placeholder_columns=["Country\\nSite", "Screened\\nn", "Randomized\\nn",
                             "Treated\\nn (%)", "Completed\\nn (%)", "Discontinued\\nn (%)"],
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
        placeholder_columns=["Eligibility Criterion", "Screen Failures\\nn", "Reason\\nCategory"],
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
        placeholder_columns=["Deviation Category\\nSubcategory",
                             "G1\\nn (%)", "G2\\nn (%)", "...", "Overall\\nn (%)"],
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
        placeholder_columns=["Body System\\nProcedure",
                             "G1\\nn (%)", "G2\\nn (%)", "...", "Overall\\nn (%)"],
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
        placeholder_columns=["ATC Level 3\\nPreferred Name",
                             "Prior\\nn (%)", "Concomitant\\nn (%)", "...", "Overall\\nn (%)"],
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
                             "G1\\nn (%)", "G2\\nn (%)", "...", "Overall\\nn (%)"],
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
'''

# Insert before 14.2 section
content = content.replace(
    "    # =====================================================================\n    # 14.2 EFFICACY",
    new_141 + "\n    # =====================================================================\n    # 14.2 EFFICACY"
)

# ============================================================
# B. 14.3.1 AE expansion (8 tables) — insert before 14.3.2 comment
# ============================================================
new_1431 = '''
    items.append(TFLItem(
        id="T14.3.1.24", title="Immune-Related Adverse Events (irAEs) by Preferred Term",
        tfl_type=T, section=S143, sort_key=24, oncology_only=True,
        population="Safety Population",
        placeholder_columns=["Preferred Term\\nSOC",
                             "G1\\nn (%)", "G2\\nn (%)", "...", "Overall\\nn (%)"],
        shell_rows=[
            {"label": "Any irAE", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Pneumonitis", "values": ["Immune-mediated lung", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Colitis", "values": ["Immune-mediated GI", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Hepatitis", "values": ["Immune-mediated hepatic", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Dermatitis/Rash", "values": ["Immune-mediated skin", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Thyroiditis", "values": ["Immune-mediated endocrine", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Nephritis", "values": ["Immune-mediated renal", "xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["irAEs identified per protocol-defined list and MedDRA SMQ [xx.x]. Confirmed by adjudication committee."],
        dataset_source="ADSL, ADAE", program_ref="t_irae_pt.sas",
        dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.25", title="Infusion-Related Reactions — Onset Timing, Maximum Grade, and Management",
        tfl_type=T, section=S143, sort_key=25,
        population="Safety Population",
        placeholder_columns=["IRR Characteristic",
                             "G1\\nn (%)", "G2\\nn (%)", "...", "Overall\\nn (%)"],
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
            {"label": "  Prophylaxis given in subsequent cycles", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["IRR defined as any AE occurring during or within 24 hours of infusion start. CTCAE [xx]."],
        dataset_source="ADSL, ADAE, ADEX", program_ref="t_irr_detail.sas",
        dictionary_versions={"CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.26", title="TEAE Outcomes by System Organ Class",
        tfl_type=T, section=S143, sort_key=26,
        population="Safety Population",
        placeholder_columns=["System Organ Class",
                             "Recovered\\nn (%)", "Recovering\\nn (%)",
                             "Not Recovered\\nn (%)", "Fatal\\nn (%)", "Unknown\\nn (%)"],
        shell_rows=[
            {"label": "Gastrointestinal disorders", "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"]},
            {"label": "General disorders", "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"]},
            {"label": "Blood and lymphatic system disorders", "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"]},
            {"label": "Skin and subcutaneous tissue disorders", "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"]},
            {"label": "Nervous system disorders", "values": ["xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "...", "..."]},
        ],
        footnotes=["Outcome assessed at last follow-up per subject. Recovered = resolved with no sequelae. MedDRA [xx.x]."],
        dataset_source="ADSL, ADAE", program_ref="t_ae_outcome.sas",
        dictionary_versions={"MedDRA": "[xx.x]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.27", title="Late-Onset TEAEs (>90 Days from First Dose) by SOC and PT",
        tfl_type=T, section=S143, sort_key=27,
        population="Safety Population with >90 Days Exposure",
        placeholder_columns=["System Organ Class\\nPreferred Term",
                             "G1\\nn (%)", "G2\\nn (%)", "...", "Overall\\nn (%)"],
        shell_rows=[
            {"label": "Any Late-Onset TEAE", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Blood and lymphatic system disorders", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Anaemia", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Neutropenia", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Skin and subcutaneous tissue disorders", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Rash", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Gastrointestinal disorders", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["Late-onset = AE start date >90 days after first dose in subjects with >90 days on treatment. MedDRA [xx.x]."],
        dataset_source="ADSL, ADAE", program_ref="t_ae_late.sas",
        dictionary_versions={"MedDRA": "[xx.x]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.28", title="TEAEs by Post-Baseline Time Window",
        tfl_type=T, section=S143, sort_key=28,
        population="Safety Population",
        placeholder_columns=["Time Window",
                             "G1\\nn (%) [E]", "G2\\nn (%) [E]", "...", "Overall\\nn (%) [E]"],
        shell_rows=[
            {"label": "0–30 Days", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "31–90 Days", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "91–180 Days", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": ">180 Days", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "Follow-up (>30d post-last-dose)", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["TEAEs assigned to time window based on onset date relative to first dose. [E] = number of events."],
        dataset_source="ADSL, ADAE", program_ref="t_ae_timewindow.sas",
        dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.29", title="Treatment-Emergent SAEs by Preferred Term and ICH E2A Criterion",
        tfl_type=T, section=S143, sort_key=29,
        population="Safety Population",
        placeholder_columns=["Preferred Term",
                             "Death\\nn", "Life-Threat\\nn",
                             "Hospitalization\\nn", "Disability\\nn",
                             "Congenital Anom.\\nn", "Other\\nn", "Total\\nn (%)"],
        shell_rows=[
            {"label": "Pneumonia", "values": ["xx", "xx", "xx", "0", "0", "xx", "xx (xx.x)"]},
            {"label": "Febrile Neutropenia", "values": ["xx", "xx", "xx", "0", "0", "0", "xx (xx.x)"]},
            {"label": "Sepsis", "values": ["xx", "xx", "xx", "0", "0", "xx", "xx (xx.x)"]},
            {"label": "Pulmonary Embolism", "values": ["xx", "xx", "xx", "0", "0", "0", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "...", "...", "...", "..."]},
        ],
        footnotes=["SAE per ICH E2A definition. Multiple criteria may apply per event. Shown for Group 1. MedDRA [xx.x]."],
        dataset_source="ADSL, ADAE", program_ref="t_sae_crit.sas",
        dictionary_versions={"MedDRA": "[xx.x]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.30", title="Recurrent TEAEs — Subjects with Same PT >=2 Occurrences by SOC",
        tfl_type=T, section=S143, sort_key=30,
        population="Safety Population",
        placeholder_columns=["System Organ Class\\nPreferred Term",
                             "Subjects\\nwith >=2 Events\\nn (%)", "Median Events\\nper Subject",
                             "G1 Total\\nEvents [E]", "G2 Total\\nEvents [E]"],
        shell_rows=[
            {"label": "Gastrointestinal disorders", "bold": True, "values": ["xx (xx.x)", "xx", "[xx]", "[xx]"]},
            {"label": "  Nausea", "indent": True, "values": ["xx (xx.x)", "xx", "[xx]", "[xx]"]},
            {"label": "  Diarrhoea", "indent": True, "values": ["xx (xx.x)", "xx", "[xx]", "[xx]"]},
            {"label": "Blood and lymphatic system disorders", "bold": True, "values": ["xx (xx.x)", "xx", "[xx]", "[xx]"]},
            {"label": "  Anaemia", "indent": True, "values": ["xx (xx.x)", "xx", "[xx]", "[xx]"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["[E] = total number of events per treatment arm. Recurrence = same PT reported >=2 separate times."],
        dataset_source="ADSL, ADAE", program_ref="t_ae_recur.sas",
        dictionary_versions={"MedDRA": "[xx.x]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.31", title="TEAEs During Follow-up Period (>30 Days Post Last Dose)",
        tfl_type=T, section=S143, sort_key=31,
        population="Safety Population with Follow-up Data",
        placeholder_columns=["System Organ Class\\nPreferred Term",
                             "G1\\nn (%)", "G2\\nn (%)", "...", "Overall\\nn (%)"],
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
'''

# Insert before 14.3.2 comment
content = content.replace(
    "    # --- 14.3.2 Other Safety",
    new_1431 + "\n    # --- 14.3.2 Other Safety"
)

print(f'Content length: {len(content)}')
with open(DEFS_PATH, 'w', encoding='utf-8') as f:
    f.write(content)
print('A + B sections added')
