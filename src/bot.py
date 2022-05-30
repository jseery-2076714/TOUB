# Discord bot handling and message processing

# Imports
from http import client
import sys
import discord
import os
from dotenv import load_dotenv
import importlib, importlib.util

from modules.convert import change_level

def module_directory(name_module, path):
    p = importlib.util.spec_from_file_location(name_module, path)
    import_module = importlib.util.module_from_spec(p)
    p.loader.exec_module(import_module)
    return import_module

# Global variables
SHEETS = module_directory("sheets", "./modules/sheets.py")
CONVERT = module_directory("convert", "./modules/convert.py")
MG = module_directory("mini_game", "./modules/mini_game.py")
TOKEN = 'OTcwNTA5NjMzMTc5NDkyMzkz.GtSges.' + 'H2lCnOWQ2zImGhEk2v_bqQIiW07j9-2YNN3z00'
SERVER = 'TOUB'
COMMANDS = {'!toub-help', '!toub-list', '!toub-level', '!toub-convert', '!toub-addunit', '!toub-minigame'}
client = discord.Client()

# Run the bot
def main():
    global TOKEN
    global SERVER
    # check if bot is running on GitHub or locally
    if '/home/runner/work/TOUB/TOUB' in sys.path:
        load_dotenv()
        print("Loading token from .env")
        TOKEN = os.getenv('DISCORD_TOKEN')
        SERVER = os.getenv('DISCORD_SERVER')
    client.run(TOKEN)



###################################################
################## CLIENT EVENTS ##################
###################################################



@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == SERVER:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    print('We have logged in as {0.user}'.format(client))
    SHEETS.set_up_api()

@client.event
async def on_message(message):
    ### check if bot sends the message, do nothing
    if message.author == client.user:
        return
    
    input = message.content.lower().split(' ')
    command =  input[0]

    ### user input: a command that starts with "!"
    ###             this is how TOUB knows it is a toub command
    if command.startswith('!toub'):
        if command in COMMANDS:
            command_inputs = []
            if (len(input) >= 2):
                command_inputs = [input[i] for i in range(1, len(input))]
            await eval(command[1:].replace('-', '_')+'(message, command_inputs)')
        else:
            await message.channel.send('Unknown command, see !toub-help')
            return
    else:
        await toub_parse(message.channel, message.content)
    return

@client.event
async def on_reaction_add(reaction, user):
    if user != client.user:
        if str(reaction.emoji) == '1️⃣' and MG.rightChoice() == 'a':
            await reaction.message.channel.send (MG.game_won())
        if str(reaction.emoji) == '2️⃣' and MG.rightChoice() == 'b':
            await reaction.message.channel.send (MG.game_won())
        if str(reaction.emoji) == '3️⃣' and MG.rightChoice() == 'c':
            await reaction.message.channel.send (MG.game_won())
        if str(reaction.emoji) == '4️⃣' and MG.rightChoice() == 'd':
            await reaction.message.channel.send (MG.game_won())
        if str(reaction.emoji) == '5️⃣' and MG.rightChoice() != 'a' or MG.rightChoice() != 'b' or MG.rightChoice() != 'c' or MG.rightChoice() != 'd' :
            await reaction.message.channel.send (MG.game_won())



###################################################
################ COMMAND FUNCTIONS ################
###################################################



### user command: !toub-help
###             asking TOUB to list all commands/formats user can use to prompt toub to do something
### bot output: list of commands, !toub-list, !toub-list-r, !toub-level, !toub-level [level], 
###             !toub-convert [value] [unit1] [unit2], !toub-convert [unit1] [unit2], !toub-minigame
async def toub_help(message, inputs):
    if (len(inputs) == 0):
        await message.channel.send('!toub-list : display all units\n'
        + '!toub-list r: display all units with ratios to SI\n'
        + '!toub-level : show what level toub is on\n'
        + '!toub-level [level] : change the bot function to desired level of TOUB (1, 2, or 3)\n'
        + '!toub-convert [value] [unit1] [unit2] : converts a value in unit1 to its value in unit2\n'
        + '!toub-convert [unit1] [unit2] : converts 1 unit in unit1 to its value in unit2\n'
        + '!toub-addunit [unit] [value] [dim] : adds unit to database\n'
        + '!toub-minigame : begins minigame')
    else:
        await message.channel.send('Invalid input, Command Format: !toub-help')
    return

