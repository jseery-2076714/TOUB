#!/usr/bin/env bash

TOKEN1='OTcwNTA5NjMzMTc5NDkyMzkz.GO0_P7.'
TOKEN2='F1him9JcnoCI3-142NLstcVCXnQojmie0RItNE'
TESTER_TOKEN1='OTcwNTI4MTAyODEzOTQ5OTky.'
TESTER_TOKEN2='Ym9Quw.qIXzCZQpin9a-fPbfvHWwiMFwrw'
echo "Decrypting token"
echo 'DISCORD_TOKEN='$TOKEN1$TOKEN2 > ./src/.env
echo 'DISCORD_SERVER=TOUB' >> ./src/.env
echo "Running unit tests"
pytest
echo "Running system tests"
python src/sys_test.py -c "$CHANNEL" -r all "$TARGET_ID" "$TESTER_TOKEN1$TESTER_TOKEN2"
rm ./src/.env