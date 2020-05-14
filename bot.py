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


@client.command(aliases = ['8ball', 'text'])
async def _8ball(ctx, *, question):
    response = 'KEKW'
    await ctx.send('Question: {}\nAnswer: {}'.format(question, response))


with open("config.ini", "r+") as file:
    client.run(file.readline())

# This is a change :)
# OMEGASMILE
