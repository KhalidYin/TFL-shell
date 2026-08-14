"""SOP content as structured data for DOCX generation."""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class SOPDocument:
    title: str
    sop_number: str
    version: str
    effective_date: str
    department: str
    sections: list = field(default_factory=list)


def build_sop_content(version: str = "1.0") -> SOPDocument:
    """Build the SOP content structure."""
    today = datetime.now().strftime("%d %B %Y")

    sop = SOPDocument(
        title="TFL Shell Template Usage and Management",
        sop_number="SOP-TFL-001",
        version=version,
        effective_date=today,
        department="Biostatistics / Statistical Programming",
    )

    sop.sections = [
        {
            "number": "1",
            "title": "PURPOSE AND SCOPE",
            "subsections": [
                {
                    "number": "1.1",
                    "title": "Purpose",
                    "content": [
                        "This Standard Operating Procedure (SOP) defines the standardized process for creating, using, and governing TFL (Tables, Figures, and Listings) shell templates for clinical study reporting.",
                        "The purpose is to ensure consistent shell structure, clear traceability to study standards, and controlled reuse across oncology and non-oncology clinical studies.",
                    ],
                },
                {
                    "number": "1.2",
                    "title": "Scope",
                    "content": [
                        "This SOP applies to clinical studies that use the ICH E3 CSR structure and require shell outputs before statistical results are produced.",
                        "The governed shell scope includes CSR Sections 14.1, 14.2, 14.3, 14.4, and 16.2.",
                        "It applies to Biostatistics, Statistical Programming, and Medical Writing functions involved in shell review, generation, and downstream execution.",
                    ],
                },
                {
                    "number": "1.3",
                    "title": "Applicable Studies",
                    "content": [
                        "Interventional clinical trials across oncology and non-oncology therapeutic areas.",
                        "Studies using standard CSR-oriented shell development before production programming begins.",
                        "Integrated reporting activities when the same shell governance rules are adopted.",
                    ],
                },
            ],
        },
        {
            "number": "2",
            "title": "DEFINITIONS AND ABBREVIATIONS",
            "subsections": [
                {
                    "number": "2.1",
                    "title": "Key Definitions",
                    "content": [
                        "TFL: Tables, Figures, and Listings that form the statistical output package of a CSR.",
                        "Shell: A governance-ready output template containing title, header metadata, column structure, analysis population, and footnotes without actual study results.",
                        "Shell-first convention: The approach in which structural examples are preserved while result cells remain placeholders.",
                        "Companion workbook: The synchronized XLSX catalog and usage guide generated alongside the DOCX shell template; it is not a workflow tracker.",
                    ],
                },
                {
                    "number": "2.2",
                    "title": "Abbreviations",
                    "content": [
                        "AE: Adverse Event",
                        "CSR: Clinical Study Report",
                        "CTCAE: Common Terminology Criteria for Adverse Events",
                        "ICH: International Council for Harmonisation",
                        "ITT: Intent-to-Treat",
                        "KM: Kaplan-Meier",
                        "MedDRA: Medical Dictionary for Regulatory Activities",
                        "PP: Per-Protocol",
                        "SAP: Statistical Analysis Plan",
                        "SOC: System Organ Class",
                        "TEAE: Treatment-Emergent Adverse Event",
                    ],
                },
            ],
        },
        {
            "number": "3",
            "title": "RESPONSIBILITIES",
            "subsections": [
                {
                    "number": "3.1",
                    "title": "Role-Specific Responsibilities",
                    "content": [
                        "Lead Statistician: Confirms shell scope, titles, populations, and methodological footnotes against the SAP and protocol.",
                        "Statistical Programmer: Generates the governed DOCX, XLSX, and SOP outputs and preserves approved shell structure during study implementation.",
                        "Medical Writer: Reviews language consistency, readability, and alignment with CSR conventions.",
                        "Quality Reviewer or Peer Reviewer: Verifies numbering, applicability, traceability notes, and consistency across all generated deliverables.",
                    ],
                },
            ],
        },
        {
            "number": "4",
            "title": "PROCEDURE",
            "subsections": [
                {
                    "number": "4.1",
                    "title": "Governed Deliverables",
                    "content": [
                        "The generator produces three coordinated deliverables: a DOCX shell template, a companion XLSX catalog workbook, and this SOP document.",
                        "All three deliverables must stay aligned on internal TFL ID, reviewer-facing display label, title, section, type, applicability, shell family, study phase scope, coverage summary, and versioning conventions.",
                    ],
                },
                {
                    "number": "4.2",
                    "title": "Shell Structure Rules",
                    "content": [
                        "Tables and listings preserve first-column structural examples such as row labels, categories, terms, or subject-structure identifiers needed to show the intended layout.",
                        "Non-structural cells use shell-style placeholders such as XX, xx (xx.x), x.xxx, or CI-like formats as appropriate to the intended display. No mock numeric results, subject-level details, or fabricated derived values are permitted in governed shell outputs.",
                        "Treatment groups may be displayed as columns, rows, or grouped subheaders according to the analysis, information density, and programming feasibility. Model estimates and treatment comparisons must remain independently identifiable and must not be placed under a treatment group merely to preserve a uniform template. Header sample sizes must remain generic (for example N=xx) rather than concrete counts.",
                        "Listing shells must not introduce fabricated subject-level records; only structural examples and result-free placeholders are permitted.",
                        "If a shell requires placeholder headers before study-specific terminology is finalized, neutral labels may be used temporarily so long as they remain governance-appropriate and result-free.",
                    ],
                },
                {
                    "number": "4.3",
                    "title": "Figure Shell Rules",
                    "content": [
                        "Figure shells retain simulated illustrations so expected visual layout is visible for review.",
                        "Simulated figures are shell artifacts only and must be replaced with study-specific production outputs during actual reporting.",
                    ],
                },
                {
                    "number": "4.4",
                    "title": "Document Formatting Rules",
                    "content": [
                        "Tables use the three-line table format (三线表) with no vertical gridlines and no internal horizontal gridlines between body rows.",
                        "Alignment follows column semantics: structural labels are generally left-aligned, numeric/statistical result columns are centered or decimal-aligned where supported, and listing identifiers or text fields may remain left-aligned. Multi-level headers must preserve their declared column spans.",
                        "Each TFL page includes sponsor, protocol, title, analysis set, and page numbering in the header block.",
                        "The main DOCX and SOP use Word-native automatic Table of Contents fields. Users must update fields in Word after opening the document to populate the TOC.",
                        "Each TFL should remain on one page when reasonably possible through spacing control and layout tuning; this is a best-effort formatting rule rather than an absolute guarantee for every shell.",
                    ],
                },
                {
                    "number": "4.5",
                    "title": "Workbook Usage",
                    "content": [
                        "The XLSX workbook functions as a catalog and usage guide, not as a workflow tracker.",
                        "It contains the master TFL inventory, section-level sheets, field definitions, usage guidance, and a controlled change log.",
                        "The workbook should retain both internal IDs for traceability and reviewer-facing display labels for presentation consistency with the DOCX shell template.",
                        "Applicability labels must clearly distinguish general, oncology-only, and non-oncology-only shells, and those labels guide shell selection for a specific study.",
                        "Governance metadata such as shell family, study phase scope, and coverage summary should be reviewed together with applicability before study-specific shell selection is finalized.",
                    ],
                },
                {
                    "number": "4.6",
                    "title": "TFL ID and File Naming Conventions",
                    "content": [
                        "TFL IDs use the pattern [Type][Section].[Sequence], where Type is T, F, or L.",
                        "Reviewer-facing output labels omit the leading type letter from the numeric portion and render as forms such as Table 14.2.11, Figure 14.2.4, or Listing 16.2.3.",
                        "Approved section values in the master shell are 14.1, 14.2, 14.3, 14.4, and 16.2.",
                        "Generated master deliverables follow controlled names such as TFL_Shell_Template, TFL_TOC, and TFL_Shell_SOP with the current version suffix.",
                        "Study-specific derivative files may prepend the protocol identifier while preserving version traceability.",
                    ],
                },
                {
                    "number": "4.7",
                    "title": "Version Control and Change Management",
                    "content": [
                        "Template-level updates must be recorded in the Change_Log sheet of the XLSX workbook.",
                        "Changes that affect scope, numbering, shell wording, traceability notes, or formatting conventions require versioned release control.",
                        "Superseded deliverables should be retained according to the organization's document retention policy.",
                        "Automated quality gates should verify generation, catalog validation, and regression tests before release or controlled reuse.",
                    ],
                },
            ],
        },
        {
            "number": "5",
            "title": "REFERENCES",
            "subsections": [
                {
                    "number": "5.1",
                    "title": "Regulatory and Industry References",
                    "content": [
                        "ICH E3: Structure and Content of Clinical Study Reports.",
                        "ICH E9 and ICH E9(R1): Statistical principles and estimand guidance for clinical trials.",
                        "CDISC ADaM and SDTM implementation guidance, current approved versions.",
                        "Applicable coding dictionaries and company programming standards used by the study team.",
                    ],
                },
            ],
        },
        {
            "number": "6",
            "title": "APPENDICES",
            "subsections": [
                {
                    "number": "Appendix A",
                    "title": "Companion Workbook",
                    "content": [
                        "Refer to the generated XLSX workbook for the governed TFL inventory, field definitions, and usage guidance.",
                    ],
                },
                {
                    "number": "Appendix B",
                    "title": "Shell Output Notes",
                    "content": [
                        "Representative table, figure, and listing shells in the DOCX template demonstrate formatting, placeholder conventions, and traceability structure only.",
                    ],
                },
            ],
        },
    ]

    return sop
