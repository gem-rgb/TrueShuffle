#!/bin/bash
set -e
cd /app
export PYTHONPATH="/app:$PYTHONPATH"
python3 -m pytest backend/tests/test_popularity_unification.py -v --tb=short 2>&1
