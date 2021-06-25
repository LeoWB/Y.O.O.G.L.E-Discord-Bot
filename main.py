import discord
from discord import Color
import discord.ext
from discord.ext import commands, tasks

import os
import sys
import json
import math

import time
import random
import requests

import deathMessage

secret_token = os.environ['TOKEN']

bot = commands.Bot(command_prefix = '~')
bot.remove_command('help')

@bot.event
async def on_ready():
    print("bot online") #will print "bot online" in the console when the bot is online




#HELP CMDS:

@bot.command()
async def help(ctx):
  await ctx.channel.send("This is the Y.O.O.G.L.E, a bot which does random little things.\n\nHelp commands:\n~accountHelp - Gives useful information on account commands (not yet implemented)\n~searchHelp - gives useful information on search commands (not yet implemented)\n~funHelp - gives useful information on fun commands(not yet implemented)\n~interactHelp - gives useful information on interact commands")

@bot.command()
async def accountHelp(ctx):
  await ctx.channel.send("")

@bot.command()
async def searchHelp(ctx):
  await ctx.channel.send("") 

@bot.command()
async def funHelp(ctx):
  await ctx.channel.send("") 

@bot.command()
async def interactHelp(ctx):
  await ctx.channel.send("Interact commands are ways to interact with friends:\n~hug(discord name) - Gives someone a hug.")
   



#ACCOUNT CMDS:

#start here




#SEARCH CMDS:

#start here




#FUN CMDS:

#start here




@bot.command()
async def ez(ctx):
  
  ez_Quotes = ["no u", "who asked", "hello world", "Anyone else really like Rick Astley", "When u fall in climing and shatter ur elbow it is funny."]
  chosen_Quote = ez_Quotes[random.randint(0, (len(ez_Quotes) - 1))]

  await ctx.channel.send(chosen_Quote)

@bot.command()
async def giftNitroTo(ctx, user:discord.Member):
  time.sleep(3)

  embed = discord.Embed()
  embed.color=Color.red()
  embed.description = "Confirm Nitro Gift [here](https://youtu.be/dQw4w9WgXcQ)"
  await ctx.channel.send(embed=embed)

@bot.command()
async def giveTreeRoleTo(ctx, user:discord.Member):
  await ctx.channel.send("Requesting Connection . . .")

  time.sleep(random.randint(1, 3))

  await ctx.channel.send("Processing Command . . .")

  time.sleep(random.randint(1, 2))

  await ctx.channel.send(f"Upgrading {user.name}'s Role . . .")

  time.sleep(random.randint(2, 5))

  await ctx.channel.send("Done! Follow this link to complete captcha and confirm you are a human.")

  embed = discord.Embed()
  embed.color = Color.blue()
  embed.description = "[captcha](https://youtu.be/dQw4w9WgXcQ)"
  await ctx.channel.send(embed=embed)
  

#INTERACT CMDS:


@bot.command()
async def hug(ctx, user:discord.Member):
  await ctx.channel.send(f"**{ctx.message.author.name} hugs {user.name}**")

@bot.command()
async def slap(ctx, user:discord.Member):
  if ctx.message.author.name == user.name:
    await ctx.channel.send(f"**{ctx.message.author.name} commited suislap**")
  else:
    await ctx.channel.send(f"**{ctx.message.author.name} slapped {user.name}**")  


@bot.command()
async def hypixel(ctx):
  await ctx.channel.send(f"Anyone for some hypixel.\n")

@bot.command()
async def kill(ctx, user:discord.Member):

  death_Messages = deathMessage.generate(user.name, ctx.message.author.name)
  
  the_Death_Message = death_Messages[random.randint(0, (len(death_Messages) - 1))]
  await ctx.channel.send(the_Death_Message)
  



#DISCOVER CMDS:

@bot.command()
async def ISSLocation(ctx):
  issloc = requests.get("http://api.open-notify.org/iss-now.json")
  data = issloc.json()
  isslongitude = float(data["iss_position"]["longitude"])
  isslatitude = float(data["iss_position"]["latitude"])

  countries = requests.get("https://gist.githubusercontent.com/erdem/8c7d26765831d0f9a8c62f02782ae00d/raw/248037cd701af0a4957cce340dabb0fd04e38f4c/countries.json")

  closestcondis = 0
  closestcon = ""

  for i in countries.json():
    conlongitude = float(i["latlng"][0])
    conlatitude = float(i["latlng"][1])

    coorddif = [math.fabs(isslongitude - conlongitude), math.fabs(isslatitude - conlatitude)]

    coorddis = math.sqrt((coorddif[0] ** 2) + (coorddif[1] ** 2))

    if coorddis >= closestcondis:
      closestcondis = coorddis
      closestcon = i["name"]

  await ctx.channel.send(f"Longitude: **{isslongitude}**\nLatitude: **{isslatitude}**\nEstimated Closest Country: **{closestcon}**")

bot.run(os.getenv("TOKEN"))