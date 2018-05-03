# Python 3.6.4
# Fetches data on cryptocurrencies and allows the user to
# either display it or compare it against other currencies.
import urllib.request
from bs4 import BeautifulSoup


def get_data():
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


def top_cryptos(amount):
    # NOTE : THIS IS NOT YET USED BY SPOOKY BOT.
    # I still need to find a way to display the contents to the user well.
    
    # Outputs the top XX cryptocurrencies.
    if amount > 20:
        return "Don't spam, keep your list to 20 or less please."
    else:
        return get_data()[:amount]


def crypto_info(symbol):
    # Returns info for any top 100 cryptocurrency given the crypto's symbol.
    top_100 = get_data()

    for currency in top_100:
        for value in currency:
            if symbol.upper() == value.upper():
                return currency
