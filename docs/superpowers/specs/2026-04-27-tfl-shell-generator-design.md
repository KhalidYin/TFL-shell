# TFL Shell Generator Design

Date: 2026-04-27
Topic: Clinical CSR TFL shell generator optimization
Status: Approved design

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

## 2. Confirmed scope

### In scope

- Table / Figure / Listing shell generation
- Oncology / Non-Oncology applicability markers
- Simulated figures for figure shells
- Word automatic TOC for DOCX outputs
- XLSX used as TFL catalog + usage guidance
- SOP used as standard governance document
- Shared catalog metadata across outputs
- Layout optimization to keep each TFL on one page when reasonably possible

### Out of scope

- CSR Section 16.1 generation
- Project-tracker style XLSX fields such as owner/priority/status as core workbook purpose
- Full mock statistical data rows in tables and listings
- Manual text-based TOC as the primary directory mechanism
- Real study data population

## 3. Deliverables

### 3.1 Main DOCX shell template

The main DOCX is the CSR-facing shell document. Its structure will be:

1. Cover page
2. Automatic Word TOC
3. Usage notes
4. Section 14.1
5. Section 14.2
6. Section 14.3
7. Section 14.4
8. Section 16.2

Each TFL entry will include:

- TFL ID
- TFL title
- Analysis population
- Applicability label:
  - General
  - Oncology only
  - Non-Oncology only
- Dataset source
- Program reference
- Main shell body
- Footnotes

#### Table shell rules

- Preserve the first-column business structure items
- Examples include statistical terms, population categories, AE hierarchy, laboratory items, timepoints, and subgroup labels
- Fill all non-first-column result cells with `XX`
- Preserve hierarchical indentation where needed
- Do not output full mock numeric result rows

#### Figure shell rules

- Keep simulated figures
- Figures remain template illustrations, not production analysis results
- Preserve title, figure body, and supporting notes
- Optimize layout so each figure shell stays on one page when reasonably possible
- Avoid page breaks splitting figure title, image, and footnotes

#### Listing shell rules

- Preserve first-column example structure or key business variable labels
- Fill all other columns with `XX`
- Do not include mock subject-level listing records
- Preserve sort/display notes such as site/subject/visit ordering where applicable

### 3.2 XLSX TOC + guidance workbook

The XLSX workbook will serve as a **catalog and usage guide**, not as a project execution tracker.

Recommended sheets:

- `TOC_Master`
- `14.1`
- `14.2`
- `14.3`
- `14.4`
- `16.2`
- `Field_Definitions`
- `Usage_Guide`
- `Change_Log`

Recommended metadata columns:

- TFL ID
- TFL Title
- TFL Type
- CSR Section
- Population
- Therapeutic Applicability
- Dataset Source
- Program Reference
- Dictionary / Standard
- Placeholder Style
- Footnote Present
- Remarks

The workbook should not be primarily modeled around:

- Status
- Priority
- Assigned To

Those are project management concepts, not core template-governance metadata.

### 3.3 SOP DOCX

The SOP describes how the template set is governed and used.

Recommended sections:

1. Purpose
2. Scope
3. Responsibilities
4. Definitions and Abbreviations
5. Applicable CSR Sections
6. TFL Naming Convention
7. Numbering Convention
8. Shell Construction Principles
9. Oncology vs Non-Oncology Rules
10. Table / Figure / Listing Rules
11. Footnote / Source / Program Reference Rules
12. TOC and XLSX Catalog Maintenance
13. Version Control and Change Management

The SOP must describe actual generator behavior, not aspirational behavior.

## 4. Chosen design approach

Use **Approach B: shell-semantic refactor**.

This means the project is intentionally shifted from a generator of mock-filled demonstration templates into a generator of **true clinical shell structures**.

Key intent:

- Table and listing definitions represent shell structure rather than pseudo-results
- Figure definitions retain simulated figure support as a controlled template aid
- Output semantics are standardized across DOCX, XLSX, and SOP

## 5. Core design rules

### 5.1 Shift metadata from mock-data semantics to shell semantics

The catalog should primarily define:

- what each TFL is
- which section it belongs to
- which study types it applies to
- what the first-column shell structure should contain
- what supporting notes and metadata should be shown

The catalog should no longer be centered on full sample result rows for tables and listings.

### 5.2 Word TOC is the primary directory mechanism

DOCX outputs must use a true Word field-based TOC.

Requirements:

- Apply consistent Heading 1 / Heading 2 / Heading 3 styles
- Insert a Word TOC field rather than manually typed directory text
- Allow users to update the TOC in Word to refresh page numbers and hierarchy

A supplemental index page is acceptable, but it must not replace the automatic TOC.

### 5.3 Non-first-column result cells use a single placeholder convention

Use one consistent placeholder convention for table and listing shells:

- First column: preserved example structure items
- All other result cells: `XX`

Do not mix:

