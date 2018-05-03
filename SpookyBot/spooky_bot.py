# Spooky Bot Version 0.5.331
# Written in Python 3.6.4
import sys
import discord
from discord.ext import commands

import configparser
config = configparser.ConfigParser()
config.read('auth.ini')

initial_extensions = ['cogs.fun', 'cogs.reference', 'cogs.utility']

bot = commands.Bot(command_prefix='b!', description=
                   "Spooky Bot - So good it's spooky!", pm_help=True)
client = discord.Client(max_messages=100)


@bot.event
async def on_ready():
    print('Logged in as: ')
    print(bot.user.name)
    await bot.change_presence(game=discord.Game(name='spooky music'),
                              status=discord.Status.online)

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file = sys.stderr)
            traceback.print_exc()

bot.run(config.get('discord', 'token'))
