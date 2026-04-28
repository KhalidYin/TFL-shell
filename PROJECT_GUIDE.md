# PROJECT_GUIDE

## 1. Project Purpose

`TFLshell` is a governed template-generation project for the statistical section
of a clinical study report (CSR). Its primary purpose is to provide:

- reusable TFL shell templates for tables, figures, and listings
- a synchronized catalog workbook for shell governance and study-specific
  selection
- an SOP-style reference document for controlled usage

The repository is intended to support pre-production shell design, review, and
handoff. It is not intended to generate final statistical results or replace
study-specific SAP interpretation.

## 2. Primary Users

The project is designed for three review and operating perspectives:

### 2.1 Lead Statistician

Focus:

- shell completeness against protocol and SAP
- endpoint and population alignment
- methodological note adequacy
- fit-for-purpose use across study phases and therapeutic areas

### 2.2 Statistical Programming Lead

Focus:

- maintainable shell catalog structure
- metadata traceability
- synchronized output generation across DOCX, XLSX, and SOP
- extensibility for study-specific implementation

### 2.3 QA or Regulatory Reviewer

Focus:

- scope control
- numbering and traceability consistency
- explicit applicability rules
- documentation alignment between generator behavior and governed guidance

## 3. Current Deliverables

The repository currently centers on three coordinated outputs:

- CSR-facing DOCX shell template
- XLSX TFL catalog and usage guide
- SOP DOCX for shell usage and governance

The implementation target remains limited to the following CSR sections:

- `14.1` Demographics and Baseline Characteristics
- `14.2` Efficacy
- `14.3` Safety
- `14.4` Special Assessments
- `16.2` Patient Data Listings

The project does not currently govern `16.1`, and it does not produce actual
analysis results.

## 4. Operating Principles

- `Shell-first`: tables and listings are result-free structures, not mock result
  packages.
- `Traceability-first`: shells should retain dataset, program, dictionary, and
  footnote context where applicable.
- `Cross-output alignment`: DOCX, XLSX, SOP, and future tests must describe the
  same rules.
- `Governance before automation`: project rules and metadata definitions must be
  documented before code expansion.

## 5. Coverage Model

The repository should be interpreted as a governed master library, not as a
claim that every clinical design is fully covered. Coverage is organized by:

- study phase: Phase I, Phase II, Phase III
- therapeutic domain: oncology, non-oncology
- shell family: demographics, efficacy, safety, special assessments, listings

### 5.1 Coverage Status Terms

- `Core`: expected baseline shell family for common studies in the given context
- `Conditional`: used only for certain designs, modalities, endpoints, or
  development strategies
- `Gap`: recognized governance need not yet covered adequately

### 5.2 Phase and Domain View

| Context | Current Interpretation |
| --- | --- |
| Phase I | Safety, tolerability, PK, ECG/QTc, dose-escalation, DLT, MTD/RP2D, and selected food-effect / crossover clinical pharmacology shells are now explicitly represented, but escalation-design variants are still not exhaustive. |
| Phase II | Early efficacy, subgroup, sensitivity, biomarker, and PRO shells are broadly represented. |
| Phase III | Confirmatory efficacy, multiplicity-aware interpretation, safety summaries, and standard listings are represented at a high level. |
| Oncology | Explicitly stronger than other domains, especially in `14.2` efficacy figures and response endpoints. |
| Non-Oncology | General shells remain the baseline, but the library now also includes explicit non-oncology-only families for responder, event-rate, respiratory exacerbation, cardiovascular event, and autoimmune flare review. |

## 6. Practical Scope by Shell Family

| Shell Family | Current State |
| --- | --- |
| `14.1` Demographics and baseline | Strong baseline support for disposition, populations, history, medications, and exposure. |
| `14.2` Efficacy | Strongest in oncology, but now also includes explicit non-oncology families for responder, event-rate, respiratory exacerbation, MACE/HF hospitalization, and autoimmune flare time-to-event review. |
| `14.3` Safety | Broad and practical; includes AE, SAE, deaths, laboratory, vital signs, ECG, QTc, AESI, and dedicated Phase I dose-escalation / DLT / RP2D shells. |
| `14.4` Special assessments | Good support for PK, ADA, biomarkers, PD, and PRO, with new food-effect and crossover PK shells for Phase I clinical pharmacology. |
| `16.2` Listings | Broad listing inventory, including safety and special-assessment support plus new DLT review, food-effect PK, respiratory exacerbation, cardiovascular event, and autoimmune flare listings. |

## 7. Current Gaps

The following are known governance gaps and should be treated as active project
work, not as hidden assumptions:

- explicit non-oncology-only shell governance now covers several high-value domains, but disease-area-specific breadth is still limited beyond respiratory, cardiovascular, and autoimmune patterns
- phase-specific selection logic is now represented at the metadata layer, but not yet fully programmatic at the item-rule level
- some Phase I shell families remain under-specified, especially cohort-expansion, `3+3`, BOIN, CRM, formal TQT, DDI, and organ-impairment variants
- confirmatory-program governance for Phase III is not yet separated cleanly
  from general efficacy coverage
- CI-level release checks should still mature beyond the current baseline generation, validation, and regression tests

## 8. Recommended Workflow

Recommended usage order:

1. Review project scope and coverage assumptions in this guide.
2. Use `PROJECT_SPEC.md` to determine whether a shell family is `Core`,
   `Conditional`, or a `Gap`.
3. Select applicable shells in the workbook.
4. Tailor titles, populations, footnotes, and study-specific terminology against
   protocol and SAP.
5. Preserve the governed structure while creating study-specific derivatives.

## 9. Risk Reminder

- `Technical risk`: documentation and output behavior can drift if versioning
  and dependency governance are not tightened.
- `Maintenance risk`: oncology growth can outpace non-oncology governance and
  create a hidden bias in the library.
- `Project risk`: without explicit phase/domain coverage rules, users may
  overstate repository completeness during review or audit.

## 10. Optimization Roadmap

### 10.1 Immediate

- formalize phase/domain coverage rules in `PROJECT_SPEC.md`
- align documentation wording across guide, spec, SOP, and workbook guidance
- define the future test contract in `test_guide.md`
- extend non-oncology families where endpoint semantics are already stable

### 10.2 Mid-term

- expand non-oncology-specific shell governance into additional disease domains
- extend Phase I into a design-oriented shell library for escalation and specialty pharmacology
- add machine-checkable metadata fields for shell family and study-phase
  applicability

### 10.3 Toolchain

- maintain automated catalog and cross-output consistency checks
- use `pre-commit` for fast local validation and `CI` for generate/validate/test quality gates

## 11. Document Ownership

This file is the project-level orientation document. If a change affects:

- project purpose
- scope boundaries
- coverage interpretation
- review roles
- roadmap priorities

then `PROJECT_GUIDE.md` must be reviewed in the same change set.
