"""Add remaining TFL expansions to definitions.py."""
import re

DEFS_PATH = r'g:\Workingspace\project-test\TFLshell\src\tflshell\data\definitions.py'

with open(DEFS_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================================
# B. 14.3.1 AE expansion (8 tables)
# Insert before line: "# 14.3 SAFETY"
# Find the LAST T14.3.1.x table and insert after it
# ============================================================

# Find the end of the last 14.3.1 AE table (T14.3.1.23)
# Insert before the 14.3.2 comment or before the 14.4 section
# Let me find a unique anchor - the last items.append before 14.4

new_1431_ae = '''

    # --- 14.3.1 AE Expansion (CDISC ADAE) ---
    items.append(TFLItem(
        id="T14.3.1.24", title="Immune-Related Adverse Events (irAEs) by Preferred Term",
        tfl_type=T, section=S143, sort_key=24, oncology_only=True,
        population="Safety Population",
        placeholder_columns=["Preferred Term",
                             "G1\\nn (%)", "G2\\nn (%)", "...", "Overall\\nn (%)"],
        shell_rows=[
            {"label": "Any irAE", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Pneumonitis", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Colitis", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Hepatitis", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Dermatitis / Rash", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Thyroiditis", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Nephritis", "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["irAEs per protocol-defined list (MedDRA SMQ). Confirmed by adjudication. CTCAE [xx]."],
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
            {"label": "  Prophylaxis in subsequent cycles", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["IRR = any AE during or within 24h of infusion start. CTCAE [xx]."],
        dataset_source="ADSL, ADAE, ADEX", program_ref="t_irr_detail.sas",
        dictionary_versions={"CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.26", title="TEAE Outcomes by System Organ Class — Resolved / Recovering / Not Recovered",
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
        footnotes=["Outcome at last follow-up. Recovered = resolved no sequelae. MedDRA [xx.x]."],
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
            {"label": "Skin disorders", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "  Rash", "indent": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "Gastrointestinal disorders", "bold": True, "values": ["xx (xx.x)", "xx (xx.x)", "...", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["Late-onset = AE start >90 days after first dose in subjects with >90 days on treatment. MedDRA [xx.x]."],
        dataset_source="ADSL, ADAE", program_ref="t_ae_late.sas",
        dictionary_versions={"MedDRA": "[xx.x]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.28", title="TEAEs by Post-Baseline Time Window — Onset Distribution",
        tfl_type=T, section=S143, sort_key=28,
        population="Safety Population",
        placeholder_columns=["Time Window",
                             "G1\\nn (%) [E]", "G2\\nn (%) [E]", "...", "Overall\\nn (%) [E]"],
        shell_rows=[
            {"label": "0-30 Days", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "31-90 Days", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "91-180 Days", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": ">180 Days", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "Follow-up (>30d post-last-dose)", "bold": True, "values": ["xx (xx.x) [xx]", "xx (xx.x) [xx]", "...", "xx (xx.x) [xx]"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["TEAEs assigned to window by onset date. [E] = total events. MedDRA [xx.x]."],
        dataset_source="ADSL, ADAE", program_ref="t_ae_timewindow.sas",
        dictionary_versions={"MedDRA": "[xx.x]", "CTCAE": "[xx]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.29", title="Treatment-Emergent SAEs by PT and ICH E2A Criterion — Group 1",
        tfl_type=T, section=S143, sort_key=29,
        population="Safety Population",
        placeholder_columns=["Preferred Term",
                             "Death\\nn", "Life-Threat\\nn", "Hospital\\nn",
                             "Disability\\nn", "Cong. Anom.\\nn", "Other\\nn", "Total\\nn (%)"],
        shell_rows=[
            {"label": "Pneumonia", "values": ["xx", "xx", "xx", "0", "0", "xx", "xx (xx.x)"]},
            {"label": "Febrile Neutropenia", "values": ["xx", "xx", "xx", "0", "0", "0", "xx (xx.x)"]},
            {"label": "Sepsis", "values": ["xx", "xx", "xx", "0", "0", "xx", "xx (xx.x)"]},
            {"label": "Pulmonary Embolism", "values": ["xx", "xx", "xx", "0", "0", "0", "xx (xx.x)"]},
            {"label": "[...]", "values": ["...", "...", "...", "...", "...", "...", "..."]},
        ],
        footnotes=["SAE per ICH E2A. Multiple criteria per event possible. SAE listing: L16.2.5. MedDRA [xx.x]."],
        dataset_source="ADSL, ADAE", program_ref="t_sae_crit.sas",
        dictionary_versions={"MedDRA": "[xx.x]"},
    ))

    items.append(TFLItem(
        id="T14.3.1.30", title="Recurrent TEAEs — Subjects with Same PT >=2 Occurrences",
        tfl_type=T, section=S143, sort_key=30,
        population="Safety Population",
        placeholder_columns=["System Organ Class\\nPreferred Term",
                             "Subjects >=2\\nEvents\\nn (%)", "Median Events\\nper Subject",
                             "G1 [E]", "G2 [E]"],
        shell_rows=[
            {"label": "Gastrointestinal disorders", "bold": True, "values": ["xx (xx.x)", "xx", "[xx]", "[xx]"]},
            {"label": "  Nausea", "indent": True, "values": ["xx (xx.x)", "xx", "[xx]", "[xx]"]},
            {"label": "  Diarrhoea", "indent": True, "values": ["xx (xx.x)", "xx", "[xx]", "[xx]"]},
            {"label": "Blood and lymphatic system disorders", "bold": True, "values": ["xx (xx.x)", "xx", "[xx]", "[xx]"]},
            {"label": "  Anaemia", "indent": True, "values": ["xx (xx.x)", "xx", "[xx]", "[xx]"]},
            {"label": "[...]", "values": ["...", "...", "...", "..."]},
        ],
        footnotes=["[E] = total number of events. Recurrence = same PT >=2 separate occurrences."],
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

# Insert before "# 14.3 SAFETY" comment
content = content.replace(
    "    # 14.3 SAFETY",
    new_1431_ae + "\n    # 14.3 SAFETY"
)

# ============================================================
# C. 14.3.2 Other Safety expansion (2 tables + 1 figure)
# ============================================================
# Find the last 14.3.2 item and insert after it
# The 14.3.2 items are right before 14.3.3 items
# Let me insert before the 14.4 section

new_1432 = '''

    # --- 14.3.2 Other Safety Expansion ---
    items.append(TFLItem(
        id="T14.3.2.4", title="Hy's Law — Component Parameters Detail at Peak Value per Subject",
        tfl_type=T, section=S143, sort_key=4,
        population="Safety Population with Baseline and >=1 Post-Baseline Labs",
        placeholder_columns=["Subject", "Group", "Peak ALT\\n(xULN)", "Peak AST\\n(xULN)",
                             "Peak TBL\\n(xULN)", "Peak ALP\\n(xULN)", "Hy's Law\\nMet?"],
        shell_rows=[
            ["xxxx/xxx", "Gx", "xx.x", "xx.x", "xx.x", "xx.x", "Yes / No"],
            ["xxxx/xxx", "Gx", "xx.x", "xx.x", "xx.x", "xx.x", "Yes / No"],
            {"label": "[...]", "values": ["...", "...", "...", "...", "...", "..."]},
        ],
        footnotes=["Hy's Law: ALT/AST >=3xULN + TBL >=2xULN + ALP <2xULN + no alternative etiology. Listing: L16.2.23."],
        dataset_source="ADSL, ADLB", program_ref="t_hyslaw_detail.sas",
    ))

    items.append(F14.3.2.1", title="eDISH Plot — Peak ALT vs. Peak Total Bilirubin with Hy's Law Zone",
        tfl_type=F, section=S143, sort_key=5,
        population="Safety Population with Baseline and Post-Baseline Labs",
        figure_description="eDISH: log-log scatter of peak ALT (xULN) vs. peak TBL (xULN). Quadrant at ALT >=3xULN, TBL >=2xULN = Hy's Law zone. Individual subject dots labeled.",
        dataset_source="ADSL, ADLB", program_ref="f_edish.sas",
        figure_type="box_plot", figure_width_inches=5.5, figure_height_inches=5.5,
    ))

    items.append(TFLItem(
        id="T14.3.2.5", title="Deaths — Primary and Secondary Causes with Narrative Cross-Reference",
        tfl_type=T, section=S143, sort_key=6,
        population="All Randomized Subjects",
        placeholder_columns=["Subject", "Group", "Primary Cause\\nof Death", "Secondary Cause",
                             "Days from\\nFirst Dose", "Days from\\nLast Dose", "Narrative ID"],
        shell_rows=[
            ["xxxx/xxx", "Gx", "Disease Progression", "Respiratory Failure", "xxx", "xx", "NAR-xxxx"],
            ["xxxx/xxx", "Gx", "Adverse Event", "Sepsis / Multi-organ Failure", "xxx", "xx", "NAR-xxxx"],
            {"label": "[...]", "values": ["...", "...", "...", "...", "...", "..."]},
        ],
        footnotes=["Primary cause per Investigator assessment. Listing: L16.2.20."],
        dataset_source="ADSL, ADAE, ADTTE", program_ref="t_death_detail.sas",
    ))
'''

# Fix the figure line
new_1432 = new_1432.replace('F14.3.2.1"', 'id="F14.3.2.1"')

# Insert before "# 14.4 SPECIAL ASSESSMENTS"
content = content.replace(
    "    # 14.4 SPECIAL ASSESSMENTS",
    new_1432 + "\n    # 14.4 SPECIAL ASSESSMENTS"
)

print(f'Content length after B+C: {len(content)}')

with open(DEFS_PATH, 'w', encoding='utf-8') as f:
    f.write(content)
print('B + C sections added')
