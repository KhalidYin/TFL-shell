from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


DEFAULT_SKILL_NAME = "tfls-shell"


def _repo_root() -> Path:
    current_path = Path(__file__).resolve()
    for parent in (current_path.parent, *current_path.parents):
        if (parent / "pyproject.toml").exists() and (parent / "Skill" / DEFAULT_SKILL_NAME).exists():
            return parent
    raise RuntimeError("无法定位 TFLshell 仓库根目录。")


def _default_agent_root(repo_root: Path) -> Path:
    return repo_root / ".agent"


def _assert_within(child: Path, parent: Path) -> None:
    child_resolved = child.resolve()
    parent_resolved = parent.resolve()
    if child_resolved != parent_resolved and parent_resolved not in child_resolved.parents:
        raise ValueError(f"目标路径不在预期目录内：{child_resolved} not under {parent_resolved}")


def install_skill(
    source_dir: Path,
    target_root: Path,
    skill_name: str = DEFAULT_SKILL_NAME,
    force: bool = False,
    dry_run: bool = False,
) -> dict:
    source_dir = source_dir.resolve()
    target_root = target_root.resolve()
    skills_dir = target_root / "skills"
    target_dir = skills_dir / skill_name

    if not source_dir.exists() or not source_dir.is_dir():
        raise FileNotFoundError(f"Skill 源目录不存在：{source_dir}")
    if not (source_dir / "SKILL.md").exists():
        raise FileNotFoundError(f"Skill 源目录缺少 SKILL.md：{source_dir}")

    _assert_within(target_dir, skills_dir)

    actions = {
        "source_dir": str(source_dir),
        "target_root": str(target_root),
        "target_dir": str(target_dir),
        "dry_run": dry_run,
        "force": force,
        "installed": False,
        "replaced_existing": False,
    }

    if dry_run:
        actions["would_create_skills_dir"] = not skills_dir.exists()
        actions["would_replace_existing"] = target_dir.exists()
        return actions

    skills_dir.mkdir(parents=True, exist_ok=True)

    if target_dir.exists():
        if not force:
            raise FileExistsError(
                f"目标 Skill 已存在：{target_dir}。如需覆盖，请添加 --force。"
            )
        shutil.rmtree(target_dir)
        actions["replaced_existing"] = True

    shutil.copytree(source_dir, target_dir, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    actions["installed"] = True
    return actions


def main(argv: list[str] | None = None) -> int:
    root = _repo_root()
    parser = argparse.ArgumentParser(description="快速安装 TFLs-Shell Skill 到 agent skills 目录。")
    parser.add_argument(
        "--source",
        default=str(root / "Skill" / DEFAULT_SKILL_NAME),
        help="Skill 源目录，默认使用仓库内 Skill/tfls-shell。",
    )
    parser.add_argument(
        "--target-root",
        default=str(_default_agent_root(root)),
        help="agent 根目录，默认是仓库本地 .agent。可传 $HOME/.agents 安装到当前用户全局目录。",
    )
    parser.add_argument("--skill-name", default=DEFAULT_SKILL_NAME, help="安装后的 skill 目录名。")
    parser.add_argument("--force", action="store_true", help="如果目标已存在，先删除后重新安装。")
    parser.add_argument("--dry-run", action="store_true", help="只显示将执行的安装动作，不写入文件。")
    args = parser.parse_args(argv)

    try:
        result = install_skill(
            source_dir=Path(args.source),
            target_root=Path(args.target_root),
            skill_name=args.skill_name,
            force=args.force,
            dry_run=args.dry_run,
        )
    except (FileExistsError, FileNotFoundError, ValueError, RuntimeError) as exc:
        print(f"安装失败：{exc}", file=sys.stderr)
        return 1

    if result["dry_run"]:
        print("安装预览：")
    elif result["installed"]:
        print("安装完成：")
    for key in ("source_dir", "target_root", "target_dir", "force", "replaced_existing"):
        print(f"- {key}: {result[key]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
