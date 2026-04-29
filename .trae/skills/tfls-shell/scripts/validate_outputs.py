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

from tflshell.data.definitions import build_catalog  # noqa: E402
from alignment_contracts import (  # noqa: E402
    build_docx_layout_contract,
    build_docx_shell_contract,
    build_sop_contract,
    build_xlsx_master_sheet_contract,
    build_xlsx_workbook_contract,
)


def _contract_passed(checks: dict) -> bool:
    return all(value is True for value in checks.values() if isinstance(value, bool))


def validate_outputs(docx: str | None = None, xlsx: str | None = None, sop: str | None = None) -> dict:
    catalog = build_catalog()
    declared_references: dict[str, dict] = {}
    checks: dict[str, dict] = {}

    if xlsx:
        check, reference = build_xlsx_master_sheet_contract(catalog, xlsx)
        checks["xlsx_master_sheet"] = check
        declared_references["xlsx_master_sheet"] = reference
        check, reference = build_xlsx_workbook_contract(catalog, xlsx)
        checks["xlsx_workbook"] = check
        declared_references["xlsx_workbook"] = reference

    if docx:
        check, reference = build_docx_shell_contract(catalog, docx)
        checks["docx_shell_template"] = check
        declared_references["docx_shell_template"] = reference
        check, reference = build_docx_layout_contract(catalog, docx)
        checks["docx_layout"] = check
        declared_references["docx_layout"] = reference

    if sop:
        check, reference = build_sop_contract(sop)
        checks["sop_governance_doc"] = check
        declared_references["sop_governance_doc"] = reference

    return {
        "validated_outputs": {
            "docx": docx,
            "xlsx": xlsx,
            "sop": sop,
        },
        "passed": all(_contract_passed(check) for check in checks.values()),
        "cross_output_checks": checks,
        "declared_references": declared_references,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="验证 TFLs-Shell Skill 生成物是否符合包内 Product 对齐契约。")
    parser.add_argument("--docx")
    parser.add_argument("--xlsx")
    parser.add_argument("--sop")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    result = validate_outputs(docx=args.docx, xlsx=args.xlsx, sop=args.sop)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        status = "通过" if result["passed"] else "失败"
        print(f"输出契约校验{status}")
        for name, checks in result["cross_output_checks"].items():
            failed = [key for key, value in checks.items() if isinstance(value, bool) and not value]
            print(f"- {name}: {'通过' if not failed else '失败: ' + ', '.join(failed)}")
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
