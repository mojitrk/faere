import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('<:uditmass:915055277500428309>'):
        await message.channel.send('<@594361076880113683>')

client.run('TOKEN')
