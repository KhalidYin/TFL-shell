import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "validate_skill_package.py"
PACKAGE_DIR = ROOT / ".trae" / "skills" / "tfls-shell"


def _run_validator(target: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(target)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )


def test_validator_accepts_current_tfls_shell_package():
    result = _run_validator(PACKAGE_DIR)

    assert result.returncode == 0
    assert "校验通过" in result.stdout


def test_validator_fails_when_required_file_is_missing(tmp_path):
    package_dir = tmp_path / "demo-skill"
    package_dir.mkdir()
    (package_dir / "SKILL.md").write_text(
        "---\n"
        'name: "demo-skill"\n'
        'description: "用于测试的 Skill。适用于验证脚本。"\n'
        "---\n\n"
        "# Demo Skill\n",
        encoding="utf-8",
    )

    result = _run_validator(package_dir)

    assert result.returncode == 1
    assert "缺少必需文件" in result.stdout
    assert "PACKAGE_GUIDE.md" in result.stdout
    assert "DEVELOPMENT_RULES.md" in result.stdout


def test_validator_fails_when_skill_md_reintroduces_project_runtime_dependency(tmp_path):
    package_dir = tmp_path / "demo-skill"
    package_dir.mkdir()
    (package_dir / "SKILL.md").write_text(
        "---\n"
        'name: "demo-skill"\n'
        'description: "用于测试的 Skill。适用于验证脚本。"\n'
        "---\n\n"
        "# Demo Skill\n\n"
        "调用方 -> TFLs-Shell SKILL -> 参考 TFLs-Shell Product -> 产出结果\n",
        encoding="utf-8",
    )
    (package_dir / "PACKAGE_GUIDE.md").write_text("# Guide\n", encoding="utf-8")
    (package_dir / "DEVELOPMENT_RULES.md").write_text("# Rules\n", encoding="utf-8")

    result = _run_validator(package_dir)

    assert result.returncode == 1
    assert "禁止表述" in result.stdout
    assert "TFLs-Shell Product" in result.stdout


def test_validator_fails_when_self_contained_assets_are_missing(tmp_path):
    package_dir = tmp_path / "demo-skill"
    package_dir.mkdir()
    (package_dir / "SKILL.md").write_text(
        "---\n"
        'name: "demo-skill"\n'
        'description: "用于测试的 Skill。适用于验证脚本。"\n'
        "---\n\n"
        "# Demo Skill\n",
        encoding="utf-8",
    )
    (package_dir / "PACKAGE_GUIDE.md").write_text("# Guide\n", encoding="utf-8")
    (package_dir / "DEVELOPMENT_RULES.md").write_text("# Rules\n", encoding="utf-8")

    result = _run_validator(package_dir)

    assert result.returncode == 1
    assert "缺少自包含资产" in result.stdout
    assert "package_assets/contract_registry.json" in result.stdout
    assert "package_assets/catalog_subset.json" in result.stdout
    assert "package_assets/minimal_runtime_requirements.txt" in result.stdout
    assert "examples/recommend_then_generate_non_oncology.json" in result.stdout
