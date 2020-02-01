FROM archlinux/base
RUN pacman -S --noconfirm fontforge

WORKDIR /cozette/

RUM mkdir build
RUN fontforge -lang ff -c 'Open("Cozette8.sfd"); Generate("build/cozette.otb")'
RUN fontforge -lang ff -c 'Open("Cozette8.sfd"); Generate("build/cozette.ttf")'
RUN fontforge -lang ff -c 'Open("Cozette8.sfd"); Generate("build/cozette.bdf")'
