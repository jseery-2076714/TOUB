#!/usr/bin/env bash

echo "Running unit tests"
pytest
echo "Running system tests"
python src/sys_test.py -c "$CHANNEL" -r all "$TARGET_ID" "$TESTER_TOKEN1$TESTER_TOKEN2"