# Python 3.6.5
from command import Command
from random_fact import random_fact


class Batfact(Command):

    def __init__(self, client):
        super().__init__(client)
        self.name = 'batfact'
        self.description = 'Says a random bat fact!'

    async def run(self, message, args):
        await self.client.send_message(message.channel, random_fact('bat'))