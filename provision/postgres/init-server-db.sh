#!/bin/bash

set -eu

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER hospital CREATEDB PASSWORD 'hospital';
    CREATE DATABASE hospital;
    GRANT ALL PRIVILEGES ON DATABASE hospital TO hospital;
EOSQL