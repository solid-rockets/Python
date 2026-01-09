#!/bin/bash
# This script is running a dedicated shell instance, so the env setup will be
# local and temporary.
WD=$(dirname $0)
VENV_PATH=$WD/.venv

if [ ! -d $VENV_PATH ]; then
  echo "Installing packages, please wait."
  python3 -m venv $VENV_PATH
  . $VENV_PATH/bin/activate
  pip3 install -r $WD/requirements.txt -q
  echo "Installation complete."
  echo ""
else
  . $VENV_PATH/bin/activate
fi

# Environment is setup, so can proceed to running the program proper.
DECKS_PATH=~/Decks # Path to decks.

if [ "$1" == "list" ]; then
  ls -l $DECKS_PATH | \
  sed '/total [0-9]*/d' | \
  sed 's/.*[0-9]*:[0-9]* //' | \
  sed 's/\.txt$//'
else
  python3 $WD/$1.py $DECKS_PATH/$2.txt
fi
