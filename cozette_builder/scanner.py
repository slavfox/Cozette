from typing import Set, Dict, Iterable, List
from pathlib import Path
from unicodedata import name as uniname


def scan_file_for_nonascii(path: Path) -> Set[int]:
    with path.open() as f:
        try:
            src = f.read()
        except UnicodeDecodeError:
            return set()
        else:
            return {codepoint for c in set(src) if (codepoint := ord(c)) > 127}


# noinspection PyShadowingBuiltins
def scan_for_codepoints(dir: Path) -> Dict[int, List[Path]]:
    non_ascii_codepoints: Dict[int, List[Path]] = {}
    for path in dir.glob("**/*"):
        if path.is_file():
            for cp in scan_file_for_nonascii(path):
                non_ascii_codepoints.setdefault(cp, []).append(path)
    return non_ascii_codepoints


def print_codepoints_for_changelog(
    codepoints: Dict[int, List[Path]], print_source_files=False
) -> None:
    for cp in sorted(codepoints):
        ch = chr(cp)
        try:
            name = uniname(ch)
        except ValueError:
            name = ""
        print(f"**{ch} U+{cp:04X} {name}**", end="")
        if print_source_files:
            print(f": {' '.join(str(p) for p in codepoints[cp])}")
        else:
            print("\n", end="")


def find_missing_codepoints(
    sfdpath: Path, codepoints: Dict[int, List[Path]]
) -> Dict[int, List[Path]]:
    with sfdpath.open() as sfd:
        defined = set(
            int(line.split()[2])
            for line in sfd.readlines()
            if line.startswith("BDFChar: ")
        )
    return {cp: paths for cp, paths in codepoints.items() if cp not in defined}
