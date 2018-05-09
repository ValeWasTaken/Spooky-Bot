from bs4 import BeautifulSoup, Tag
import urllib.request, discord
from command import Command


class UrbanDefine(Command):
    def __init__(self, client):
        super().__init__(client)
        self.name = 'ud'
        self.description = 'Gives the Urban Dictionary definition of input.'

    async def run(self, message, args):
        if not args:
            await self.client.send_message(message.channel, 'Please make sure you use the correct format: !ud word')
        try:
            definition = self.ud_define(' '.join(args))
            embed = discord.Embed(title="Here is your Urban "
                                        "Dictionary definition!", color=0x00ff00)
            embed.add_field(name="Word", value=definition[0], inline=True)
            embed.add_field(name="Meaning", value=definition[1], inline=True)
            embed.add_field(name="Example", value=definition[2], inline=True)
            embed.add_field(name="Upvotes", value=definition[3])
            embed.add_field(name="Downvotes", value=definition[4])
            await self.client.send_message(message.channel, embed=embed)
        except Exception as e:
            print(f'User generated the error {e} after entering: "{args}"')
            await self.client.send_message(message.channel, "Sorry, your word or phrase wasn't found. :(")

    def filter_out_tags(self, tag, result=''):
        # Remove tags while changing <br> tags to '\n' for formatting.
        for x in tag.contents:
            if isinstance(x, Tag):  # Check if content is a tag
                if x.name == 'br':  # If tag is <br>, change it to a '\n'
                    result += '\n'
                else:  # For any other tag, recurse
                    result = self.filter_out_tags(x, result)
            else:
                result += x
        return result

    def clean(self, text):
        # Fix apostrophes. Makes sures not to end with newline.
        text = text.replace('&apos;', "'")
        if text.endswith('\n'):
            text = text[:-1]
        return text

    def ud_define(self, message):
        term = message.replace(' ', '+')  # Make the search term URL-friendly.
        url = f"https://www.urbandictionary.com/define.php?term={term}"
        soup = BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser')

        # Scrapes and cleans (if needed) the text for all desired values.
        word = soup.find("a", class_="word").get_text()
        meaning = self.clean(self.filter_out_tags(soup.find("div", class_="meaning")))
        example = self.clean(self.filter_out_tags(soup.find("div", class_="example")))

        count = soup.find_all("span", class_="count")
        up_count, down_count = count[0].get_text(), count[1].get_text()

        return word, meaning, example, up_count, down_count
