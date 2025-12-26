#!/bin/bash
# Run this file using the `. setup.sh` command.

if [ -d $1 ]; then
  cd $1

  if [ ! -d .venv ]; then
    python3 -m venv .venv
    . .venv/bin/activate
    pip3 install -r requirements.txt
  else
    . .venv/bin/activate
  fi
else
  echo "Project not found: $1"
fi
