#!/bin/bash

# Change this to point to the directory where decks reside.
# Then, refer to decks by their filename only, extension excluded.
# Ex. if deck on path "~/Decks/sample.txt", use "sample"
decks_path=./Decks

if [ "$1" == "list" ]; then
  ls -l $decks_path | \
  sed '/total [0-9]*/d' | \
  sed 's/.*[0-9]*:[0-9]* //' | \
  sed 's/\.txt$//'
else
  python3 $1.py $decks_path/$2.txt
fi
