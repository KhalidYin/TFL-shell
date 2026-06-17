import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    ROOT / "Skill" / "tfls-shell" / "scripts" / "generate_project_aligned_outputs.py"
)


def _run_generate_script(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )


def test_generate_script_creates_project_named_xlsx_output(tmp_path):
    result = _run_generate_script("--type", "xlsx", "--output-dir", str(tmp_path), "--json")

    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["runtime_summary"]["mode"] == "skill_runtime_preferred"
    assert payload["runtime_summary"]["catalog_source"].endswith(
        "package_assets/catalog_subset.json"
    )
    assert payload["runtime_summary"]["wrapper_layer"] == "runtime/wrappers"
    assert payload["requested_outputs"] == ["xlsx"]
    assert payload["artifact_count"] == 1
    assert payload["artifacts"][0]["kind"] == "xlsx"
    assert payload["artifacts"][0]["file_name"].startswith("TFL_TOC_v")
    assert tmp_path.joinpath(payload["artifacts"][0]["file_name"]).exists()
