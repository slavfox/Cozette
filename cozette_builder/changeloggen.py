import re
from pathlib import Path
from unicodedata import name

from git import Repo

REPO_ROOT = Path(__file__).parent.parent
COZETTE_SFD = REPO_ROOT / "Cozette" / "Cozette.sfd"


def get_last_ver():
    repo = Repo(REPO_ROOT)
    return sorted(repo.tags, key=lambda tag: tag.commit.committed_date)[-1]


def get_last_cozette_sfd() -> str:
    return (
        get_last_ver()
        .commit.tree["Cozette/Cozette.sfd"]
        .data_stream.read()
        .decode("utf-8")
    )


char_regex = re.compile(
    r"BDFChar: (-?\d+) (-?\d+) (-?\d+) (-?\d+) (-?\d+) (-?\d+) (-?\d+)"
)


def get_codepoints(cozette_sfd: str):
    codepoints = {}
    current_codepoint = None
    for line in cozette_sfd.splitlines():
        if current_codepoint:
            codepoints[current_codepoint] = line
            current_codepoint = None
        elif match := char_regex.match(line):
            current_codepoint = int(match.group(2))
    return codepoints


def print_codepoint(codepoint):
    try:
        chrname = " " + name(chr(codepoint))
    except ValueError:
        chrname = ""
    print(f"- {chr(codepoint)} (U+{codepoint:04X}{chrname})")


def get_changelog():
    previous_codepoints = get_codepoints(get_last_cozette_sfd())
    with COZETTE_SFD.open() as f:
        current_codepoints = get_codepoints(f.read())

    print(
        f"Changelog since {get_last_ver()}: {len(current_codepoints)} glyphs found"
    )
    added = set(current_codepoints) - set(previous_codepoints)
    removed = set(previous_codepoints) - set(current_codepoints)
    changed = set()
    for k, v in current_codepoints.items():
        if k in previous_codepoints and previous_codepoints[k] != v:
            changed.add(k)

    if added:
        print("### Added\n")
        for codepoint in sorted(added):
            print_codepoint(codepoint)
        print("")

    if changed:
        print("### Changed\n")
        for codepoint in sorted(changed):
            print_codepoint(codepoint)
        print("")

    if removed:
        print("### Removed\n")
        for codepoint in sorted(removed):
            print_codepoint(codepoint)
        print("")
