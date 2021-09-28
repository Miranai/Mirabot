import os
import discord

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('lala'):
    await message.channel.send('<a:lalaJAM:879412508371349524>')

client.run(os.environ['TOKEN'])