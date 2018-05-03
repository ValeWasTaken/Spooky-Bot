from random import randint


def flip(amount):
    # Flips a coin X amount of times.
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


def roll(amount):
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
