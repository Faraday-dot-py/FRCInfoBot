import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv("DISCORD_GUILD")

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    print("Recieved message")
    if message.author == client.user:
        return

    print(f"{message.content} ---")

    if message.content.lower() != None:
        print("Sent message")
        await message.channel.send(f"Hello @{message.id}")


client.run(TOKEN)