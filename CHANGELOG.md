# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog], and this project adheres to
[Semantic Versioning].

## [Unreleased]

Nothing!

## [1.8.0]
### Added
#### Glyphs
- [Pomicons](https://github.com/gabrielelana/pomicons)

## [1.7.2]
### Changed
- Bumped version number, since I accidentally released 1.7.0 again as 1.7.1.

## [1.7.1]
### Added
- U+20BD RUBLE SIGN ₽

## [1.7.0]
### Added
- U+263A WHITE SMILING FACE ☺
- U+2669 QUARTER NOTE ♩
- U+266A EIGHTH NOTE ♪
- U+266B BEAMED EIGHTH NOTES ♫
- U+266C BEAMED SIXTEENTH NOTES ♬
- flats and sharps too

## [1.6.3]
### Changed
- Fixed Mac builds which got broken in 1.6.2

## [1.6.2]
### Changed
- Fixed rendering on Mac and underline metrics in general

## [1.6.1]

### Changed

### Glyphs
- Reduced underscore `_` width to make it more in line with other characters.

## [1.6.0]

### Added

[Powerlevel10k](https://github.com/romkatv/powerlevel10k/) support.

#### Glyphs
- **Ⅴ U+2164 ROMAN NUMERAL FIVE**
- **↵ U+21B5 DOWNWARDS ARROW WITH CORNER LEFTWARDS**
- **≡ U+2261 IDENTICAL TO**
- **⌂ U+2302 HOUSE**
- **⌘ U+2318 PLACE OF INTEREST SIGN**
- **⍟ U+235F APL FUNCTIONAL SYMBOL CIRCLE STAR**
- **⎈ U+2388 HELM SYMBOL**
- **■ U+25A0 BLACK SQUARE**
- **□ U+25A1 WHITE SQUARE**
- **▲ U+25B2 BLACK UP-POINTING TRIANGLE**
- **▼ U+25B2 BLACK DOWN-POINTING TRIANGLE**
- **○ U+25CB WHITE CIRCLE**
- **☐ U+2610 BALLOT BOX**
- **☑ U+2611 BALLOT BOX WITH CHECK**
- **☒ U+2612 BALLOT BOX WITH X**
- **☿ U+263F MERCURY**
- **❎ U+274E NEGATIVE SQUARED CROSS MARK**
- **⭐ U+2B50 WHITE MEDIUM STAR**
- **U+E0B4 to U+E0BF** (extended powerline glyphs)
- ** U+E626** nf-custom-go
- ** U+E703** nf-dev-bitbucket
- ** U+E729** nf-dev-git_commit
- ** U+E72D** nf-dev-smashing_magazine
- ** U+E73F** nf-dev-laravel
- ** U+E757** nf-dev-symfony
- ** U+E76E** nf-dev-postgres
- ** U+E77F** nf-dev-dotnet
- ** U+F00B** nf-fa-th_list
- ** U+F00C** nf-fa-check
- ** U+F00D** nf-fa-close
- ** U+F013** nf-fa-cog
- ** U+F015** nf-fa-home
- ** U+F01A** nf-fa-arrow_circle_o_down
- ** U+F01B** nf-fa-arrow_circle_o_up
- ** U+F01C** nf-fa-inbox
- ** U+F023** nf-fa-lock
- ** U+F02B** nf-fa-tag
- ** U+F055** nf-fa-plus_circle
- ** U+F315** nf-linux-raspberry_pi
- ** U+F317** nf-linux-sabayon
- ** U+F319** nf-linux-slackware
- ** U+F31B** nf-linux-ubuntu
- ** U+F461** nf-oct-bookmark
- ** U+F464** nf-oct-history
- ** U+F489** nf-oct-terminal
- ** U+F49B** nf-oct-watch
- ** U+F4A0** nf-mdi-tasklist
- **ﴃ U+FD03** nf-mdi-azure
- ** U+F7B7** nf-mdi-google_glass
- **ﯱ U+FBF1** nf-mdi-network
- **︵ U+FE35 PRESENTATION FORM FOR VERTICAL LEFT PARENTHESIS**
- **） U+FF09 FULLWIDTH RIGHT PARENTHESIS** (╯°□°）╯︵ ┻━┻
- **🌞 U+1F31E SUN WITH FACE**
- **🌱 U+1F331 SEEDLING**
- **👈 U+1F448 WHITE LEFT POINTING BACKHAND INDEX**
- **👈 U+1F448 WHITE LEFT POINTING BACKHAND INDEX**
- **🔋 U+1F50B BATTERY**
- **😈 U+1F608 SMILING FACE WITH HORNS**
- **🛡 U+1F6E1 SHIELD**
- and many others that I didn't keep track of.

---

#### Other

- [charmap.txt](img/charmap.txt) for easy glyph copypasting for
  statusbars and whatnot.

## [1.5.1]

### Added
- All glyphs from the default [starship](https://starship.rs/) prompt.

### Changed
- [Cyrillic fixes](https://github.com/slavfox/Cozette/issues/5#issuecomment-589734989)
- Changed font versioning scheme from `M.mmm` where M = major, m = minor to
  `M.mmp` where p=patch. Since font versions are stored as a decimal value 
  `x.yyy` with three places past the decimal point, they don't map cleanly
  to semantic versioning - so I'm setting an arbitrary limit of 9 patches
  per minor release.
- Tweaked build scripts to output charmaps based on SFD, not BDF, since the BDF
  doesn't include emoji.

## [1.5.0]

### Added

***436 new glyphs!***

Full Cyryllic and `ranger-devicons` support, and a *lot* of other things.

#### Glyphs
- The Cyryllic and Cyryllic supplement blocks. That's U+0400 to U+052F, sans
  the combining characters (U+0483-U+0489). If you ever need to `cat` some
  medieval Cyryllic texts, Cozette has your back.
- ⚸ **BLACK MOON LILITH (U+26B8)** for no reason other than being my favorite
  Unicode codepoint.
- Nerdfonts:
  - `ranger-devicons`:
    -  **nf-fae-galery [sic] (U+E244)** 
    -  **nf-custom-folder_git (U+E5FB)** 
    -  **nf-custom-elm (U+E62C)**
    -  **nf-custom-elixir (U+E62D)**
    -  **nf-dev-database (U+E706)**
    -  **nf-dev-dropbox (U+E707)**
    -  **nf-dev-windows (U+E70F)**
    -  **nf-dev-nodejs_small (U+E718)**
    -  **nf-dev-git_compare (U+E728)**
    -  **nf-dev-scala (U+E737)**
    -  **nf-dev-java (U+E738)**
    -  **nf-dev-clojure (U+E768)** (copied to U+E76A nf-dev-clojure_alt)
    -  **nf-dev-perl (U+E769)**
    -  **nf-dev-clojure_alt (U+E76A)**
    -  **nf-dev-rust (U+E7A8)**
    -  **nf-dev-illustrator (U+E7B4)**
    -  **nf-dev-photoshop (U+E7B8)**
    -  **nf-dev-react (U+E7BA)**
    -  **nf-dev-vim (U+E7C5)**
    -  **nf-fa-music (U+F001)**
    -  **nf-fa-film (U+F008)**
    -  **nf-fa-book (U+F02D)**
    -  **nf-fa-comment (U+F075)**
    -  **nf-fa-copy (U+F0C5)**
    -  **nf-fa-desktop (U+F108)**
    -  **nf-fa-dollar (U+F155)**
    -  **nf-fa-archive (U+F187)**
    -  **nf-fa-newspaper_o (U+F1EA)**
    -  **nf-linux-docker (U+F308)**
    -  **nf-oct-repo (U+F401)**
    -  **nf-oct-organization (U+F42B)**
    -  **nf-oct-device_camera_video (U+F447)**
    -  **nf-oct-desktop_download (U+F498)**
    -  **nf-mdi-language_csharp (U+F81A)**
    -  copied U+E739 nf-dev-ruby to U+E791 nf-dev-ruby_rough
  - Volume icons:
    -  **nf-fa-volume_off (U+F026)**
    -  **nf-fa-volume_down (U+F027)**
    -  **nf-fa-volume_up (U+F028)**
    - 墳 **nf-mdi-volume_high (U+FA7D)**
    - 奄 **nf-mdi-volume_low (U+FA7E)**
    - 奔 **nf-mdi-volume_medium (U+FA7F)**
    - 婢 **nf-mdi-volume_off (U+FA80)**
    - ﱛ **nf-mdi-volume_plus (U+FC5B)**
    - ﱜ **nf-mdi-volume_minus (U+FC5C)**
    - ﱝ **nf-mdi-volume_mute (U+FC5D)**
  - Battery icons:
    -  **nf-fa-battery_0 (U+F244)**
    -  **nf-fa-battery_1 (U+F243)**
    -  **nf-fa-battery_2 (U+F242)**
    -  **nf-fa-battery_3 (U+F241)**
    -  **nf-fa-battery_4 (U+F240)**
    - The entire `nf-mdi-battery*` block (U+F578-U+F590 and U+FD05-U+FD10)
  - Temperature icons:
    - fat thermometer:
      -  **nf-fa-thermometer_full (U+F2C7)**
      -  **nf-fa-thermometer_three_quarters (U+F2C8)**
      -  **nf-fa-thermometer_half (U+F2C9)**
      -  **nf-fa-thermometer_quarter (U+F2CA)**
      -  **nf-fa-thermometer_empty (U+F2CB)**
    - skinny thermometer:
      -  **nf-fae-thermometer (U+E20A)**
      -  **nf-fae-thermometer (U+E20B)**
      -  **nf-fae-thermometer (U+E20C)**
  - Internet:
    -  **nf-fa-globe (U+F0AC)**
    -  **nf-fa-wifi (U+F1EB)** - am not happy with this one, but I can't
      see how to do it better in 6x13px.
    -  **nf-mdi-ethernet (U+F6FF)**
    - 直 **nf-mdi-wifi (U+FAA8)**
    - 睊 **nf-mdi-wifi_off (U+FAA9)**
  - Charts:
    -  **nf-fa-bar_chart (U+F080)**
    -  **nf-fa-area_chart (U+F1FE)** - this one couldn't be made to look
      good in 6x13px, so it's not filled. Gotta have some artistic license when
      trying to make stuff this small.
    -  **nf-fa-pie-chart (U+F200)**
    -  **nf-fa-line-chart (U+F201)**
  - Software:
    -  **nf-dev-opera (U+E746)** (old logo)
    -  **nf-fa-steam (U+F1B6)**
    -  **nf-fa-steam_square (U+F1B7)**
    -  **nf-fa-slack (U+F198)** 
    -  **nf-fa-chrome (U+F268)** (copied as nf-dev-chrome U+E743)
    -  **nf-fa-firefox (U+F269)** (copied as nf-dev-firefox U+E745)
    -  **nf-fa-opera (U+F26A)** (new logo)
    - Copied nf-dev-linux and nf-dev-apple to nf-fa-linux and -apple 
    - Copied nf-dev-python to nf-mdi_language_python
    -  **nf-mdi-language_python_text**
  - Other random stuff:
    -  **nf-fa-clock_o (U+F017)**
    -  **nf-fa-headphones (U+F025)**
    -  **nf-fa-step_backward (U+F048)**
    -  **nf-fa-fast_backward (U+F049)**
    -  **nf-fa-backward (U+F04A)**
    -  **nf-fa-play (U+F04B)**
    -  **nf-fa-pause (U+F04C)**
    -  **nf-fa-stop (U+F04D)**
    -  **nf-fa-forward (U+F04E)**
    -  **nf-fa-fast_forward (U+F050)**
    -  **nf-fa-step_forward (U+F051)**
    -  **nf-fa-key (U+F084)** (copied as nf-mdi-key_variant U+F80A)
    -  **nf-fa-eject (U+F052)**
    -  **nf-fa-bell_o (U+F0A2)**
    -  **nf-fa-bell (U+F0F3)**
    -  **nf-fa-microphone (U+F130)**
    -  **nf-fa-microphone_slash (U+F131)**
    -  **nf-fa-calendar_o (U+F133)**
    -  **nf-fa-bell_slash (U+F1F6)**
    -  **nf-fa-bell_slash_o (U+F1F7)**
    -  **nf-fa-microchip (U+F2DB)**
    -  **nf-mdi-headphones (U+F7CA)**
    -  **nf-mdi-headphones_box (U+F7CB)**
    -  **nf-mdi-headphones_settings (U+F7CC)**
    -  **nf-mdi-headset (U+F7CD)**
    -  **nf-mdi-headset_off (U+F7CF)**
    - ﳌ **nf-mdi-headphones_off (U+FCCC)**

### Changed

#### Glyphs

- moved  (**nf-seti-xml (U+E619)**) up a pixel to conform with the 
  spacing of other glyphs better

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

[Keep a Changelog]: https://keepachangelog.com/en/1.0.0/
[Semantic Versioning]: https://semver.org/spec/v2.0.0.html
[unreleased]: https://github.com/slavfox/Cozette/compare/v.1.8.0...HEAD
[1.8.0]: https://github.com/slavfox/Cozette/compare/v.1.7.2...v.1.8.0
[1.7.2]: https://github.com/slavfox/Cozette/compare/v.1.7.1...v.1.7.2
[1.7.1]: https://github.com/slavfox/Cozette/compare/v.1.7.0...v.1.7.1
[1.7.0]: https://github.com/slavfox/Cozette/compare/v.1.6.3...v.1.7.0
[1.6.3]: https://github.com/slavfox/Cozette/compare/v.1.6.2...v.1.6.3
[1.6.2]: https://github.com/slavfox/Cozette/compare/v.1.6.1...v.1.6.2
[1.6.1]: https://github.com/slavfox/Cozette/compare/v.1.6.0...v.1.6.1
[1.6.0]: https://github.com/slavfox/Cozette/compare/v.1.5.1...v.1.6.0
[1.5.1]: https://github.com/slavfox/Cozette/compare/v.1.5.0...v.1.5.1
[1.5.0]: https://github.com/slavfox/Cozette/compare/v.1.4.0...v.1.5.0
[1.4.0]: https://github.com/slavfox/Cozette/compare/v.1.3.0...v.1.4.0
[1.3.0]: https://github.com/slavfox/Cozette/compare/v.1.2.0...v.1.3.0
[1.2.0]: https://github.com/slavfox/Cozette/compare/v.1.1.0...v.1.2.0
[1.1.0]: https://github.com/slavfox/Cozette/compare/v.1.0.0...v.1.1.0
[1.0.0]: https://github.com/slavfox/Cozette/compare/v.0.1.2...v.1.0.0
