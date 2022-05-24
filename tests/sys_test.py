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


# Write tests for the bot


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Convert command tests !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Testing convert command - non-SI to non-SI
@test_collector()
async def test_convert_nonSI_nonSI_0(interface):
    await interface.assert_reply_equals("!toub-convert 0 feet yard", "0.0 feet = 0.00e+00 yard")


@test_collector()
async def test_convert_nonSI_nonSI_1(interface):
    await interface.assert_reply_equals("!toub-convert 1 feet yard", "1.0 feet = 0.33333333333333337 yard")


@test_collector()
async def test_convert_nonSI_nonSI_2(interface):
    await interface.assert_reply_equals("!toub-convert 2 feet yard", "2.0 feet = 0.6666666666666667 yard")


# Testing convert command - SI to SI
@test_collector()
async def test_convert_SI_SI_0(interface):
    await interface.assert_reply_equals("!toub-convert 0 centimeter meter", "0.0 centimeter = 0.00e+00 meter")


@test_collector()
async def test_convert_SI_SI_1(interface):
    await interface.assert_reply_equals("!toub-convert 1 centimeter meter", "1.0 centimeter = 0.01 meter")


@test_collector()
async def test_convert_SI_SI_2(interface):
    await interface.assert_reply_equals("!toub-convert 2 centimeter meter", "2.0 centimeter = 0.02 meter")


# Testing convert command - SI to non-SI
@test_collector()
async def test_convert_SI_nonSI_0(interface):
    await interface.assert_reply_equals("!toub-convert 0 centimeter feet", "0.0 centimeter = 0.00e+00 feet")


@test_collector()
async def test_convert_SI_nonSI_1(interface):
    await interface.assert_reply_equals("!toub-convert 1 centimeter feet", "1.0 centimeter = 0.03280839895013123 feet")


@test_collector()
async def test_convert_SI_nonSI_2(interface):
    await interface.assert_reply_equals("!toub-convert 2 centimeter feet", "2.0 centimeter = 0.06561679790026247 feet")


# Testing convert command - non-SI to SI
@test_collector()
async def test_convert_nonSI_SI_0(interface):
    await interface.assert_reply_equals("!toub-convert 0 feet centimeter", "0.0 feet = 0.00e+00 centimeter")


@test_collector()
async def test_convert_nonSI_SI_1(interface):
    await interface.assert_reply_equals("!toub-convert 1 feet centimeter", "1.0 feet = 30.48 centimeter")


@test_collector()
async def test_convert_nonSI_SI_2(interface):
    await interface.assert_reply_equals("!toub-convert 2 feet centimeter", "2.0 feet = 60.96 centimeter")


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Level 1 default message behavior testing !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Testing - non-SI to SI
@test_collector()
async def test_level1_nonSI_SI_0(interface):
    await interface.assert_reply_equals("0 feet", "0.00e+00 centimeter")


@test_collector()
async def test_level1_nonSI_SI_1(interface):
    await interface.assert_reply_equals("1 feet", "30.48 centimeter")


@test_collector()
async def test_level1_nonSI_SI_2(interface):
    await interface.assert_reply_equals("2 feet", "60.96 centimeter")


# Testing - SI to SI
@test_collector()
async def test_level1_SI_SI_0(interface):
    await interface.assert_reply_equals("0 centimeter", "0.00e+00 centimeter")


@test_collector()
async def test_level1_SI_SI_1(interface):
    await interface.assert_reply_equals("1 centimeter", "1.0 centimeter")


@test_collector()
async def test_level1_SI_SI_2(interface):
    await interface.assert_reply_equals("2 centimeter", "2.0 centimeter")


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Level command tests !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Testing getting current level
@test_collector()
async def test_current_level(interface):
    await interface.assert_reply_equals("!toub-level", "Current level: 1")

# Testing setting level to level 2
@test_collector()
async def test_set_level2(interface):
    await interface.assert_reply_equals("!toub-level 2", "Current level: 2")


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Level 2 default message behavior testing !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""
# Testing - non-SI to obscure
@test_collector()
async def test_level2_nonSI_obscure(interface):
    await interface.assert_reply_equals("0 feet", "0.0 centimeter")
    await interface.assert_reply_equals("1 feet", "30.48 centimeter")
    await interface.assert_reply_equals("2 feet", "60.96 centimeter")
"""

# Testing - SI to SI
@test_collector()
async def test_level2_SI_SI_0(interface):
    await interface.assert_reply_equals("0 centimeter", "0.00e+00 centimeter")


@test_collector()
async def test_level2_SI_SI_1(interface):
    await interface.assert_reply_equals("1 centimeter", "1.0 centimeter")


@test_collector()
async def test_level2_SI_SI_2(interface):
    await interface.assert_reply_equals("2 centimeter", "2.0 centimeter")


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! More level command tests !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Testing setting level to level 3
@test_collector()
async def test_set_level3(interface):
    await interface.assert_reply_equals("!toub-level 3", "Current level: 3")


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Level 3 default message behavior testing !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""
# Testing - non-SI to obscure
@test_collector()
async def test_level3_nonSI_obscure(interface):
    await interface.assert_reply_equals("0 feet", "0.0 centimeter")
    await interface.assert_reply_equals("1 feet", "30.48 centimeter")
    await interface.assert_reply_equals("2 feet", "60.96 centimeter")


# Testing - SI to obscure
@test_collector()
async def test_level3_SI_obscure(interface):
    await interface.assert_reply_equals("0 centimeter", "0.0 centimeter")
    await interface.assert_reply_equals("1 centimeter", "1.0 centimeter")
    await interface.assert_reply_equals("2 centimeter", "2.0 centimeter")
"""

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! More level testing !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Testing setting level to invalid level
@test_collector()
async def test_set_level_invalid(interface):
    await interface.assert_reply_equals("!toub-level 4", "Not a valid level. Default to level 1")


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Help command test !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Testing help command
@test_collector()
async def test_help(interface):
    await interface.assert_reply_equals("!toub-help", '!toub-list : display all units\n'
        + '!toub-list r: display all units with ratios to SI\n'
        + '!toub-level : show what level toub is on\n'
        + '!toub-level [level] : change the bot function to desired level of TOUB (1, 2, or 3)\n'
        + '!toub-convert [value] [unit1] [unit2] : converts a value in unit1 to its value in unit2\n'
        + '!toub-convert [unit1] [unit2] : converts 1 unit in unit1 to its value in unit2\n'
        + '!toub-addunit [unit] [value] [dim] : adds unit to database\n'
        + '!toub-minigame : begins minigame')

# Actually run the bot

if __name__ == "__main__":
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    run_dtest_bot(sys.argv, test_collector)
