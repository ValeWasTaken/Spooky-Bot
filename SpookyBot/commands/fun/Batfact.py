# Python 3.6.5
from command import Command
from random_fact import random_fact


class Batfact(Command):

    def __init__(self, client):
        super().__init__(client)
        self.name = 'batfact'
        self.brief = 'Says a random bat fact!'
        self.description = '!batfact returns a random fact about bats to the user. ' \
                           'There is currently over 70 facts, feel free to suggest more! '\
                           'To call this command type "!batfact"'

    async def run(self, message, args):
        await self.client.send_message(message.channel, random_fact('bat'))