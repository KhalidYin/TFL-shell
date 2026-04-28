# PROJECT_SPEC

## 1. Specification Purpose

This document defines the governed project specification for the `TFLshell`
repository. It is the primary source for:

- scope boundaries
- numbering and labeling rules
- applicability rules
- phase and therapeutic-area coverage expectations
- shell-family selection logic
- metadata expectations for future automation

## 2. Controlled Scope

### 2.1 In-Scope CSR Sections

The governed master-shell scope is restricted to:

- `14.1` Demographics and Baseline Characteristics
- `14.2` Efficacy
- `14.3` Safety
- `14.4` Special Assessments
- `16.2` Patient Data Listings

### 2.2 Out of Scope

The following are out of scope for the governed master library unless this
document is revised explicitly:

- `16.1` statistical tables and supporting narratives outside the defined shell
  outputs
- final study results
- study-specific SAP decision making
- subject-level mock datasets
- project-tracker workflows centered on owners, due dates, or status flags

## 3. Output Types

The library governs three output classes:

- `Table`
- `Figure`
- `Listing`

Tables and listings are shell-only and result-free.
Figures may retain simulated visuals for reviewer understanding.

## 4. Numbering and Labeling Rules

### 4.1 Internal IDs

Internal IDs follow:

`[Type][Section].[Sequence]`

Examples:

- `T14.2.11`
- `F14.2.4`
- `L16.2.3`

### 4.2 Reviewer-Facing Labels

Reviewer-facing labels omit the leading type letter from the numeric portion.

Examples:

- `Table 14.2.11`
- `Figure 14.2.4`
- `Listing 16.2.3`

### 4.3 Synchronization Rule

The following must always stay aligned:

- internal ID
- reviewer-facing label
- section
- title
- type
- applicability
- shell family
- study phase scope
- coverage summary

Any change to one of these fields requires review of the catalog, generators,
and guidance documents in the same change set.

## 5. Applicability Rules

Each shell must carry one controlled applicability label:

- `General`
- `Oncology only`
- `Non-Oncology only`

### 5.1 Interpretation

- `General` means intended for both oncology and non-oncology studies unless the
  protocol or SAP requires otherwise.
- `Oncology only` means the shell is based on oncology-specific endpoint or
  review practice and should not be reused by default outside oncology.
- `Non-Oncology only` means the shell is driven by non-oncology practice and
  should not be generalized automatically.

### 5.2 Current Governance Note

Current repository implementation is still stronger for `Oncology only` than for
`Non-Oncology only`, but the library now includes explicit non-oncology-only
shells for responder, event-rate, time-to-event, respiratory exacerbation,
cardiovascular event, and autoimmune flare review.

## 6. Shell Construction Rules

### 6.1 Tables

- preserve structural rows needed to communicate intended display semantics
- keep result-bearing cells generic and non-final
- allow placeholder styles that match the target display format
- use controlled `Group 1` / `Group 2` headers with an optional separate
  ellipsis expansion column where the master shell needs to indicate more groups
- do not merge the ellipsis expansion column with `Overall`, `Total`, `HR`, or
  other analytic columns
- allow `Overall` only when a pooled summary is clinically standard and should
  remain in the governed shell
- keep sample-size headers generic, for example `N=xx`
- do not retain subgroup-only tables when the same analytical intent is better
  covered by the main table plus a forest plot
- require source-listing references to be specific when a governed listing
  exists

### 6.2 Listings

- preserve listing structure and key variable labels
- do not introduce fabricated subject-level records
- preserve sort and display guidance where relevant

### 6.3 Figures

- simulated visuals are allowed as shell artifacts
- simulated visuals must not imply final analysis output
- figure title, body, notes, and pagination should remain grouped where
  reasonably possible

## 7. Metadata Requirements

Each governed shell should be traceable through metadata. The minimum governed
metadata model is:

- `TFL ID`
- `Display Label`
- `Title`
- `Type`
- `Section`
- `Shell Family`
- `Study Phase Scope`
- `Coverage Summary`
- `Population`
- `Applicability`
- `Dataset Source`
- `Program Reference`
- `Dictionary / Standard`
- `Placeholder Style`
- `Footnotes`
- `Remarks`

The future preferred metadata model should additionally include:

- `Shell Family`
- `Endpoint Class`
- `Analysis Class`
- `Regulatory Criticality`
- item-level phase tagging that is more specific than `Study Phase Scope`
- machine-checkable coverage classification beyond the current `Coverage Summary`

## 8. Coverage Matrix

The matrix below defines governance expectations at the shell-family level.

| Study Context | Demographics `14.1` | Efficacy `14.2` | Safety `14.3` | Special `14.4` | Listings `16.2` |
| --- | --- | --- | --- | --- | --- |
| Phase I Oncology | Core | Conditional | Core | Core | Core |
| Phase I Non-Oncology | Core | Conditional | Core | Core | Core |
| Phase II Oncology | Core | Core | Core | Conditional | Core |
| Phase II Non-Oncology | Core | Core | Core | Conditional | Core |
| Phase III Oncology | Core | Core | Core | Conditional | Core |
| Phase III Non-Oncology | Core | Core | Core | Conditional | Core |

