# Cozette
A bitmap programming font optimized for coziness.

![sample.png](img/sample.png)

Cozette is based on [Dina][], which itself is based on [Proggy][].
It's also heavily inspired by [Creep][]. I absolutely adore Creep, and was
using it up until I got a higher-DPI screen for which it was slightly too
small - which prompted me to make Cozette.

# Installation

**Note:** vscode doesn't support bitmap fonts. Until Cozette has a vectorized
version, it won't work in vscode.

[You can get Cozette over at the Releases tab](https://github.com/slavfox/Cozette/releases)!

If you're on Linux, the preferred format is `.otb` or `.ttf`. To install the
font, just throw it in your fonts directory (you probably want to follow your
distro's instructions). On Ubuntu, if you don't want to reconsider your distro
choice, you might need to
[specifically enable bitmap fonts](https://bugs.launchpad.net/ubuntu/+source/fontconfig/+bug/1560114).

If you're on Mac, download the `.dfont` and install it with `Font Book.app`.

If you're on Windows,
[follow the instructions from here](https://wiki.archlinux.org/index.php/installation_guide).

# Unicode support

As of release 1.0, these are the characters included in Cozette:

![characters.png](./img/characters.png)

Supporting as many characters as possible is, however, an important objective
for this font, as I'd, ideally, like it to be able to display anything I
might need it to. If you want any additional characters added, just submit
an issue and I'll do my best.

# Roadmap

The eventual goal is feature (and character range)-parity with Creep. Here's
where Cozette is so far, in the order the features are going to be implemented:

- [x] ASCII
- [x] Powerline
- [x] Build scripts to handle exporting
- [x] Box-drawing (mostly)
- [x] Braille
- [ ] Nerdfonts:
  - [x] nf-seti-*
  - [ ] nf-dev-*
- [ ] Glyph map generation (so I don't have to keep `characters.png` up to date)
- [ ] "True" TTF version
  - [  ] Windows support
- [ ] Bold version
- [ ] Italic version
- [ ] Ligatures

# License

Cozette is licensed [MIT][] 💜

[Dina]: https://www.dcmembers.com/jibsen/download/61/
[Proggy]: https://github.com/bluescan/proggyfonts
[MIT]: ./LICENSE
[Creep]: https://github.com/romeovs/creep
