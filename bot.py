import discord
DISCORD_TOKEN = 'MTEwODkyODQyODU3ODcwOTU5NQ.G2VeOK.yRlplAb_OIDOdOioOp8S4jwOT4RTOyWfAClPTw'

#define intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

#create client object
client = discord.Client(intents=intents)

if __name__ == '__main__':
    #start the bot
    client.run(DISCORD_TOKEN)