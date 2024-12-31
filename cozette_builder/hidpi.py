# Based on bdfscale by Philip Jones (https://github.com/philj56/bdfscale) under the MIT License; original license
# included below:
#
# MIT License
#
# Copyright (c) 2019 Philip Jones
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from io import StringIO
from typing import TextIO

# Lines that need all numbers scaled
scale_lines = [
    "SIZE",
    "FONTBOUNDINGBOX",
    "PIXEL_SIZE",
    "POINT_SIZE",
    "AVERAGE_WIDTH",
    "FONT_ASCENT",
    "FONT_DESCENT",
    "UNDERLINE_POSITION",
    "UNDERLINE_THICKNESS",
    "X_HEIGHT",
    "CAP_HEIGHT",
    "RAW_ASCENT",
    "RAW_DESCENT",
    "NORM_SPACE",
    "SUPERSCRIPT_",
    "SUBSCRIPT_",
    "FIGURE_WIDTH",
    "AVG_LOWERCASE_WIDTH",
    "AVG_UPPERCASE_WIDTH" "DWIDTH",
    "DWIDTH",
    "BBX",
    "QUAD_WIDTH",
]


def double_size(src: TextIO, out: TextIO):
    bitmap = False
    for line in src.readlines():
        if line.startswith("ENDCHAR"):
            bitmap = False
        elif bitmap:
            line = line.strip()
            pad = len(line) % 2
            line = line + "0" * pad
            size = len(line) * 2

            # Do the actual scaling
            binary = bin(int(line.strip(), 16))[2:]
            rescaled = "".join([x * 2 for x in binary])
            res = hex(int(rescaled, 2))[2:].upper()

            line = "0" * (size - len(res)) + res  # Pad out to desired length
            line = (line + "\n") * 2  # And correct number of lines
        elif any([line.startswith(x) for x in scale_lines]):
            words = line.split()
            for i, num in enumerate(words[1:]):
                words[i + 1] = str(int(num) * 2)
            line = " ".join(words) + "\n"
        elif line.startswith("SIZE "):
            words = line.strip().split()
            words[1] = str(int(words[1]) * 2)
            line = " ".join(words) + "\n"
        elif line.startswith("FONT "):
            xlfd = line[len("FONT ") :].strip().split("-")
            # PIXEL_SIZE
            xlfd[7] = f"{int(xlfd[7]) * 2}"
            # POINT_SIZE
            xlfd[8] = f"{int(xlfd[8]) * 2}"
            # AVERAGE_WIDTH
            xlfd[12] = f"{int(xlfd[12]) * 2}"
            line = "FONT " + "-".join(xlfd) + "\n"
        elif line.startswith("BITMAP"):
            bitmap = True
        if line.startswith("FAMILY_NAME"):
            out.write(line)
            continue
        out.write(line.replace("Cozette", "CozetteHiDpi"))
