import discord
import responses
from dotenv import load_dotenv

#load environment variables from the .env file
load_dotenv()

#retrieve the bot token from env variables in code
import os
bot_token = os.getenv('BOT_TOKEN')

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


#define intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

def run_discord_bot():
    #create client object
    client = discord.Client(intents=intents)

    #tells us that bot is up and ready
    @client.event
    async def on_ready():
        print(f'{client.user} is awake!')
    
    @client.event
    async def on_message(message):
        #prevents infinite loop of messages
        if message.author == client.user:
            return
        
        #defined terms for debugging
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.content)

        print(f"{username} said: '{user_message}' ({channel})")

        #lets user get private message, if ? is at position 0
        if user_message[0] == '?':
            #returns message from position 1 onwards
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else: 
            await send_message(message, user_message, is_private=False)

    client.run(bot_token)