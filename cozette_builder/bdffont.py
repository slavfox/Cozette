from __future__ import annotations

from typing import (
    Dict,
    Iterable,
    List,
    Literal,
    NamedTuple,
    TextIO,
    Tuple,
    Union,
)

import numpy as np  # type: ignore
from fontTools.pens.ttGlyphPen import TTGlyphPen  # type: ignore

Bit = Union[Literal[1], Literal[0]]


class BBX(NamedTuple):
    w: int
    h: int
    x: int
    y: int


class BdfGlyph:
    def __init__(self, bits: np.array, meta: Dict[str, str]):

        self.bbx = bbx = BBX(*[int(s) for s in meta["BBX"].split()])
        # this is probably wrong
        self.bits: np.array = bits[0 : bbx.h, 0 : bbx.w]
        self.metadata = meta

    @classmethod
    def from_str(cls, s: str, meta: Dict[str, str]) -> BdfGlyph:
        return cls.from_iterable((int(l, 16) for l in s.splitlines()), meta)

    @classmethod
    def from_iterable(
        cls, values: Iterable[int], meta: Dict[str, str]
    ) -> BdfGlyph:
        return BdfGlyph(
            np.unpackbits(
                np.array([[v] for v in values], dtype=np.uint8), axis=1
            ),
            meta=meta,
        )

    def __str__(self) -> str:
        return "\n".join(
            "".join("#" if ch else " " for ch in line) for line in self.bits
        )

    def draw(self, ppp: float):
        pen = TTGlyphPen(None)
        for y, row in enumerate(reversed(self.bits)):
            for x, col in enumerate(row):
                if col:
                    pen.moveTo(
                        ((x + self.bbx.x) * ppp, (y + self.bbx.y) * ppp)
                    )
                    pen.lineTo(
                        ((x + self.bbx.x + 1) * ppp, (y + self.bbx.y) * ppp)
                    )
                    pen.lineTo(
                        (
                            (x + self.bbx.x + 1) * ppp,
                            (y + self.bbx.y + 1) * ppp,
                        )
                    )
                    pen.lineTo(
                        ((x + self.bbx.x) * ppp, (y + self.bbx.y + 1) * ppp)
                    )
                    pen.lineTo(
                        ((x + self.bbx.x) * ppp, (y + self.bbx.y) * ppp)
                    )
                    pen.closePath()
        return pen.glyph()

    def meta(self, k) -> List[str]:
        return self.metadata[k].strip('"').strip().split()


def parse_char(bdfstream: TextIO) -> Tuple[Dict[str, str], List[int]]:
    specs = {}
    while not (line := bdfstream.readline()).startswith("BITMAP"):
        parts = line.split(maxsplit=1)
        specs[parts[0]] = parts[1].strip()
    bitmap = []
    while not (line := bdfstream.readline()).startswith("ENDCHAR"):
        bitmap.append(int(line.strip(), 16))
    return specs, bitmap


class BdfFont:
    def __init__(self, metadata: Dict[str, str], glyphs: Dict[int, BdfGlyph]):
        self.metadata: Dict[str, str] = metadata
        self.glyphs: Dict[int, BdfGlyph] = glyphs

    @classmethod
    def from_bdf(cls, bdfstream: TextIO):
        metadata = {}
        while not (line := bdfstream.readline()).startswith("CHARS "):
            try:
                k, val = line.split(maxsplit=1)
                metadata[k] = val.strip()
            except ValueError:
                pass
        glyphs = {}
        for i in range(int(line.split()[1])):
            meta, char = parse_char(bdfstream)
            glyphs[int(meta["ENCODING"])] = BdfGlyph.from_iterable(char, meta)
        return cls(metadata, glyphs)

    @property
    def codepoints(self) -> Tuple[int, ...]:
        return tuple(self.glyphs.keys())

    @property
    def str_codepoints(self) -> Tuple[str, ...]:
        return tuple(f"U+{i:X}" for i in self.glyphs)

    def meta(self, k) -> List[str]:
        return self.metadata[k].strip('"').strip().split()
