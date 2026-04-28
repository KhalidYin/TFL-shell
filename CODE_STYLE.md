# CODE_STYLE

## 1. Purpose

This document defines repository-level coding and governance conventions for the
`TFLshell` project. It applies to:

- Python source code
- shell catalog definitions
- generated DOCX and XLSX guidance behavior
- project documentation that describes generator rules

## 2. General Principles

- prefer small, explicit, domain-readable changes over broad implicit changes
- keep generator behavior aligned with governed documentation
- treat shell metadata as controlled project data, not as informal content
- prefer light automation and repeatable validation over manual convention drift

## 3. Source Organization

Expected responsibility boundaries:

- `src/tflshell/data/`: shell definitions and governed content sources
- `src/tflshell/models/`: domain models and shared shell semantics
- `src/tflshell/generators/`: output builders for DOCX, XLSX, and figures
- `src/tflshell/docx_utils/`: Word-specific document helpers
- `src/tflshell/figures/`: reusable shell-figure rendering components
- `docs/`: design notes and governed project documentation

Do not mix long-form governance wording directly into unrelated generator code
when it belongs in a shared content source or project document.

## 4. Naming Conventions

### 4.1 Python

- modules: `snake_case`
- functions: `snake_case`
- classes: `PascalCase`
- constants: `UPPER_SNAKE_CASE`
- enum members: `UPPER_SNAKE_CASE`

### 4.2 Clinical Shell Domain

- internal TFL IDs must remain in controlled form, for example `T14.3.1`
- reviewer-facing labels must be derived consistently from IDs
- section terminology must use the controlled CSR section numbers
- applicability labels must use only the governed set:
  `General`, `Oncology only`, `Non-Oncology only`

### 4.3 Filenames

Generated master files should use stable controlled names, for example:

- `TFL_Shell_Template_v<version>.docx`
- `TFL_TOC_v<version>.xlsx`
- `TFL_Shell_SOP_v<version>.docx`

Project documents should use explicit names:

- `PROJECT_GUIDE.md`
- `PROJECT_SPEC.md`
- `CODE_STYLE.md`
- `test_guide.md`

## 5. Version Governance

Versioning must be internally consistent across:

- package version
- output filenames
- document properties
- title-page or cover-page display text
- SOP version references
- guidance documents

### 5.1 Change Rule

If a version changes, review all version-bearing surfaces in the same pass.
Do not leave legacy version strings in:

- docstrings
- constants
- document metadata
- generated cover pages
- workbook change logs

### 5.2 Current Rule

Future code changes must treat version governance as a controlled task rather
than a cosmetic cleanup.

## 6. Catalog and Metadata Rules

### 6.1 Required Metadata

Each shell definition should preserve:

- ID
- title
- type
- section
- shell family
- study phase scope
- coverage summary
- population
- applicability
- dataset source
- program reference
- dictionary versions where relevant
- placeholder style
- footnote context where relevant

### 6.2 Metadata Design

- keep metadata explicit rather than inferred when the meaning is governed
- avoid adding free-text fields when a controlled field would be more stable
- do not overload one field with mixed governance meaning
- treat future phase/domain coverage attributes as first-class metadata

### 6.3 Traceability

Traceability wording should be short and operational:

- dataset lineage belongs in metadata or footnotes
- long policy text belongs in documents or shared content structures
- generator code should render traceability consistently rather than redefining
  it ad hoc

## 7. Documentation Synchronization Rules

Any change affecting shell behavior must review the matching documentation
surfaces.

### 7.1 Required Sync Group

Review together when rules change:

- `PROJECT_GUIDE.md`
- `PROJECT_SPEC.md`
- `CODE_STYLE.md`
- `test_guide.md`
- design notes in `docs/superpowers/specs/`
- governed SOP content
- workbook usage guidance
- main DOCX introduction text

### 7.2 Trigger Examples

Run a documentation sync review when changing:

- scope boundaries
- section coverage
- applicability wording
- placeholder rules
- versioning logic
- output field names
- shell-family interpretation
- phase or therapeutic-area coverage

## 8. Editing Standards

- use UTF-8 for project text files
- prefer Markdown for governance and project documentation
- keep comments short and purposeful
- do not add placeholder text such as `TBD` or `TODO` in governed documents
  that are meant to define an approved baseline

## 9. Change Discipline

### 9.1 Small Changes

For localized fixes:

- update the nearest relevant document
- note the impacted governed rule
- avoid unrelated refactoring

### 9.2 Structural Changes

For new shell families, new metadata, or output-rule changes:

- update the project documents first or in the same change set
- update design notes if the change shifts project behavior materially
- update future tests or test guidance expectations

## 10. Formatting and Tooling

Recommended lightweight tooling:

- `black` for Python formatting
- `ruff` or equivalent for linting
- `pre-commit` for lightweight validation hooks

Tooling should remain lightweight and automatable. Avoid introducing a heavy
process burden for small governance-safe changes.

### 10.1 Automation Contract

- use `pre-commit` for fast local checks such as catalog validation and pytest
- use CI for the full quality gate: output generation, catalog validation,
  regression tests, and generated-artifact drift detection
- if output generation rules change, update the automation config in the same
  change set

## 11. Risk Reminder

- `Technical risk`: version or metadata drift can silently break trust in
  generated outputs.
- `Maintenance risk`: uncontrolled free-text growth in shell definitions makes
  future validation harder.
- `Project risk`: code changes without document sync can cause regulatory-facing
  wording conflicts.

## 12. Optimization Guidance

### 12.1 Immediate

- centralize version-bearing strings further
- reduce duplicated guidance wording across generator surfaces

### 12.2 Mid-term

- add a machine-readable shell-family layer
- validate metadata completeness automatically
- grow the automation gate toward richer cross-output checks

### 12.3 Toolchain

- add pre-commit checks for Markdown hygiene and version-string drift
- add tests for numbering, applicability, and cross-output wording consistency
