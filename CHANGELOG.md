# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

#### Glyphs

- Four variations on a `+`:

  - U+2719 OUTLINED GREEK CROSS
  - U+271A HEAVY GREEK CROSS
  - U+271B OPEN CENTRE CROSS
  - U+271C HEAVY OPEN CENTRE CROSS

  These should come in handy for git prompts and the like.

### Fixed

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

- nf-dev-linux (U+E712) for vim statusbars on Linuces
- U+25CF BLACK CIRCLE for git prompts

#### Other

- Added notes on Ubuntu to the Installation section of the README

## [1.1.0] - 2020-02-02

### Added

#### Glyphs

- nf-dev-apple (U+E711) for vim statusbars on Macs
- nf-oct-zap (U+26A1 HIGH VOLTAGE SIGN) for term prompts

### Changed

- Tweaked some settings to hopefully make it work nicer on MacOS.

## [1.0.0] - 2020-02-02

Still broken on Windows.

### Added

#### Glyphs

- Box drawing (mostly)
- Braille
- nf-seti

[unreleased]: https://github.com/slavfox/Cozette/compare/v1.2.0...HEAD
[1.1.0]: https://github.com/slavfox/Cozette/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/slavfox/Cozette/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/slavfox/Cozette/compare/v0.1.2...v1.0.0