### user command: !toub-list-r
###             prompts toub to list all possible units with ratios to SI
### bot output: all possible units the user can chooose from with ratios to SI
### user command: !toub-list
###             prompts toub to list all possible units the user can chooose from
### bot output: all possible units the user can chooose from
async def toub_list(message, inputs):
    if (len(inputs) > 1 or (len(inputs) == 1 and inputs[0] != 'r')):
        await message.channel.send('Invalid input, Command Format: !toub-list, !toub-list-r')
        return
    # default
    if (len(inputs) == 0):
        units = SHEETS.get_col('unit')
        finalMessage = '__**Units**__ \n'
        for unit in units:
            finalMessage += unit + '\n'
        await message.channel.send(finalMessage)
    # r input flag
    else:
        units = SHEETS.get_col('unit')
        finalMessage = '__**Units : CM**__ \n'
        for unit in units:
            if(SHEETS.get_data(unit)[1]):
                value = str(SHEETS.get_data(unit)[1]) + ' cm\n'
            elif(str(SHEETS.get_data(unit)[2])):
                value = str(SHEETS.get_data(unit)[2]) + ' cm^2 \n'
            else:
                value = str(SHEETS.get_data(unit)[3]) + ' cm^3 \n'
            finalMessage += unit + ' : ' + value
        await message.channel.send(finalMessage)
    return

### user command: !toub-level [level], !toub-level
###             asking TOUB to change the level of the game (1, 2, or 3), or asking TOUB for the current level 
### bot output: the current level of the bot
### restrictions: ONLY ADMINISTRATORS CAN CHANGE THE LEVEL, if user attempts to change the level to an invalid
###               level, the bot defaults to setting the level to 1
async def toub_level(message, inputs):
    if (len(inputs) > 1):
        await message.channel.send('Invalid input, Command Format: !toub-level, !toub-level [level]')
        return

    if(len(inputs) == 0):
        await message.channel.send('Current level: ' + str(SHEETS.level))
        ### sends the current level, does not change level
    else:
        if (not message.author.guild_permissions.administrator):
            await message.channel.send("You don't have permission to change the level!")
            return

        templevel = float(inputs[0])
        ### change to level 1
        if(templevel == 1.0):
            CONVERT.change_level(1)
            await message.channel.send('Current level: ' + str(SHEETS.level))
        ### change to level 2
        elif(templevel == 2.0):
            CONVERT.change_level(2)
            await message.channel.send('Current level: ' + str(SHEETS.level))
        ### change to level 3
        elif (templevel == 3.0):
            CONVERT.change_level(3)
            await message.channel.send('Current level: ' + str(SHEETS.level))                    
        ### Not a valid level, default to level 1
        else:
            CONVERT.change_level(1)
            await message.channel.send('Not a valid level. Default to level 1')
    return

### user command: !toub-convert [value] [unit1] [unit2]
###             converts a value of unit1 tto unit2
### bot output: the conversion 
### user command: !toub-convert [unit1] [unit2]
###             converts 1 unit1 to unit2
### bot output: the conversion 
async def toub_convert(message, inputs):
    if not(len(inputs) == 2 or len(inputs) == 3):
        await message.channel.send('Invalid input, Command Format: !toub-convert [unit1] [unit2], !toub-convert [value] [unit1] [unit2]')
        return
    try:
        value = float(inputs[0])
        firstUnit = inputs[1]
        secondUnit = inputs[2]
        result = CONVERT.convert_unit(value, firstUnit, secondUnit)
        if(result == ''):
            await message.channel.send("Cannot convert units with different dimensions!")
        else:
            await message.channel.send(str(value) + " " + str(firstUnit) + " = " + result)
    except ValueError:
        firstUnit = inputs[0]
        secondUnit = inputs[1]
        result = CONVERT.convert_unit(1, firstUnit, secondUnit)
        await message.channel.send("1.0 " + str(firstUnit) + " = " + result)
    return

### user command: !toub-addunit [unit] [value] [dim]
###             adds the unit conversion into the google sheets database
### bot output: success or failure in adding the unit
async def toub_addunit(message, inputs):
    if not(len(inputs) == 3):
        await message.channel.send('Invalid input, Command Format: !toub-addunit [unit] [value] [dim]')
        return
    if(not message.author.guild_permissions.administrator):
        await message.channel.send("You don't have permission to add a unit!")
        return
    unit = inputs[0]
    value = float(inputs[1])
    dimension = int(inputs[2])
    if(dimension > 3 or dimension < 1):
        await message.channel.send("Invalid dimension, must be between 1-3")
        return
    SHEETS.add_unit(unit, value, dimension)
    await message.channel.send("Unit: " + unit + " = " + str(value) + "cm^" + str(dimension) + " added!")
    return

### user command: !toub-minigame
###             prompts toub to begin mini game
### bot output: the minigame
async def toub_minigame(message, inputs):
    if not(len(inputs) == 0):
        await message.channel.send('Invalid input, Command Format: !toub-minigame')
        return
    await message.channel.send(MG.prompt())
    msg = await message.channel.send(MG.game_func1())
    await msg.add_reaction('1️⃣')
    await msg.add_reaction('2️⃣')
    await msg.add_reaction('3️⃣')
    await msg.add_reaction('4️⃣')
    await msg.add_reaction('5️⃣')
    return

### not a toub command
async def toub_parse(channel, content):
    parsed = CONVERT.parse_message(content)
    if(parsed == content):
        return
    else:
        await channel.send(CONVERT.parse_message(content))

if __name__ == "__main__":
    main()