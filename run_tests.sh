#!/usr/bin/env bash

TARGET_ID="970509633179492393"
CHANNEL="970505630026694707"
TESTER_TOKEN1='OTcwNTI4MTAyODEzOTQ5OTky.'
TESTER_TOKEN2='Ym9Quw.qIXzCZQpin9a-fPbfvHWwiMFwrw'
echo "Running unit tests"
pytest
echo "Running system tests"
python tests/sys_test.py -c "$CHANNEL" -r all "$TARGET_ID" "$TESTER_TOKEN1$TESTER_TOKEN2"