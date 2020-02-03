import subprocess
from typing import Tuple, Dict, Optional
from shlex import quote
from pathlib import Path
from cozette_builder.bdf.bdffont import BdfFont
import textwrap
import tempfile

Color = Tuple[int, int, int]


def hex_to_rgb(color: str) -> Color:
    h = int(color, 16)
    return h >> 16, (h >> 8) & 0x00FF, h & 0x0000FF


Palette = Dict[str, Optional[Color]]


default_palette: Palette = dict(
    fg=hex_to_rgb("feffff"),
    bg=hex_to_rgb("2d2b33"),
    black=hex_to_rgb("383640"),
    red=hex_to_rgb("a09ebb"),
    green=hex_to_rgb("92b6b1"),
    yellow=hex_to_rgb("edaf97"),
    blue=hex_to_rgb("8789c0"),
    magenta=hex_to_rgb("e47b66"),
    cyan=hex_to_rgb("6b9080"),
    white=hex_to_rgb("969a97"),
    nc=None,
)

# Todo: rewrite this to use files instead of a string
def save_sample(
    font: str,
    sample: str,
    output_path: Path,
    fgcolor: str = "#abb2bf",
    bgcolor: str = "#282c34",
    palette: Palette = None,
):
    if palette is None:
        palette = default_palette
    colored, stripped = colored_and_stripped_text(sample, palette)

    lines = stripped.splitlines()
    h, w = len(lines), max(len(line) for line in lines)
    with tempfile.NamedTemporaryFile("w", delete=False) as f:
        f.write(colored)
        fp = f.name
    cmd = quote(
        f"tput civis &&"
        f"cat {fp} && sleep 0 && "
        f"import -window $WINDOWID {output_path}"
    )
    subprocess.run(
        [
            "xterm",
            "-fg",
            fgcolor,
            "-bg",
            bgcolor,
            "-fa",
            font,
            "-geometry",
            f"{w}x{h}",
            "-dc",
            "-e",
            f"bash -c {cmd}",
        ],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    Path(fp).unlink()


def color_escape_seq(color: Color = None):
    if color is None:
        return f"\033[38;0m"
    return f"\033[38;2;{color[0]};{color[1]};{color[2]}m"


def colored_and_stripped_text(text: str, palette: Palette) -> Tuple[str, str]:
    colored_text = text
    stripped_text = text
    for color in palette.keys():
        # The PyCharm MyPy plugin throws a fit at `palette.get(color)` because
        # it doesn't know that palette.get returns an Optional[Color], PyCharm
        # itself throws a fit here because of
        # https://youtrack.jetbrains.com/issue/PY-40439, and it sometimes
        # forgets that `palette` has a `.get` method, so ignore all those
        # warnings:
        # noinspection Mypy, PyTypedDict, PyUnresolvedReferences
        colored_text = colored_text.replace(
            f"${color.upper()}$", color_escape_seq(palette[color])
        )
        stripped_text = stripped_text.replace(f"${color.upper()}$", "")
    return colored_text, stripped_text


# Todo: write a fill() that ignores character codes


def save_charlist(bdf_font: Path, output_path: Path):
    with bdf_font.open() as f:
        bdf = BdfFont.from_bdf(f)
    save_sample(
        "Clozette",
        textwrap.fill(
            "".join(
                chr(c)
                for c in bdf.codepoints
                if c >= 32
                and c
                not in (
                    127,
                    # dumb as shit workaround for a weird bug
                    0x26A1,
                )
            )
        ),
        output_path,
    )
