# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

Nothing!

## [1.3.0] - 2020-02-10

### Added

#### Glyphs

- Nerdfonts:
  - ****nf-custom-folder_open (U+E5FE)****
  - ****nf-custom-c (U+E61D)****, C logo
  - **nf-custom-cpp (U+E61E)**, C++ logo
  - **nf-indent-line (U+E621)**, indentation guide
  - **nf-custom-vim (U+E62B)**
  - **nf-dev-visualstudio (U+E70C)**
  - **nf-dev-terminal (U+E795)** (black `>_` symbol)
  - **nf-dev-terminal_badge (U+E7A2)** (white `>_` symbol), also copied as 
    **nf-fa-terminal (U+F120)**
  - **nf-dev-ruby (U+E739)**
  - **nf-dev-ubuntu (U+E73A)**
  - **nf-dev-php (U+E73D)**
  - **nf-dev-markdown (U+E73E)**
  - **nf-dev-erlang (U+E7AF)**
  - **nf-dev-erlang (U+E7B1)**
  - **nf-fa-h_square (U+F0FD)** \[My vim uses it for C headers\]
  - Copied some nf glyphs to code points that should be the same glyph (eg. 
    nf-dev-heroku U+E77B and nf-seti-heroku U+E607) 
  - **nf-linux-archlinux (U+F303)**
  
- Four variations on a `+`:

  - **U+2719 OUTLINED GREEK CROSS**
  - **U+271A HEAVY GREEK CROSS**
  - **U+271B OPEN CENTRE CROSS**
  - **U+271C HEAVY OPEN CENTRE CROSS**

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

- **U+25CF BLACK CIRCLE** for git prompts
- **nf-dev-linux (U+E712)** for vim statusbars on Linuces

#### Other

- Added notes on Ubuntu to the Installation section of the README

## [1.1.0] - 2020-02-02

### Added

#### Glyphs

- **nf-oct-zap (U+26A1 HIGH VOLTAGE SIGN)** for term prompts
- **nf-dev-apple (U+E711)** for vim statusbars on Macs

### Changed

- Tweaked some settings to hopefully make it work nicer on MacOS.

## [1.0.0] - 2020-02-02

Still broken on Windows.

### Added

#### Glyphs

- Box drawing (mostly)
- Braille
- nf-seti

[unreleased]: https://github.com/slavfox/Cozette/compare/v.1.3.0...HEAD
[1.3.0]: https://github.com/slavfox/Cozette/compare/v.1.2.0...v.1.3.0
[1.2.0]: https://github.com/slavfox/Cozette/compare/v.1.1.0...v.1.2.0
[1.1.0]: https://github.com/slavfox/Cozette/compare/v.1.0.0...v.1.1.0
[1.0.0]: https://github.com/slavfox/Cozette/compare/v.0.1.2...v.1.0.0
