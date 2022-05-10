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
To build and test the source code for TOUB the first time, ensure you have at least Python version 3.10 installed, and run the following command to install all dependencies:<br>`python -m pip install flake8 pytest distest distest-check python-dotenv gspread google-api-python-client pandas oauth2client`<br>
Then run the run_tests.sh shell script to run the tests.
For future testing, you can simply run the run_tests.sh shell script to rerun the tests.
When pushing to the repo, our CI system (GitHub Actions) runs the python-app.yml script on the GitHub servers, which installs all dependencies and run the test script automatically.

### Running the bot:
To run the bot code locally, ensure you have at least Python version 3.10 installed, and change your directory to the TOUB/src directory.
Then simply run the command `python bot.py` in the terminal to begin running the bot locally.

### Currently operational use cases:
All members of any Discord channel with TOUB integration are able to use the bot commands we have currently implemented, which include: !toub-help , !toub-list , !toub-list-r , !toub-level , !toub-convert , !toub-minigame
