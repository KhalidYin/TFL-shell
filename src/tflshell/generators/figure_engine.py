"""Backward-compatible figure generation entrypoint."""

from tflshell.figures.registry import (
    FIGURE_CLASS_MAP,
    build_mock_figure_data,
    generate_figure_buffer,
    supported_figure_types,
)

__all__ = [
    "FIGURE_CLASS_MAP",
    "build_mock_figure_data",
    "generate_figure_buffer",
    "supported_figure_types",
]
