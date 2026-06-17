"""Historical workflow prototype kept for reference.

This module is not the canonical reusable Skill package. The active Skill
delivery target lives under `Skill/`.
"""

from __future__ import annotations

import os

from tflshell import __version__
from tflshell.data.definitions import build_catalog
from tflshell.generators.docx_shell import DocxShellGenerator
from tflshell.generators.docx_sop import DocxSopGenerator
from tflshell.generators.xlsx_toc import XlsxTocGenerator
from tflshell.models.catalog import TFLCatalog
from tflshell.recommend import RecommendRequest, recommend_shells
from tflshell.utils.naming import make_filename


def _resolve_requested_outputs(raw: str) -> list[str]:
    if raw == "all":
        return ["docx", "xlsx", "sop"]
    return [part.strip() for part in raw.split(",") if part.strip()]


def _filtered_catalog(catalog: TFLCatalog, shell_ids: list[str]) -> TFLCatalog:
    items = [catalog.get(shell_id) for shell_id in shell_ids]
    return TFLCatalog([item for item in items if item is not None])


def _build_recommend_request(args, sources) -> RecommendRequest:
    return RecommendRequest(
        sources=sources,
        section_scope=args.section or [],
        therapeutic_area_hint=args.area,
        study_phase_hint=args.phase,
        include_figures=not args.no_figures,
        include_listings=not args.no_listings,
    )


def _recommend_payload(
    result: RecommendResult, mode: str, requested_outputs: list[str] | None = None
) -> dict:
    payload = result.to_dict()
    payload["task_mode"] = mode
    payload["request_summary"]["mode"] = mode
    payload["request_summary"]["desired_outputs"] = requested_outputs or []
    payload.setdefault(
        "generation_results",
        {
            "generated": False,
            "requested_outputs": [],
            "artifacts": [],
        },
    )
    payload.setdefault(
        "validation_results",
        {
            "catalog_validation": {
                "ran": False,
                "passed": False,
                "warning_count": 0,
                "warnings": [],
            }
        },
    )
    return payload


def _artifact(kind: str, path: str) -> dict:
    return {
        "kind": kind,
        "path": path,
        "file_name": os.path.basename(path),
    }


def _generate_outputs(args, catalog: TFLCatalog, payload: dict) -> dict:
    requested_outputs = _resolve_requested_outputs(args.type)
    output_dir = args.output_dir
    artifacts: list[dict] = []

    if "docx" in requested_outputs:
        output_path = os.path.join(
            output_dir,
            make_filename("TFL_Shell_Template", __version__, ".docx"),
        )
        path = DocxShellGenerator(
            catalog,
            output_path=output_path,
            therapeutic_area="all",
            generate_figures=not args.no_figures,
            sponsor=args.sponsor,
            protocol=args.protocol,
            presentation_profile=args.presentation_profile,
        ).generate()
        artifacts.append(_artifact("docx", path))

    if "xlsx" in requested_outputs:
        output_path = os.path.join(
            output_dir,
            make_filename("TFL_TOC", __version__, ".xlsx"),
        )
        path = XlsxTocGenerator(catalog, output_path=output_path).generate()
        artifacts.append(_artifact("xlsx", path))

    if "sop" in requested_outputs:
        output_path = os.path.join(
            output_dir,
            make_filename("TFL_Shell_SOP", __version__, ".docx"),
        )
        path = DocxSopGenerator(output_path=output_path).generate()
        artifacts.append(_artifact("sop", path))

    payload["generation_results"] = {
        "generated": bool(artifacts),
        "requested_outputs": requested_outputs,
        "output_dir": output_dir,
        "artifact_count": len(artifacts),
        "artifacts": artifacts,
        "filters": {
            "sections": payload["recommendation_state"]["base_package"]["sections"],
            "shell_ids": payload["recommendation_state"]["base_package"]["shell_ids"],
            "therapeutic_area": payload["interpreted_context"]["therapeutic_area"],
        },
        "stats": {
            "recommended_shell_count": payload["recommendation_state"]["base_package"][
                "total_items"
            ],
        },
    }
    return payload


def _attach_validation_results(payload: dict, catalog: TFLCatalog) -> dict:
    warnings = catalog.validate()
    payload["validation_results"] = {
        "catalog_validation": {
            "ran": True,
            "passed": not warnings,
            "warning_count": len(warnings),
            "warnings": warnings,
        }
    }
    return payload


def run_skill(args, sources) -> dict:
    """Run the CLI skill workflow and return a structured result."""
    catalog = build_catalog()
    request = _build_recommend_request(args, sources)
    recommendation = recommend_shells(request, catalog=catalog)

    if args.mode == "recommend":
        payload = _recommend_payload(recommendation, mode="recommend")
        scoped_catalog = _filtered_catalog(
            catalog, payload["recommendation_state"]["base_package"]["shell_ids"]
        )
        return _attach_validation_results(payload, scoped_catalog)

    payload = _recommend_payload(
        recommendation,
        mode="generate",
        requested_outputs=_resolve_requested_outputs(args.type),
    )
    scoped_catalog = _filtered_catalog(
        catalog, payload["recommendation_state"]["base_package"]["shell_ids"]
    )
    payload = _generate_outputs(args, scoped_catalog, payload)
    return _attach_validation_results(payload, scoped_catalog)


def format_skill_result(result: dict) -> str:
    """Return a user-readable skill summary."""
    if result["task_mode"] == "recommend":
        context = result["interpreted_context"]
        package = result["recommendation_state"]["base_package"]
        lines = [
            "TFL Skill Recommend",
            f"- Study phase: {context['study_phase']}",
            f"- Therapeutic area: {context['therapeutic_area']}",
            f"- Sections: {', '.join(package['sections'])}",
            f"- Shell families: {', '.join(package['shell_families'])}",
            f"- Recommended shell count: {package['total_items']}",
        ]
        return "\n".join(lines)

    package = result["recommendation_state"]["base_package"]
    artifacts = result["generation_results"]["artifacts"]
    lines = [
        "TFL Skill Generate",
        f"- Study phase: {result['interpreted_context']['study_phase']}",
        f"- Therapeutic area: {result['interpreted_context']['therapeutic_area']}",
        f"- Sections: {', '.join(package['sections'])}",
        f"- Recommended shell count: {package['total_items']}",
        f"- Generated outputs: {', '.join(a['file_name'] for a in artifacts)}",
    ]
    return "\n".join(lines)
