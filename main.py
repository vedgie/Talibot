import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

intents = nextcord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

client = nextcord.Client(intents=intents)
taliServerID = 1159668784785788969
channelID = 834528598379593728
prefix = 'i blame'
reaction_word = 'talibot'
reaction_emoji = '👀'

@client.event
async def on_ready():
    print("Bot is now active")
    print(f"Connected to server with ID: {taliServerID}")
    print("-------------------")

@client.event
async def on_message(message):
    if message.content and message.channel.id == 834528598379593728:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} | Author: {message.author.name} | Message: {message.content}")

        if message.content.lower().startswith(prefix.lower()):
            print("Attempting to send response")
            await message.channel.send(':NODDERS:')

    if reaction_word.lower() in message.content.lower():
        await message.add_reaction(reaction_emoji)
  
client.run(os.getenv('BOT_TOKEN'))