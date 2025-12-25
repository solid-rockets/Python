#!/bin/bash
# Run this file using the `. setup.sh` command.

if [ ! -f .venv ]; then
  python3 -m venv .venv
  . .venv/bin/activate
  pip3 install -r requirements.txt
else
  . .venv/bin/activate
fi
