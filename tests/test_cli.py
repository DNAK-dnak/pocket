from pocket.cli import build_parser


def test_compare_requires_reference():
    args = build_parser().parse_args(["compare", "take.wav", "--ref", "song.mp3"])
    assert args.command == "compare"
    assert args.ref == "song.mp3"
