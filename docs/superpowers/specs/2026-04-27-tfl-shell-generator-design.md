# TFL Shell Generator Design

Date: 2026-04-27
Topic: Clinical CSR TFL shell generator optimization
Status: Approved design and implementation baseline

## 1. Objective

Optimize the current project into a reusable **clinical statistics TFL shell generator** for CSR deliverables, covering:

- 14.1 Demographics and Baseline Characteristics
- 14.2 Efficacy
- 14.3 Safety
- 14.4 Special Assessments
- 16.2 Patient Data Listings

The optimized generator must support both:

- Oncology studies
- Non-Oncology studies

It must generate three coordinated deliverables:

1. A main CSR TFL Shell DOCX template
2. A TFL TOC + guidance XLSX workbook
3. A TFL Shell Standard SOP DOCX

## 2. Agreed boundaries

### 2.1 In scope

- Table / Figure / Listing shell generation
- CSR Sections 14.1 / 14.2 / 14.3 / 14.4 / 16.2 only
- Oncology / Non-Oncology applicability markers
- Reviewer-facing display labels synchronized across outputs
- Simulated figures for figure shells
- Word automatic TOC for DOCX outputs
- XLSX used as TFL catalog + usage guidance
- SOP used as standard governance document
- Shared catalog metadata across outputs
- Layout optimization to keep each TFL on one page when reasonably possible

### 2.2 Out of scope

- CSR Section 16.1 generation
- Real study data population
- Full mock statistical data rows in tables and listings
- Mock subject-level listing records
- Project-tracker style XLSX fields such as owner / priority / status as the workbook’s core purpose
- Manual text-based TOC as the primary directory mechanism
- Guaranteed one-page fit for every possible shell

### 2.3 Hard rules

- The active section scope remains 14.1 / 14.2 / 14.3 / 14.4 / 16.2 only.
- Tables and listings are shell-first, result-free outputs.
- Figures may retain simulated illustrations for review purposes only.
- Reviewer-facing labels must omit the internal leading type letter from the numeric portion, for example `Table 14.2.11` rather than `Table T14.2.11`.
- Header sample sizes must remain generic such as `N=xx`; concrete counts are not allowed in governed shell headers.
- The workbook is a catalog and usage guide, not a workflow tracker.
- The SOP, workbook guidance, and main DOCX introduction must describe the same governance rules.

### 2.4 Best-effort rules

- Each TFL should remain on one page when reasonably possible.
- Figure heading, image, caption, and notes should stay grouped when reasonably possible.
- Very wide or long tables/listings may still flow naturally when layout constraints make a single page impractical.

## 3. Deliverables

### 3.1 Main DOCX shell template

The main DOCX is the CSR-facing shell document. Its implemented structure is:

1. Cover page
2. Automatic Word TOC
3. Introduction and usage notes
4. Section 14.1
5. Section 14.2
6. Section 14.3
7. Section 14.4
8. Section 16.2

Each TFL entry is expected to include:

- Reviewer-facing display label
- TFL title
- Analysis population
- Applicability handling through shared metadata
- Dataset source and program/dictionary traceability through footnotes where applicable
- Main shell body
- Footnotes

#### Table shell rules

- Preserve the first-column structural/business items.
- Typical first-column examples include statistical terms, population categories, AE hierarchy, laboratory items, timepoints, and subgroup labels.
- Non-structural cells use shell-style placeholders appropriate to the intended display rather than actual results.
- Expandable treatment/group structures may include one or more generic groups, an ellipsis `...` pattern, and a final `Total` column where appropriate.
- All shell header and body cells are left-aligned.
- Do not output fabricated numeric result rows.

#### Figure shell rules

- Keep simulated figures.
- Figures remain shell illustrations, not production analysis results.
- Preserve title, figure body, and supporting notes.
- Optimize layout so each figure shell stays on one page when reasonably possible.
- Avoid page breaks splitting figure title, image, and footnotes where reasonably possible.

#### Listing shell rules

- Preserve first-column structural examples or key business variable labels.
- Non-structural cells use shell placeholders appropriate to the intended listing style rather than subject-level mock content.
- Do not include fabricated listing records.
- Preserve sort/display notes such as site / subject / visit ordering where applicable.

### 3.2 XLSX TOC + guidance workbook

The XLSX workbook serves as a **catalog and usage guide**, not as a project execution tracker.

Implemented sheets:

- `TOC_Master`
- `14.1_Demographics`
- `14.2_Efficacy`
- `14.3_Safety`
- `14.4_Special`
- `16.2_Listings`
- `Field_Definitions`
- `Usage_Guide`
- `Change_Log`

Implemented metadata columns:

- `TFL ID`
- `Display Label`
- `Title`
- `Type`
- `Section`
- `Population`
- `Applicability`
- `Dataset Source`
- `Program Reference`
- `Dictionary / Standard`
- `Placeholder Style`
- `Footnotes`
- `Remarks`

The workbook should not be primarily modeled around:

- Status
- Priority
- Assigned To

Those are project-management concepts, not core template-governance metadata.

