# Python 3.6.5
from random import randint
from command import Command


class Flip(Command):
    def __init__(self, client):
        super().__init__(client)
        self.name = 'flip'
        self.brief = 'Flips an input amount of coins for you.'
        self.description = '!flip by default will return either heads or '\
                           'tails. However, you can flip for any amount '\
                           '1000000 or less. To do so, type "!flip number" '\
                           'for example, "!flip 5000".'

    async def run(self, message, args):
        if not args or not args[0].isdigit() and not args[0].startswith('-'):
            await self.client.send_message(message.channel, self.flip(1))
            return
        try:
            await self.client.send_message(message.channel, self.flip(int(args[0])))
        except Exception as e:
            print(f'User generated the error {e} after trying to flip "{args[0]}"')
            await self.client.send_message(message.channel, 'Please use the correct format: !flip number')

    def flip(self, amount):
        if amount < 1:
            return "I flipped absolutely nothing. I hope you are happy."
        if amount == 1:
            result = randint(0, 1)
            return "I flipped a coin. It landed on {}!".format(
                'Heads' if result == 0 else 'Tails')
        elif amount > 1000000:
            return "Don't bully bots. You don't need to flip a coin over "\
                   "a million times. >:|"
        else:
            h_count = 0
            t_count = 0

            for flip in range(amount):
                result = randint(0,1)
                if result == 0:
                    h_count += 1
                else:
                    t_count += 1

            return "I flipped a coin {} times. The coin landed on Heads {} "\
                   "times and Tails {} times!".format(amount, h_count, t_count)
