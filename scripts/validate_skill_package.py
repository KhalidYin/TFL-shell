from __future__ import annotations

import argparse
import sys
from pathlib import Path

REQUIRED_FILES = ("SKILL.md", "PACKAGE_GUIDE.md", "DEVELOPMENT_RULES.md")
REQUIRED_SELF_CONTAINED_ASSETS = (
    "package_assets/contract_registry.json",
    "package_assets/catalog_subset.json",
    "package_assets/output_manifest.json",
    "package_assets/minimal_runtime_requirements.txt",
    "examples/recommend_then_generate_non_oncology.json",
)
REQUIRED_CONTRACT_DOCS = (
    "docs/product_alignment_contract.md",
    "docs/catalog_schema_contract.md",
    "docs/docx_shell_contract.md",
    "docs/xlsx_workbook_contract.md",
    "docs/sop_contract.md",
    "docs/table_layout_contract.md",
)
REQUIRED_RUNTIME_SCRIPTS = (
    "scripts/alignment_contracts.py",
    "scripts/export_catalog_subset.py",
    "scripts/export_product_contracts.py",
    "scripts/generate_project_aligned_outputs.py",
    "scripts/package_bundle.py",
    "scripts/recommend_then_generate.py",
    "scripts/validate_outputs.py",
)
FORBIDDEN_SKILL_PATTERNS = (
    "调用方 -> TFLs-Shell SKILL -> 参考 TFLs-Shell Product ->",
    "TFLs-Shell Product",
    "默认依赖某个完整项目",
    "运行时依赖整个上游项目",
)


def _parse_frontmatter(skill_md_path: Path) -> dict[str, str]:
    text = skill_md_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    if len(lines) < 3 or lines[0].strip() != "---":
        raise ValueError("SKILL.md 缺少合法 frontmatter 起始分隔符。")

    end_index = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            end_index = index
            break

    if end_index is None:
        raise ValueError("SKILL.md 缺少合法 frontmatter 结束分隔符。")

    frontmatter: dict[str, str] = {}
    for raw_line in lines[1:end_index]:
        if ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        frontmatter[key.strip()] = value.strip().strip('"').strip("'")
    return frontmatter


def validate_skill_package(package_dir: Path) -> list[str]:
    errors: list[str] = []

    if not package_dir.exists():
        return [f"目标目录不存在：{package_dir}"]
    if not package_dir.is_dir():
        return [f"目标路径不是目录：{package_dir}"]

    missing_files = [name for name in REQUIRED_FILES if not (package_dir / name).exists()]
    if missing_files:
        errors.append(f"缺少必需文件：{', '.join(missing_files)}")
        return errors

    missing_assets = [
        name for name in REQUIRED_SELF_CONTAINED_ASSETS if not (package_dir / Path(name)).exists()
    ]
    if missing_assets:
        errors.append(f"缺少自包含资产：{', '.join(missing_assets)}")

    missing_contract_docs = [
        name for name in REQUIRED_CONTRACT_DOCS if not (package_dir / Path(name)).exists()
    ]
    if missing_contract_docs:
        errors.append(f"缺少契约文档：{', '.join(missing_contract_docs)}")

    missing_runtime_scripts = [
        name for name in REQUIRED_RUNTIME_SCRIPTS if not (package_dir / Path(name)).exists()
    ]
    if missing_runtime_scripts:
        errors.append(f"缺少契约脚本：{', '.join(missing_runtime_scripts)}")

    skill_md_path = package_dir / "SKILL.md"
    try:
        frontmatter = _parse_frontmatter(skill_md_path)
    except ValueError as exc:
        errors.append(str(exc))
        return errors

    for field_name in ("name", "description"):
        if not frontmatter.get(field_name):
            errors.append(f"SKILL.md frontmatter 缺少字段：{field_name}")

    if frontmatter.get("name") and frontmatter["name"] != package_dir.name:
        errors.append(
            f"SKILL.md frontmatter 中的 name 与目录名不一致：{frontmatter['name']} != {package_dir.name}"
        )

    skill_md_text = skill_md_path.read_text(encoding="utf-8")
    for pattern in FORBIDDEN_SKILL_PATTERNS:
        if pattern in skill_md_text:
            errors.append(f"检测到禁止表述：{pattern}")

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="校验 TFLs-Shell Skill 包结构与基础约束。")
    parser.add_argument(
        "package_dir",
        nargs="?",
        default=str(Path("Skill/tfls-shell")),
        help="待校验的 Skill 包目录。",
    )
    args = parser.parse_args(argv)

    package_dir = Path(args.package_dir)
    errors = validate_skill_package(package_dir)
    if errors:
        print(f"Skill 包校验失败：{package_dir}")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Skill 包校验通过：{package_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
