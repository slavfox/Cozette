import subprocess
from typing import Tuple, Dict, Optional, NamedTuple
from shlex import quote
from pathlib import Path
from unicodedata import east_asian_width as charwidth
from cozette_builder.bdf.bdffont import BdfFont
import platform
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


class Sample(NamedTuple):
    text: str
    width: int
    height: int


def wrap_text(src: str, width=79) -> Sample:
    sample_h = 1
    running_w = 0
    idx = 0
    linebreaks = []
    while idx < len(src):
        if running_w >= width:
            linebreaks.append(idx - 1)
            running_w = 0
            sample_h += 1
        if any(
            (h := f"${color}$") == src[idx : len(h)]
            for color in default_palette.keys()
        ):
            idx += len(h)
        else:
            running_w += 1 if charwidth(src[idx]) != "W" else 2
            idx += 1
    for idx in reversed(linebreaks):
        src = src[:idx] + "\n" + src[idx:]
    return Sample(src, width, sample_h)


def read_sample(src_path: Path) -> Sample:
    with src_path.open() as f:
        src = f.read()
    stripped = src
    for color in default_palette.keys():
        stripped = stripped.replace(f"${color.upper()}$", "")
    lines = stripped.splitlines()
    h, w = len(lines), max(len(line) for line in lines)
    return Sample(src, w, h)


# Todo: rewrite this to use files instead of a string
def save_sample(
    font: str,
    sample: Sample,
    output_path: Path,
    fgcolor: str = "#abb2bf",
    bgcolor: str = "#282c34",
    palette: Palette = None,
):
    if palette is None:
        palette = default_palette
    colored = color_text(sample.text, palette)
    print(colored)
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
            f"{sample.width}x{sample.height}",
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


def color_text(text: str, palette: Palette) -> str:
    colored_text = text
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
    return colored_text


def save_charlist(bdf_font: Path, output_path: Path):
    with bdf_font.open() as f:
        bdf = BdfFont.from_bdf(f)
    save_sample(
        "Clozette",
        wrap_text(
            "".join(
                chr(c) for c in bdf.codepoints if c >= 32 and c not in (127,)
            )
        ),
        output_path,
    )
