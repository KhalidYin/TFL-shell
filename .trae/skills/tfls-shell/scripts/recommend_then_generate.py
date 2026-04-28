from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def _bootstrap_repo_imports() -> None:
    repo_root = Path(__file__).resolve().parents[4]
    package_root = Path(__file__).resolve().parents[1]
    src_path = repo_root / "src"
    if str(package_root) not in sys.path:
        sys.path.insert(0, str(package_root))
    if str(src_path) not in sys.path:
        sys.path.insert(0, str(src_path))


_bootstrap_repo_imports()

from tflshell import __version__  # noqa: E402
from tflshell.data.definitions import build_catalog  # noqa: E402
from tflshell.models.catalog import TFLCatalog  # noqa: E402
from tflshell.recommend import InputSource, RecommendRequest, recommend_shells  # noqa: E402
from tflshell.utils.naming import make_filename  # noqa: E402
from alignment_contracts import (  # noqa: E402
    build_docx_shell_contract,
    build_sop_contract,
    build_xlsx_master_sheet_contract,
)
from package_bundle import describe_package_bundle  # noqa: E402
from runtime.wrappers.docx_wrapper import generate as generate_docx  # noqa: E402
from runtime.wrappers.sop_wrapper import generate as generate_sop  # noqa: E402
from runtime.wrappers.xlsx_wrapper import generate as generate_xlsx  # noqa: E402


def _resolve_requested_outputs(raw: str) -> list[str]:
    if raw == "all":
        return ["docx", "xlsx", "sop"]
    return [raw]


def _filtered_catalog(catalog: TFLCatalog, shell_ids: list[str]) -> TFLCatalog:
    items = [catalog.get(shell_id) for shell_id in shell_ids]
    return TFLCatalog([item for item in items if item is not None])


def _normalize_area(raw: str) -> str:
    if raw == "Oncology":
        return "oncology"
    if raw == "Non-Oncology":
        return "non-oncology"
    return "all"


def _build_request(args) -> RecommendRequest:
    sources = [InputSource(content_text=text) for text in (args.text or [])]
    for file_path in args.input_file or []:
        sources.append(InputSource(file_path=file_path))
    if not sources:
        raise ValueError("至少提供一个 --text 或 --input-file。")

    return RecommendRequest(
        sources=sources,
        section_scope=args.section or [],
        therapeutic_area_hint=args.area,
        study_phase_hint=args.phase,
        include_figures=not args.no_figures,
        include_listings=not args.no_listings,
    )


def _runtime_summary() -> dict:
    package_root = Path(__file__).resolve().parents[1]
    return {
        "mode": "skill_runtime_preferred",
        "catalog_source": str(package_root / "package_assets" / "catalog_subset.json").replace("\\", "/"),
        "registry_source": str(package_root / "package_assets" / "contract_registry.json").replace("\\", "/"),
        "wrapper_layer": "runtime/wrappers",
    }


def _generate_from_recommendation(args, recommendation) -> dict:
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    catalog = build_catalog()
    shell_ids = recommendation.recommendation_state["base_package"]["shell_ids"]
    scoped_catalog = _filtered_catalog(catalog, shell_ids)
    requested_outputs = _resolve_requested_outputs(args.type)
    artifacts: list[dict[str, str]] = []

    therapeutic_area = _normalize_area(recommendation.interpreted_context["therapeutic_area"])

    for output_kind in requested_outputs:
        if output_kind == "docx":
            output_path = output_dir / make_filename("TFL_Shell_Template", __version__, ".docx")
            generated_path = Path(
                generate_docx(
                    scoped_catalog,
                    str(output_path),
                    therapeutic_area=therapeutic_area,
                    generate_figures=not args.no_figures,
                    sponsor=args.sponsor,
                    protocol=args.protocol,
                    presentation_profile=args.presentation_profile,
                )
            )
        elif output_kind == "xlsx":
            output_path = output_dir / make_filename("TFL_TOC", __version__, ".xlsx")
            generated_path = Path(generate_xlsx(scoped_catalog, str(output_path)))
        elif output_kind == "sop":
            output_path = output_dir / make_filename("TFL_Shell_SOP", __version__, ".docx")
            generated_path = Path(generate_sop(scoped_catalog, str(output_path)))
        else:
            raise ValueError(f"不支持的输出类型：{output_kind}")
        artifacts.append(
            {
                "kind": output_kind,
                "path": str(generated_path),
                "file_name": generated_path.name,
            }
        )

    return {
        "generated": True,
        "version": __version__,
        "runtime_summary": _runtime_summary(),
        "requested_outputs": requested_outputs,
        "artifact_count": len(artifacts),
        "output_dir": str(output_dir),
        "artifacts": artifacts,
    }


