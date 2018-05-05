# Python 3.6.4
# Returns a message flipped upside down (and lowercase).
# ˙(ǝsɐɔɹǝʍoן puɐ) uʍop ǝpısdn pǝddıןɟ ǝbɐssǝɯ ɐ suɹnʇǝɹ
from command import Command

class Reverse(Command):
    def __init__(self, client):
        super().__init__(client)
        self.name = 'reverse'
        self.description = 'Reverses and flips your message upside down.'

    async def run(self, message, args):
        if not args:
            await self.client.send_message(message.channel, self.flip_text('What do you want me to flip?'))
        else:
            text = ' '.join(args)
            await self.client.send_message(message.channel, self.flip_text(text))

    def flip_text(self, message):
        message = message.lower()
        alphabet = "abcdefghijklmnopqrstuvwxyz!?()[].<>"
        flipped_alphabet = "ɐqɔpǝɟbɥıظʞןɯuodbɹsʇnʌʍxʎz¡¿)(][˙><"
        normal_to_flipped = ''.maketrans(alphabet, flipped_alphabet)

        return message.translate(normal_to_flipped)[::-1]
