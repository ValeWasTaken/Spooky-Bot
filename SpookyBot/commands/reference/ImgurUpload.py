# Python 3.6.4
# Create an Imgur PIN and store confidential information.
from imgur_auth import authenticate
# Check for proper input and scrape Reddit images.
from reddit_scraper import check_input, scrape
from command import Command

# Contains all hidden info (user,pass,ID,secret,etc)
imgur = authenticate()

class ImgurUpload(Command):
    def __init__(self, client):
        super().__init__(client)
        self.name = 'imgur'
        self.description = 'Scrapes a sub-reddit for images then uploads them to an Imgur album.'

    async def run(self, message, args):
        await self.client.send_message(message.channel, self.main(args))

    def make_album(self, name, description, images):
        # Creates a new album and adds the given images to it.
        fields = {
            'title': name,
            'description': description,
            'privacy': 'public'}
        new_album = imgur.create_album(fields)
        imgur.album_add_images(new_album['id'], images)
        return new_album


    def upload_image(self, title, link, count):
        # Uploads images to be placed inside the album.
        config = {
            'name':  f'Picture #{count}',
            'title': title}
        image = imgur.upload_from_url(link, config=config, anon=False)
        return image


    def main(self, command):
        # Takes the inputted data and runs through the functions
        # required to scrape the pictures from Reddit and upload
        # them to Imgur as an album. Then returns the link.
        titles, links = scrape(check_input(command))
        subreddit = command[0]
        threads = len(links)
        id = []
        for thread in range(threads):
            id.append(self.upload_image(titles[thread], links[thread], thread)['id'])
        album = self.make_album(f"Spooky Bot's /r/{subreddit} Album",
                           'Created by Spooky Bot! -- discord.gg/vale',id)
        album_url = album['id']
        return f'Here is your /r/{subreddit} album: https://imgur.com/a/{album_url}'
