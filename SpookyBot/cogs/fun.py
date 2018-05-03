import discord
from discord.ext import commands

import os
import sys
sys.path.append(os.path.realpath('./cogs/fun'))

from flip_text import flip_text
from is_it_halloween import is_it_halloween
from random_fact import random_fact

class FunCommands:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def batfact(self):
        """Returns random bat fact for the user."""
        await self.bot.say(random_fact('bat'))

    @commands.command()
    async def reverse(self, *args):
        if not args:
            await self.bot.say(flip_text('What do you want me to flip?'))
        else:
            message = ' '.join(args)
            await self.bot.say(flip_text(message))

    @commands.command()
    async def halloween(self):
        """Returns time until Halloween (PST) for the user."""
        await self.bot.say(is_it_halloween())

def setup(bot):
    bot.add_cog(FunCommands(bot))
