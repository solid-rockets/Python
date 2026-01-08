#!/bin/bash

# Change this to point to the directory where decks reside.
# Then, refer to decks by their filename only, extension excluded.
# Ex. if deck on path "~/Decks/sample.txt", use "sample"
decks_path=./Decks

python3 $1.py $decks_path/$2.txt