- blank cells
- `[...]`
- `TBD`
- `XX`

Consistency matters for usability and SOP alignment.

### 5.4 Figure shells retain simulated visuals

Unlike table and listing shells, figures will retain simulated images.

The simulated figures exist only to:

- illustrate expected figure form
- support reviewer understanding
- improve shell usability

They must not be positioned or labeled in a way that suggests final production results.

### 5.5 XLSX must be governance-oriented

The workbook should help users:

- locate TFLs
- understand applicability
- understand metadata fields
- understand how the DOCX and catalog are intended to be used

It should not behave like a staffing or workflow tracker by default.

### 5.6 SOP and generator behavior must remain aligned

If the SOP states that:

- 16.1 is excluded
- Word TOC is used
- tables/listings use first-column examples plus `XX`
- figures include simulated illustrations

then the generator must actually do those things.

## 6. Layout and pagination rules

The user confirmed the preferred layout rule is:

- each TFL should stay on one page when reasonably possible
- only oversized content may flow naturally to the next page

Implementation implications:

- prioritize single-page containment for figures
- keep title, body, and footnotes together as much as possible
- reduce unnecessary vertical spacing
- avoid page breaks that split a figure shell across pages
- allow very long tables/listings to continue only when unavoidable

This is a best-effort layout rule, not an absolute guarantee for every possible shell.

## 7. Planned code changes

### 7.1 `src/tflshell/data/definitions.py`

Refactor definitions toward shell-oriented metadata.

Expected changes:

- reduce reliance on full `sample_data_rows` for tables and listings
- encode first-column shell structure more directly
- retain figure metadata needed for simulated figure generation
- remove Section 16.1 output entries from active generation scope

### 7.2 `src/tflshell/generators/docx_shell.py`

Expected changes:

- replace the current manual TOC page with true Word TOC insertion
- update table output so first-column structure is preserved and all other cells show `XX`
- update listing output to follow the same shell rule
- retain simulated figure rendering
- improve pagination/layout behavior so each TFL stays on one page when reasonably possible
- remove 16.1 from generated sections

### 7.3 `src/tflshell/generators/xlsx_toc.py`

Expected changes:

- redesign workbook purpose from tracker-like output to catalog/guidance output
- revise sheet set and metadata columns
- align workbook semantics with shell governance rather than execution workflow

### 7.4 `src/tflshell/generators/docx_sop.py`

Expected changes:

- insert a true Word automatic TOC
- restructure SOP chapters around governance and usage rules
- ensure text matches actual generator behavior

### 7.5 `src/tflshell/docx_utils/toc_builder.py`

Expected changes:

- use this module as the formal shared TOC insertion utility
- support both main DOCX and SOP generation

## 8. Key risks and mitigations

### Risk 1: Partial refactor leaves old mock-data semantics in place

If the generator only changes rendering while definitions still center on full sample rows, future maintenance may reintroduce pseudo-results.

Mitigation:

- move table/listing metadata toward shell-first definitions
- make the data model itself express shell intent

### Risk 2: Users think the TOC is broken because Word has not updated fields yet

Mitigation:

- include clear usage notes in DOCX and SOP explaining how to update the TOC in Word

### Risk 3: Heading-level inconsistency causes missing or malformed TOC entries

Mitigation:

- standardize heading usage across sections and individual TFLs

### Risk 4: Oncology / Non-Oncology usage remains ambiguous

Mitigation:

- label each TFL clearly as General, Oncology only, or Non-Oncology only in both DOCX and XLSX
- state in the SOP how non-applicable shells should be handled

### Risk 5: Figure layout breaks across pages

Mitigation:

- keep figure heading, image, caption, and notes grouped
- tune image size and spacing for single-page containment

### Risk 6: Output inconsistency across DOCX / XLSX / SOP

Mitigation:

- use a shared source catalog for numbering, titles, applicability, and metadata

## 9. Acceptance criteria

### Main DOCX

- Includes Word automatic TOC
- Excludes Section 16.1
- Covers only 14.1 / 14.2 / 14.3 / 14.4 / 16.2
- Tables preserve first-column example items and use `XX` elsewhere
- Listings preserve first-column example items and use `XX` elsewhere
- Figures retain simulated visuals
- Each TFL stays on one page when reasonably possible

### XLSX

- Functions as a catalog/guidance workbook
- Uses section-specific sheets plus master TOC
- Includes field definitions and usage guidance
- Matches DOCX numbering and applicability

### SOP

- Includes Word automatic TOC
- Describes scope, naming, numbering, applicability, and shell rules
- Matches actual generator behavior

## 10. Implementation note

This design intentionally treats tables/listings and figures differently:

- Tables and listings are shell-only structures with `XX` placeholders outside the first column
- Figures retain simulated images because the user explicitly requires mock visual content for figure shells

That distinction is deliberate and must be preserved during implementation.
