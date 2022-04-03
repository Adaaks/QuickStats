from datetime import datetime
import os
import discord
import asyncio
import configparser
from colorama import init, Fore, Back, Style
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord.ext import commands, tasks
from discord.ext.commands.core import command
import time
import urllib.request
from PIL import Image

config = configparser.ConfigParser()
config.read_file(open(r"Config.ini"))
token = str(config.get("auth","bot_token"))
timeamount = int(config.get("optional","delay"))

profile = str(config.get("optional","default_profile_picture"))
username = str(config.get("optional","default_username"))

percent3 = 0
namegame = ""
init()
highscore = 0
notepad = ""
placeid = 0
channelid = 0

test = "False"
test1 = "False"

enemy = 0
enemycheck="False"

goale = 0
goalcheck= "False"

client = commands.Bot(command_prefix= '/')
slash = SlashCommand(client,sync_commands =True)

# Saves Data
with open('Database/gameid.txt','r') as file:
    read = file.read()
    placeid = int(read)
    file.close()
    pass
  
with open('Database/gameid.txt','w') as file:
  write = file.write(str(placeid))
  file.close()
  pass

# channel id

with open('Database/channelid.txt','r') as file:
    read = file.read()
    channelid = int(read)
    file.close()
    pass
  
with open('Database/channelid.txt','w') as file:
  write = file.write(str(channelid))
  file.close()
  pass

# goal id

with open('Database/goalid.txt','r') as file:
    read = file.read()
    goale = int(read)
    file.close()
    pass
  
with open('Database/goalid.txt','w') as file:
  write = file.write(str(goale))
  file.close()
  pass

## goal check
with open('Database/goalcheck.txt','r') as file:
    read = file.read()
    goalcheck = str(read)
    file.close()
    pass
  
with open('Database/goalcheck.txt','w') as file:
  write = file.write(str(goalcheck))
  file.close()
  pass

# objective

with open('Database/objectiveid.txt','r') as file:
    read = file.read()
    enemy = str(read)
    file.close()
    pass
  
with open('Database/objectiveid.txt','w') as file:
  write = file.write(str(enemy))
  file.close()
  pass

## bool values

with open('Database/enemycheck.txt','r') as file:
    read = file.read()
    enemycheck = str(read)
    file.close()
    pass
  
with open('Database/enemycheck.txt','w') as file:
  write = file.write(str(enemycheck))
  file.close()
  pass

# saves test val
with open('Database/test.txt','r') as file:
    read = file.read()
    test = str(read)
    file.close()
    pass
  
with open('Database/test.txt','w') as file:
  write = file.write(str(test))
  file.close()
  pass
# saves test val1
with open('Database/test1.txt','r') as file:
    read = file.read()
    test1 = str(read)
    file.close()
    pass
  
with open('Database/test1.txt','w') as file:
  write = file.write(str(test1))
  file.close()
  pass

@slash.slash(name="write", description ='to add a message to notepad')
async def notepad(ctx, notes:str):
    
    global notepad
    message = str(notes)+'\n'
    with open('Database/notepad.txt','a') as file:
        
            
        write = file.write(str(message))
        file.close()
        pass
    await ctx.send("✅ **Added message to notepad**")

@slash.slash(name="view", description ='to view notepad')
async def view(ctx):
    global notepad
    
    with open('Database/notepad.txt','r') as file:
        
        read = file.read()
        notepad = str(read)
        file.close()
        pass

    if not notepad:
        await ctx.send(":x: **Your notepad is empty!**")
    else:
        await ctx.send(notepad)

@slash.slash(name="clear", description ='to clear notepad')
async def clear(ctx):
    global notepad
    
    with open('Database/notepad.txt','w') as file:
        
            
        write = file.write("")
        file.close()
        pass
    await ctx.send(":wastebasket: **Cleared notepad**")









           

# gets the place id
@slash.slash(name="game", description ='to set a game id - to track')
async def place(ctx, game:int):
    global placeid
    placeid = str(game)
    global test
    test = "True"
    if game < 1:
        test = "False"
        await ctx.send("❌ **Game has been removed!**")
        print(Fore.RED + "Game ID has been removed")
        with open('Database/gameid.txt','w') as file:
          write = file.write(str(placeid))
          file.close()
          pass

          with open('Database/test.txt','w') as file:
           write = file.write(str(test))
           file.close()
           pass
    else:
        with open('Database/gameid.txt','w') as file:
          write = file.write(str(placeid))
          file.close()
          pass

          with open('Database/test.txt','w') as file:
           write = file.write(str(test))
           file.close()
           pass
           print(Fore.CYAN + "Game ID has been set")
           await ctx.send("✅ **Set successfully to "+str(placeid)+"!**")

