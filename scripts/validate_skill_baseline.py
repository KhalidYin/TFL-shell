from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


DEFAULT_SKILL_DIR = Path("Skill/tfls-shell")

BASELINE_ASSETS = {
    "output_manifest.json": "build_output_manifest",
    "contract_registry.json": "build_contract_registry",
}

REQUIRED_GENERATION_SCRIPTS = (
    "alignment_contracts.py",
    "export_catalog_subset.py",
    "export_product_contracts.py",
    "generate_project_aligned_outputs.py",
    "package_bundle.py",
    "recommend_then_generate.py",
    "validate_outputs.py",
)


def _repo_root() -> Path:
    current_path = Path(__file__).resolve()
    for parent in (current_path.parent, *current_path.parents):
        if (parent / "pyproject.toml").exists() and (parent / "src" / "tflshell").exists():
            return parent
    raise RuntimeError("无法定位 TFLshell 仓库根目录。")


def _load_export_module():
    repo_root = _repo_root()
    scripts_dir = repo_root / "Skill" / "tfls-shell" / "scripts"
    src_dir = repo_root / "src"
    for path in (scripts_dir, src_dir):
        if str(path) not in sys.path:
            sys.path.insert(0, str(path))

    module_path = scripts_dir / "export_product_contracts.py"
    spec = importlib.util.spec_from_file_location("tfls_shell_export_product_contracts", module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"无法加载契约导出脚本：{module_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_skill_baseline(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_dir = skill_dir.resolve()

    if not skill_dir.exists():
        return [f"Skill 目录不存在：{skill_dir}"]

    missing_scripts = [
        script_name
        for script_name in REQUIRED_GENERATION_SCRIPTS
        if not (skill_dir / "scripts" / script_name).exists()
    ]
    if missing_scripts:
        errors.append(f"缺少生成/验证脚本：{', '.join(missing_scripts)}")

    missing_assets = [
        asset_name
        for asset_name in BASELINE_ASSETS
        if not (skill_dir / "package_assets" / asset_name).exists()
    ]
    if missing_assets:
        errors.append(f"缺少回归基线资产：{', '.join(missing_assets)}")

    if errors:
        return errors

    export_module = _load_export_module()
    for asset_name, builder_name in BASELINE_ASSETS.items():
        expected_payload = getattr(export_module, builder_name)()
        actual_payload = _read_json(skill_dir / "package_assets" / asset_name)
        if actual_payload != expected_payload:
            errors.append(
                f"{asset_name} 与 Product 当前导出不一致；如变更是有意的，"
                "请运行 Skill/tfls-shell/scripts/export_product_contracts.py 后再提交。"
            )

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="校验 Skill 包回归基线是否与 Product 当前实现一致。")
    parser.add_argument(
        "skill_dir",
        nargs="?",
        default=str(DEFAULT_SKILL_DIR),
        help="待校验的 Skill 包目录，默认 Skill/tfls-shell。",
    )
    parser.add_argument("--json", action="store_true", help="输出 JSON 格式校验结果。")
    args = parser.parse_args(argv)

    errors = validate_skill_baseline(Path(args.skill_dir))
    if args.json:
        print(json.dumps({"passed": not errors, "errors": errors}, indent=2, ensure_ascii=False))
    elif errors:
        print(f"Skill 回归基线校验失败：{args.skill_dir}")
        for error in errors:
            print(f"- {error}")
    else:
        print(f"Skill 回归基线校验通过：{args.skill_dir}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
