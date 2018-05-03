import discord
from discord.ext import commands as comm

import os
import sys
sys.path.append(os.path.realpath('./cogs/utility'))

import random_util as rand
import shorten_url
import command_help

class UtilityCommands:
    def __init__(self, bot):
        self.bot = bot

    @comm.command()
    async def commands(self, query: str=None):
        """Returns a list of commands or information about specific commands."""
        if not query:
            await bot.say(command_help.h('commands'))
        try:
            await bot.say(command_help.h(query))
        except Exception as e:
            print(f'User generated the error {e} after entering {query} in commands.')

    @comm.command()
    async def roll(self, num: str=None):
        """Rolls a random number for the user."""
        if not num or not num[0].isdigit() and not num[0].startswith('-'):
            await self.bot.say(rand.roll(100))
            return
        try:
            await self.bot.say(rand.roll(int(num)))
        except Exception as e:
            print(f'User generated the error {e} after entering: "{num}""')
            await self.bot.say(f'Please use the correct format: !roll number')

    @comm.command()
    async def flip(self, num: str=None):
        """Flips coins to determine heads or tails for the user."""
        if not num or not num[0].isdigit() and not num[0].startswith('-'):
            await self.bot.say(rand.flip(1))
            return
        try:
            await self.bot.say(rand.flip(int(num)))
        except Exception as e:
            print(f'User generated the error {e} after entering: "{num}"')
            await self.bot.say('Please use the correct format: !flip number')

    @comm.command()
    async def shorten(self, *args):
        """Reduces a URL length for the user."""
        if not args:
            await self.bot.say('Please make sure to use the correct format: !shorten link')
        try:
            url = ' '.join(args)
            result = shorten_url.get_tinyurl(url)
            await self.bot.say(f'Your shortened URL is: {result}')
        except Exception as e:
            print(f'User generated the error {e} after entering: "{args}"')
            await self.bot.say("Something went wrong, sorry! :(")

    @comm.command(pass_context=True)
    async def info(user: discord.Member):
        """Provides information about a user in the channel."""
        embed = discord.Embed(title="{}'s info".format(user.name), description=\
                              "Here's what I could find.", color=0x00ff00)
        embed.add_field(name="Name", value=user.name, inline=True)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Status", value=user.status, inline=True)
        embed.add_field(name="Highest role", value=user.top_role)
        embed.add_field(name="Joined", value=user.joined_at)
        embed.set_thumbnail(url=user.avatar_url)
        await self.bot.say(embed=embed)

def setup(bot):
    bot.add_cog(UtilityCommands(bot))
