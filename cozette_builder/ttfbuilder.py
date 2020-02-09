from pathlib import Path
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from cozette_builder.bdffont import BdfFont, BdfGlyph

class TTFBuilder:
    @classmethod
    def from_bdf_path(cls, path: Path):
        with path.open() as f:
            bdf = BdfFont.from_bdf(f)
        return cls(bdf)

    def __init__(self, bdf: BdfFont):
        self.bdf = bdf
        upm = 1000
        self.fb = FontBuilder(unitsPerEm=upm)
        self.ppp = upm / int(self.bdf.meta("SIZE")[0])
        w, h, startx, starty = self.bdf.meta("FONTBOUNDINGBOX")
        self.ascent = int(self.bdf.meta("FONT_ASCENT")[0])
        self.descent = int(self.bdf.meta("FONT_DESCENT")[0])
        self.w = int(w)
        self.h = int(h)
        self.startx = int(startx)
        self.starty = int(starty)

    def build(self, output_path: Path):
        glyph_names = {
            k: glyph.meta("STARTCHAR")[0] for k, glyph in
            self.bdf.glyphs.items()
        }
        ascent = round(self.ascent * self.ppp)
        descent = round(self.descent * self.ppp)

        self.fb.setupGlyphOrder(list(glyph_names.values()))
        self.fb.setupCharacterMap(glyph_names)
        advance_widths = {
            name: 700 for name in glyph_names.values()
        }
        # copied from fontbuilder for now
        familyName = "HelloTestFont"
        styleName = "TotallyNormal"
        version = "0.1"

        nameStrings = dict(
            familyName=dict(en=familyName, nl="HalloTestFont"),
            styleName=dict(en=styleName, nl="TotaalNormaal"),
            uniqueFontIdentifier="fontBuilder: " + familyName + "." + styleName,
            fullName=familyName + "-" + styleName,
            psName=familyName + "-" + styleName,
            version="Version " + version,
        )
        self.fb.setupGlyf(
            {name: self.bdf.glyphs[k].draw(self.ppp) for k, name in
             glyph_names.items()}
        )
        metrics = {}
        glyphTable = self.fb.font["glyf"]
        for name in glyph_names.values():
            metrics[name] = (700, glyphTable[name].xMin)
        self.fb.setupHorizontalMetrics(metrics)
        self.fb.setupHorizontalHeader(ascent=ascent, descent=-descent)
        self.fb.setupNameTable(nameStrings)
        self.fb.setupOS2(sTypoAscender=ascent, usWinAscent=ascent,
                    usWinDescent=descent)
        self.fb.setupPost()
        self.fb.save(str(output_path))



