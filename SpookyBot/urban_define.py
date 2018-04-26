from bs4 import BeautifulSoup, Tag
import urllib.request
# Defines words using UrbanDictionary.com


def filter_out_tags(tag, result=''):
    # Remove tags while changing <br> tags to '\n' for formatting.
    for x in tag.contents:
        if isinstance(x, Tag):  # Check if content is a tag
            if x.name == 'br':  # If tag is <br>, change it to a '\n'
                result += '\n'
            else:  # For any other tag, recurse
                result = filter_out_tags(x, result)
        else:
            result += x
    return result


def clean(text):
    # Fix apostrophes. Makes sures not to end with newline.
    text = text.replace('&apos;', "'")
    if text.endswith('\n'):
        text = text[:-1]
    return text


def ud_define(message):
    term = message.replace(' ', '+')  # Make the search term URL-friendly.
    url = f"https://www.urbandictionary.com/define.php?term={term}"
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser')

    # Scrapes and cleans (if needed) the text for all desired values.
    word = soup.find("a", class_="word").get_text()
    meaning = clean(filter_out_tags(soup.find("div", class_="meaning")))
    example = clean(filter_out_tags(soup.find("div", class_="example")))

    count = soup.find_all("span", class_="count")
    up_count, down_count = count[0].get_text(), count[1].get_text()

    return word, meaning, example, up_count, down_count
