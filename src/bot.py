# Discord bot handling and message processing
import sys
import discord
import os
from dotenv import load_dotenv
import importlib, importlib.util
 
def module_directory(name_module, path):
    P = importlib.util.spec_from_file_location(name_module, path)
    import_module = importlib.util.module_from_spec(P)
    P.loader.exec_module(import_module)
    return import_module
 
sheets = module_directory("sheets", "./modules/sheets.py")
convert = module_directory("convert", "./modules/convert.py")
mg = module_directory("mini_game", "./modules/mini_game.py")


def main():
    TOKEN = 'OTcwNTA5NjMzMTc5NDkyMzkz.GtSges.' + 'H2lCnOWQ2zImGhEk2v_bqQIiW07j9-2YNN3z00'
    SERVER = 'TOUB'
    # check if bot is running on GitHub or locally
    if '/home/runner/work/TOUB/TOUB' in sys.path:
        load_dotenv()
        print("Loading token from .env")
        TOKEN = os.getenv('DISCORD_TOKEN')
        SERVER = os.getenv('DISCORD_SERVER')

    client = discord.Client()


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

    @client.event
    async def on_message(message):
        ### check if bot sends the message, do nothing
        if message.author == client.user:
            return

        ### Base case
        elif message.content.startswith('$hello'):
            await message.channel.send('Hello!')
           
        ### user input: a command that starts with "!"
        ###             this is how TOUB knows it is a toub command
        elif message.content.startswith('!'):
            input = message.content.lower().split(' ')
            command =  input[0][1:]


            ### user command: !toub-help
            ###             asking TOUB to list all commands/formats user can use to prompt toub to do something
            ### bot output: list of commands, !toub-list, !toub-list-r, !toub-level, !toub-level [level], 
            ###             !toub-convert [value] [unit1] [unit2], !toub-convert [unit1] [unit2], !toub-minigame
            if(command == 'toub-help'):
                await message.channel.send('!toub-list : display all units\n'
                + '!toub-list-r : display all units with ratios to SI\n'
                + '!toub-level : show what level toub is on\n'
                + '!toub-level [level] : change the bot function to desired level of TOUB (1, 2, or 3)\n'
                + '!toub-convert [value] [unit1] [unit2] : converts a value in unit1 to its value in unit2\n'
                + '!toub-convert [unit1] [unit2] : converts 1 unit in unit1 to its value in unit2\n'
                + '!toub-minigame : begins minigame')
            
            ### user command: !toub-list, !toub-list-r
            ###             prompts toub to list all possible units the user can chooose from
            ### bot output: all possible units the user can chooose from
            elif('toub-list' in command):
                ### user command: !toub-list-r
                ###             prompts toub to list all possible units with ratios to SI
                ### bot output: all possible units the user can chooose from with ratios to SI
                if('-r' in command):
                    units = sheets.get_col('unit')
                    finalMessage = '__**Units : CM**__ \n'
                    for unit in units:
                        if(sheets.get_data(unit)[1]):
                            value = str(sheets.get_data(unit)[1]) + ' cm\n'
                        elif(str(sheets.get_data(unit)[2])):
                            value = str(sheets.get_data(unit)[2]) + ' cm^2 \n'
                        else:
                            value = str(sheets.get_data(unit)[3]) + ' cm^3 \n'
                        finalMessage += unit + ' : ' + value
                    await message.channel.send(finalMessage)

                else:
                    ### user command: !toub-list
                    ###             prompts toub to list all possible units the user can chooose from
                    ### bot output: all possible units the user can chooose from
                    units = sheets.get_col('unit')
                    finalMessage = '__**Units**__ \n'
                    for unit in units:
                        finalMessage += unit + '\n'
                    await message.channel.send(finalMessage)
            
            ### user command: !toub-level [level], !toub-level
            ###             asking TOUB to change the level of the game (1, 2, or 3), or asking TOUB for the current level 
            ### bot output: the current level of the bot
            ### restrictions: ONLY ADMINISTRATORS CAN CHANGE THE LEVEL, if user attempts to change the level to an invalid
            ###               level, the bot defaults to setting the level to 1
            elif('toub-level' in command):
                if(not message.author.guild_permissions.administrator):
                    await message.channel.send("You don't have permission to change the level!")
                    return
                templevel = float(input[1])
                ### change to level 1
                if(templevel == 1.0):
                    sheets.level = 1
                    await message.channel.send('Current level: ' + str(sheets.level))
                ### change to level 2
                elif(templevel == 2.0):
                    sheets.level = 2
                    await message.channel.send('Current level: ' + str(sheets.level))
                ### change to level 3
                elif (templevel == 3.0):
                    sheets.level = 3
                    await message.channel.send('Current level: ' + str(sheets.level))
                ### sends the current level, does not change level
                elif (command == 'toub-level'):
                    await message.channel.send('Current level: ' + str(sheets.level))
                ### Not a valid level, default to level 1
                else :
                    sheets.level = 1
                    await message.channel.send('Not a valid level. Default to level 1')

            elif('toub-currentLevel' in command):
                await message.channel.send('Current leve: ' + str(sheets.level))

            ### user command: !toub-convert [value] [unit1] [unit2], !toub-convert [unit1] [unit2]
            ###             converts a value of unit1 tto unit2, or converts 1 unit1 to unit2
            ### bot output: the conversion 
            elif(command == 'toub-convert'):
                ### user command: !toub-convert [value] [unit1] [unit2]
                ###             converts a value of unit1 tto unit2
                ### bot output: the conversion 
                units = sheets.get_col('unit')
                try:
                    value = float(input[1])
                    firstUnit = input[2]
                    secondUnit = input[3]
                    if(firstUnit not in units):
                        await message.channel.send(firstUnit + " is not in our current database. Use '!toub-add-unit [unit] [value in cm]' to add it!")
                        return
                    if(secondUnit not in units):
                        await message.channel.send(secondUnit + " is not in our current database. Use '!toub-add-unit [unit] [value in cm] [dimension]' to add it!")
                        return
                    result = convert.convert_unit(value, firstUnit, secondUnit)
                    await message.channel.send(str(value) + " " + str(firstUnit) + " = " + result)
                    return

                ### user command: !toub-convert [unit1] [unit2]
                ###             converts 1 unit1 to unit2
                ### bot output: the conversion 
                except ValueError:
                    firstUnit = input[1]
                    secondUnit = input[2]
                    if(firstUnit not in units):
                        await message.channel.send(firstUnit + " is not in our current database. Use '!toub-add-unit [unit] [value in cm]' to add it!")
                        return
                    if(secondUnit not in units):
                        await message.channel.send(secondUnit + " is not in our current database. Use '!toub-add-unit [unit] [value in cm] [dimension]' to add it!")
                        return
                    result = convert.convert_unit(1, firstUnit, secondUnit)
                    await message.channel.send(str(value) + " " + str(firstUnit) + " = " + result)
                    return
            
            elif(command == 'toub-add-unit'):
                unit = input[1]
                value = float(input[2])
                dimension = int(input[3])
                if(dimension > 3 or dimension < 1):
                    await message.channel.send("Invalid dimension, must be between 1-3")
                    return
                sheets.add_unit(unit, value, dimension)
                await message.channel.send("Unit: " + unit + " : " + str(value) + " added!")
                return

            ### user command: !toub-minigame
            ###             prompts toub to begin mini game
            ### bot output: the minigame
            elif(command == 'toub-minigame'):
                await message.channel.send(mg.prompt())
                msg = await message.channel.send(mg.game_func1())
                await msg.add_reaction('1️⃣')    
                await msg.add_reaction('2️⃣')  
                await msg.add_reaction('3️⃣')    
                await msg.add_reaction('4️⃣')  
       
        ### not a toub command
        else:
            parsed = convert.parse_message(message.content)
            if(parsed == message.content):
                return
            else:
                await message.channel.send(convert.parse_message(message.content))

    @client.event
    async def on_reaction_add(reaction, user):
        if user != client.user:
            if str(reaction.emoji) == '1️⃣':
                await reaction.message.channel.send (mg.game_won())

    client.run(TOKEN)


if __name__ == "__main__":
    main()