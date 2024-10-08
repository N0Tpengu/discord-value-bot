import os
import discord

# Read the token from token.txt file
with open('token.txt', 'r') as file:
    TOKEN = file.read().strip()

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
