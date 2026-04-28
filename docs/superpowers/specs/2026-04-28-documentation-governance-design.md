# Documentation Governance Design

Date: 2026-04-28
Topic: Documentation baseline for TFL shell governance review
Status: Approved for documentation-only execution

## 1. Objective

Create a project documentation baseline that turns the current repository from a
"working generator with review notes" into a governed template library with
clear scope, selection logic, and future testability.

This documentation pass must:

- define project purpose, users, and deliverables
- define the controlled scope for CSR TFL shells
- define how Phase I, II, and III expectations map to shell families
- define how oncology and non-oncology applicability is interpreted
- define code and metadata governance expectations
- define a future testing contract without implementing tests in this round

## 2. Approved Scope

### 2.1 In scope

- Add `PROJECT_GUIDE.md`
- Add `PROJECT_SPEC.md`
- Add `CODE_STYLE.md`
- Add `test_guide.md`
- Add a new design note in `docs/superpowers/specs/`
- Consolidate the recent review findings into stable project rules
- Introduce a phase-by-therapy-area coverage matrix
- Define future test categories and the intended `tests/` structure

### 2.2 Out of scope

- No Python code changes
- No changes to generated DOCX or XLSX outputs
- No initialization of the `tests/` directory in this round
- No automated consistency checks in this round
- No git commit in this round unless explicitly requested later

## 3. Problem Statement

The repository already provides a broad TFL shell catalog and synchronized
DOCX/XLSX/SOP outputs, but the governance layer is incomplete.

Current gaps identified during review:

- oncology coverage is explicit, but non-oncology-specific governance is not
- Phase I, II, and III expectations are not documented as controlled selection
  rules
- version governance still contains legacy `v2.0` references in code and
  metadata
- project dependencies are not fully declared in `pyproject.toml`
- cross-output consistency is expected conceptually but not yet verified by
  tests

## 4. Design Principles

### 4.1 Documentation-first

The project rules require documentation to lead implementation. Therefore this
round must define stable documentation artifacts before any code or test
changes.

### 4.2 Governance over aspiration

Each document must describe current scope, current gaps, and intended next
steps separately. Documentation must not imply that Phase I-III and
oncology/non-oncology parity are already fully achieved.

### 4.3 Role-aware reviewability

The new documentation must be readable and useful for:

- lead statisticians
- statistical programming leads
- QA or regulatory reviewers

### 4.4 Future-testable structure

The documents must define metadata and invariants in a way that can later be
validated automatically.

## 5. Deliverable Design

### 5.1 `PROJECT_GUIDE.md`

Purpose:

- explain what the project is for
- define intended users and review perspectives
- summarize current maturity and roadmap
- describe the Phase I-III and oncology/non-oncology coverage model at a high
  level

### 5.2 `PROJECT_SPEC.md`

Purpose:

- define the controlled scope and boundaries
- define shell numbering, applicability, and selection logic
- define the coverage matrix and shell-family expectations
- define required metadata and tailoring principles

### 5.3 `CODE_STYLE.md`

Purpose:

- define naming, versioning, metadata, and documentation synchronization rules
- define how generator changes must remain aligned with project docs
- define acceptable change patterns for catalog, outputs, and guidance wording

### 5.4 `test_guide.md`

Purpose:

- define the future test contract
- define the intended `tests/` structure
- define minimum regression checks for catalog and cross-output consistency

## 6. Coverage-Matrix Strategy

The new documentation will not claim that every study design is already fully
implemented. Instead it will introduce a governance matrix with three states:

- `Core`: expected baseline shell family for common studies in this phase/domain
- `Conditional`: only needed for certain designs, endpoints, or modalities
- `Gap`: recognized need that is not yet governed well enough in the repository

This is preferred over a binary "covered / not covered" model because it better
matches real clinical reporting practice.

## 7. Risks and Mitigations

### Risk 1: Documents overstate repository maturity

Mitigation:

- separate current implementation from target governance state
- explicitly label current gaps and next-step priorities

### Risk 2: New docs drift from existing design note

Mitigation:

- reuse the same core boundaries: sections 14.1, 14.2, 14.3, 14.4, 16.2 only
- keep applicability, placeholder, and governance wording aligned

### Risk 3: Future implementation ignores the new baseline

Mitigation:

- include explicit synchronization rules in `CODE_STYLE.md`
- include explicit test expectations in `test_guide.md`

## 8. Acceptance Criteria

- The repository contains the five new markdown documents defined in scope.
- `PROJECT_GUIDE.md` explains purpose, users, scope, and roadmap clearly.
- `PROJECT_SPEC.md` contains a phase/domain coverage matrix and shell selection
  rules.
- `CODE_STYLE.md` defines version governance and documentation synchronization
  rules.
- `test_guide.md` defines a future `tests/` structure and minimum regression
  checks.
- No document contains `TBD`, `TODO`, or contradictory scope claims.

## 9. Execution Note

This is a documentation-only governance pass. It establishes the baseline needed
for the next implementation round, which is expected to address:

- version cleanup
- dependency declaration cleanup
- cross-output consistency checks
- `tests/` initialization
- non-oncology-specific shell governance expansion
