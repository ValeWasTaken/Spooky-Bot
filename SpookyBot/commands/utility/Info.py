from command import Command
import discord
from re import search

class Info(Command):
    def __init__(self, client):
        super().__init__(client)
        self.name = 'info'
        self.description = 'Provides information on a Discord user.'

    async def run(self, message, args):
        id
        if not args[0]:
            id = message.author.id
        else:
            id = search(r'<@!?(\d+)>', args[0]).groups()[0]

        user = self.client.get_member(id)

        embed = discord.Embed(title="{}'s info".format(user.name), description=\
                              "Here's what I could find.", color=0x00ff00)
        embed.add_field(name="Name", value=user.name, inline=True)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Status", value=user.status, inline=True)
        embed.add_field(name="Highest role", value=user.top_role)
        embed.add_field(name="Joined", value=user.joined_at)
        embed.set_thumbnail(url=user.avatar_url)

        await self.client.send_message(message.channel, embed=embed)
