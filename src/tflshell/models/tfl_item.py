"""TFLItem dataclass — a single TFL shell definition v2.2."""

from dataclasses import dataclass, field

from tflshell import config
from tflshell.models.enums import TFLType, Section
from tflshell.utils.naming import display_label_from_id, display_number_from_id


PLACEHOLDER_STYLE_MAP = {
    "text": "XX",
    "count_percent": "xx (xx.x)",
    "count_percent_int": "xx (xx)",
    "ci": "(xx.x, xx.x)",
    "estimate_ci": "xx.x (xx.x, xx.x)",
    "pvalue": "x.xxx",
    "count_total": "xx / xx",
    "rate": "xx.xx",
}


@dataclass
class TFLItem:
    """A single TFL shell definition with header, traceability, and shell structure."""

    id: str
    title: str
    tfl_type: TFLType
    section: Section
    population: str
    oncology_only: bool = False
    non_oncology_only: bool = False
    sort_key: int = 0
    description: str = ""
    placeholder_columns: list[str] = field(default_factory=list)
    footnotes: list[str] = field(default_factory=list)
    figure_description: str = ""

    # Header / traceability fields
    sponsor_placeholder: str = config.SPONSOR_PLACEHOLDER
    protocol_placeholder: str = config.PROTOCOL_PLACEHOLDER
    dataset_source: str = ""
    program_ref: str = ""
    source_listing: str = ""
    dictionary_versions: dict = field(default_factory=dict)
    table_notes: str = ""

    # Figure metadata
    figure_type: str = ""
    figure_width_inches: float = config.FIGURE_DEFAULT_WIDTH
    figure_height_inches: float = config.FIGURE_DEFAULT_HEIGHT

    # v2.2 shell semantics (rich: each row can be list[str] or dict with label/bold/indent/values)
    shell_rows: list = field(default_factory=list)
    result_placeholder: str = "XX"
    placeholder_style: str = "text"
    shell_family: str = ""
    study_phase_scope: str = ""
    coverage_summary: str = ""

    @property
    def therapeutic_areas(self) -> list[str]:
        if self.oncology_only:
            return ["Oncology"]
        if self.non_oncology_only:
            return ["Non-Oncology"]
        return ["Oncology", "Non-Oncology"]

    @property
    def applicability_label(self) -> str:
        if self.oncology_only:
            return "Oncology only"
        if self.non_oncology_only:
            return "Non-Oncology only"
        return "General"

    @property
    def shell_family_label(self) -> str:
        if self.shell_family:
            return self.shell_family
        family_map = {
            Section.SEC_14_1: "Demographics and Baseline",
            Section.SEC_14_2: "Efficacy",
            Section.SEC_14_3: "Safety",
            Section.SEC_14_4: "Special Assessments",
            Section.SEC_16_2: "Patient Listings",
        }
        return family_map.get(self.section, self.section.title)

    @property
    def study_phase_scope_label(self) -> str:
        if self.study_phase_scope:
            return self.study_phase_scope
        if self.section in (Section.SEC_14_1, Section.SEC_14_3, Section.SEC_16_2):
            return "Phase I-III"
        if self.section == Section.SEC_14_2:
            return "Phase I-III (conditional for Phase I)"
        if self.section == Section.SEC_14_4:
            return "Phase I-III (core in Phase I; conditional in Phase II-III)"
        return "Phase I-III"

    @property
    def coverage_summary_label(self) -> str:
        if self.coverage_summary:
            return self.coverage_summary
        if self.section in (Section.SEC_14_1, Section.SEC_14_3, Section.SEC_16_2):
            return "Core"
        if self.section == Section.SEC_14_2:
            return "Core (Phase II-III); Conditional (Phase I)"
        if self.section == Section.SEC_14_4:
            return "Core (Phase I); Conditional (Phase II-III)"
        return "Core"

    @property
    def is_oncology(self) -> bool:
        return "Oncology" in self.therapeutic_areas

    @property
    def is_non_oncology(self) -> bool:
        return "Non-Oncology" in self.therapeutic_areas

    @property
    def badge(self) -> str | None:
        if self.oncology_only:
            return "[ONCOLOGY ONLY]"
        if self.non_oncology_only:
            return "[NON-ONCOLOGY ONLY]"
        return None

    @property
    def display_number(self) -> str:
        return display_number_from_id(self.id)

    @property
    def display_label(self) -> str:
        return display_label_from_id(self.id)

    @property
    def placeholder_example(self) -> str:
        return PLACEHOLDER_STYLE_MAP.get(self.placeholder_style, self.result_placeholder)

    @property
    def placeholder_summary(self) -> str:
        if self.placeholder_style == "text":
            return "First column retained; non-structural cells use XX"
        return (
            "First column retained; non-structural cells use shell placeholders "
            f"such as {self.placeholder_example}"
        )

    def footnote_text(self) -> list[str]:
        notes = list(self.footnotes)
        if self.source_listing:
            notes.insert(0, f"Source Listing: {self.source_listing}")
        if self.dataset_source:
            notes.append(f"Dataset: {self.dataset_source}."
                         f" Program: {self.program_ref}." if self.program_ref
                         else f"Dataset: {self.dataset_source}.")
        if self.dictionary_versions:
            dict_str = ", ".join(f"{k} {v}" for k, v in self.dictionary_versions.items())
            notes.append(f"Coding dictionary versions: {dict_str}.")
        if self.table_notes:
            notes.append(f"Note: {self.table_notes}")
        return notes

    @property
    def is_figure_generated(self) -> bool:
        return self.tfl_type == TFLType.FIGURE and bool(self.figure_type)

    @property
    def has_shell_rows(self) -> bool:
        return bool(self.shell_rows)

    @staticmethod
    def _normalize_row(row) -> dict:
        """Normalize a shell row from list or dict form to rich dict form.

        List form: ["Label", "val1", "val2", ...] → {"label": "Label", "bold": False, "indent": False, "values": ["val1", ...]}
        Dict form: {"label": ..., "bold": ..., "indent": ..., "values": [...]} passes through.
        """
        if isinstance(row, dict):
            return {
                "label": row.get("label", ""),
                "bold": row.get("bold", False),
                "indent": row.get("indent", False),
                "values": row.get("values", []),
            }
        # Flat list form
        label = row[0] if len(row) > 0 else ""
        values = list(row[1:]) if len(row) > 1 else []
        return {"label": label, "bold": False, "indent": False, "values": values}

    @property
    def shell_data_rows_rich(self) -> list[dict]:
        """Return shell rows as list of dicts with bold/indent/value metadata.

        Each dict: {"label": str, "bold": bool, "indent": bool, "values": list[str]}
        """
        return [self._normalize_row(r) for r in self.shell_rows]

    @property
    def shell_data_rows(self) -> list[list[str]]:
        """Return rows as flat list[list[str]] for backward compatibility."""
        if self.tfl_type == TFLType.FIGURE:
            return []
        if self.shell_rows:
            result = []
            for row in self.shell_rows:
                if isinstance(row, dict):
                    label = ("    " if row.get("indent") else "") + row.get("label", "")
                    result.append([label] + list(row.get("values", [])))
                else:
                    result.append(list(row))
            return result
        return [[self.placeholder_example] * max(len(self.placeholder_columns), 1) for _ in range(3)]
