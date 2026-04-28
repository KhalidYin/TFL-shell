# Format and Traceability Remediation Design

Date: 2026-04-28
Topic: TFL format remediation, subgroup cleanup, arm-label normalization, and source-listing correction
Status: Approved for direct execution

## 1. Objective

Bring the current shell library closer to clinical-statistical and regulatory
review expectations by fixing structural output defects and reducing ambiguity in
the controlled templates.

This round focuses on existing content quality rather than on expanding library
breadth.

## 2. Problems Confirmed

### 2.1 Invalid expandable-column pattern

Some tables encode ellipsis, effect columns, and overall columns in merged or
compressed header structures. Combined with the current DOCX renderer, this can
silently drop data values when the number of header columns does not match the
number of row values.

### 2.2 Redundant subgroup tables

Several subgroup analysis tables duplicate the role already played by the main
analysis table plus the forest plot. These tables add maintenance burden and
increase the chance of format defects without a proportional review benefit.

### 2.3 Inconsistent arm naming

The repository currently mixes:

- `XXX Group 1 / XXX Group 2`
- `G1 / G2 / Gx`
- `Treatment A / Treatment B`
- `Control`
- `Overall`

This is not appropriate for a controlled template library.

### 2.4 Weak source-listing traceability

Many shells reuse generic `source_listing` placeholders rather than pointing to
the most relevant governed subject-level listing.

## 3. Scope

### 3.1 In scope

- remove or refactor shells with header/value cardinality defects
- forbid the ellipsis-plus-merged-column pattern in table headers
- prune low-value subgroup tables where a forest plot already covers the use case
- normalize arm naming across tables, listings, and figures
- correct high-frequency `source_listing` mappings
- add tests for column cardinality, forbidden header tokens, arm-label
  normalization, and source-listing integrity
- update project docs to reflect the stricter governance rule

### 3.2 Out of scope

- complete one-to-one semantic review of every single listing in the repository
- redesigning the entire section architecture
- changing the therapeutic coverage roadmap

## 4. Design Decisions

### 4.1 Header rule

Every table must satisfy:

- `len(placeholder_columns) - 1 == number of data values in each row`

No compressed header token such as `"...\n...\nOverall"` or
`"...\n...\nEffect [95% CI]"` is allowed.

### 4.2 Representation rule for many-arm cases

The controlled master template should prioritize the common two-arm pattern.

Therefore:

- standard shells use two explicit arm columns
- `Overall/Total` is only allowed where pooled summaries are clinically standard
- generic ellipsis columns are removed from the master library

### 4.3 Subgroup expression rule

For subgroup analyses, the default controlled representation should be:

- main result table
- forest plot for subgroup treatment effect

Standalone subgroup tables should be removed when they merely restate the forest
plot content.

### 4.4 Arm-label rule

Use a single neutral standard:

- `Treatment A`
- `Treatment B`

Use `Overall` only when a pooled total is truly needed.
Do not use `G1`, `G2`, `Gx`, `Group 1`, or mixed synonyms in the master library.

### 4.5 Source-listing rule

`source_listing` must point to the most relevant governed listing ID when one
exists. Generic pooled placeholders are not acceptable for final controlled
templates.

Where a governed listing does not yet exist, the shell should not pretend to
have exact traceability.

## 5. Implementation Plan

### 5.1 Structural remediation

- update shared header templates in `definitions.py`
- fix or remove tables with mismatched header/value cardinality
- add a hard validation check in tests for column cardinality

### 5.2 Subgroup cleanup

Remove these low-value subgroup tables from the controlled catalog:

- `T14.2.3`
- `T14.2.17`
- `T14.2.18`
- `T14.3.1.11`
- `T14.3.1.12`

Keep the corresponding forest plots where applicable.

### 5.3 Arm-label normalization

- replace `XXX Group 1 / XXX Group 2` with `Treatment A / Treatment B`
- replace `G1 / G2 / Gx` labels in table and listing placeholders
- fix KM risk-table labels so they no longer collapse both arms to `Treatment`

### 5.4 Source-listing correction

Apply family-based mapping first for the highest-impact classes:

- general efficacy tables -> protocol deviations, rescue/intercurrent, or
  efficacy-support listings where governed
- oncology response tables -> response-assessment and survival listings
- non-oncology respiratory/cardiovascular/autoimmune families -> their dedicated
  listings
- Phase I DLT / food-effect shells -> dedicated DLT / PK listings

### 5.5 Validation

Add tests that fail if:

- a table uses forbidden merged ellipsis header tokens
- row-value cardinality does not match header structure
- prohibited arm-label variants remain in governed placeholders
- representative `source_listing` mappings remain generic

## 6. Acceptance Criteria

- no retained table has header/value cardinality mismatch
- removed subgroup tables no longer appear in generated outputs
- new generated outputs use normalized arm labels
- KM risk table preserves full arm labels
- representative `source_listing` mappings are specific rather than generic
- tests and validation pass

## 7. Risks and Mitigations

### Risk 1: Over-removal of pooled summaries

Mitigation:

- allow `Overall` only where clinically standard rather than banning it

### Risk 2: Traceability still incomplete in some families

Mitigation:

- fix the high-frequency governed mappings now
- document the remaining families for later controlled cleanup

### Risk 3: Content drift between docs and outputs

Mitigation:

- update governance docs in the same change set
- regenerate controlled outputs after remediation
