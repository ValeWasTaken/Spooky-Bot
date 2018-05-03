# Python 3.6.4
# Provides a list of all commands and their full usage.


def h(query):
    if query == 'commands':
        return 'The current list of publicly available commands are: \n' \
               '!answer question -- Answer any question Wolfram Alpha is capable of.\n' \
               '!batfact -- Says a random bat fact!\n' \
               '!check cryptocurrency_symbol -- Checks crypto price / info.\n' \
               '!flip (amount) -- Flips a coin for you.\n' \
               '!halloween -- Gives time until Halloween.\n' \
               '!imgur subreddit sortType amount -- Scrapes a sub-reddit for images \
               then uploads them to an Imgur album.\n' \
               '!info @user -- Provides information on a Discord user.\n' \
               '!reverse message -- Reverses and flips your message upside down.\n' \
               '!roll (amount) -- Rolls a random number for you.\n'\
               '!shorten URL -- Uses tiny_url.com to shorten your URL.\n'\
               '!ud word -- Gives the Urban Dictionary definition of input.\n'\
               'For more information on a command type "!commands (command)".'
    else:
        try:
            return explain_command(query)
        except Exception as e:
            print(f'User was given {e} with input {query} while using "!help"')


def explain_command(command):
    return {
        'answer':
            '!answer will answer any question capable of the Wolfram Alpha '
            'engine. Most commonly these are math questions, but feel free '
            'to experiment with all kinds of questions! Example inputs could '
            'be "!answer (22*5) -4 / 11.2" or "!answer weather in Tokyo".',
        'batfact':
            '!batfact returns a random fact about bats to the user. '
            'There is currently over 70 facts, feel free to suggest more! '
            'To call this command type "!batfact"',
        'check':
            '!check returns the price and general information for a given '
            'cryptocurrency. Currently it only supports searching via symbol '
            'and only includes top 100 cryptocurrencies. Example usage: '
            '"!check BTC".',
        'flip':
            '!flip by default will return either heads or tails. '
            'However, you can flip for any amount 1000000 or less. '
            'To do so, type "!flip number" for example, "!flip 5000".',
        'halloween':
            '!halloween finds the time remaining until Halloween. '
            'currently this only supports PST but will updated later. '
            'To call this command type "!halloween"',
        'imgur':
            '!imgur will search a given sub-reddit according to a sort type '
            ' (hot, new, or top) and amount (25 or less) and then uploads '
            'the images to an Imgur album. Example usage: "!imgur programmer_humor '
            'new 20".',
        'info':
            '!info will give information about a user. At the moment that '
            'information is: Name, Status, Join Date, ID, and Highest role. '
            'To use this command type "!info @name".',
        'reverse':
            '!reverse will reverse a sentence and then flip it upside down. '
            'Example usage: "!reverse Reverse this message please.',
        'roll':
            '!roll by default will return a random number between 1 and 100. '
            'However, you can roll for any amount 1000000 or less. '
            'To do so, type "!roll number" for example, "!roll 5000".',
        'shorten':
            '!shorten will use tinyurl.com to shorten the length of your '
            'URL. To use this command type "!shorten yourURLhere"',
        'ud':
            '!ud will search UrbanDictionary.com to find your definition. '
            'To use this command type "!ud word".',
        'commands':
            '!commands gives information to the user about the rest of the '
            'bots commands. You can use "!commands" for a list of '
            'all publicly useable commands or "!commands command to learn '
            'more about a particular command.'
    }.get(command)
