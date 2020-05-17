import discord
from discord.ext import commands


class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is ready')
        print('Smile')

    #Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong! {}ms'.format(round(self.client.latency * 1000)))

    @commands.command(aliases = ['8ball', 'text'])
    async def _8ball(self, ctx, *, question):
        response = 'KEKW'
        await ctx.send('Question: {}\nAnswer: {}'.format(question, response))


def setup(client):
    client.add_cog(Example(client))
