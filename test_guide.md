# test_guide

## 1. Purpose

This document defines the active testing contract for the `TFLshell` project.
It was designed before test implementation and is now used as the baseline for
the initialized `tests/` suite.

## 2. Testing Principles

- tests must verify governed behavior, not just implementation details
- cross-output consistency is a first-class project requirement
- tests should stay lightweight, targeted, and easy to run locally
- new functional changes should add or update focused tests
- the canonical test root must be `tests/`

## 3. Test Root

Use the canonical test root:

`tests/`

Recommended initial structure:

```text
tests/
  unit/
    models/
    utils/
    data/
    generators/
  integration/
    catalog/
    outputs/
    consistency/
  fixtures/
    catalog/
    output_samples/
```

### 3.1 Directory Intent

- `tests/unit/models/`: ID, label, applicability, placeholder, and metadata
  semantics
- `tests/unit/utils/`: naming and formatting helpers
- `tests/unit/data/`: catalog integrity and metadata completeness
- `tests/unit/generators/`: focused output-generation behaviors where full file
  rendering is not required
- `tests/integration/catalog/`: catalog coverage and summary behavior
- `tests/integration/outputs/`: generated DOCX/XLSX/SOP structural checks
- `tests/integration/consistency/`: cross-output agreement checks
- `tests/fixtures/`: stable sample inputs and lightweight output fixtures

## 4. Minimum Regression Set

The active minimum regression set should include the following categories.

### 4.1 Catalog Integrity

- every TFL ID is unique
- every non-figure shell has placeholder columns
- every non-figure shell has shell rows
- every shell has dataset source metadata
- every shell has shell family, study phase scope, and coverage summary metadata
- every shell section matches its ID
- every label derived from an ID is stable and reviewer-facing

### 4.2 Scope Control

- only governed sections are present
- `16.1` remains excluded unless the project specification changes
- applicability labels remain within the controlled set

### 4.3 Coverage Governance

- shell families can be mapped to the phase/domain coverage model
- oncology-only shells remain explicitly tagged
- non-oncology-specific governance content remains visible and testable
- supported non-oncology families remain represented for respiratory, cardiovascular, and autoimmune review
- phase-scope and coverage-summary metadata remain complete and valid

### 4.4 Output Structure

- DOCX shell output includes a TOC field
- SOP output includes a TOC field
- workbook contains all expected sheets
- workbook header columns match the governed metadata model
- workbook includes governance metadata columns for shell family and phase scope
- generated outputs preserve controlled labels and titles
- retained tables may use a separate ellipsis expansion column, but not a merged ellipsis-plus-analytic header
- retained tables keep header/value column counts aligned
- representative source-listing references are specific rather than generic

### 4.5 Cross-Output Consistency

- ID and display label align across DOCX, XLSX, and SOP
- representative new shell families appear in DOCX and XLSX together
- section naming aligns across outputs
- applicability wording aligns across outputs
- placeholder-policy wording does not drift materially
- workbook field names and project spec names remain synchronized
- removed redundant subgroup tables stay removed from generated outputs

## 5. Test Priorities

### 5.1 Priority 1

Implement first:

- catalog integrity checks
- workbook sheet and field checks
- label and numbering consistency checks

### 5.2 Priority 2

Implement second:

- DOCX and SOP structural checks
- section-scope verification
- applicability and placeholder wording checks
- representative shell-family spot checks across generated outputs

### 5.3 Priority 3

Implement later:

- coverage-matrix validation against richer item-level metadata
- snapshot-like checks for stable guidance text
- richer output comparisons for controlled sections

## 6. Test Design Rules

- prefer direct semantic assertions over fragile full-file snapshots
- inspect Office outputs structurally rather than visually where possible
- use sample fixtures that are small but representative
- isolate domain rules from rendering rules when writing tests

## 7. When to Add Tests

Add or update tests when:

- a new shell family is introduced
- scope boundaries are changed
- applicability or numbering behavior changes
- workbook field definitions change
- generator guidance wording changes materially
- version-governance logic is refactored
- shell header structure rules are tightened
- source-listing mapping rules are corrected
- recommendation heuristics, interpreted context fields, or recommend CLI output
  contracts are changed
- presentation profile defaults, spacing policies, or generate CLI rendering
  options are changed

## 8. What Not to Test Excessively

Avoid low-value tests that only repeat implementation structure, such as:

- restating every hardcoded string without checking its governed meaning
- brittle line-by-line document snapshots
- very broad tests that fail for unrelated wording changes

## 9. Suggested Tooling

Recommended future tooling:

- `pytest`
- fixture-based unit tests
- lightweight structural readers for DOCX and XLSX outputs
- `pre-commit` integration for fast local checks
- CI execution of `generate`, `validate`, and `pytest`

## 10. Definition of Done for Future Test Initialization

Testing should not be considered initialized until all of the following are
true:

1. `tests/` exists as the canonical test root.
2. At least one unit test validates catalog integrity.
3. At least one integration test validates workbook structure.
4. At least one consistency test validates cross-output label agreement.
5. Test instructions are documented in repository-level guidance.

## 11. Risk Reminder

- `Technical risk`: without tests, documentation and output behavior may drift
  silently.
- `Maintenance risk`: broad shell growth without validation will make future
  cleanup expensive.
- `Project risk`: coverage claims can outpace verified implementation behavior.

## 12. Optimization Guidance

### 12.1 Immediate

- keep this guide aligned with `PROJECT_SPEC.md`
- prioritize tests that verify governed invariants
- keep recommend-prototype tests focused on governed defaults, ambiguity
  handling, and stable recommendation outputs rather than on prompt wording

### 12.2 Mid-term

- add fixtures for representative oncology and non-oncology shell sets
- add phase-aware metadata checks after the catalog model evolves

### 12.3 Toolchain

- keep `pytest` in the managed workflow
- keep local hooks and CI aligned with the controlled quality gate
