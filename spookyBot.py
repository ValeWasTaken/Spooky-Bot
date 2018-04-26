# Spooky Bot Version 0.5.20
# Written in Python 3.6.4
import discord
from discord.ext import commands
import wolfram_alpha

# Self-made functions / libraries
from is_it_halloween import is_it_halloween
from f_random import f_roll, f_flip
from f_facts import f_facts
import urban_define
import shorten_url
import f_commands
import imgur_upload

bot = commands.Bot(command_prefix='!', description=\
                   "Spooky Bot - So good it's spooky!", pm_help=True)
client = discord.Client(max_messages=100)

@bot.event
async def on_ready():
    print('Logged in as: ')
    print(bot.user.name)
    await bot.change_presence(game=discord.Game(name='spooky music'),\
                              status=discord.Status.online)
 
@bot.command()
async def halloween():
    await bot.say(is_it_halloween())

@bot.command()
async def batfact():
    await bot.say(f_facts('bat'))

@bot.command()
async def commands(query : str=None):
    if not query:
        await bot.say(f_commands.help('commands'))
    try:
        await bot.say(f_commands.help(query))
    except Exception as e:
        print(f'User generated the error {e} after entering {query} in help.')
        await bot.say('Sorry, something went wrong. :(')

@bot.command()
async def roll(num : str=None):
    if not num or not num[0].isdigit() and not num[0].startswith('-'):
        await bot.say(f_roll(100))
        return
    try:
        await bot.say(f_roll(int(num)))
    except Exception as e:
        print(f'User generated the error {e} after entering: "{num}')
        await bot.say(f'Please use the correct format: !roll number')

@bot.command()
async def flip(num : str=None):
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
    await bot.say(imgur_upload.main(args))

@bot.command()
async def answer(*args):
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
    if not args:
        await bot.say('Please make sure you use the correct format: !ud word')
    try:
        definition = urban_define.ud_define(' '.join(args))
        embed = discord.Embed(title="Here is your Urban "\
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
