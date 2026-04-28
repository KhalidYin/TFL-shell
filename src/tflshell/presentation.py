"""Presentation profiles for governed TFL shell rendering."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TableLayoutConfig:
    """Table row and width presentation settings."""

    group_header_space_before: int
    group_header_space_after: int
    indented_row_space_before: int
    indented_row_space_after: int
    standard_row_space_before: int
    standard_row_space_after: int
    cell_line_spacing: int
    indent_prefix: str
    width_pct: int


@dataclass(frozen=True)
class ParagraphLayoutConfig:
    """Heading and body paragraph spacing settings."""

    subheading_space_before: int
    subheading_space_after: int
    shell_heading_space_before: int
    shell_heading_space_after: int
    footnote_label_space_before: int
    footnote_label_space_after: int
    footnote_item_space_before: int
    footnote_item_space_after: int
    listing_note_space_before: int
    listing_note_space_after: int
    figure_space_before: int
    figure_space_after: int
    caption_space_before: int
    caption_space_after: int
    figure_note_space_before: int
    figure_note_space_after: int


@dataclass(frozen=True)
class PresentationProfile:
    """Top-level presentation profile."""

    name: str
    table_layout_policy: str
    listing_layout_policy: str
    footnote_layout_policy: str
    table: TableLayoutConfig
    paragraphs: ParagraphLayoutConfig


CSR_STANDARD_PROFILE = PresentationProfile(
    name="csr_standard",
    table_layout_policy="grouped_standard",
    listing_layout_policy="traceability_standard",
    footnote_layout_policy="standard_footnote",
    table=TableLayoutConfig(
        group_header_space_before=6,
        group_header_space_after=1,
        indented_row_space_before=0,
        indented_row_space_after=1,
        standard_row_space_before=1,
        standard_row_space_after=1,
        cell_line_spacing=12,
        indent_prefix="    ",
        width_pct=100,
    ),
    paragraphs=ParagraphLayoutConfig(
        subheading_space_before=6,
        subheading_space_after=4,
        shell_heading_space_before=2,
        shell_heading_space_after=2,
        footnote_label_space_before=6,
        footnote_label_space_after=1,
        footnote_item_space_before=0,
        footnote_item_space_after=0,
        listing_note_space_before=2,
        listing_note_space_after=3,
        figure_space_before=6,
        figure_space_after=2,
        caption_space_before=0,
        caption_space_after=2,
        figure_note_space_before=2,
        figure_note_space_after=2,
    ),
)

COMPACT_REVIEW_PROFILE = PresentationProfile(
    name="compact_review",
    table_layout_policy="grouped_compact",
    listing_layout_policy="compact_listing",
    footnote_layout_policy="compact_footnote",
    table=TableLayoutConfig(
        group_header_space_before=4,
        group_header_space_after=1,
        indented_row_space_before=0,
        indented_row_space_after=0,
        standard_row_space_before=0,
        standard_row_space_after=1,
        cell_line_spacing=11,
        indent_prefix="  ",
        width_pct=100,
    ),
    paragraphs=ParagraphLayoutConfig(
        subheading_space_before=4,
        subheading_space_after=2,
        shell_heading_space_before=1,
        shell_heading_space_after=1,
        footnote_label_space_before=4,
        footnote_label_space_after=1,
        footnote_item_space_before=0,
        footnote_item_space_after=0,
        listing_note_space_before=1,
        listing_note_space_after=2,
        figure_space_before=4,
        figure_space_after=1,
        caption_space_before=0,
        caption_space_after=1,
        figure_note_space_before=1,
        figure_note_space_after=1,
    ),
)

AUTHORING_SHELL_PROFILE = PresentationProfile(
    name="authoring_shell",
    table_layout_policy="grouped_standard",
    listing_layout_policy="traceability_standard",
    footnote_layout_policy="standard_footnote",
    table=TableLayoutConfig(
        group_header_space_before=8,
        group_header_space_after=2,
        indented_row_space_before=0,
        indented_row_space_after=1,
        standard_row_space_before=1,
        standard_row_space_after=1,
        cell_line_spacing=12,
        indent_prefix="    ",
        width_pct=100,
    ),
    paragraphs=ParagraphLayoutConfig(
        subheading_space_before=8,
        subheading_space_after=4,
        shell_heading_space_before=3,
        shell_heading_space_after=3,
        footnote_label_space_before=6,
        footnote_label_space_after=2,
        footnote_item_space_before=0,
        footnote_item_space_after=1,
        listing_note_space_before=2,
        listing_note_space_after=4,
        figure_space_before=8,
        figure_space_after=3,
        caption_space_before=0,
        caption_space_after=2,
        figure_note_space_before=2,
        figure_note_space_after=3,
    ),
)

_PROFILES = {
    CSR_STANDARD_PROFILE.name: CSR_STANDARD_PROFILE,
    COMPACT_REVIEW_PROFILE.name: COMPACT_REVIEW_PROFILE,
    AUTHORING_SHELL_PROFILE.name: AUTHORING_SHELL_PROFILE,
}


def get_presentation_profile(name: str | None) -> PresentationProfile:
    """Return a supported presentation profile by name."""
    if not name:
        return CSR_STANDARD_PROFILE
    cleaned = name.strip().lower().replace("-", "_").replace(" ", "_")
    try:
        return _PROFILES[cleaned]
    except KeyError as exc:
        supported = ", ".join(sorted(_PROFILES))
        raise ValueError(f"Unsupported presentation profile '{name}'. Supported profiles: {supported}.") from exc
