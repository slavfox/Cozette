# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

Nothing!

## [1.4.0] - The `vim-airline` Update - 2020-02-15

### Added

Full support for vim-airline!

#### Glyphs

- У  **U+0423 CYRILLIC CAPITAL LETTER U**
- а  **U+0430 CYRILLIC SMALL LETTER A**
- б  **U+0431 CYRILLIC SMALL LETTER BE**
- ч  **U+0447 CYRILLIC SMALL LETTER CHE**
- ё  **U+0451 CYRILLIC SMALL LETTER IO** (copy of U+00EB LATIN SMALL LETTER E
  WITH DIAERESIS)
- ᚠ  **U+16A0 RUNIC LETTER FEHU FEOH FE F**
- ⁰  **U+2070 SUPERSCRIPT ZERO**
- ⁴  **U+2074 SUPERSCRIPT FOUR**
- ⁵  **U+2075 SUPERSCRIPT FIVE**
- ⁶  **U+2076 SUPERSCRIPT SIX**
- ⁷  **U+2077 SUPERSCRIPT SEVEN**
- ⁸  **U+2078 SUPERSCRIPT EIGHT**
- ⁹  **U+2079 SUPERSCRIPT NINE**
- ₁  **U+2081 SUBSCRIPT ONE**
- ∞  **U+221E INFINITY**
- ∥  **U+2225 PARALLEL TO**
- ∦  **U+2226 NOT PARALLEL TO**
- ⊝  **U+229D CIRCLED DASH**
- ⎇  **U+2387 ALTERNATIVE KEY SYMBOL** (the alt key symbol)
- ⏎  **U+23CE RETURN SYMBOL**
- ␊  **U+240A SYMBOL FOR LINE FEED**
- ␤  **U+2424 SYMBOL FOR NEWLINE**
- ▶  **U+25B6 BLACK RIGHT-POINTING TRIANGLE**
- ◀  **U+25C0 BLACK LEFT-POINTING TRIANGLE**
- ☰  **U+2630 TRIGRAM FOR HEAVEN** (often used for hamburger menus)
- ☱  **U+2631 TRIGRAM FOR LAKE**
- ☲  **U+2632 TRIGRAM FOR FIRE**
- ☳  **U+2633 TRIGRAM FOR THUNDER**
- ☴  **U+2634 TRIGRAM FOR WIND**
- ☵  **U+2635 TRIGRAM FOR WATER**
- ☶  **U+2636 TRIGRAM FOR MOUNTAIN**
- ☷  **U+2637 TRIGRAM FOR EARTH**
- ⭠  **U+2B60 LEFTWARDS TRIANGLE-HEADED ARROW**
- ⭡  **U+2B61 UPWARDS TRIANGLE-HEADED ARROW**
- ⭢  **U+2B62 RIGHTWARDS TRIANGLE-HEADED ARROW**
- ⭣  **U+2B63 DOWNWARDS TRIANGLE-HEADED ARROW**
- ⭤  **U+2B64 LEFT RIGHT TRIANGLE-HEADED ARROW**
- ⭥  **U+2B65 UP DOWN TRIANGLE-HEADED ARROW**
- ⭦  **U+2B66 NORTH WEST TRIANGLE-HEADED ARROW**
- ⭧  **U+2B67 NORTH EAST TRIANGLE-HEADED ARROW**
- ⭨  **U+2B68 SOUTH EAST TRIANGLE-HEADED ARROW**
- ⭩  **U+2B69 SOUTH WEST TRIANGLE-HEADED ARROW**
- ⮀  **U+2B80 LEFTWARDS TRIANGLE-HEADED ARROW OVER RIGHTWARDS TRIANGLE-HEADED
  ARROW**
- ⮁  **U+2B81 UPWARDS TRIANGLE-HEADED ARROW LEFTWARDS OF DOWNWARDS
  TRIANGLE-HEADED ARROW**
- ⮂  **U+2B82 RIGHTWARDS TRIANGLE-HEADED ARROW OVER LEFTWARDS TRIANGLE-HEADED
  ARROW**
- ⮃  **U+2B83 DOWNWARDS TRIANGLE-HEADED ARROW LEFTWARDS OF UPWARDS TRIANGLE-HEADED
  ARROW**
- ㏑  **U+33D1 SQUARE LN**
- Ꞩ  **U+A7A8 LATIN CAPITAL LETTER S WITH OBLIQUE STROKE**

#### Other

