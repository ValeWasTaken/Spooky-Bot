# Python 3.6.5
from command import Command
from random_fact import random_fact


class Magic8ball(Command):

    def __init__(self, client):
        super().__init__(client)
        self.name = '8ball'
        self.brief = 'Provides magical *totally* accurate yes/no/maybe answers.'
        self.description = '!8ball returns a most definitely accurate and '\
                            '*totally* not completely random answer to any '\
                            'yes/no/maybe question. To call this command just '\
                            'type "!8ball" or "!8ball Your question here"'

    async def run(self, message, args):
        await self.client.send_message(message.channel, 
                random_fact('8ball_answers'))
