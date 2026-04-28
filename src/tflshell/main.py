"""CLI entry point for TFLshell."""

import argparse
import os
import sys

from tflshell import __version__
from tflshell.config import DEFAULT_OUTPUT_DIR
from tflshell.data.definitions import build_catalog
from tflshell.generators.docx_shell import DocxShellGenerator
from tflshell.generators.xlsx_toc import XlsxTocGenerator
from tflshell.generators.docx_sop import DocxSopGenerator
from tflshell.models.enums import TFLType, Section
from tflshell.utils.naming import make_filename


def _normalize_area(raw: str) -> str:
    cleaned = raw.strip().lower().replace("_", "-").replace(" ", "-")
    if cleaned in ("oncology",):
        return "Oncology"
    if cleaned in ("non-oncology", "nononcology"):
        return "Non-Oncology"
    return cleaned


def cmd_generate(args):
    """Generate TFL deliverables."""
    catalog = build_catalog()
    types = args.type
    if types == "all":
        types = "docx,xlsx,sop"
    selected = [t.strip() for t in types.split(",")]
    results = []

    for run_type in selected:
        if run_type == "docx":
            out = args.output_docx or os.path.join(
                args.output_dir,
                make_filename("TFL_Shell_Template", __version__, ".docx"),
            )
            gen = DocxShellGenerator(
                catalog, output_path=out,
                therapeutic_area=args.area,
                generate_figures=not args.no_figures,
                sponsor=args.sponsor, protocol=args.protocol,
            )
            path = gen.generate()
            results.append(("DOCX Shell Template", path))
        elif run_type == "xlsx":
            out = args.output_xlsx or os.path.join(
                args.output_dir,
                make_filename("TFL_TOC", __version__, ".xlsx"),
            )
            gen = XlsxTocGenerator(catalog, output_path=out)
            path = gen.generate()
            results.append(("XLSX Table of Contents", path))
        elif run_type == "sop":
            out = args.output_sop or os.path.join(
                args.output_dir,
                make_filename("TFL_Shell_SOP", __version__, ".docx"),
            )
            gen = DocxSopGenerator(output_path=out)
            path = gen.generate()
            results.append(("SOP Document", path))
        else:
            print(f"Unknown type: {run_type}")
            return 1

    for desc, path in results:
        print(f"  [{desc}] {path}")

    stats = catalog.summary_stats()
    print(f"\n  TFLs in catalog: {stats['total']}")
    print(f"  Tables: {stats['tables']} | Figures: {stats['figures']} "
          f"({stats['figures_generated']} generated) | Listings: {stats['listings']}")
    return 0


def cmd_list(args):
    catalog = build_catalog()
    items = catalog.all()
    if args.section:
        items = catalog.by_section(Section.from_number(args.section))
    if args.type:
        items = [i for i in items if i.tfl_type == TFLType(args.type)]
    if args.area != "all":
        area = _normalize_area(args.area)
        items = [i for i in items if area in i.therapeutic_areas]

    if not items:
        print("No TFLs match the specified filters.")
        return 0

    print(f"{'TFL ID':12s} {'Type':8s} {'Section':8s} {'Area':22s} {'Dataset':15s} Title")
    print("-" * 110)
    for item in items:
        areas = "+".join(item.therapeutic_areas)
        ds = item.dataset_source[:14] if item.dataset_source else "-"
        print(f"{item.id:12s} {item.tfl_type.value:8s} {item.section.number:8s} "
              f"{areas:22s} {ds:15s} {item.title}")

    print(f"\n  Total: {len(items)} TFL(s)")
    if not args.section:
        print("\n  Summary by Section:")
        summary = catalog.section_summary()
        for sec_num, counts in summary.items():
            print(f"    Section {sec_num} ({counts['title']}): "
                  f"{counts['total']} TFLs "
                  f"(T:{counts['tables']} F:{counts['figures']} L:{counts['listings']})")
    return 0


def cmd_validate(args):
    catalog = build_catalog()
    warnings = catalog.validate()
    if warnings:
        print(f"Validation found {len(warnings)} issue(s):")
        for w in warnings:
            print(f"  WARNING: {w}")
        return 1
    stats = catalog.summary_stats()
    print(f"Catalog validation passed. ({stats['total']} TFLs)")
    print(f"  Tables: {stats['tables']} | Figures: {stats['figures']} "
          f"({stats['figures_generated']} with matplotlib) | Listings: {stats['listings']}")
    print(f"  Oncology-only: {stats['oncology_only']} | "
          f"Non-Oncology-only: {stats['non_oncology_only']} | "
          f"General: {stats['general']}")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="tflshell",
        description=f"Clinical TFL Shell Template Generator v{__version__}",
    )
    parser.add_argument("--version", action="version", version=f"tflshell {__version__}")
    subparsers = parser.add_subparsers(dest="command")

    gen = subparsers.add_parser("generate", help="Generate TFL deliverables")
    gen.add_argument("--type", "-t", default="all",
                     choices=["docx", "xlsx", "sop", "all"])
    gen.add_argument("--area", "-a", default="all",
                     choices=["oncology", "non-oncology", "all"])
    gen.add_argument("--output-docx", "-d", default=None)
    gen.add_argument("--output-xlsx", "-x", default=None)
    gen.add_argument("--output-sop", "-s", default=None)
    gen.add_argument("--output-dir", "-o", default=DEFAULT_OUTPUT_DIR)
    gen.add_argument("--sponsor", default=None, help="Sponsor name override")
    gen.add_argument("--protocol", default=None, help="Protocol number override")
    gen.add_argument("--no-figures", action="store_true",
                     help="Disable figure generation")
    gen.set_defaults(func=cmd_generate)

    lst = subparsers.add_parser("list", help="List TFLs")
    lst.add_argument("--section", "-s", choices=["14.1", "14.2", "14.3", "14.4", "16.2"])
    lst.add_argument("--type", "-t", choices=["Table", "Figure", "Listing"])
    lst.add_argument("--area", "-a", default="all",
                     choices=["oncology", "non-oncology", "all"])
    lst.set_defaults(func=cmd_list)

    val = subparsers.add_parser("validate", help="Validate TFL catalog")
    val.set_defaults(func=cmd_validate)

    args = parser.parse_args(argv)

    if not args.command:
        parser.print_help()
        return 0

    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
