import os
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from shlex import quote
from shutil import copy
from typing import Optional, Sequence, cast

import crayons  # type: ignore

from cozette_builder.imagegen import read_sample, save_charlist, save_sample
from cozette_builder.ttfbuilder import TTFBuilder

REPO_ROOT = Path(__file__).resolve().parent
BUILD_DIR = REPO_ROOT / "build"
FONTNAME = "Cozette"


@dataclass
class Generate:
    filename: str
    bitmap_fmt: Optional[str] = None

    def __str__(self):
        return (
            f'Generate("{self.filename}", "{self.bitmap_fmt}")'
            if self.bitmap_fmt
            else f'Generate("{self.filename}")'
        )


def save_images(bdfpath):
    with tempfile.TemporaryDirectory() as tmpdirname:
        print(crayons.yellow("Making tmp fontdir"))
        tmpdirpath = Path(tmpdirname)
        copy(bdfpath, tmpdirname)
        subprocess.run(["mkfontdir", tmpdirname])
        subprocess.run(["xset", "+fp", tmpdirname])
        subprocess.run(["xset", "fp", "rehash"])

        print(crayons.yellow("Saving character map"))
        save_charlist(FONTNAME, bdfpath, REPO_ROOT / "img" / "characters.png")

        print(crayons.yellow("Saving sample image"))
        save_sample(
            FONTNAME,
            read_sample(REPO_ROOT / "img" / "sample.txt"),
            REPO_ROOT / "img" / "sample.png",
        )
        subprocess.run(["xset", "-fp", tmpdirname])
    subprocess.run(["xset", "fp", "rehash"])


def fontforge(open: Path, generate: Sequence[Generate]):
    BUILD_DIR.mkdir(exist_ok=True)
    script = "; ".join(
        [
            f'Open("{open}")',
            'RenameGlyphs("AGL with PUA")',
            'Reencode("unicode")',
        ]
        + [str(gen) for gen in generate]
    )
    # No idea why this doesn't work without shell=True
    subprocess.run(
        [f"fontforge -lang ff -c {quote(script)}"], cwd=BUILD_DIR, shell=True
    )


def rename_single(dir: Path, pattern: str, newname: str) -> Path:
    return cast(Path, next(dir.glob(pattern)).rename(dir / newname))


def mkbdf() -> Path:
    print()
    fontforge(
        open=REPO_ROOT / "Cozette" / "Cozette.sfd",
        generate=[Generate("cozette.", bitmap_fmt="bdf")],
    )
    bdfpath = rename_single(BUILD_DIR, "*.bdf", "cozette.bdf")
    return bdfpath


def gen_bitmap_formats(bdfpath: Path):
    fontforge(
        open=bdfpath,
        generate=[
            Generate("cozette.", "otb"),
            Generate("cozette.", "fnt"),
            Generate("cozette_bitmap.ttf", "otb"),
            Generate("cozette_bitmap.dfont", "sbit"),
        ],
    )
    rename_single(BUILD_DIR, "*.fnt", "cozette.fnt")


def fix_ttf(ttfpath: Path):
    outname = "CozetteVector"
    script = "; ".join(
        [
            f'Open("{ttfpath}")',
            "SelectWorthOutputting()",
            "RemoveOverlap()",
            "CorrectDirection()",
            "Simplify()",
            "Simplify(-1, 1.02)",
            'RenameGlyphs("AGL with PUA")',
            'Reencode("unicode")',
            f'Generate("{outname}.dfont")',
            f'Generate("{outname}.otf.dfont")',
            f'Generate("{outname}.otf")',
            "ScaleToEm(1024)",
            f'Generate("{outname}.ttf")',
        ]
    )

    # No idea why this doesn't work without shell=True
    subprocess.run(
        [f"fontforge -lang ff -c {quote(script)}"], cwd=BUILD_DIR, shell=True
    )
    ttfpath.unlink()


if __name__ == "__main__":
    BUILD_DIR.mkdir(exist_ok=True)
    os.chdir(BUILD_DIR)
    print(crayons.blue("Building .bdf..."))
    bdfpath = mkbdf()
    print(crayons.green("Done!", bold=True))
    print(crayons.blue("Building bitmap formats..."))
    gen_bitmap_formats(bdfpath)
    print(crayons.green("Done!", bold=True))
    print(crayons.blue("Saving sample images..."))
    save_images(bdfpath)
    print(crayons.green("Done!", bold=True))
    print(crayons.blue("Generating TTF..."))
    ttfbuilder = TTFBuilder.from_bdf_path(bdfpath)
    ttfbuilder.build("cozette-tmp.ttf")
    print(crayons.green("Done!", bold=True))
    print(crayons.blue("Fixing TTF..."))
    fix_ttf(Path("cozette-tmp.ttf"))
    print(crayons.green("Done!", bold=True))
