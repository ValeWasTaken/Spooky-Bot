from bs4 import BeautifulSoup
import urllib.request


def format_url(text):
    # Formats the URL into text that tinyurl.com will convert to.
    prefix = 'https://tinyurl.com/create.php?source=indexpage&url='
    suffix = '&submit=Make+TinyURL%21&alias='
    formatted_url = prefix + text.replace('/', '%2F') + suffix
    return formatted_url


def get_tinyurl(text):
    # Generate and return a tinyurl link.
    url = format_url(text)
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser')
    tiny_url = soup.find_all('div', class_='indent')[1].get_text()
    tiny_url = tiny_url.replace('[Open in new window][Copy to clipboard]', '')
    return tiny_url
