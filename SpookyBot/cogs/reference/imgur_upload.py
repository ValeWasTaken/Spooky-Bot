# Python 3.6.4
from imgur_auth import authenticate
# Create an Imgur PIN and store confidential information.
from reddit_scraper import check_input, scrape
# Check for proper input and scrape Reddit images.

client = authenticate() # Contains all hidden info (user,pass,ID,secret,etc)


def make_album(name, description, images):
    # Creates a new album and adds the given images to it.
    fields = {
        'title': name,
        'description': description,
        'privacy': 'public'}
    new_album = client.create_album(fields)
    client.album_add_images(new_album['id'], images)
    return new_album


def upload_image(title, link, count):
    # Uploads images to be placed inside the album.
    config = {
        'name':  f'Picture #{count}',
        'title': title}    
    image = client.upload_from_url(link, config=config, anon=False)
    return image


def main(command):
    # Takes the inputted data and runs through the functions
    # required to scrape the pictures from Reddit and upload
    # them to Imgur as an album. Then returns the link.
    titles, links = scrape(check_input(command))
    subreddit = command[0]
    threads = len(links)
    id = []
    for thread in range(threads):
        id.append(upload_image(titles[thread], links[thread], thread)['id'])
    album = make_album(f"Spooky Bot's /r/{subreddit} Album",
                       'Created by Spooky Bot! -- discord.gg/vale',id)
    album_url = album['id']
    return f'Here is your /r/{subreddit} album: https://imgur.com/a/{album_url}'