### 3.3 SOP DOCX

The SOP describes how the template set is governed and used.

Its implemented chapter model is organized as:

1. Purpose and Scope
2. Definitions and Abbreviations
3. Responsibilities
4. Procedure
5. References
6. Appendices

The SOP must describe actual generator behavior, not aspirational behavior.

## 4. Chosen design approach

Use **Approach B: shell-semantic refactor**.

This project is intentionally shifted from a generator of mock-filled demonstration templates into a generator of **true clinical shell structures**.

Key intent:

- Table and listing definitions represent shell structure rather than pseudo-results.
- Figure definitions retain simulated figure support as a controlled template aid.
- Output semantics are standardized across DOCX, XLSX, and SOP.

## 5. Governing shell rules

### 5.1 Metadata is shell-centric rather than mock-result-centric

The shared catalog should primarily define:

- what each TFL is
- which section it belongs to
- which study types it applies to
- what the first-column shell structure should contain
- what supporting notes and metadata should be shown
- how the output should be rendered for reviewers

The catalog should not be centered on full sample result rows for tables and listings.

### 5.2 Word TOC is the primary directory mechanism

DOCX outputs use a true Word field-based TOC.

Requirements:

- Apply consistent Heading 1 / Heading 2 / Heading 3 styles.
- Insert a Word TOC field rather than manually typed directory text.
- Allow users to update the TOC in Word to refresh page numbers and hierarchy.

A supplemental index page is acceptable, but it must not replace the automatic TOC.

### 5.3 Placeholder behavior follows shell style, not a single literal token

Table and listing shells preserve first-column structural examples while keeping all result-bearing content generic and result-free.

Current placeholder policy:

- First column: preserved structural examples
- Non-structural cells: controlled shell placeholders chosen to match the intended display style
- Expandable treatment/group structures: may use `...` together with `Total`
- Sample-size headers: generic forms such as `N=xx`

Representative placeholder forms may include:

- `XX`
- `xx (xx.x)`
- `xx (xx)`
- `x.xxx`
- `(xx.x, xx.x)`
- `xx.x (xx.x, xx.x)`
- `xx / xx`
- `xx.xx`

The key rule is not the literal token itself; it is that the shell remains clearly non-result-bearing while preserving the intended display semantics.

### 5.4 Internal IDs and reviewer-facing labels are intentionally different

Internal IDs remain controlled metadata, for example:

- `T14.2.11`
- `F14.2.4`
- `L16.2.3`

Reviewer-facing output labels omit the leading type letter from the numeric portion and render as:

- `Table 14.2.11`
- `Figure 14.2.4`
- `Listing 16.2.3`

This distinction must stay synchronized across the DOCX shell, XLSX workbook, and SOP.

### 5.5 Applicability must remain explicit

Each TFL should remain identifiable as one of:

- General
- Oncology only
- Non-Oncology only

Applicability metadata supports both filtering and reviewer interpretation. The documentation should make clear that non-applicable shells are governed through labeling and selection logic rather than by blurring therapeutic-area scope.

### 5.6 Figures retain simulated visuals by design

Unlike table and listing shells, figures retain simulated images.

The simulated figures exist only to:

- illustrate expected figure form
- support reviewer understanding
- improve shell usability

They must not be positioned or labeled in a way that suggests final production results.

### 5.7 The workbook must remain governance-oriented

The workbook should help users:

- locate TFLs
- understand applicability
- understand metadata fields
- understand how the DOCX and catalog are intended to be used
- track high-level template changes through the controlled change log

It should not behave like a staffing or workflow tracker by default.

### 5.8 SOP and generator behavior must remain aligned

If the SOP states that:

- 16.1 is excluded
- Word TOC is used
- tables/listings are shell-first and result-free
- display labels omit the internal leading type letter
- figures include simulated illustrations
- workbook semantics are governance-oriented

then the generator and workbook guidance must actually do those things.

## 6. Layout and pagination rules

The preferred layout rule remains:

- each TFL should stay on one page when reasonably possible
- only oversized content may flow naturally to the next page

Implementation implications:

- prioritize single-page containment for figures
- keep title, body, and footnotes together as much as possible
- reduce unnecessary vertical spacing
- avoid page breaks that split a figure shell across pages
- allow very long tables/listings to continue only when unavoidable

This is a best-effort layout rule, not an absolute guarantee for every possible shell.

## 7. Current implemented behavior

### 7.1 Shared naming and placeholder semantics

The current implementation already centralizes key semantics in shared model and utility code:

- `src/tflshell/models/tfl_item.py`
  - provides `display_number`, `display_label`, `applicability_label`, `placeholder_example`, and `placeholder_summary`
- `src/tflshell/utils/naming.py`
  - maps internal IDs to reviewer-facing display labels
- `src/tflshell/docx_utils/toc_builder.py`
  - provides shared Word TOC insertion behavior used by DOCX outputs

These shared helpers should be treated as the implementation truth behind the documentation vocabulary.

### 7.2 `src/tflshell/generators/docx_shell.py`

