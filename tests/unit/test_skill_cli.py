import pytest


pytestmark = pytest.mark.skip(
    reason=(
        "Historical tests for the repository-level workflow prototype. "
        "Reusable Skill package review now happens under .trae/skills/ and this "
        "prototype is no longer the canonical Skill deliverable."
    )
)
