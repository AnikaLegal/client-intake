#!/bin/bash
set -e
export DJANGO_SETTINGS_MODULE=clerk.settings.test
pytest -s -vv --reuse-db
