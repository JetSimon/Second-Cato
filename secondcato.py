import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    print(message.author)
    if str(message.author) == "Cato#1946":
        await message.channel.send(message.content)

@client.event
async def on_message_edit(before, after):
    if str(after.author) == "Cato#1946":
        await message.channel.send("Cato Edited: " + before.content+ "\n\nNow Says: " + after.content)

client.run(TOKEN)

