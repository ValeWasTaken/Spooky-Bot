# Python 3.6.5
import praw


def fix_subreddit(subreddit):
    # Formats any realistically possible subreddit URL into correct format.
    # i.e. remove HTTPS://www.reddit.com, /r/, r/, etc..
    if subreddit.endswith('/'):
        subreddit = subreddit[:-1]
    subreddit = subreddit.split('/')[-1]
    return subreddit


def check_input(message):
    invalid = 'Invalid input. Please use the format: '\
               '"!imgur subredditName hot/new/top numberUnder26"'
    try:
        subreddit = fix_subreddit(str(message[0]))
        category = str(message[1]).lower()
        amount = int(message[2])

        if category not in ['hot', 'new', 'top'] or not 0 < amount < 26:
            return invalid
        else:
            values = subreddit, category, amount
            return values

    except Exception as e:
        print(f'User generated error: "{e}" running !imgur')
        return invalid


def scrape(values):
    subreddit, category, amount = values
    r = praw.Reddit('SpookyBot')  # SpookyBot is defined in praw.ini
    subreddit = r.subreddit(subreddit)
    urls = ['.jpg', 'jpeg', '.png', '.gif']
    titles, links = [], []
    submissions = {
        'hot': subreddit.hot(limit=amount),
        'new': subreddit.new(limit=amount),
        'top': subreddit.top(limit=amount)}

    for submission in submissions[category]:
        title = submission.title
        url = submission.url
        if url[-4:] in urls:
            titles.append(title)
            links.append(url)
    return titles, links


if __name__ == '__main__':
    # Allow user to set test function without limits outside of Discord.
    print(scrape(('subreddit_name', 'top', 10)))
