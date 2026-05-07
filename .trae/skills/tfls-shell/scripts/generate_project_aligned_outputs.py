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
from tflshell.utils.naming import make_filename  # noqa: E402
from runtime.wrappers.docx_wrapper import generate as generate_docx  # noqa: E402
from runtime.wrappers.sop_wrapper import generate as generate_sop  # noqa: E402
from runtime.wrappers.xlsx_wrapper import generate as generate_xlsx  # noqa: E402


def _resolve_requested_outputs(raw: str) -> list[str]:
    if raw == "all":
        return ["docx", "xlsx", "sop"]
    return [raw]


def _runtime_summary() -> dict:
    package_root = Path(__file__).resolve().parents[1]
    return {
        "mode": "skill_runtime_preferred",
        "catalog_source": str(package_root / "package_assets" / "catalog_subset.json").replace("\\", "/"),
        "registry_source": str(package_root / "package_assets" / "contract_registry.json").replace("\\", "/"),
        "wrapper_layer": "runtime/wrappers",
    }


def generate_outputs(args) -> dict:
    catalog = build_catalog()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    requested_outputs = _resolve_requested_outputs(args.type)
    artifacts: list[dict[str, str]] = []

    for output_kind in requested_outputs:
        if output_kind == "docx":
            output_path = output_dir / make_filename("TFL_Shell_Template", __version__, ".docx")
            generated_path = Path(
                generate_docx(
                    catalog,
                    str(output_path),
                    therapeutic_area=args.area,
                    generate_figures=not args.no_figures,
                    sponsor=args.sponsor,
                    protocol=args.protocol,
                    presentation_profile=args.presentation_profile,
                )
            )
        elif output_kind == "xlsx":
            output_path = output_dir / make_filename("TFL_TOC", __version__, ".xlsx")
            generated_path = Path(generate_xlsx(catalog, str(output_path)))
        elif output_kind == "sop":
            output_path = output_dir / make_filename("TFL_Shell_SOP", __version__, ".docx")
            generated_path = Path(generate_sop(catalog, str(output_path)))
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
        "runtime_summary": _runtime_summary(),
        "version": __version__,
        "requested_outputs": requested_outputs,
        "artifact_count": len(artifacts),
        "output_dir": str(output_dir),
        "artifacts": artifacts,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="为 TFLs-Shell SKILL 生成与当前项目一致命名和结构的正式输出。"
    )
    parser.add_argument("--type", default="all", choices=["docx", "xlsx", "sop", "all"])
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--area", default="all", choices=["oncology", "non-oncology", "all"])
    parser.add_argument("--sponsor", default=None)
    parser.add_argument("--protocol", default=None)
    parser.add_argument(
        "--presentation-profile",
        default="csr_standard",
        choices=["csr_standard", "compact_review", "authoring_shell"],
    )
    parser.add_argument("--no-figures", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    result = generate_outputs(args)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"已生成 {result['artifact_count']} 个输出到 {result['output_dir']}")
        for artifact in result["artifacts"]:
            print(f"- [{artifact['kind']}] {artifact['path']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