def _build_validation_results(scoped_catalog: TFLCatalog, generation_results: dict) -> dict:
    catalog_warnings = scoped_catalog.validate()
    artifact_names = [artifact["file_name"] for artifact in generation_results["artifacts"]]
    cross_output_checks = {
        "requested_outputs": generation_results["requested_outputs"],
        "artifact_count": generation_results["artifact_count"],
        "artifact_names": artifact_names,
        "all_artifacts_exist": all(Path(artifact["path"]).exists() for artifact in generation_results["artifacts"]),
    }
    declared_references: dict[str, dict] = {}

    xlsx_artifact = next(
        (artifact for artifact in generation_results["artifacts"] if artifact["kind"] == "xlsx"),
        None,
    )
    if xlsx_artifact is not None:
        checks, references = build_xlsx_master_sheet_contract(
            scoped_catalog,
            xlsx_artifact["path"],
        )
        cross_output_checks["xlsx_master_sheet"] = checks
        declared_references["xlsx_master_sheet"] = references

    docx_artifact = next(
        (artifact for artifact in generation_results["artifacts"] if artifact["kind"] == "docx"),
        None,
    )
    if docx_artifact is not None:
        checks, references = build_docx_shell_contract(
            scoped_catalog,
            docx_artifact["path"],
        )
        cross_output_checks["docx_shell_template"] = checks
        declared_references["docx_shell_template"] = references

    sop_artifact = next(
        (artifact for artifact in generation_results["artifacts"] if artifact["kind"] == "sop"),
        None,
    )
    if sop_artifact is not None:
        checks, references = build_sop_contract(sop_artifact["path"])
        cross_output_checks["sop_governance_doc"] = checks
        declared_references["sop_governance_doc"] = references

    return {
        "catalog_validation": {
            "warning_count": len(catalog_warnings),
            "warnings": catalog_warnings,
        },
        "declared_references": declared_references,
        "cross_output_checks": cross_output_checks,
        "rule_violations": [],
        "warnings": catalog_warnings,
    }


def run(args) -> dict:
    request = _build_request(args)
    recommendation = recommend_shells(request)
    catalog = build_catalog()
    base_package = recommendation.recommendation_state["base_package"]
    scoped_catalog = _filtered_catalog(catalog, base_package["shell_ids"])
    generation_results = _generate_from_recommendation(args, recommendation)
    generation_results["filters"] = {
        "therapeutic_area": _normalize_area(recommendation.interpreted_context["therapeutic_area"]),
        "section_scope": base_package["sections"],
        "shell_ids": base_package["shell_ids"],
    }
    validation_results = _build_validation_results(scoped_catalog, generation_results)
    request_summary = dict(recommendation.request_summary)
    request_summary["task_mode"] = "recommend_then_generate"
    request_summary["desired_outputs"] = generation_results["requested_outputs"]
    request_summary["output_dir"] = generation_results["output_dir"]

    return {
        "task_mode": "recommend_then_generate",
        "version": __version__,
        "package_bundle": describe_package_bundle(),
        "runtime_summary": generation_results["runtime_summary"],
        "request_summary": request_summary,
        "interpreted_context": recommendation.interpreted_context,
        "ingestion_state": recommendation.ingestion_state,
        "extraction_state": recommendation.extraction_state,
        "normalization_state": recommendation.normalization_state,
        "ambiguity_state": recommendation.ambiguity_state,
        "recommendation_state": recommendation.recommendation_state,
        "recommendation_summary": {
            "sections": base_package["sections"],
            "shell_families": base_package["shell_families"],
            "shell_ids": base_package["shell_ids"],
            "total_items": base_package["total_items"],
        },
        "generation_results": generation_results,
        "validation_results": validation_results,
        "risk_notes": recommendation.risk_notes,
        "optimization_suggestions": recommendation.optimization_suggestions,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="从文本输入直接完成推荐并生成与当前项目一致命名和结构的正式输出。"
    )
    parser.add_argument("--text", action="append")
    parser.add_argument("--input-file", action="append")
    parser.add_argument("--section", action="append", choices=["14.1", "14.2", "14.3", "14.4", "16.2"])
    parser.add_argument("--area", default="unknown", choices=["oncology", "non-oncology", "all", "unknown"])
    parser.add_argument("--phase", default="unknown", choices=["phase-i", "phase-ii", "phase-iii", "mixed", "unknown"])
    parser.add_argument("--type", default="all", choices=["docx", "xlsx", "sop", "all"])
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--sponsor", default=None)
    parser.add_argument("--protocol", default=None)
    parser.add_argument(
        "--presentation-profile",
        default="csr_standard",
        choices=["csr_standard", "compact_review", "authoring_shell"],
    )
    parser.add_argument("--no-figures", action="store_true")
    parser.add_argument("--no-listings", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    result = run(args)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("已完成 recommend -> generate")
        print(f"- Sections: {', '.join(result['recommendation_summary']['sections'])}")
        print(f"- 输出数量: {result['generation_results']['artifact_count']}")
        for artifact in result["generation_results"]["artifacts"]:
            print(f"  - [{artifact['kind']}] {artifact['path']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
