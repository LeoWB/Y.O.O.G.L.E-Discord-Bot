import discord
import os
import time
import discord.ext
from discord.ext import commands, tasks
import random
import deathMessage

secret_token = os.environ['TOKEN']

bot = commands.Bot(command_prefix = '~')
bot.remove_command('help')

@bot.event
async def on_ready():
    print("bot online") #will print "bot online" in the console when the bot is online

#help commands:

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
   
#account commands:

#search commands:

#fun commands:

@bot.command()
async def ez(ctx):
  
  ez_Quotes = ["no u", "who asked", "hello world"]
  chosen_Quote = ez_Quotes[random.randint(0, (len(ez_Quotes) - 1))]

  await ctx.channel.send(chosen_Quote)

#interact commands:


@bot.command()
async def hug(ctx, user:discord.Member):
  await ctx.channel.send(f"**{ctx.message.author.name} hugs {user.name}**")

@bot.command()
async def hypixel(ctx):
  await ctx.channel.send(f"Anyone for some hypixel.\n")

@bot.command()
async def kill(ctx, user:discord.Member):

  death_Messages = deathMessage.generate(user.name, ctx.message.author.name)
  
  the_Death_Message = death_Messages[random.randint(0, (len(death_Messages) - 1))]
  await ctx.channel.send(the_Death_Message)
  


bot.run(os.getenv("TOKEN"))