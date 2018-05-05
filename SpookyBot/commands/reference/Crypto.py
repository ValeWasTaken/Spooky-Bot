# Python 3.6.4
# Fetches data on cryptocurrencies and allows the user to
# either display it or compare it against other currencies.
import urllib.request, discord
from bs4 import BeautifulSoup
from command import Command

class Crypto(Command):
    def __init__(self, client):
        super().__init__(client)
        self.name = 'crypto'
        self.description = 'Checks crypto price / info.'

    async def run(self, message, args):
        if args[0] == 'top':
            await self.format_top(self.top_cryptos(args[1]))
        elif args[0] == 'info':
            await self.format_info(self.crypto_info(args[1]), message)
        else:
            await self.client.send_message(message.channel, f'{args[0]} is an invalid option.')

    def format_top(self, data):
        # TODO: find a nice way to format data
        pass

    async def format_info(self, data, message):
        try:
            rank, crypto_name, sign, worth, change = data
            embed = discord.Embed(title=f"{crypto_name} info", color=0x00ff00)
            embed.add_field(name="Rank: ", value=rank)
            embed.add_field(name="Symbol: ", value=sign)
            embed.add_field(name="Price (24h change)",
                            value=f"{worth} ({change})")
            await self.client.send_message(message.channel, embed=embed)
        except Exception as e:
            print(f'User generated the error {e} whilst retrieving crypto info.')
            await self.client.send_message(message.channel, "Please use the correct format: '!check symbol'"
                          "\nEx: '!check BTC' to check Bitcoin stats.")

    def get_data(self):
        url = "https://cryptoreport.com/"
        soup = BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser')
        all_data = soup.find_all('td', class_="mobile-td")
        values = []

        # Fetch all the data. (Ex: 1, Bitcoin, BTC, $123.45, 3.35%)
        for data_chunk in all_data:
            if data_chunk.get_text() == '':
                pass
            else:
                values.append(data_chunk.get_text())
        # "values" is all our data together, so now we need to group them!
        length = 5  # This is how large each data set is. (See above example.)
        # Now we zip together pairs of 5 data_chunks at a time for each crypto.
        # Then we put it all into one big list full of tuples. (1 tuple = 1 crypto)
        return list(zip(*[values[i::length] for i in range(length)]))


    def top_cryptos(self, amount):
        if amount > 20:
            return "Don't spam, keep your list to 20 or less please."
        else:
            return self.get_data()[:amount]


    def crypto_info(self, symbol):
        top_100 = self.get_data()
        for currency in top_100:
            for value in currency:
                if symbol.upper() == value.upper():
                    return currency
