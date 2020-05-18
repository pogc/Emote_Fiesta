import discord
from discord.ext import commands
import sys
# sys.path.insert(1, '../.')
from emote_fetch import test_function
from emote_fetch import db_string


class Test(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def test(self, ctx):
        await ctx.send('test')

    @commands.command()
    async def emote(self, ctx, name):
        try:
            await ctx.send(test_function()[name])
        except KeyError:
            await ctx.send('No emote? SoBayed')

    @commands.command()
    async def emote_db(self, ctx, name):
        try:
            await ctx.send(db_string(name))
        except KeyError:
            await ctx.send('No emote? SoBayed')


def setup(client):
    client.add_cog(Test(client))

