"""Skill-oriented recommendation prototype for governed TFL shell selection."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from pathlib import Path
import re

from tflshell.data.definitions import build_catalog
from tflshell.models.catalog import TFLCatalog
from tflshell.models.enums import Section, TFLType


_DEFAULT_CORE_SECTIONS = ["14.1", "14.3", "16.2"]
_ALL_SECTIONS = ["14.1", "14.2", "14.3", "14.4", "16.2"]

_EFFICACY_KEYWORDS = [
    "primary endpoint",
    "efficacy",
    "response",
    "survival",
    "time-to-event",
    "time to event",
    "responder",
    "exacerbation",
    "mace",
    "cardiovascular event",
    "heart failure hospitalization",
]
_SPECIAL_KEYWORDS = [
    "pk",
    "ada",
    "biomarker",
    "pd",
    "pro",
    "food effect",
    "crossover",
]
_PHASE_I_KEYWORDS = [
    "phase i",
    "phase 1",
    "dose escalation",
    "dlt",
    "mtd",
    "rp2d",
    "3+3",
    "boin",
    "crm",
]
_ONCOLOGY_KEYWORDS = [
    "tumor",
    "recist",
    "bor",
    "orr",
    "dcr",
    "dor",
    "ttr",
    "target lesion",
    "waterfall",
    "spider",
    "swimmer",
    "pfs",
    "os",
]
_NON_ONCOLOGY_KEYWORDS = [
    "exacerbation",
    "mace",
    "cardiovascular",
    "heart failure hospitalization",
    "autoimmune",
    "flare",
    "copd",
    "pulmonary",
]


@dataclass
class InputSource:
    """Single recommend input source."""

    source_type: str = "user_prompt"
    content_text: str = ""
    title: str = ""
    file_path: str | None = None
    priority: str = "primary"
    language: str = "mixed"
    notes: str = ""


@dataclass
class RecommendRequest:
    """Minimal request object for the recommend prototype."""

    sources: list[InputSource]
    section_scope: list[str] = field(default_factory=list)
    therapeutic_area_hint: str = "unknown"
    study_phase_hint: str = "unknown"
    include_figures: bool = True
    include_listings: bool = True


@dataclass
class RecommendResult:
    """Structured result for the recommend prototype."""

    task_mode: str
    request_summary: dict
    interpreted_context: dict
    ingestion_state: dict
    extraction_state: dict
    normalization_state: dict
    ambiguity_state: dict
    recommendation_state: dict
    risk_notes: list[str]
    optimization_suggestions: dict

    def to_dict(self) -> dict:
        """Return the result as a plain dict."""
        return asdict(self)


def _normalize_text(value: str) -> str:
    return " ".join(value.lower().replace("_", " ").replace("-", " ").split())


def _contains_keyword(text: str, keyword: str) -> bool:
    normalized_keyword = _normalize_text(keyword)
    if not normalized_keyword:
        return False
    if any(char in normalized_keyword for char in "+/"):
        return normalized_keyword in text
    pattern = r"\b" + re.escape(normalized_keyword).replace(r"\ ", r"\s+") + r"\b"
    return re.search(pattern, text) is not None


def _contains_any(text: str, keywords: list[str]) -> bool:
    return any(_contains_keyword(text, keyword) for keyword in keywords)


def _normalize_phase_hint(raw: str) -> str:
    cleaned = _normalize_text(raw)
    if cleaned in ("phase i", "phase 1", "phase-i"):
        return "Phase I"
    if cleaned in ("phase ii", "phase 2", "phase-ii"):
        return "Phase II"
    if cleaned in ("phase iii", "phase 3", "phase-iii"):
        return "Phase III"
    if cleaned in ("mixed", "phase i-iii", "phase 1-3"):
        return "Mixed"
    return "Unknown"


def _normalize_area_hint(raw: str) -> str:
    cleaned = _normalize_text(raw)
    if cleaned == "oncology":
        return "Oncology"
    if cleaned in ("non oncology", "non-oncology", "nononcology"):
        return "Non-Oncology"
    if cleaned == "all":
        return "General"
    return "Unknown"


def _load_source_content(source: InputSource) -> tuple[str, list[str]]:
    issues: list[str] = []
    if source.content_text.strip():
        return source.content_text, issues
    if not source.file_path:
        issues.append("No inline content or file path provided.")
        return "", issues

    path = Path(source.file_path)
    if not path.exists():
        issues.append(f"File not found: {path}")
        return "", issues

    try:
        return path.read_text(encoding="utf-8"), issues
    except UnicodeDecodeError:
        try:
            return path.read_text(encoding="utf-8", errors="ignore"), issues
        except OSError as exc:
            issues.append(f"Failed to read source file: {exc}")
            return "", issues
    except OSError as exc:
        issues.append(f"Failed to read source file: {exc}")
        return "", issues


def _build_ingestion_state(sources: list[InputSource]) -> tuple[dict, str]:
    recognized_sources = []
    unreadable_sources = []
    input_warnings = []
    combined_chunks: list[str] = []

    for idx, source in enumerate(sources, start=1):
        content_text, issues = _load_source_content(source)
        usable = bool(content_text.strip())
        source_id = f"src-{idx:03d}"
        record = {
            "source_id": source_id,
            "source_type": source.source_type,
            "usable": usable,
            "language": source.language,
            "has_structured_signal": usable,
            "issues": issues,
        }
        recognized_sources.append(record)
        if usable:
            combined_chunks.append(content_text)
        else:
            unreadable_sources.append(record)
            input_warnings.extend(issues)

    if not combined_chunks:
        input_warnings.append("No usable source content detected; recommendation falls back to governed defaults.")

    ingestion_state = {
        "recognized_sources": recognized_sources,
        "unreadable_sources": unreadable_sources,
        "input_warnings": input_warnings,
    }
    return ingestion_state, "\n".join(combined_chunks)


def _detect_phase(text: str, hint: str) -> tuple[str, list[str]]:
    assumptions: list[str] = []
    normalized_hint = _normalize_phase_hint(hint)
    if normalized_hint != "Unknown":
        return normalized_hint, assumptions
    if _contains_keyword(text, "phase iii") or _contains_keyword(text, "phase 3"):
        return "Phase III", assumptions
    if _contains_keyword(text, "phase ii") or _contains_keyword(text, "phase 2"):
        return "Phase II", assumptions
    if _contains_any(text, _PHASE_I_KEYWORDS):
        return "Phase I", assumptions
    assumptions.append("Study phase remains unknown; default recommendation uses cross-phase core sections.")
    return "Unknown", assumptions


def _detect_area(text: str, hint: str) -> tuple[str, list[dict], list[str]]:
    conflicts: list[dict] = []
    assumptions: list[str] = []
    normalized_hint = _normalize_area_hint(hint)

    explicit_non_oncology = _contains_keyword(text, "non oncology")
    explicit_oncology = _contains_keyword(text, "oncology") and not explicit_non_oncology
    has_oncology = explicit_oncology or _contains_any(text, _ONCOLOGY_KEYWORDS)
    has_non_oncology = explicit_non_oncology or _contains_any(text, _NON_ONCOLOGY_KEYWORDS)

    inferred = "Unknown"
    if has_oncology and not has_non_oncology:
        inferred = "Oncology"
    elif has_non_oncology and not has_oncology:
        inferred = "Non-Oncology"
    elif has_oncology and has_non_oncology:
        inferred = "Unknown"
        conflicts.append(
            {
                "field": "therapeutic_area",
                "source_a": "input-content",
                "value_a": "Oncology-like endpoint language",
                "source_b": "input-content",
                "value_b": "Non-Oncology-like endpoint language",
            }
        )

    if normalized_hint != "Unknown" and inferred != "Unknown" and normalized_hint != inferred:
        conflicts.append(
            {
                "field": "therapeutic_area",
                "source_a": "execution-preferences",
                "value_a": normalized_hint,
                "source_b": "input-content",
                "value_b": inferred,
            }
        )
        assumptions.append(f"Use user-provided therapeutic area hint '{normalized_hint}' over conflicting textual signals.")
        return normalized_hint, conflicts, assumptions

    if normalized_hint != "Unknown":
        return normalized_hint, conflicts, assumptions
    if inferred != "Unknown":
        return inferred, conflicts, assumptions

    assumptions.append("Therapeutic area remains unknown; recommendation keeps general shells unless stronger evidence appears.")
    return "Unknown", conflicts, assumptions


def _extract_primary_endpoints(text: str) -> list[str]:
    endpoints = []
    if _contains_keyword(text, "time to event"):
        endpoints.append("Time-to-Event")
    if _contains_keyword(text, "response") or _contains_keyword(text, "responder"):
        endpoints.append("Response / Responder")
    if (
        _contains_keyword(text, "survival")
        or _contains_keyword(text, "pfs")
        or _contains_keyword(text, "os")
    ):
        endpoints.append("Survival")
    if _contains_keyword(text, "exacerbation"):
        endpoints.append("Exacerbation")
    if _contains_keyword(text, "mace") or _contains_keyword(text, "cardiovascular"):
        endpoints.append("Cardiovascular Event")
    if _contains_keyword(text, "autoimmune") or _contains_keyword(text, "flare"):
        endpoints.append("Autoimmune Flare")
    return endpoints


def _extract_populations(text: str) -> list[str]:
    populations = []
    if _contains_keyword(text, "safety population"):
        populations.append("Safety Population")
    if _contains_keyword(text, "fas") or _contains_keyword(text, "full analysis set"):
        populations.append("Full Analysis Set")
    if _contains_keyword(text, "itt") or _contains_keyword(text, "intent to treat"):
        populations.append("Intent-to-Treat Population")
    return populations


def _extract_safety_focus(text: str) -> list[str]:
    focus = []
    if _contains_keyword(text, "ae") or _contains_keyword(text, "adverse event"):
        focus.append("Adverse Events")
    if _contains_keyword(text, "lab") or _contains_keyword(text, "laboratory"):
        focus.append("Laboratory")
    if _contains_keyword(text, "ecg") or _contains_keyword(text, "qtc"):
        focus.append("ECG / QTc")
    if _contains_keyword(text, "vital sign"):
        focus.append("Vital Signs")
    return focus


def _build_extraction_state(text: str, phase_hint: str, area_hint: str) -> tuple[dict, dict]:
    phase, phase_assumptions = _detect_phase(text, phase_hint)
    area, area_conflicts, area_assumptions = _detect_area(text, area_hint)
    primary_endpoints = _extract_primary_endpoints(text)
    analysis_populations = _extract_populations(text)
    safety_focus = _extract_safety_focus(text)

    extraction_state = {
        "study_context": {
            "study_phase": phase,
            "therapeutic_area": area,
            "indication": "Unknown",
            "development_intent": "dose-escalation" if phase == "Phase I" and _contains_any(text, _PHASE_I_KEYWORDS) else "unknown",
        },
        "analysis_context": {
            "primary_endpoints": primary_endpoints,
            "secondary_endpoints": [],
            "analysis_populations": analysis_populations,
            "key_time_to_event": "Time-to-Event" in primary_endpoints or "Survival" in primary_endpoints,
            "key_responder": "Response / Responder" in primary_endpoints,
            "key_safety_focus": safety_focus,
        },
        "traceability_context": {
            "expects_patient_listings": True,
            "expects_program_refs": True,
            "expects_dictionary_traceability": True,
        },
    }

    ambiguity_state = {
        "missing_fields": [],
        "conflicts": area_conflicts,
        "assumptions": phase_assumptions + area_assumptions,
        "needs_user_confirmation": False,
    }
    if phase == "Unknown":
        ambiguity_state["missing_fields"].append("study_phase")
    if area == "Unknown":
        ambiguity_state["missing_fields"].append("therapeutic_area")
    return extraction_state, ambiguity_state


def _derive_section_scope(text: str, requested_sections: list[str]) -> list[str]:
    sections = set(_DEFAULT_CORE_SECTIONS)
    if _contains_any(text, _EFFICACY_KEYWORDS):
        sections.add("14.2")
    if _contains_any(text, _SPECIAL_KEYWORDS):
        sections.add("14.4")
    if requested_sections:
        allowed = {s for s in requested_sections if s in _ALL_SECTIONS}
        sections &= allowed
        if not sections:
            sections = allowed
    return sorted(sections, key=_ALL_SECTIONS.index)


def _derive_family_candidates(text: str, phase: str, area: str, sections: list[str]) -> list[str]:
    families: list[str] = []

    def add(name: str):
        if name not in families:
            families.append(name)

    if "14.1" in sections:
        add("Demographics and Baseline")

    if "14.2" in sections:
        add("General Efficacy")
        if area == "Oncology":
            add("Oncology Efficacy")
        elif area == "Non-Oncology":
            add("Non-Oncology Efficacy")
            if _contains_keyword(text, "exacerbation"):
                add("Respiratory Exacerbation")
            if (
                _contains_keyword(text, "mace")
                or _contains_keyword(text, "cardiovascular")
                or _contains_keyword(text, "heart failure hospitalization")
            ):
                add("Cardiovascular MACE and HF Hospitalization")
            if _contains_keyword(text, "autoimmune") or _contains_keyword(text, "flare"):
                add("Autoimmune Flare and Responder")

    if "14.3" in sections:
        add("Safety")
        if phase == "Phase I" and _contains_any(text, _PHASE_I_KEYWORDS):
            add("Phase I Safety and Dose Escalation")

    if "14.4" in sections:
        add("Special Assessments")
        if phase == "Phase I" and (
            _contains_keyword(text, "food effect")
            or _contains_keyword(text, "crossover")
            or _contains_keyword(text, "pk")
        ):
            add("Phase I Clinical Pharmacology")

    if "16.2" in sections:
        add("Patient Listings")
        if phase == "Phase I" and _contains_any(text, _PHASE_I_KEYWORDS):
            add("Specialized Patient Listings")
        if area == "Oncology":
            add("Oncology Listings")
        elif area == "Non-Oncology":
            add("Non-Oncology Listings")
            if _contains_keyword(text, "exacerbation"):
                add("Respiratory Exacerbation")
            if (
                _contains_keyword(text, "mace")
                or _contains_keyword(text, "cardiovascular")
                or _contains_keyword(text, "heart failure hospitalization")
            ):
                add("Cardiovascular MACE and HF Hospitalization")
            if _contains_keyword(text, "autoimmune") or _contains_keyword(text, "flare"):
                add("Autoimmune Flare and Responder")

    return families


def _filter_items(
    catalog: TFLCatalog,
    sections: list[str],
    area: str,
    families: list[str],
    include_figures: bool,
    include_listings: bool,
):
    items = catalog.all()
    section_set = set(sections)
    items = [item for item in items if item.section.number in section_set]

    if area == "Oncology":
        items = catalog.by_therapeutic_area("oncology")
        items = [item for item in items if item.section.number in section_set]
    elif area == "Non-Oncology":
        items = catalog.by_therapeutic_area("non-oncology")
        items = [item for item in items if item.section.number in section_set]

    if not include_figures:
        items = [item for item in items if item.tfl_type != TFLType.FIGURE]
    if not include_listings:
        items = [item for item in items if item.tfl_type != TFLType.LISTING]

    if families:
        items = [item for item in items if item.shell_family_label in families]

    return items


def _build_normalization_state(
    text: str,
    request: RecommendRequest,
    extraction_state: dict,
) -> dict:
    sections = _derive_section_scope(text, request.section_scope)
    phase = extraction_state["study_context"]["study_phase"]
    area = extraction_state["study_context"]["therapeutic_area"]
    if area == "Unknown":
        applicability_hint = "General"
    elif area == "Oncology":
        applicability_hint = "Oncology only"
    else:
        applicability_hint = "Non-Oncology only"

    families = _derive_family_candidates(text, phase, area, sections)
    if phase == "Phase I":
        phase_scope_hint = "Phase I"
    elif phase in ("Phase II", "Phase III"):
        phase_scope_hint = phase
    else:
        phase_scope_hint = "Phase I-III"

    return {
        "mapped_governance_fields": {
            "section_scope": sections,
            "applicability_hint": applicability_hint,
            "shell_family_candidates": families,
            "study_phase_scope_hint": phase_scope_hint,
            "include_figures": request.include_figures,
            "include_listings": request.include_listings,
        },
        "mapping_rationale": [
            "Start with governed core sections for incomplete contexts.",
            "Add efficacy sections only when endpoint language is detected.",
            "Add special assessments only when PK/ADA/biomarker-like signals are detected.",
        ],
    }


def _build_recommendation_state(
    text: str,
    catalog: TFLCatalog,
    extraction_state: dict,
    normalization_state: dict,
    ambiguity_state: dict,
    request: RecommendRequest,
) -> tuple[dict, list[str], dict]:
    mapped = normalization_state["mapped_governance_fields"]
    items = _filter_items(
        catalog,
        mapped["section_scope"],
        extraction_state["study_context"]["therapeutic_area"],
        mapped["shell_family_candidates"],
        request.include_figures,
        request.include_listings,
    )

    optional_expansions = []
    if "14.4" not in mapped["section_scope"]:
        optional_expansions.append(
            {
                "target": "14.4",
                "reason": "Add PK / ADA / biomarker / PRO shells if the study includes special assessments.",
            }
        )
    if extraction_state["study_context"]["therapeutic_area"] == "Unknown":
        optional_expansions.append(
            {
                "target": "oncology-vs-non-oncology refinement",
                "reason": "Clarify therapeutic area to surface domain-specific efficacy and listing families.",
            }
        )

    governance_warnings = list(ambiguity_state["assumptions"])
    if ambiguity_state["missing_fields"]:
        governance_warnings.append(
            f"Missing context fields: {', '.join(ambiguity_state['missing_fields'])}."
        )

    gap_notes = []
    if extraction_state["study_context"]["study_phase"] == "Phase I" and any(
        token in text for token in ("boin", "crm", "3+3", "cohort expansion")
    ):
        gap_notes.append(
            "Phase I design-specific selection remains only partially programmatic; review escalation-design shells manually."
        )

    recommendation_state = {
        "base_package": {
            "sections": mapped["section_scope"],
            "shell_families": mapped["shell_family_candidates"],
            "shell_ids": [item.id for item in items],
            "total_items": len(items),
        },
        "optional_expansions": optional_expansions,
        "governance_warnings": governance_warnings,
        "gap_notes": gap_notes,
    }

    risk_notes = []
    if ambiguity_state["missing_fields"]:
        risk_notes.append(
            "Recommendation relies on governed defaults because some study-defining fields remain unknown."
        )
    if not items:
        risk_notes.append(
            "Current filters returned no items; review section scope, therapeutic-area hint, and shell-family mapping."
        )

    optimization_suggestions = {
        "immediate": [
            "Provide a study phase or clearer endpoint wording to reduce default-based recommendations.",
        ],
        "mid_term": [
            "Extend recommendation rules from section-level heuristics to item-level prioritization after V1 stabilizes.",
        ],
        "toolchain": [
            "Add contract tests for interpreted context and recommendation state stability.",
        ],
    }
    return recommendation_state, risk_notes, optimization_suggestions


def recommend_shells(request: RecommendRequest, catalog: TFLCatalog | None = None) -> RecommendResult:
    """Return a governed recommendation result for the minimal recommend prototype."""
    if not request.sources:
        raise ValueError("RecommendRequest requires at least one input source.")

    catalog = catalog or build_catalog()
    ingestion_state, combined_text = _build_ingestion_state(request.sources)
    normalized_text = _normalize_text(combined_text)
    extraction_state, ambiguity_state = _build_extraction_state(
        normalized_text,
        request.study_phase_hint,
        request.therapeutic_area_hint,
    )
    normalization_state = _build_normalization_state(normalized_text, request, extraction_state)
    recommendation_state, risk_notes, optimization_suggestions = _build_recommendation_state(
        normalized_text,
        catalog,
        extraction_state,
        normalization_state,
        ambiguity_state,
        request,
    )

    interpreted_context = {
        "study_phase": extraction_state["study_context"]["study_phase"],
        "therapeutic_area": extraction_state["study_context"]["therapeutic_area"],
        "primary_endpoints": extraction_state["analysis_context"]["primary_endpoints"],
        "analysis_populations": extraction_state["analysis_context"]["analysis_populations"],
        "include_figures": request.include_figures,
        "include_listings": request.include_listings,
    }
    request_summary = {
        "task_mode": "recommend",
        "source_count": len(request.sources),
        "requested_sections": request.section_scope,
        "therapeutic_area_hint": request.therapeutic_area_hint,
        "study_phase_hint": request.study_phase_hint,
    }

    return RecommendResult(
        task_mode="recommend",
        request_summary=request_summary,
        interpreted_context=interpreted_context,
        ingestion_state=ingestion_state,
        extraction_state=extraction_state,
        normalization_state=normalization_state,
        ambiguity_state=ambiguity_state,
        recommendation_state=recommendation_state,
        risk_notes=risk_notes,
        optimization_suggestions=optimization_suggestions,
    )


def format_recommendation(result: RecommendResult) -> str:
    """Return a user-readable summary for CLI output."""
    context = result.interpreted_context
    package = result.recommendation_state["base_package"]
    lines = [
        "TFL Skill Recommend Prototype",
        f"- Study phase: {context['study_phase']}",
        f"- Therapeutic area: {context['therapeutic_area']}",
        f"- Sections: {', '.join(package['sections'])}",
        f"- Shell families: {', '.join(package['shell_families'])}",
        f"- Recommended shell count: {package['total_items']}",
    ]
    if context["primary_endpoints"]:
        lines.append(f"- Primary endpoint signals: {', '.join(context['primary_endpoints'])}")
    if result.ambiguity_state["missing_fields"]:
        lines.append(
            f"- Missing context: {', '.join(result.ambiguity_state['missing_fields'])}"
        )
    if result.recommendation_state["optional_expansions"]:
        lines.append("- Optional expansions:")
        for item in result.recommendation_state["optional_expansions"]:
            lines.append(f"  - {item['target']}: {item['reason']}")
    return "\n".join(lines)
