# Python 3.6.5
from random import randint
from command import Command


class Roll(Command):
    def __init__(self, client):
        super().__init__(client)
        self.name = 'roll'
        self.brief = 'Rolls a random number for you.'
        self.description = '!roll by default will return a random number '\
                           'between 1 and 100. However, you can roll for '\
                           'any amount 1000000 or less. To do so, type '\
                           '"!roll number" for example, "!roll 5000".'

    async def run(self, message, args):
        if not args or not args[0].isdigit() and not args[0].startswith('-'):
            await self.client.send_message(message.channel, self.roll(100))
            return
        try:
            await self.client.send_message(message.channel, self.roll(int(args[0])))
        except Exception as e:
            print(
                f'User generated the error {e} after trying to roll "{args[0]}"')
            await self.client.send_message(message.channel, 'Please use the correct format: !roll number')

    def roll(self, amount):
        # Generates a random number between 1 and the given amount.
        if amount < 1:
            return "You almost rolled something. You didn't. But you almost did."
        if amount == 1:
            return "Did you really need my help? It's one. You rolled a 1 out of 1."
        if amount > 1000000:
            return "Don't bully bots. You don't need to roll over "\
                "a million times. >:|"
        else:
            return f'You rolled a {randint(0, amount)} out of {amount}'
