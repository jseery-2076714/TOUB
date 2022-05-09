import discord
import os
from convert import convertUnit, parseMessage
import sheets

from dotenv import load_dotenv

### installing setup
### pip install discord.py
### pip install distest
### pip install -U pytest

### install google sheets api stuff:
### pip install gspread
### pip install --upgrade google-api-python-client oauth2client 
def main():
    load_dotenv()
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
        sheets.setUpAPI()

    @client.event
    async def on_message(message):
        ### check if bot sends the message, do nothing
        if message.author == client.user:
            return


        ### Base case
        elif message.content.startswith('$hello'):
            await message.channel.send('Hello!')
        
        ### Checking for specific toub commands
        elif message.content.startswith('!'):
            input = message.content.lower().split(' ')
            command =  input[0][1:]

            ### lists all the commands/formats
            ### Need a command to change level
            if(command == 'toub-help'):
                await message.channel.send('!toub-list : display all units\n'
                + '!toub-list-r : display all units with ratios to SI\n'
                + '!toub-level [level] : change the bot function to desired level of TOUB (1, 2, or 3)\n'
                + '!toub-convert [value] [unit1] [unit2] : converts a value in unit1 to its value in unit2\n'
                + '!toub-convert [unit1] [unit2] : converts 1 unit in unit1 to its value in unit2\n'
                + '!toub-minigame : begins minigame')
            
            ### lists all the units
            elif('toub-list' in command):
                ### lists units with ratios to SI
                if('-r' in command):
                    print('display all units in SI')
                
                else:
                    print(print('display all units'))
            
            ### changes the level of the bot
            ### options (1, 2, 3)
            elif('toub-level' in command):
                ### change to level 1
                if(command == 'toub-level 1'):
                    sheets.level = 1
                ### change to level 2
                elif(command == 'toub-level 2'):
                    sheets.level = 2
                ### change to level 3
                elif (command == 'toub-level 3'):
                    sheets.level = 3
                ### Not a valid level
                else :
                    sheets.level = 1
                    await message.channel.send('Not a valid level. Default to level 1')


            ### converts from unit1 to unit2 (if value is entered, convert to that number of values, else value is 1)
            elif(command == 'toub-convert'):
                try:
                    value = float(input[1])
                    firstUnit = input[2]
                    secondUnit = input[3]
                    print(value)
                    print(firstUnit)
                    print(secondUnit)
                    result = convertUnit(value, firstUnit, secondUnit)
                    await message.channel.send(str(value) + " " + str(firstUnit) + " = " + result)
                except ValueError:
                    firstUnit = input[1]
                    secondUnit = input[2]
                    result = convertUnit(1, firstUnit, secondUnit)
                    await message.channel.send(str(value) + " " + str(firstUnit) + " = " + result)

            ### minigame
            elif(command == 'toub-minigame'):
                print('Choose the best conversion')
                print('Option 1')
                print('Option 2')
                print('Option 3')
                print('Option 4')
                if message.author == client.user:
                    await message.add_reaction('U+0031 U+FE0F U+20E3')
                    await message.add_reaction('U+0032 U+FE0F U+20E3')
                    await message.add_reaction('U+0033 U+FE0F U+20E3')
                    await message.add_reaction('U+0034 U+FE0F U+20E3')

        else:
            parsed = parseMessage(message.content)
            if(parsed == message.content):
                return
            else:
                await message.channel.send(parseMessage(message.content))

            


    ''' Proposed Design Features - commands are headed with “!toub-”
    Default:
    “help” - lists all the commands/formats
    “list” - lists all the units
        “-r” - lists units with ratios to SI
    “convert [unit1] [unit2]” - converts from unit1 to unit2 
    “Add [unitname] [SI conversion] - adds a custom unit
    “profile” - users have profiles?
    Game:
    “game-help” - details how the game is played
    “game-play” - starts a game instance
    “game-guess [guess]” - users guesses unit conversion 
    '''

    client.run(TOKEN)

if __name__ == "__main__":
    main()