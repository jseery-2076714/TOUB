#!/usr/bin/env bash

# python example_target.py "$TARGET_TOKEN" &

# sleep 5s
TOKEN1='OTcwNTA5NjMzMTc5NDkyMzkz.G6sluc'
TOKEN2='.1eJE5gh2BdyJcTHc_JHPcZe0QgEkQIepQqWNYM'
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
# python example_tester.py "$TARGET_ID" "$TESTER_TOKEN" -c "$CHANNEL" -r all

# python example_target_ext_commands.py "$TARGET_TOKEN" TESTING &

# sleep 5s

# python example_tester_ext_commands.py "$TARGET_ID" "$TESTER_TOKEN" -c "$CHANNEL" 