# Spooky Bot Version 0.5.30
# Written in Python 3.6.4
import discord
from discord.ext import commands
import wolfram_alpha

# Self-made functions / libraries
from is_it_halloween import is_it_halloween
from f_random import f_roll, f_flip
from f_facts import f_facts
import f_commands
import f_crypto
import imgur_upload
import urban_define
import shorten_url

bot = commands.Bot(command_prefix='!', description=
                   "Spooky Bot - So good it's spooky!", pm_help=True)
client = discord.Client(max_messages=100)


@bot.event
async def on_ready():
    print('Logged in as: ')
    print(bot.user.name)
    await bot.change_presence(game=discord.Game(name='spooky music'),
                              status=discord.Status.online)


@bot.command()
async def halloween():
    # Returns time until Halloween (PST) for the user.
    await bot.say(is_it_halloween())


@bot.command()
async def batfact():
    # Returns random bat fact for the user.
    await bot.say(f_facts('bat'))


@bot.command()
async def commands(query : str=None):
    # Returns a list of commands or information about specific commands.
    if not query:
        await bot.say(f_commands.help('commands'))
    try:
        await bot.say(f_commands.help(query))
    except Exception as e:
        print(f'User generated the error {e} after entering {query} in help.')
        await bot.say('Sorry, something went wrong. :(')


@bot.command()
async def roll(num : str=None):
    # Rolls a random number for the user.
    if not num or not num[0].isdigit() and not num[0].startswith('-'):
        await bot.say(f_roll(100))
        return
    try:
        await bot.say(f_roll(int(num)))
    except Exception as e:
        print(f'User generated the error {e} after entering: "{num}')
        await bot.say(f'Please use the correct format: !roll number')


@bot.command()
async def check(symbol: str = None):
    if not symbol:
        await bot.say("Please use the correct format: '!check symbol'"
                      "\nEx: '!check BTC' to check Bitcoin stats.")
    else:
        try:
            symbol = symbol.upper()
            rank, crypto_name, sign, worth, change = f_crypto.crypto_info(symbol)
            embed = discord.Embed(title=f"{crypto_name} info", color=0x00ff00)
            embed.add_field(name="Rank: ", value=rank)
            embed.add_field(name="Symbol: ", value=sign)
            embed.add_field(name="Price (24h change)",
                            value=f"{worth} ({change})")
            await bot.say(embed=embed)
        except Exception as e:
            print(f'User generated the error {e} after entering: {symbol}')
            await bot.say("Please use the correct format: '!check symbol'"
                          "\nEx: '!check BTC' to check Bitcoin stats.")


@bot.command()
async def flip(num : str=None):
    # Flips coins to determine heads or tails for the user.
    if not num or not num[0].isdigit() and not num[0].startswith('-'):
        await bot.say(f_flip(1))
        return
    try:
        await bot.say(f_flip(int(num)))
    except Exception as e:
        print(f'User generated the error {e} after entering: "{num}"')
        await bot.say('Please use the correct format: !flip number')


@bot.command()
async def imgur(*args):
    # Scrapes a given sub-reddit for pictures and uploads them into
    # an Imgur album.
    await bot.say(imgur_upload.main(args))


@bot.command()
async def answer(*args):
    # Feeds the user input into Wolfram Alpha for an answer.
    # Note to self, should probably replace *args here with question : str=None
    if not args:
        await bot.say('Please ask a question Wolfram Alpha can answer!')
    try:
        question = ' '.join(args)
        await bot.say(wolfram_alpha.solve(question))
    except Exception as e:
        print(f'User generated the error {e} after entering: "{args}"')
        await bot.say("I couldn't find an answer for that, sorry. :(")


@bot.command()
async def shorten(*args):
    # Reduces a URL length for the user.
    if not args:
        await bot.say('Please make sure to use the correct format: !shorten link')
    try:
        url = ' '.join(args)
        result = shorten_url.get_tinyurl(url)
        await bot.say(f'Your shortened URL is: {result}')
    except Exception as e:
        print(f'User generated the error {e} after entering: "{args}"')
        await bot.say("Something went wrong, sorry! :(")


@bot.command()
async def ud(*args):
    # Defines a word using UrbanDictionary.com
    if not args:
        await bot.say('Please make sure you use the correct format: !ud word')
    try:
        definition = urban_define.ud_define(' '.join(args))
        embed = discord.Embed(title="Here is your Urban "
                                    "Dictionary definition!", color=0x00ff00)
        embed.add_field(name="Word", value=definition[0], inline=True)
        embed.add_field(name="Meaning", value=definition[1], inline=True)
        embed.add_field(name="Example", value=definition[2], inline=True)
        embed.add_field(name="Upvotes", value=definition[3])
        embed.add_field(name="Downvotes", value=definition[4])
        await bot.say(embed=embed)
    except Exception as e:
        print(f'User generated the error {e} after entering: "{args}"')
        await bot.say("Sorry, your word or phrase wasn't found. :(")


@bot.command(pass_context=True)
async def info(user: discord.Member):
    # Provides information about a user in the channel.
    embed = discord.Embed(title="{}'s info".format(user.name), description=\
                          "Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)
    
    
bot.run("INSERT BOT'S SECRET TOKEN HERE")
