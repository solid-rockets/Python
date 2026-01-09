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
python3 $WD/main.py
