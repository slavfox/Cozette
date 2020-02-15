import os
import subprocess
import tempfile
import argparse
from dataclasses import dataclass
from pathlib import Path
from shlex import quote
from shutil import copy, rmtree
from typing import Optional, Sequence, cast

import crayons  # type: ignore

from cozette_builder.imagegen import (
    read_sample,
    save_charlist,
    save_sample,
    add_margins,
)
from cozette_builder.ttfbuilder import TTFBuilder
from cozette_builder.scanner import (
    scan_for_codepoints,
    print_codepoints_for_changelog,
    find_missing_codepoints,
)

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
        save_charlist(FONTNAME, bdfpath, REPO_ROOT / "img")

        print(crayons.yellow("Saving sample image"))
        save_sample(
            FONTNAME,
            read_sample(REPO_ROOT / "img" / "sample.txt"),
            REPO_ROOT / "img" / "sample.png",
        )
        subprocess.run(["xset", "-fp", tmpdirname])
    subprocess.run(["xset", "fp", "rehash"])
    add_margins(REPO_ROOT / "img" / "sample.png")


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


def gen_bitmap_formats() -> Path:
    fontforge(
        open=REPO_ROOT / "Cozette" / "Cozette.sfd",
        generate=[
            Generate("cozette.", bitmap_fmt="bdf"),
            Generate("cozette.", "otb"),
            Generate("cozette.", "fnt"),
            Generate("cozette_bitmap.ttf", "otb"),
            Generate("cozette_bitmap.dfont", "sbit"),
        ],
    )
    rename_single(BUILD_DIR, "*.fnt", "cozette.fnt")
    bdfpath = rename_single(BUILD_DIR, "*.bdf", "cozette.bdf")
    return bdfpath


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
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="action")
    images = subparsers.add_parser("images")
    fonts = subparsers.add_parser("fonts")
    scan = subparsers.add_parser("scan")
    # noinspection PyTypeChecker
    scan.add_argument("path", type=Path)  # type: ignore
    scan.add_argument("-s", "--print-source-files", action="store_true")
    args = parser.parse_args()
    if args.action == "scan":
        missing_codepoints = find_missing_codepoints(
            REPO_ROOT / "Cozette" / "Cozette.sfd",
            scan_for_codepoints(args.path),
        )
        if missing_codepoints:
            print_codepoints_for_changelog(
                missing_codepoints, print_source_files=args.print_source_files
            )
        else:
            print(
                crayons.green(
                    f"All codepoints under {args.path} already "
                    f"supported by Cozette."
                )
            )
    elif args.action in ("images", "fonts"):
        rmtree(BUILD_DIR, ignore_errors=True)
        BUILD_DIR.mkdir(exist_ok=True)
        os.chdir(BUILD_DIR)
        print(crayons.blue("Building bitmap formats..."))
        bdfpath = gen_bitmap_formats()
        print(crayons.green("Done!", bold=True))
        print(crayons.green("Done!", bold=True))
        if args.action == "images":
            print(crayons.blue("Saving sample images..."))
            save_images(bdfpath)
            print(crayons.green("Done!", bold=True))
        else:
            print(crayons.blue("Generating TTF..."))
            ttfbuilder = TTFBuilder.from_bdf_path(bdfpath)
            ttfbuilder.build("cozette-tmp.ttf")
            print(crayons.green("Done!", bold=True))
            print(crayons.blue("Fixing TTF..."))
            fix_ttf(Path("cozette-tmp.ttf"))
            print(crayons.green("Done!", bold=True))
    else:
        parser.print_usage()
