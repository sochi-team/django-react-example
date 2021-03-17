#!/usr/bin/env bash

set -eu

SCRIPT_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

PROVISION_DIR="$SCRIPT_DIR/provision/"

docker-compose -f "$PROVISION_DIR/docker-compose.dev.yml" --env-file "$PROVISION_DIR/dev.env" $@