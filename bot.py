import discOMEGALULrd
from discord.ext import commands

client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready():
    print('Bot is ready')
    print('Smile')


with open("config.ini", "r+") as file:
    client.run(file.readline())

# No changes :)
