# Spooky Bot Version 0.5.41
# Written in Python 3.6.5
import sys
import os
import discord
from command_handler import CommandHandler
import configparser


sys.path.append(os.path.realpath('./resources'))

# --- WILL BE REDUNDANT
for root, dirs, files in os.walk(r'./commands'):
    for dir in dirs[:3]:
        sys.path.append(os.path.realpath(f'{root}/{dir}'))
# ---

config = configparser.ConfigParser()
config.read('config.ini')

client = discord.Client(max_messages=100)
handler = CommandHandler(client, config)
handler.register_commands_in_dir('./commands')


@client.event
async def on_ready():
    print('Logged in as: ')
    print(client.user.name)
    await client.change_presence(game=discord.Game(name='spooky music'),
                                 status=discord.Status.online)


@client.event
async def on_message(message):
    await handler.handle(message)

client.run(config['Discord']['token'])
