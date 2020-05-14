import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'hive.')


@client.event
async def on_ready():
    print('Bot is ready')
    print('Smile')


@client.command()
async def ping(ctx):
    await ctx.send('Pong! {}ms'.format(round(client.latency * 1000)))


with open("config.ini", "r+") as file:
    client.run(file.readline())

# This is a change :)
# OMEGASMILE
