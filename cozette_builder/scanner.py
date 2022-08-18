import re
from pathlib import Path
from typing import Dict, Iterable, List, Set
from unicodedata import name as uniname, east_asian_width as eaw

UESCAPE = re.compile(r"\\[uU]([0-9A-Fa-f]{4,5})")


def scan_file_for_nonascii(path: Path) -> Set[int]:
    with path.open() as f:
        try:
            src = f.read()
        except UnicodeDecodeError:
            return set()
        nonascii = {codepoint for c in set(src) if (codepoint := ord(c)) > 127}
        escapes = UESCAPE.finditer(src)
        nonascii |= {int(esc.group(1), 16) for esc in escapes}
        return nonascii


# noinspection PyShadowingBuiltins
def scan_for_codepoints(dir: Path) -> Dict[int, List[Path]]:
    if dir.is_file():
        return {cp: [dir] for cp in scan_file_for_nonascii(dir)}
    non_ascii_codepoints: Dict[int, List[Path]] = {}
    for path in dir.glob("**/*"):
        if path.is_file():
            for cp in scan_file_for_nonascii(path):
                non_ascii_codepoints.setdefault(cp, []).append(path)
    return non_ascii_codepoints


def print_codepoints_for_changelog(
    codepoints: Dict[int, List[Path]], print_source_files=False, reverse=False
) -> None:
    for cp in sorted(codepoints, reverse=reverse):
        ch = chr(cp)
        try:
            name = uniname(ch).strip()
        except ValueError:
            name = ""
        if name:
            if "VARIATION SELECTOR" in name:
                continue
            name = " " + name
        print(f"**{ch} U+{cp:04X}{name}** {eaw(ch)}", end="")
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
