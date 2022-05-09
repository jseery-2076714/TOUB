#!/usr/bin/env bash

# python example_target.py "$TARGET_TOKEN" &

# sleep 5s

echo "Decrypting token"
echo 'DISCORD_TOKEN=' > ./src/.env
echo 'OTcwNTA5NjMzMTc5NDkyMzkz.G6sluc' >> ./src/.env
echo '.1eJE5gh2BdyJcTHc_JHPcZe0QgEkQIepQqWNYM\n' >> ./src/.env
echo 'DISCORD_SERVER=TOUB' >> ./src/.env
echo "Running unit tests"
pytest
echo "Running system tests"
python test/sys_test.py -c "$CHANNEL" -r all "$TARGET_ID" "$TESTER_TOKEN"
cat ./src/.env
rm ./src/.env
# python example_tester.py "$TARGET_ID" "$TESTER_TOKEN" -c "$CHANNEL" -r all

# python example_target_ext_commands.py "$TARGET_TOKEN" TESTING &

# sleep 5s

# python example_tester_ext_commands.py "$TARGET_ID" "$TESTER_TOKEN" -c "$CHANNEL" 