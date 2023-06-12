import argparse
import subprocess
from dataclasses import dataclass
from pathlib import Path
from shlex import quote
from shutil import rmtree
from typing import Optional, Sequence, cast

import crayons  # type: ignore

from cozette_builder.changeloggen import get_changelog, get_last_ver
from cozette_builder.hidpi import double_size
from cozette_builder.imagegen import (
    add_margins,
    read_sample,
    save_charlist,
    save_sample,
)
from cozette_builder.scanner import (
    find_missing_codepoints,
    print_codepoints_for_changelog,
    scan_for_codepoints,
)

REPO_ROOT = Path(__file__).resolve().parent
BUILD_DIR = REPO_ROOT / "build"
FONTNAME = "Cozette"
SFDPATH = REPO_ROOT / "Cozette" / "Cozette.sfd"


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


def save_images():
    print(crayons.yellow("Saving character map"))
    save_charlist(FONTNAME, SFDPATH, REPO_ROOT / "img")

    print(crayons.yellow("Saving sample image"))
    save_sample(
        FONTNAME,
        read_sample(REPO_ROOT / "img" / "sample.txt"),
        REPO_ROOT / "img" / "sample.png",
    )
    add_margins(REPO_ROOT / "img" / "sample.png")


def fontforge(open: Path, generate: Sequence[Generate]):
    BUILD_DIR.mkdir(exist_ok=True)
    script = "; ".join(
        [
            f'Open("{open}")',
            # 'RenameGlyphs("AGL with PUA")',
            # 'Reencode("unicode")',
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
            Generate("cozette.", "psf"),
            Generate("cozette.", "fnt"),
            Generate("cozette.dfont", "sbit"),
        ],
    )
    rename_single(BUILD_DIR, "*.fnt", "cozette.fnt")
    return rename_single(BUILD_DIR, "*.bdf", "cozette.bdf")


def fix_ttf(ttfpath: Path, name: str):
    print(crayons.yellow(f"Generating TTF for {name}..."))
    version = "1.0"
    with SFDPATH.open() as f:
        for line in f.readlines():
            if line.startswith("Version "):
                version = line.split()[1]
                break
    script = "; ".join(
        [
            f'Open("{ttfpath}")',
            "SelectWorthOutputting()",
            "RemoveOverlap()",
            "CorrectDirection()",
            "ScaleToEm(2048)",
            'RenameGlyphs("AGL with PUA")',
            'Reencode("unicode")',
            f'SetTTFName(0x409, 3, "{name}")',
            f'SetTTFName(0x409, 5, "{version}")',
            f'SetTTFName(0x409, 8, "Slavfox")',
            f'SetTTFName(0x409, 9, "Slavfox")',
            f'SetTTFName(0x409, 11, "https://github.com/slavfox/Cozette")',
            f'SetTTFName(0x409, 13, "MIT")',
            'SetTTFName(0x409, 14, "https://opensource.org/licenses/MIT")',
            f'Generate("{name}.dfont")',
            f'Generate("{name}.otf")',
            f'Generate("{name}.ttf")',
        ]
    )

    # No idea why this doesn't work without shell=True
    subprocess.run(
        [f"fontforge -lang ff -c {quote(script)}"],
        cwd=BUILD_DIR,
        shell=True,
        check=True,
    )
    ttfpath.unlink()


def make_hidpi(bdf_path: Path, out_path: Path):
    print(crayons.yellow("Generating hidpi font..."))
    with bdf_path.open() as i:
        with out_path.open("w") as o:
            double_size(i, o)
    print(crayons.green("Done!"))


def gen_variants(bdf_path: Path):
    hidpi_path = BUILD_DIR / "cozette_hidpi.bdf"

    def bnp_invoc_ttf(name: str, format: str):
        return [
            REPO_ROOT / "bitsnpicas.sh",
            "convertbitmap",
            "-f",
            format,
            "-o",
            BUILD_DIR / f"{name}_tmp.{format}",
            "-s",
            "Cozette",
            "-r",
            name,
            "-T",
        ]

    subprocess.run(
        [
            BUILD_DIR.parent / "bitsnpicas.sh",
            "convertbitmap",
            "-f",
            "psf",
            "-o",
            BUILD_DIR / f"cozette.psf",
            bdf_path,
        ],
        check=True,
    )
    subprocess.run(
        bnp_invoc_ttf("CozetteVector", "ttf") + [SFDPATH], check=True
    )
    subprocess.run(
        bnp_invoc_ttf("CozetteVectorBold", "ttf") + ["-b", SFDPATH],
        check=True,
    )
    print(crayons.yellow("Fixing TTF variants..."))
    fix_ttf(BUILD_DIR / "CozetteVector_tmp.ttf", "CozetteVector")
    fix_ttf(BUILD_DIR / "CozetteVectorBold_tmp.ttf", "CozetteVectorBold")
    print(crayons.green("Done!"))
    make_hidpi(bdf_path, hidpi_path)
    fontforge(
        open=hidpi_path,
        generate=[
            Generate(f"{hidpi_path.stem}.", "otb"),
            Generate(f"{hidpi_path.stem}.", "fnt"),
            Generate(f"{hidpi_path.stem}.dfont", "sbit"),
        ],
    )
    rename_single(BUILD_DIR, "*-26.fnt", "cozette_hidpi.fnt")
    subprocess.run(
        [
            BUILD_DIR.parent / "bitsnpicas.sh",
            "convertbitmap",
            "-f",
            "psf",
            "-o",
            hidpi_path.with_suffix(".psf"),
            hidpi_path,
        ],
        check=True,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="action")
    images = subparsers.add_parser("images")
    changelog = subparsers.add_parser("changelog")
    fonts = subparsers.add_parser("fonts")
    scan = subparsers.add_parser("scan")
    # noinspection PyTypeChecker
    scan.add_argument("path", type=Path)  # type: ignore
    scan.add_argument("-s", "--print-source-files", action="store_true")
    scan.add_argument("-r", "--reverse", action="store_true")
    args = parser.parse_args()
    if args.action == "scan":
        missing_codepoints = find_missing_codepoints(
            SFDPATH,
            scan_for_codepoints(args.path),
        )
        if missing_codepoints:
            print_codepoints_for_changelog(
                missing_codepoints,
                print_source_files=args.print_source_files,
                reverse=args.reverse,
            )
        else:
            print(
                crayons.green(
                    f"All codepoints under {args.path} already "
                    f"supported by Cozette."
                )
            )
    if args.action == "images":
        print(crayons.blue("Saving sample images..."))
        save_images()
        print(crayons.green("Done!", bold=True))
    elif args.action == "fonts":
        rmtree(BUILD_DIR, ignore_errors=True)
        BUILD_DIR.mkdir(exist_ok=True)
        print(crayons.blue("Building bitmap formats..."))
        bdf_path = gen_bitmap_formats()
        print(crayons.green("Done!", bold=True))
        print(crayons.blue("Building variants..."))
        gen_variants(bdf_path)
        print(crayons.green("Done!", bold=True))
    elif args.action == "changelog":
        get_changelog()
    else:
        parser.print_usage()