The main DOCX generator already implements:

- landscape document setup
- cover page generation
- Word-native TOC insertion
- introduction / usage guidance
- section generation for 14.1 / 14.2 / 14.3 / 14.4 / 16.2
- therapeutic-area filtering support
- reviewer-facing display labels in shell headings
- simulated figure rendering for figure shells
- page break insertion after each TFL
- best-effort grouping of shell components and notes

### 7.3 `src/tflshell/generators/xlsx_toc.py`

The workbook generator already implements:

- a governance-oriented workbook structure
- `TOC_Master` plus section-specific sheets
- `Field_Definitions`, `Usage_Guide`, and `Change_Log`
- both internal IDs and reviewer-facing display labels
- workbook wording that describes adaptive shell placeholders rather than an `XX`-only policy
- remarks and traceability-oriented metadata for governance use

### 7.4 `src/tflshell/data/sop_content.py`

The structured SOP content already documents:

- section scope limited to 14.1 / 14.2 / 14.3 / 14.4 / 16.2
- shell-first conventions
- adaptive placeholder behavior
- generic sample-size header expectations
- reviewer-facing display labels and internal IDs
- workbook purpose and change-management expectations
- Word TOC update behavior
- simulated figure rules

### 7.5 Documentation alignment expectation

The narrative spec, generated SOP content, workbook guidance text, and DOCX introduction should describe the same policy baseline. If one surface is intentionally revised, the others should be reviewed in the same pass.

## 8. Known gaps and future improvements

### 8.1 Placeholder-policy tightening remains a future decision

The current implementation supports adaptive shell placeholders. If the team later decides to enforce a stricter single-placeholder policy, that should be treated as a deliberate future design change rather than as current behavior.

### 8.2 Pagination control can be strengthened further

Current pagination is best effort. Future work may improve keep-together behavior for:

- shell heading + body + footnotes
- figure image + caption + notes
- especially wide or long tables that currently rely on natural document flow

### 8.3 Therapeutic-area behavior can be documented more explicitly

The product already supports therapeutic applicability metadata and filtering, but future documentation can describe more explicitly:

- how shared shells are reused,
- how oncology-only shells are handled,
- how non-oncology-only shells are handled,
- and how common shell families differ from specialized variants.

### 8.4 Cross-output consistency checks can be automated

A later refinement could add tests or verification routines that check consistency across:

- section coverage
- display labels
- workbook field names
- placeholder-policy wording
- generated guidance text

### 8.5 Metadata standardization can be deepened further

The project already has shared metadata semantics, but future work may further standardize:

- shell-family identification
- reusable shell-pattern classification
- richer placeholder-style taxonomy by TFL family
- more explicit traceability fields across outputs

## 9. Key risks and mitigations

### Risk 1: Documentation drifts back to obsolete `XX`-only wording

Mitigation:

- Keep the main spec, SOP content, workbook guidance, and DOCX introduction synchronized whenever placeholder policy is revised.

### Risk 2: Users confuse current behavior with future enhancements

Mitigation:

- Keep current implemented behavior and future improvements in clearly separate sections.

### Risk 3: Workbook semantics drift from the main specification

Mitigation:

- Document the workbook’s actual sheet names and column names in the main spec.
- Reuse workbook terminology consistently across all documentation surfaces.

### Risk 4: Applicability handling remains ambiguous to reviewers

Mitigation:

- Keep `General`, `Oncology only`, and `Non-Oncology only` as explicit governed labels.
- State clearly how applicability is intended to guide shell selection and interpretation.

### Risk 5: TOC behavior is mistaken for a broken feature when Word fields are not updated

Mitigation:

- Continue to include explicit usage notes that users must update TOC fields in Word after opening the generated DOCX.

## 10. Acceptance criteria

### Main DOCX

- Includes Word automatic TOC
- Excludes Section 16.1
- Covers only 14.1 / 14.2 / 14.3 / 14.4 / 16.2
- Uses reviewer-facing display labels such as `Table 14.x.x`
- Tables preserve first-column structural examples and use result-free shell placeholders elsewhere
- Listings preserve first-column structural examples and use result-free shell placeholders elsewhere
- Figures retain simulated visuals
- Each TFL stays on one page when reasonably possible

### XLSX

- Functions as a catalog/guidance workbook
- Uses the implemented section-specific sheets plus master TOC
- Includes field definitions and usage guidance
- Preserves both internal ID traceability and reviewer-facing display labels
- Matches DOCX and SOP terminology for applicability and placeholder policy

### SOP

- Includes Word automatic TOC
- Describes scope, naming, numbering, applicability, and shell rules
- Matches actual generator behavior
- Distinguishes internal IDs from reviewer-facing labels

## 11. Implementation note

This design intentionally treats tables/listings and figures differently:

- Tables and listings are shell-only structures with preserved structural examples and result-free placeholders outside the structural content.
- Figures retain simulated images because reviewer interpretation benefits from visible shell illustrations.

That distinction is deliberate and must be preserved across documentation and generated outputs.
