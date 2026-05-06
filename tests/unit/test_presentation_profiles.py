
from tflshell.presentation import (
    AUTHORING_SHELL_PROFILE,
    COMPACT_REVIEW_PROFILE,
    CSR_STANDARD_PROFILE,
    get_presentation_profile,
)


def test_get_presentation_profile_defaults_to_csr_standard():
    profile = get_presentation_profile(None)

    assert profile == CSR_STANDARD_PROFILE
    assert profile.table.width_pct == 100
    assert profile.table.group_header_space_before == 6


def test_compact_review_profile_is_tighter_than_csr_standard():
    compact = get_presentation_profile("compact_review")
    standard = get_presentation_profile("csr_standard")

    assert compact == COMPACT_REVIEW_PROFILE
    assert compact.table.group_header_space_before < standard.table.group_header_space_before
    assert compact.paragraphs.subheading_space_before < standard.paragraphs.subheading_space_before
    assert compact.table.indent_prefix == "  "


def test_authoring_shell_profile_preserves_more_editing_space():
    profile = get_presentation_profile("authoring-shell")

    assert profile == AUTHORING_SHELL_PROFILE
    assert (
        profile.paragraphs.shell_heading_space_before
        >= CSR_STANDARD_PROFILE.paragraphs.shell_heading_space_before
    )
    assert (
        profile.paragraphs.figure_space_before
        >= CSR_STANDARD_PROFILE.paragraphs.figure_space_before
    )


def test_unknown_profile_raises_clear_error():
    try:
        get_presentation_profile("draft_layout")
    except ValueError as exc:
        assert "Unsupported presentation profile" in str(exc)
    else:
        raise AssertionError("Expected ValueError for unsupported presentation profile")


def test_generate_cli_accepts_presentation_profile(tmp_path):
    from tflshell.main import main

    output_dir = tmp_path / "out"
    exit_code = main(
        [
            "generate",
            "--type",
            "docx",
            "--output-dir",
            str(output_dir),
            "--no-figures",
            "--presentation-profile",
            "compact_review",
        ]
    )

    generated = output_dir / "TFL_Shell_Template_v2.1.0.docx"
    assert exit_code == 0
    assert generated.exists()
