import discord
import os
import random
import requests
import json
from discord.ext import commands
import asyncio
import logging
from keep_alive import keep_alive

client = discord.Client()

hello_words = ["hello","hi","hey","Hey","Hello","Hi"]

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    #if message.content.startswith("Hello"):
    #    await message.channel.send(f"Hello {message.author.mention}!")
  
    if message.content.startswith("Hello"):
        await message.channel.send(f"Hello {message.author.mention}!")

    if message.content.startswith("hello"):
        await message.channel.send(f"Hello {message.author.mention}!")

    if message.content.startswith("Hey"):
        await message.channel.send(f"Hello {message.author.mention}!")

    if message.content.startswith("hey"):
        await message.channel.send(f"Hello {message.author.mention}!")

    if message.content.startswith("hi"):
        await message.channel.send(f"Hello {message.author.mention}!")

    if message.content.startswith("Hi"):
        await message.channel.send(f"Hello {message.author.mention}!")

    #if message.content.startswith('Hey'):
    #   await message.channel.send('Hello!')

    #user = discord.utils.get(client.users, name="USERNAME", discriminator="1234")
    #if user is None:
    #  print("User not found")
    #else:
    #  await message.channel.send(f"{user.mention} is the best")

    #if any(word in msg for word in hello_words):
    #    await message.channel.send(f"Hello {message.author.mention}!")


#@client.event
#async def on_member_join(member):
#  channel = discord.utils.get(member.guild.channels, name= "💬general-talk")
#  await channel.send(f"{member.mention} welcome to Virtual Campus!\n")

@client.event
async def on_member_join(member):
  guild = client.get_guild(788721702225444864)
  channel = guild.get_channel(958562911670927430)
  await channel.send(f"Welcome to the {guild.name} server {member.mention}! :partying_face:")
  await member.send(f"Welcome to the {guild.name} server, {member.mention}! :partying_face:")


keep_alive()
client.run(os.getenv('TOKEN'))
