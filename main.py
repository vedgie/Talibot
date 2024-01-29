# I worked too hard on this for what it's worth
# But I did want to learn discord bots so this was a good tutorial
# ur mum lole

import nextcord
from nextcord.ext import commands
from datetime import datetime
import os
from dotenv import load_dotenv
import re
import random

load_dotenv()

intents = nextcord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
intents.guilds = True

client = nextcord.Client(intents=intents)
taliServerID = 792511515574927452
prefix = 'i blame'
reaction_word = 'talibot'
reaction_emoji1 = '👀'
reaction_emoji2 = "🌭"
custom_emoji_name = 'NODDERS'

def contains_url(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return bool(url_pattern.search(text))

@client.event
async def on_ready():
    print("Bot is now active")
    print("Guilds:")
    for guild in client.guilds:
        print(f"- {guild.name} (ID: {guild.id})")
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

    if message.author.name == 'mrtalidar' and message.channel.id ==  792638579792543745:
        if message.attachments or message.embeds or contains_url(message.content):
            await message.add_reaction(reaction_emoji2)
    
    if reaction_word.lower() in message.content.lower():
        await message.add_reaction(reaction_emoji1)

    if isinstance(message.channel, nextcord.DMChannel) and message.author != client.user:
        try:
            channel_id, message_content = map(str.strip, message.content.split(maxsplit=1))
            channel_id = int(channel_id)
            channel = client.get_channel(channel_id)
            if channel:
                await channel.send(message_content)
                await message.author.send(f"Message sent to <#{channel_id}> successfully!")
            else:
                await message.author.send(f"Channel with ID {channel_id} not found")
        except ValueError:
            await message.author.send("Invalid format. Please provide channel ID and message.")

@client.slash_command(name="roll", description="Choose a die to roll")
async def roll(interaction: nextcord.Interaction):
    #
    pass

@roll.subcommand(name="custom", description="Custom die roll")
async def customdie(interaction: nextcord.Interaction, die_number = int):
  # Maybe validate and return some message?
  die_size = int(die_number)
  if die_size <=1 or die_size > 1000000:
    await interaction.send(f"Don't put stupid numbers, you know what you did. Fuccin idiot.")
    return

  result = random.randint(1, die_size)
  message = f"You rolled a {result}"
  await interaction.send(message)

client.run(os.getenv('BOT_TOKEN'))