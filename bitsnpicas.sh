#!/usr/bin/env sh
BITSNPICAS_URL="https://github.com/kreativekorp/bitsnpicas/releases/download/v2.0/BitsNPicas.jar"
mkdir -p deps
if [ ! -f deps/BitsNPicas.jar ]; then
  echo "Downloading BitsNPicas.jar..."
  wget -O deps/BitsNPicas.jar $BITSNPICAS_URL
  echo "Done."
fi
java -jar deps/BitsNPicas.jar $@
