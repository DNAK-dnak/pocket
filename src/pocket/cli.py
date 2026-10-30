"""Command-line entry point."""

import argparse

from pocket import __version__


def build_parser():
    parser = argparse.ArgumentParser(
        prog="pocket",
        description="Feel and timing analysis for contemporary pianists.",
    )
    parser.add_argument("--version", action="version", version=f"pocket {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    analyze = sub.add_parser("analyze", help="feel report for your recording")
    analyze.add_argument("take", help="path to your recording")

    reference = sub.add_parser("reference", help="profile a reference track")
    reference.add_argument("track", help="path to the reference track")

    compare = sub.add_parser("compare", help="your feel against a reference")
    compare.add_argument("take", help="path to your recording")
    compare.add_argument("--ref", required=True, help="path to the reference track")

    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    print(f"'{args.command}' is not implemented yet. See the roadmap in README.md.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
