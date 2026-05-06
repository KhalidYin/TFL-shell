"""TFLCatalog — container and query interface for TFL definitions."""

from tflshell.models.enums import FigureType, Section, TFLType
from tflshell.models.tfl_item import TFLItem


class TFLCatalog:
    """Container for all TFL definitions with query methods."""

    def __init__(self, items: list[TFLItem]):
        self._items: list[TFLItem] = sorted(items, key=lambda x: (x.section.number, x.sort_key))
        self._by_id: dict[str, TFLItem] = {item.id: item for item in self._items}

    def all(self) -> list[TFLItem]:
        return list(self._items)

    def by_section(self, section: Section) -> list[TFLItem]:
        return [item for item in self._items if item.section == section]

    def by_type(self, tfl_type: TFLType) -> list[TFLItem]:
        return [item for item in self._items if item.tfl_type == tfl_type]

    def tables(self) -> list[TFLItem]:
        return self.by_type(TFLType.TABLE)

    def figures(self) -> list[TFLItem]:
        return self.by_type(TFLType.FIGURE)

    def listings(self) -> list[TFLItem]:
        return self.by_type(TFLType.LISTING)

    def by_figure_type(self, figure_type: FigureType) -> list[TFLItem]:
        ft = figure_type.value
        return [i for i in self._items if i.tfl_type == TFLType.FIGURE and i.figure_type == ft]

    def generated_figures(self) -> list[TFLItem]:
        """Figures that have matplotlib generation capability."""
        return [i for i in self._items if i.is_figure_generated]

    def by_therapeutic_area(self, area: str) -> list[TFLItem]:
        cleaned = area.strip().lower().replace("_", "-").replace(" ", "-")
        if cleaned == "oncology":
            target = "Oncology"
        elif cleaned in ("non-oncology", "nononcology"):
            target = "Non-Oncology"
        else:
            target = area
        return [item for item in self._items if target in item.therapeutic_areas]

    def get(self, tfl_id: str) -> TFLItem | None:
        return self._by_id.get(tfl_id)

    def section_summary(self) -> dict[str, dict]:
        summary = {}
        for section in Section:
            items = self.by_section(section)
            figures = [i for i in items if i.tfl_type == TFLType.FIGURE]
            summary[section.number] = {
                "title": section.title,
                "total": len(items),
                "tables": len([i for i in items if i.tfl_type == TFLType.TABLE]),
                "figures": len(figures),
                "figures_generated": len([f for f in figures if f.is_figure_generated]),
                "listings": len([i for i in items if i.tfl_type == TFLType.LISTING]),
            }
        return summary

    def summary_stats(self) -> dict:
        """Return high-level catalog statistics."""
        return {
            "total": len(self._items),
            "tables": len(self.tables()),
            "figures": len(self.figures()),
            "figures_generated": len(self.generated_figures()),
            "listings": len(self.listings()),
            "oncology_only": len([i for i in self._items if i.oncology_only]),
            "non_oncology_only": len([i for i in self._items if i.non_oncology_only]),
            "general": len(
                [i for i in self._items if not i.oncology_only and not i.non_oncology_only]
            ),
        }

    def validate(self) -> list[str]:
        warnings = []
        seen_ids = set()
        for item in self._items:
            if item.id in seen_ids:
                warnings.append(f"Duplicate TFL ID: {item.id}")
            seen_ids.add(item.id)

            expected_prefix = item.tfl_type.value[0]
            if not item.id.startswith(expected_prefix):
                warnings.append(
                    f"ID prefix mismatch: {item.id} should start with '{expected_prefix}'"
                )
            if item.section.number not in item.id:
                warnings.append(
                    f"ID section mismatch: {item.id} does not contain {item.section.number}"
                )
            if item.tfl_type != TFLType.FIGURE and not item.placeholder_columns:
                warnings.append(f"Missing placeholder_columns for {item.tfl_type.value} {item.id}")
            if item.tfl_type != TFLType.FIGURE and not item.has_shell_rows:
                warnings.append(f"Missing shell_rows for {item.tfl_type.value} {item.id}")
            if item.tfl_type != TFLType.FIGURE and not item.display_number:
                warnings.append(f"Missing display_number for {item.tfl_type.value} {item.id}")
            if item.tfl_type != TFLType.FIGURE and not item.placeholder_example:
                warnings.append(f"Missing placeholder example for {item.tfl_type.value} {item.id}")
            # Figures with figure_type must be valid FigureType values
            if item.tfl_type == TFLType.FIGURE and item.figure_type:
                valid_types = {ft.value for ft in FigureType}
                if item.figure_type not in valid_types:
                    warnings.append(
                        f"Unknown figure_type '{item.figure_type}' for {item.id}. "
                        f"Valid types: {valid_types}"
                    )
            # Every governed shell should retain dataset traceability metadata.
            if not item.dataset_source:
                warnings.append(f"Missing dataset_source for {item.id}")

        return warnings

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __repr__(self) -> str:
        return f"TFLCatalog({len(self._items)} items)"
