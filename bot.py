import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready():
    print('Bot is ready')
    print('Smile')


with open("config.ini", "r+") as file:
    client.run(file.readline())

# This is a change :)
# Cock and ball torture (CBT), penis torture or dick torture is a sexual activity involving application of pain or constriction to the penis or testicles. This may involve directly painful activities, such as genital piercing, wax play, genital spanking, squeezing, ball-busting, genital flogging, urethral play, tickle torture, erotic electrostimulation, kneeing or kicking.[1] The recipient of such activities may receive direct physical pleasure via masochism, or emotional pleasure through erotic humiliation, or knowledge that the play is pleasing to a sadistic dominant. Many of these practices carry significant health risks
