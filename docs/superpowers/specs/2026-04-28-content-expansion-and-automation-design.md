# Content Expansion and Automation Design

Date: 2026-04-28
Topic: Non-oncology shell-family expansion and cross-output automation
Status: Approved for direct execution

## 1. Objective

Expand the repository in a content-first way so that the master shell library
better supports non-oncology CSR programs and so that generated outputs are
verified automatically against drift.

This round will:

- add three non-oncology-focused shell families
- strengthen cross-output verification across DOCX, SOP, and XLSX
- add lightweight automation entry points through pre-commit and CI
- update project documentation to reflect the new content and roadmap

## 2. Scope

### 2.1 In scope

- Add respiratory exacerbation shell family
- Add cardiovascular MACE / heart-failure hospitalization shell family
- Add autoimmune flare / responder shell family
- Add corresponding listings and figures where practically useful
- Add cross-output consistency tests for generated DOCX, SOP, and workbook
- Add a lightweight CI workflow
- Add a lightweight pre-commit configuration
- Update project governance documents and testing guidance

### 2.2 Out of scope

- Full implementation of the long-range Phase I design library
- Disease-area-specific expansion for every non-oncology therapeutic domain
- New figure engines beyond current reusable supported figure types
- Full snapshot testing of Office outputs

## 3. Design Decisions

### 3.1 Content-first non-oncology families

The new non-oncology content will be organized into governed shell families
rather than isolated one-off shells.

Families to add now:

- Respiratory exacerbation
- Cardiovascular MACE / HF hospitalization
- Autoimmune flare / responder

Each family should include:

- at least one efficacy table
- one time-to-event or summary table where clinically appropriate
- one listing entry for subject-level review
- one figure where the pattern is naturally visual and already supported

### 3.2 Reuse existing section boundaries

New content must stay inside existing governed sections:

- `14.2` for efficacy
- `16.2` for patient listings

Safety-like clinical-event content may still appear in `14.2` when it serves a
non-oncology efficacy or adjudicated endpoint framework.

### 3.3 Controlled metadata

Each newly added item must explicitly declare:

- `shell_family`
- `study_phase_scope`
- `coverage_summary`
- `non_oncology_only=True`

This avoids over-reliance on default inference and makes the new families easier
to validate.

### 3.4 Cross-output consistency strategy

The repository now has enough generated surfaces that simple structural tests are
not enough.

This round will add consistency checks that confirm:

- the workbook row count matches the DOCX shell count
- selected representative shell IDs and titles appear in DOCX and workbook
- SOP guidance retains key governance wording aligned with workbook/doc rules

The tests should focus on stable semantics, not brittle whole-file snapshots.

### 3.5 Automation strategy

Use both of the following:

- `pre-commit` for fast local checks (`validate`, `pytest`)
- GitHub Actions for the full pipeline (`generate`, `validate`, `pytest`)

The CI workflow is the correct place to exercise artifact generation reliably.

## 4. New Content Outline

### 4.1 Respiratory exacerbation family

Planned artifacts:

- annualized moderate/severe exacerbation rate table
- time to first exacerbation table
- exacerbation KM figure
- exacerbation listing

### 4.2 Cardiovascular MACE / HF hospitalization family

Planned artifacts:

- adjudicated MACE composite summary
- time to first MACE or HF hospitalization table
- MACE/HF KM figure
- adjudicated cardiovascular event listing

### 4.3 Autoimmune flare / responder family

Planned artifacts:

- responder table based on protocol-defined flare/responder status
- flare rate or time-to-flare table
- flare timeline / KM-style figure where appropriate
- autoimmune flare / rescue-treatment listing

## 5. Documentation Changes

The following documents must be updated in the same change set:

- `PROJECT_GUIDE.md`
- `PROJECT_SPEC.md`
- `test_guide.md`

Updates must describe:

- newly represented non-oncology families
- current remaining gaps after this round
- the long-range Phase I expansion roadmap
- the new automation expectations

## 6. Long-Range Phase I Roadmap

This round will not fully implement the following, but it must document them as
the next design-library expansion targets:

- `3+3`
- `BOIN`
- `CRM`
- `dose expansion`
- `TQT`
- `DDI`
- `renal impairment`
- `hepatic impairment`

## 7. Acceptance Criteria

- New respiratory, cardiovascular, and autoimmune non-oncology shell families
  exist in the catalog.
- Each new family is represented in generated outputs.
- Workbook, DOCX, and tests recognize the new shell IDs.
- Cross-output consistency tests pass.
- CI and pre-commit configuration files exist and run the intended checks.
- Documentation reflects both new coverage and remaining roadmap gaps.

## 8. Risks and Mitigations

### Risk 1: Content becomes too generic

Mitigation:

- use explicit family names and endpoint language
- avoid collapsing all non-oncology content into one generic event framework

### Risk 2: Output drift returns

Mitigation:

- add file-content verification, not just command success checks
- test representative IDs across generated outputs

### Risk 3: Phase I roadmap remains vague

Mitigation:

- list target design families explicitly in project docs
- separate "implemented now" from "roadmap next"
