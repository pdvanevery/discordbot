#import discord and commands
from dotenv import load_dotenv
import discord
from discord.ext import commands
import random

load_dotenv()

import os

bot_token = os.getenv('BOT_TOKEN')

#set intents for bot
intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.messages = True
intents.guilds = True
intents.reactions = True

#create instance of bot and the command prefix
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello! How can I assist you?')

bot.run(bot_token)