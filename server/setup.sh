#!/usr/bin/env bash

set -eu

SCRIPT_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

ENV_DIR="${SCRIPT_DIR}/env"

echo "==================================="
echo "Setup virtual environment"
echo "==================================="
python3 -m venv "$ENV_DIR"

echo "==================================="
echo "Activate the virtual environment"
echo "==================================="
source "$ENV_DIR/bin/activate"

echo "==================================="
echo "Install requirement dependencies"
echo "==================================="
python -m pip install -r requirements.txt