@slash.slash(name="goal", description ='to set a visits goal')
async def goal(ctx, visits:int):
    global goale
    global goalcheck
    goale = str(visits)
    goalcheck = "True"
    

    if int(goale) == 0:
        goalcheck = "False"

        with open('Database/goalid.txt','w') as file:
            
            write = file.write(str(goale))
            file.close()
            pass
        with open('Database/goalcheck.txt','w') as file:
            write = file.write(str(goalcheck))
            file.close()
            pass
        await ctx.send("❌ **Goal has been removed!**")
        print(Fore.RED +"Goal has been removed")
    else:
        with open('Database/goalid.txt','w') as file:
          write = file.write(str(goale))
          file.close()
          pass
          with open('Database/goalcheck.txt','w') as file:
              write = file.write(str(goalcheck))
              file.close()
              pass
          print(Fore.CYAN +"Goal has been set")
          await ctx.send("✅ **Set successfully to "+str(goale)+"!**")

@slash.slash(name="enemy", description ='to set a enemy')
async def objective(ctx, enemyid:int):
    global enemy
    global enemycheck
    enemy = str(enemyid)
    enemycheck = "True"

    if int(enemy) == 0:
        enemycheck = "False"
        with open('Database/enemycheck.txt','w') as file:
          write = file.write(str(enemycheck))
          file.close()
          pass
          print(Fore.RED +"Enemy has been removed")
          await ctx.send("❌ **Enemy has been removed")
    else:
    
        with open('Database/objectiveid.txt','w') as file:
          write = file.write(str(enemy))
          file.close()
          pass

        with open('Database/enemycheck.txt','w') as file:
          write = file.write(str(enemycheck))
          file.close()
          pass
        print(Fore.CYAN +"Enemy has been set")
        
        await ctx.send("✅ **Set successfully to "+str(enemy)+"!**")


@slash.slash(
    
    name="channel",
    description ='to set the channel',
    guild_ids=[],
    options=[
        create_option(
            name ="channel",
            description="Select a channel",
            required = True,
            option_type = 7,
        )
    ]
)
async def channel(ctx:SlashContext, channel:int):
    global channelid
    channelid = int(channel.id)
    global test1
    test1 = "True"


    
    
    with open('Database/channelid.txt','w') as file:
      write = file.write(str(channelid))
      file.close()
      pass

    

    with open('Database/test1.txt','w') as file:
      write = file.write(str(test1))
      file.close()
      pass
    print(Fore.CYAN +"Channel has been set")
    await ctx.send("✅ **Set successfully to <#"+str(channelid)+">!**")


@slash.slash(name="help", description ='to receive help about the bot')
async def help(ctx):
    await ctx.send(" :question: __**Help**__ :question:\n/channel - sets the channel for the bot to send game statistic updates to!\n/game - set your game place id, found on the url /games/yourid\n/goal - to set a visits goal (optional)\n/enemy - to set a enemy place (optional)\n\n/config - displays the current bot settings\n\n:notepad_spiral: **Notepad** :notepad_spiral:\n/write - writes to notepad\n/view -  views notepad\n/clear - clears notepad\n\n- This bot will send statistic updates every 60 seconds!")
@slash.slash(name="config", description ='to get current bot settings')
async def config(ctx):
    await ctx.send(" :gear: __**Configuration**__ :gear:\nGame ID = "+ str(placeid) +"\nChannel: <#"+str(channelid)+">"+"\nGoal: "+str(goale)+"\nEnemy: "+ str(enemy))

  
