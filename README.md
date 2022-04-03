# Python Based
# QuickStats
This is a discord bot, which provides you with your roblox's game statistics

# Setup 

- Download the file as .ZIP

- Open Setup.py, to install all required modules to successfully run the program with no issues
- Afterwards, open Config.ini - assign your bot token and you have the ability to change the delay in between each statistic update (recommended is 60 seconds)

- You're now ready to open up QuickStats.py, it will prompt you to add a Game ID + Channel for the statistics to be sent, follow the steps below in a channel:
  - Write /game (game id of game you wish to track)
  - Write /channel (channel mention of place for statistics to appear
- Once completed, and program is still open it will send a statistic in the chosen channel

# Commands

- /channel - sets the channel for the bot to send game statistic updates to!
- /game - set your game place id, found on the url /games/yourid
- /goal (visits goal) = displays a goal and how far you are away from the chosen visit count
- /enemy (enemy place id) = displays how far you are away/ahead from another places place in visits

- /write (message) = stores a message in a text file
- /view = displays the text inside your notepad
- /clear = clears all messages from notepad

- /config = displays your current config (game, channel, goal, enemy)

# Features

- This bot will set the embed colour to the average colour used in your games icon, to match it up and make it look pretty
- Displays the peak of the highest concurrent players
- Stores all data inputted into a database(folder), with text files to save all the settings when you shut down the bot
- Comes with a default profile picture and username, once you run the bot (disable if not wanted via Config.ini)

# Example:
![alt text](https://cdn.discordapp.com/attachments/846481615278702602/960271532469387364/Screenshot_2022-04-03_211508.png)
