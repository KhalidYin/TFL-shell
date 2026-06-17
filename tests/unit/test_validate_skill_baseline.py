import json
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "validate_skill_baseline.py"
PACKAGE_DIR = ROOT / "Skill" / "tfls-shell"


def _run_validator(target: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(target)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )


def _copy_skill_package(tmp_path: Path) -> Path:
    copied = tmp_path / "tfls-shell"
    shutil.copytree(PACKAGE_DIR, copied, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    return copied


def test_skill_baseline_accepts_current_package():
    result = _run_validator(PACKAGE_DIR)

    assert result.returncode == 0
    assert "回归基线校验通过" in result.stdout


def test_skill_baseline_fails_when_output_manifest_drifts(tmp_path):
    package_dir = _copy_skill_package(tmp_path)
    manifest_path = package_dir / "package_assets" / "output_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["catalog_summary"]["total"] = -1
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    result = _run_validator(package_dir)

    assert result.returncode == 1
    assert "output_manifest.json 与 Product 当前导出不一致" in result.stdout


def test_skill_baseline_fails_when_generation_script_is_missing(tmp_path):
    package_dir = _copy_skill_package(tmp_path)
    (package_dir / "scripts" / "recommend_then_generate.py").unlink()

    result = _run_validator(package_dir)

    assert result.returncode == 1
    assert "缺少生成/验证脚本" in result.stdout
    assert "recommend_then_generate.py" in result.stdout