@tasks.loop(seconds = 1)
async def myStats():   
    try:
        channelz = client.get_channel(channelid)
        
        ##########################################
        ##########################################
        ##########################################
        ##########################################
        ##########################################
        ##########################################
        ##########################################
        ##########################################
        ##########################################
        ##########################################

        import requests
        global namegame

        # Your Game
        response22 = requests.get('https://www.roblox.com/places/api-get-details?assetId='+str(placeid))
        gamed = response22.json()
        game23 = gamed['TotalUpVotes']
        favcount = gamed['FavoritedCount']
        lastupdated = gamed['Updated']
        game2a = gamed['OnlineCount']
        game2 = gamed['VisitedCount']
        game23z = gamed['TotalDownVotes']
        namegame = gamed['Name']
        getuniverseid = gamed['UniverseId']
        
        imageur = requests.get('https://thumbnails.roblox.com/v1/games/icons?universeIds='+str(getuniverseid)+'&size=150x150&format=Png&isCircular=false')
        imaged2 = imageur.json()
        iconting = imaged2['data'][0]['imageUrl']

        thumbnailz = requests.get("https://thumbnails.roblox.com/v1/games/multiget/thumbnails?universeIds="+str(getuniverseid)+"&size=768x432&format=Png&isCircular=false")
        thumbjason = thumbnailz.json()
        thumbnail = thumbjason['data'][0]["thumbnails"][0]['imageUrl']
        
       

        # Gets the main colours of the icon, to set for the embed colour
        urllib.request.urlretrieve(iconting,'Database/gameicon.png')
        def most_common_used_color(img):
            width, height = img.size
            r_total = 0
            g_total = 0
            b_total = 0
            count = 0
            for x in range(0, width):
                for y in range(0, height):
                    r, g, b = img.getpixel((x, y))
                    r_total += r
                    g_total += g
                    b_total += b
                    count += 1
            return (r_total/count, g_total/count, b_total/count)
        img = Image.open('Database/gameicon.png')
        img = img.convert('RGB')
        common_color = most_common_used_color(img)
        def rgb_to_hex(rgb):
            return '#%02x%02x%02x' % rgb
        r = int(common_color[0])
        g = int(common_color[1])
        b = int(common_color[2])
        hexcode = rgb_to_hex((r,g,b))
        hexcode = hexcode[1:len(hexcode)]
        intcode = int(hexcode, 16)


        if enemycheck == "True":
            
           #Objective
            response1 = requests.get('https://www.roblox.com/places/api-get-details?assetId='+str(enemy))
            gamez = response1.json()
            game3 = gamez['VisitedCount']
            peasant = gamez['Builder']
            
            # To set if your behind or in-front of your objective
            viszts = ""

            final = game3 - game2
            
            
            if final > 0:
              viszts = "visits behind"
              decider = "-"
            else:
              viszts = "visits in-front of"
              final = final + abs(final)+ abs(final)
              decider = "+"
          
        total = game23z + game23
        try:
          global percent3
          percent = game23 / total
        
        
          percent2 = percent * 100
          percent3 = int(percent2)
        except ZeroDivisionError:
          print("Zero Division Error")
        
      # Getting the highscore for the most players played at once
        global highscore
        with open('Database/playinghighscore.txt','r') as file:
          read = file.read()
          highscore = int(read)
          file.close()
          pass
        
        
        if game2a > highscore:
          with open('Database/playinghighscore.txt','w') as file:

            write = file.write(str(game2a))
            
            file.close()
            pass
        

        month, day, year = str(lastupdated).split('/')
        new_date = f'{day}/{month}/{year}'
        commavisits = "{:,}".format(game2)
        commaplays = "{:,}".format(game2a)
        
        if enemycheck == "True":
            commaobjective = "{:,}".format(final)
        commalikes = "{:,}".format(game23)
        commafavs = "{:,}".format(favcount)
        global goalcheck
        
        if goalcheck == "True":
            
            commagoal = "{:,}".format(int(goale))
            goalamount = int(goale)-int(game2)
            commagoalleft = "{:,}".format(goalamount)
            if goalamount > 0:
              goalmsg = str(commagoalleft) + " visits left"
              
            else:
              goalmsg = "✅ Goal met!"
              
             
            
            
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        embed = discord.Embed(title=str(namegame), description=':star: '+ str(commafavs),color=intcode)
        embed.set_author(name='Statistics', url='https://www.roblox.com/games/'+str(placeid), icon_url=str(iconting))
        embed.set_footer(text='Sent at ' + str(current_time))
        embed.timestamp = discord.Embed.Empty
        embed.add_field(name='Likes', value=str(commalikes)+' ('+str(percent3)+'%)')
        embed.add_field(name='Playing', value=str(commaplays)+' ('+str(highscore)+')')
        embed.add_field(name='Visits', value=str(commavisits))
        
        if goalcheck == "True":
           
            embed.add_field(name='Goal', value="["+str(commagoal)+"] "+str(goalmsg))

        if enemycheck == "True":
            embed.add_field(name='Enemy', value=str(decider)+str(commaobjective) + ' ' +  viszts + ' ' +"@"+ peasant)
        embed.set_image(url = thumbnail)

        await channelz.send(embed=embed)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='over ' +str(namegame)))
        print(Fore.MAGENTA +"Sent a statistic")
        await asyncio.sleep(timeamount)
    except AttributeError:
        print(Fore.RED +"Attribute Error (an issue within the statistic loop)")
        
        #########################################
        ##########################################
        ##########################################
        ##########################################
        ##########################################
        ##########################################
        ##########################################
        ##########################################
        ##########################################
        ##########################################

@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send("<@"+str(guild.owner_id)+">"+ ":wave: **Hey! I'm QuickStats!**\nPlease execute the following commands to get up & running:\n-/game (your game place id)\n-/channel (mention the channel you wish updates to be shown)")
        break

@client.event
async def on_ready():
     if profile == "true":
         pfp_path = "Database/QuickStatsIcon.png"
         fp = open(pfp_path, 'rb')
         pfp = fp.read()
         await client.user.edit(avatar=pfp)
     if username == "true":
        await client.user.edit(username="QuickStats")

     await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='over games'))
     print(Fore.GREEN +"Bot: Online")
     @tasks.loop(seconds = 3)
     async def myCheck():
         
         global test
         global test1    
         if test == "True" and test1 == "True" and not myStats.is_running():
             myStats.start()
             print(Fore.GREEN +"Status: Statistics enabled")    
         elif test == "False" and test1 == "False":
             print(Fore.RED +"Status: Not running" + Fore.YELLOW + "\n\nConfigure via:\n/game (your placeid)\n/channel (channel to send stats)\n\nAdditional optional commands can be seen via /help")
             myStats.cancel()
     myCheck.start()
     
@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        await message.channel.send(message.author.mention + " - " + "My prefix is **/**")

    await client.process_commands(message)

try:
    
    client.run(token)
except:
    print(Fore.RED + "[ERROR] Please insert your BOT TOKEN in config.ini < auth < bot_token")
    time.sleep(5)
    quit()