### 8.1 Matrix Interpretation

- `Core` means the shell family should normally be represented in a governed
  study package for this context.
- `Conditional` means the shell family depends on modality, endpoint strategy,
  therapeutic mechanism, or protocol design.
- `Gap` is not shown at the family row level above because the gap is more often
  at the subfamily level and is listed below.

## 9. Subfamily Expectations

### 9.1 Phase I Core or Conditional Subfamilies

| Subfamily | Status |
| --- | --- |
| Subject disposition, demographics, populations | Core |
| Exposure, dose intensity, treatment duration | Core |
| AE, SAE, deaths, laboratory, vital signs, ECG/QTc | Core |
| PK concentration and parameter summaries | Core when PK is collected |
| Dose-escalation, DLT, MTD, RP2D, cohort review | Core to Conditional |
| Food-effect or crossover-specific summaries | Conditional |
| Intensive ECG or TQT-oriented interpretation | Conditional to Gap depending on program |
| Exploratory efficacy or biomarker summaries | Conditional |

### 9.2 Phase II Core or Conditional Subfamilies

| Subfamily | Status |
| --- | --- |
| Primary and secondary efficacy summaries | Core |
| Sensitivity, subgroup, and estimand-supporting tables | Core |
| Standard safety package | Core |
| Biomarker, PK/PD, ADA, PRO | Conditional |
| Early go/no-go design summaries or adaptive decision displays | Gap |

### 9.3 Phase III Core or Conditional Subfamilies

| Subfamily | Status |
| --- | --- |
| Confirmatory efficacy package | Core |
| Multiplicity-aware interpretation support | Core |
| Standard integrated safety package | Core |
| Exposure-response, immunogenicity, exploratory biomarkers | Conditional |
| Formal intercurrent-event governance surfaces beyond general estimand wording | Gap |

### 9.4 Oncology-Specific Subfamilies

| Subfamily | Status |
| --- | --- |
| BOR, ORR, DCR, DOR, TTR | Core where tumor response is relevant |
| PFS, OS, KM, forest, subgroup survival | Core in registrational and many Phase II/III settings |
| Waterfall, spider, swimmer | Core to Conditional depending on study objective |
| RECIST and central review traceability | Core |

### 9.5 Non-Oncology-Specific Subfamilies

| Subfamily | Status |
| --- | --- |
| General confirmatory efficacy shells | Core |
| Domain-specific clinical endpoint packages | Conditional to Core depending on program |
| Explicit non-oncology-only shell variants | Core in supported families |
| Respiratory exacerbation packages | Core where protocol-defined exacerbations drive efficacy |
| Cardiovascular MACE / HF hospitalization packages | Core where adjudicated cardiovascular outcomes drive efficacy |
| Autoimmune flare / responder packages | Core where protocol-defined flare or responder rules are central |

## 10. Study-Specific Tailoring Rules

The master library is a controlled baseline. Study-specific use is expected, but
tailoring must follow these rules:

- retain shell numbering control unless the change is formally approved
- keep only applicable shell variants for the study context
- tailor populations, titles, and footnotes using protocol and SAP language
- replace placeholders with study-specific terminology only when governance
  remains intact
- do not remove traceability notes without an approved justification
- do not convert a `General` shell into a therapeutic-area-specific shell
  silently

## 11. Required Review Questions

Before declaring a study package complete, reviewers should confirm:

1. Are all `Core` shell families represented?
2. Are all selected `Conditional` shell families justified by protocol or SAP?
3. Are known `Gap` areas documented and consciously handled?
4. Are applicability labels still accurate after study-specific tailoring?
5. Are workbook, SOP, and DOCX terms still aligned?

## 12. Risk Reminder

- `Technical risk`: ungoverned metadata growth can make automation unreliable.
- `Maintenance risk`: shell reuse without controlled applicability can create
  silent domain drift.
- `Project risk`: phase-coverage claims can become overstated unless `Gap`
  status is tracked explicitly.

## 13. Optimization Direction

### 13.1 Immediate

- keep supported non-oncology families explicit and governed
- align SOP wording with the coverage matrix and workbook metadata
- preserve machine-checkable cross-output rules for representative IDs

### 13.2 Mid-term

- add testable invariants for numbering, scope, applicability, and cross-output
  wording
- build a controlled shell-family registry
- expand Phase I design families for `3+3`, BOIN, CRM, dose expansion, TQT, DDI,
  and renal/hepatic impairment

### 13.3 Toolchain

- automate coverage-matrix validation against catalog metadata
- validate label and field consistency across DOCX, XLSX, SOP, and spec wording
- run `generate`, `validate`, and `pytest` in CI before controlled release
