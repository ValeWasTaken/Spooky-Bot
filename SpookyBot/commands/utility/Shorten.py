# Python 3.6.4
from bs4 import BeautifulSoup
import urllib.request
from command import Command

class Shorten(Command):
    def __init__(self, client):
        super().__init__(client)
        self.name = 'shorten'
        self.description = 'Uses tiny_url.com to shorten your URL.'

    async def run(self, message, args):
        if not args:
            await self.client.send_message(message.channel, 'Please make sure to use the correct format: !shorten link')
        try:
            url = ' '.join(args)
            result = self.get_tinyurl(url)
            await self.client.send_message(message.channel, f'Your shortened URL is: {result}')
        except Exception as e:
            print(f'User generated the error {e} after entering: "{args}"')
            await self.client.send_message(message.channel, "Something went wrong, sorry! :(")

    def get_tinyurl(self, text):
        # Generate and return a tinyurl link.
        url = self.format_url(text)
        soup = BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser')
        tiny_url = soup.find_all('div', class_='indent')[1].get_text()
        tiny_url = tiny_url.replace('[Open in new window][Copy to clipboard]', '')
        return tiny_url

    def format_url(self, text):
        # Formats the URL into text that tinyurl.com will convert to.
        prefix = 'https://tinyurl.com/create.php?source=indexpage&url='
        suffix = '&submit=Make+TinyURL%21&alias='
        formatted_url = prefix + text.replace('/', '%2F') + suffix
        return formatted_url
