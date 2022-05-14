# TOUB
Totally Obscure Units Bot<br>
This bot takes any non-SI unit measurement in all Discord chat messages and converts that measurement to obscure units that are unknown to the vast majority of people and likely completely useless. The bot can be integrated into Discord servers like any other bot, and can be adjusted to suit the desired level of chaos.
This repo contains both the bot source code and installation instructions, as well as a copy of the unit conversion database.

### Current Layout:
reports (Weekly Reports)<br>
src (Source Code)<br>
--data (Bot Data)<br>
test (Test Code)<br>

### Build/test instructions:
To build and test the source code for TOUB the first time, ensure you have at least Python version 3.10 installed, change your current directory to the TOUB root directory, and run the following command to install all dependencies:<br>`python -m pip install -r requirements.txt`<br>
Then run the command `pytest` from the shell to run the unit tests. To run the system tests, first run the main bot using the command `python bot.py`, then run the command `python src/sys_test.py -c "<Discord channel ID>" -r all "<target bot ID>" "<tester bot token>"`<br>
When pushing to the repo, our CI system (GitHub Actions) runs the python-app.yml script on the GitHub servers, which installs all dependencies and runs the test scripts automatically.

### Running the bot:
To run the bot code locally, ensure you have at least Python version 3.10 installed, and change your directory to the root TOUB directory.
Then simply run the command `python src/bot.py` in the terminal to begin running the bot locally.<br>
Once the bot is running, all interactions with the bot are done through the Discord server with which the bot is integrated.
On the server with TOUB integration, all available commands can be viewed by typing the command `!toub-help` into the Discord server.

### Currently operational use cases:
All members of any Discord channel with TOUB integration are able to use the bot commands we have currently implemented, which include: !toub-help , !toub-list , !toub-list-r , !toub-level , !toub-convert , !toub-minigame
