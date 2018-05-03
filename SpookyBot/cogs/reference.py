import discord
from discord.ext import commands

import os
import sys
sys.path.append(os.path.realpath('./cogs/reference'))

import crypto
# import imgur_upload
import wolfram_alpha
import urban_define

class ReferenceCommands:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def answer(self, *args):
        # Feeds the user input into Wolfram Alpha for an answer.
        if not args:
            await self.bot.say('Please ask a question Wolfram Alpha can answer!')
        try:
            question = ' '.join(args)
            await self.bot.say(wolfram_alpha.solve(question))
        except Exception as e:
            print(f'User generated the error {e} after entering: "{args}"')
            await self.bot.say("I couldn't find an answer for that, sorry. :(")

    @commands.command()
    async def imgur(self, *args):
        """Scrapes a given sub-reddit for pictures and uploads them into
        an Imgur album."""
        await self.bot.say(imgur_upload.main(args))

    @commands.command()
    async def ud(self, *args):
        """Defines a word using UrbanDictionary.com"""
        if not args:
            await self.bot.say('Please make sure you use the correct format: !ud word')
        try:
            definition = urban_define.ud_define(' '.join(args))
            embed = discord.Embed(title="Here is your Urban "
                                        "Dictionary definition!", color=0x00ff00)
            embed.add_field(name="Word", value=definition[0], inline=True)
            embed.add_field(name="Meaning", value=definition[1], inline=True)
            embed.add_field(name="Example", value=definition[2], inline=True)
            embed.add_field(name="Upvotes", value=definition[3])
            embed.add_field(name="Downvotes", value=definition[4])
            await self.bot.say(embed=embed)
        except Exception as e:
            print(f'User generated the error {e} after entering: "{args}"')
            await self.bot.say("Sorry, your word or phrase wasn't found. :(")

    @commands.command()
    async def check(symbol: str = None):
        if not symbol:
            await self.bot.say("Please use the correct format: '!check symbol'"
                          "\nEx: '!check BTC' to check Bitcoin stats.")
        else:
            try:
                symbol = symbol.upper()
                rank, crypto_name, sign, worth, change = crypto.crypto_info(symbol)
                embed = discord.Embed(title=f"{crypto_name} info", color=0x00ff00)
                embed.add_field(name="Rank: ", value=rank)
                embed.add_field(name="Symbol: ", value=sign)
                embed.add_field(name="Price (24h change)",
                                value=f"{worth} ({change})")
                await self.bot.say(embed=embed)
            except Exception as e:
                print(f'User generated the error {e} after entering: {symbol}')
                await self.bot.say("Please use the correct format: '!check symbol'"
                              "\nEx: '!check BTC' to check Bitcoin stats.")

def setup(bot):
    bot.add_cog(ReferenceCommands(bot))