- `build.py scan` command to scan all the files in a given directory for non
  ASCII glyphs and list those that aren't included in Cozette (yet):
  
  ```
  $ python build.py scan -s ~/.vim/plugged/vim-airline-themes/
  All codepoints under /home/fox/.vim/plugged/vim-airline-themes already supported by Cozette.
  ```

- Now also generating a character map that includes the code points

### Changed

#### Glyphs

- Ξ **U+039E GREEK CAPITAL LETTER XI**: removed the "serifs" since some tools
  use it as an alternate hamburger menu icon 
- ╱ ╲ ╳  
  **U+2571 BOX DRAWINGS LIGHT DIAGONAL UPPER RIGHT TO LOWER LEFT**  
  **U+2572 BOX DRAWINGS LIGHT DIAGONAL UPPER LEFT TO LOWER RIGHT**  
  **U+2573 BOX DRAWINGS LIGHT DIAGONAL CROSS**  
  
  Tweaked to make them more symmetrical.
  
#### Other

- Tweaked image generation, changed to match the github readme colors
- Made README nicer, included a mention of the AUR package and the new charmap
  
## [1.3.0] - 2020-02-10

### Added

#### Glyphs

- Nerdfonts:
  -  **nf-custom-folder_open (U+E5FE)** 
  -  **nf-custom-cpp (U+E61D)**, C++ logo
  -  **nf-custom-c (U+E61E)**, C logo
  -  **nf-indent-line (U+E621)**, indentation guide
  -  **nf-custom-vim (U+E62B)**
  -  **nf-dev-visualstudio (U+E70C)**
  -  **nf-dev-terminal (U+E795)** (black `>_` symbol)
  -  **nf-dev-terminal_badge (U+E7A2)** (white `>_` symbol), also copied as 
    **nf-fa-terminal (U+F120)**
  -  **nf-dev-ruby (U+E739)**
  -  **nf-dev-ubuntu (U+E73A)**
  -  **nf-dev-php (U+E73D)**
  -  **nf-dev-markdown (U+E73E)**
  -  **nf-dev-erlang (U+E7AF)**
  -  **nf-dev-erlang (U+E7B1)**
  -  **nf-fa-h-square (U+F0FD)** \[My vim uses it for C headers\]
  - Copied some nf glyphs to code points that should be the same glyph (eg. 
     nf-dev-heroku U+E77B and nf-seti-heroku U+E607) 
  -  **nf-linux-archlinux (U+F303)**
  
- Four variations on a `+`:

  - ✙ **U+2719 OUTLINED GREEK CROSS**
  - ✚ **U+271A HEAVY GREEK CROSS**
  - ✛ **U+271B OPEN CENTRE CROSS**
  - ✜ **U+271C HEAVY OPEN CENTRE CROSS**

  These should come in handy for git prompts and the like.
  
#### Build scripts

- Automatic character map generation
- Automatic sample image generation
- True vector .ttf font building

### Changed

- Github Actions to use the new build scripts

#### Glyphs

- Repositioned some (Powerline and Devicons) icon glyphs so that they're
  vertically centered within the line instead of starting at the font baseline.
  This is mostly relevant for tall prompt icons like the git branch symbol,
  which now looks better in the context of a prompt.
- Made nf-dev-linux lose some weight to make it more recognizable as
  Tux.

---

## [1.2.0] - 2020-02-03

### Added

#### Glyphs

- ● **U+25CF BLACK CIRCLE** for git prompts
-  **nf-dev-linux (U+E712)** for vim statusbars on Linuces

#### Other

- Added notes on Ubuntu to the Installation section of the README

## [1.1.0] - 2020-02-02

### Added

#### Glyphs

- ⚡ **nf-oct-zap (U+26A1 HIGH VOLTAGE SIGN)** for term prompts
-  **nf-dev-apple (U+E711)** for vim statusbars on Macs

### Changed

- Tweaked some settings to hopefully make it work nicer on MacOS.

## [1.0.0] - 2020-02-02

Still broken on Windows.

### Added

#### Glyphs

- Box drawing (mostly)
- Braille
- nf-seti

[unreleased]: https://github.com/slavfox/Cozette/compare/v.1.4.0...HEAD
[1.4.0]: https://github.com/slavfox/Cozette/compare/v.1.3.0...v.1.4.0
[1.3.0]: https://github.com/slavfox/Cozette/compare/v.1.2.0...v.1.3.0
[1.2.0]: https://github.com/slavfox/Cozette/compare/v.1.1.0...v.1.2.0
[1.1.0]: https://github.com/slavfox/Cozette/compare/v.1.0.0...v.1.1.0
[1.0.0]: https://github.com/slavfox/Cozette/compare/v.0.1.2...v.1.0.0
