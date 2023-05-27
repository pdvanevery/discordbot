import discord
from dotenv import load_dotenv

#load environment variables from the .env file
load_dotenv()

#retrieve the bot token from env variables in code
import os
bot_token = os.getenv('BOT_TOKEN')


#define intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

#create client object
client = discord.Client(intents=intents)

#tells us that bot is up and ready
@client.event
async def on_ready():
    print(f'{client.user} is running!')

if __name__ == '__main__':
    #start the bot
    client.run(bot_token)