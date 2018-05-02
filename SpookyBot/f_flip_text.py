# Python 3.6.4
# Returns a message flipped upside down (and lowercase).
# ˙(ǝsɐɔɹǝʍoן puɐ) uʍop ǝpısdn pǝddıןɟ ǝbɐssǝɯ ɐ suɹnʇǝɹ


def f_flip_text(message):
    message = message.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz!?()[].<>"
    flipped_alphabet = "ɐqɔpǝɟbɥıظʞןɯuodbɹsʇnʌʍxʎz¡¿)(][˙><"
    normal_to_flipped = ''.maketrans(alphabet, flipped_alphabet)

    return message.translate(normal_to_flipped)[::-1]
