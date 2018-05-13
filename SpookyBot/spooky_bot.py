# Spooky Bot Version 0.5.4
# Written in Python 3.6.5
import sys
import os
import discord
from command_handler import CommandHandler
import configparser

# This allows importing of everything in the "./resources" directory
sys.path.append(os.path.realpath('./resources'))

# Get the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Create a discord client
client = discord.Client(max_messages=100)
# Create a command handler
handler = CommandHandler(client, config)
# Register all commands
handler.register_commands_in_dir('./commands')


@client.event
async def on_ready():
    print('Logged in as: ')
    print(client.user.name)
    await client.change_presence(game=discord.Game(name='spooky music'),
                                 status=discord.Status.online)


@client.event
async def on_message(message):
    # Handle commands
    await handler.handle(message)

client.run(config['Discord']['token'])
