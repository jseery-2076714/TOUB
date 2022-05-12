"""
A functional demo of all possible test cases. This is the format you will want to use with your testing bot.
    Run with:
        python example_tests.py TARGET_NAME TESTER_TOKEN
"""
from ast import arguments
import asyncio
import sys
from distest import TestCollector
from distest import run_dtest_bot
from discord import Embed, Member, Status
from distest import TestInterface
import platform


test_collector = TestCollector()
created_channel = None


@test_collector()
async def test_hello(interface):
    await interface.assert_reply_equals("$hello", "Hello!")

# Write tests for the bot 

# Non SI to SI
# 1 inch to 2.54 cm
@test_collector()
async def test_nonSI_to_SI(interface):
    await interface.assert_reply_equals("!toub-convert 1 inch cm", "2.54 cm")


# Actually run the bot

if __name__ == "__main__":
    
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    run_dtest_bot(sys.argv, test_collector)
    