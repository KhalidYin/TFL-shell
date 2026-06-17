import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "install_skill_to_agents.py"
SOURCE = ROOT / "Skill" / "tfls-shell"


def _run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )


def test_install_skill_dry_run_reports_target(tmp_path):
    result = _run("--target-root", str(tmp_path / ".agent"), "--dry-run")

    assert result.returncode == 0
    assert "安装预览" in result.stdout
    assert "tfls-shell" in result.stdout


def test_install_skill_default_target_is_local_agent():
    result = _run("--dry-run")

    assert result.returncode == 0
    assert str(ROOT / ".agent" / "skills" / "tfls-shell") in result.stdout


def test_install_skill_copies_package_to_target_root(tmp_path):
    target_root = tmp_path / ".agents"
    result = _run("--target-root", str(target_root))

    assert result.returncode == 0
    installed = target_root / "skills" / "tfls-shell"
    assert (installed / "SKILL.md").exists()
    assert (installed / "package_assets" / "output_manifest.json").exists()


def test_install_skill_refuses_existing_target_without_force(tmp_path):
    target_root = tmp_path / ".agents"
    first = _run("--target-root", str(target_root))
    second = _run("--target-root", str(target_root))

    assert first.returncode == 0
    assert second.returncode == 1
    assert "已存在" in second.stderr


def test_install_skill_force_replaces_existing_target(tmp_path):
    target_root = tmp_path / ".agents"
    installed = target_root / "skills" / "tfls-shell"
    first = _run("--target-root", str(target_root))
    marker = installed / "extra.tmp"
    marker.write_text("old", encoding="utf-8")
    second = _run("--target-root", str(target_root), "--force")

    assert first.returncode == 0
    assert second.returncode == 0
    assert not marker.exists()
    assert (installed / "SKILL.md").exists()
