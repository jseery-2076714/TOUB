import discord
import os
import convert

from dotenv import load_dotenv

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
        if(command == 'toub-help'):
            print('display help')
        
        ### lists all the units
        elif('toub-list' in command):
            ### lists units with ratios to SI
            if('-r' in command):
                print('display all units with ratios to SI')
            
            else:
                print(print('display all units'))
        
        ### converts from unit1 to unit2 (if value is entered, convert to that number of values, else value is 1)
        elif(command == 'toub-convert'):
            try:
                value = float(input[1])
                firstUnit = input[2]
                secondUnit = input[3]
                convert(value, firstUnit, secondUnit)
            except ValueError:
                firstUnit = input[1]
                secondUnit = input[2]
                convert(1, firstUnit, secondUnit)

        ### minigame
        elif(command == 'toub-minigame'):
            print("START MINIGAME")

        


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