# I worked too hard on this for what it's worth
# But I did want to learn discord bots so this was a good tutorial
# ur mum lole

import nextcord
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

intents = nextcord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

client = nextcord.Client(intents=intents)
taliServerID = 792511515574927452
channelID = 834528598379593728
prefix = 'i blame'
reaction_word = 'talibot'
reaction_emoji = '👀'
custom_emoji_name = 'NODDERS'

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
            custom_emoji = nextcord.utils.get(message.guild.emojis, name=custom_emoji_name)
            await message.channel.send(str(custom_emoji))

    if reaction_word.lower() in message.content.lower():
        await message.add_reaction(reaction_emoji)
  
client.run(os.getenv('BOT_TOKEN'))