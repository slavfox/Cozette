from pathlib import Path

from fontTools.fontBuilder import FontBuilder, _panoseDefaults  # type: ignore

from cozette_builder.bdffont import BdfFont

with (Path(__file__).resolve().parent.parent / "LICENSE").open() as f:
    LICENSE_TEXT = f.read()


def get_version():
    cozette_path = (
        Path(__file__).resolve().parent.parent / "Cozette" / "Cozette.sfd"
    )
    with cozette_path.open() as f:
        for line in f:
            if line.startswith("Version:"):
                _, v = line.split()
    return v


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

    def build(self, output_path: str):
        glyph_names = {
            k: glyph.meta("STARTCHAR")[0]
            for k, glyph in self.bdf.glyphs.items()
            if k >= 0
        }
        ascent = round(self.ascent * self.ppp)
        descent = round(self.descent * self.ppp)

        self.fb.setupGlyphOrder(list(glyph_names.values()))
        self.fb.setupCharacterMap(glyph_names)
        advance_widths = {
            name: int(self.bdf.glyphs[k].meta("SWIDTH")[0])
            for k, name in glyph_names.items()
        }
        family_name = "CozetteVector"
        style_name = "Regular"
        version = get_version()

        # scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=IWS-Chapter08
        namestrings = {
            "familyName": {"en": family_name},
            "styleName": {"en": style_name},
            "uniqueFontIdentifier": f"fontBuilder: {family_name}.{style_name}",
            "fullName": family_name,
            "psName": f"{family_name}-{style_name}",
            "version": f"Version {version}",
            "copyright": "(c) 2020 Slavfox",
            "manufacturer": "Slavfox",
            "designer": "Slavfox",
            "description": "Programming bitmap font optimized for coziness",
            "vendorURL": "https://github.com/slavfox",
            "designerURL": "https://github.com/slavfox",
            "licenseDescription": LICENSE_TEXT,
            "licenseInfoURL": "https://opensource.org/licenses/MIT",
            "sampleText": "A wizard’s job is to vex chumps quickly in fog.",
        }
        self.fb.setupGlyf(
            {
                name: self.bdf.glyphs[k].draw(self.ppp)
                for k, name in glyph_names.items()
            }
        )
        metrics = {
            name: (w, self.fb.font["glyf"][name].xMin)
            for name, w in advance_widths.items()
        }
        self.fb.setupHorizontalMetrics(metrics)
        self.fb.setupHorizontalHeader(ascent=ascent, descent=-descent)
        self.fb.setupNameTable(namestrings)
        self.fb.setupOS2(
            sTypoAscender=ascent,
            usWinAscent=ascent,
            usWinDescent=descent,
            panose={
                **_panoseDefaults,
                "bFamilyType": 2,  # Text and display
                "bProportion": 9,  # Monospace
            },
        )
        self.fb.setupPost(isFixedPitch=1)
        self.fb.save(output_path)
