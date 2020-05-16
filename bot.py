import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = 'hive.')


@client.command()
async def load(ctx, extension):
    client.load_extension('cogs.{}'.format(extension))


@client.command()
async def unload(ctx, extension):
    client.unload_extension('cogs.{}'.format(extension))


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension('cogs.{}'.format(filename[:-3]))


with open("config.ini", "r+") as file:
    client.run(file.readline())

# This is a change :)
# OMEGASMILE
