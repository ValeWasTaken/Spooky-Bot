# Python 3.6.5
# Gives remaining time until Halloween (PST)
from command import Command
from datetime import datetime as dt


class Halloween(Command):
    def __init__(self, client):
        super().__init__(client)
        self.name = 'halloween'
        self.brief = 'Gives time until Halloween (PST).'
        self.description = '!halloween finds the time remaining until Halloween. '\
            'currently this only supports PST but will updated later. '\
            'To call this command type "!halloween"'

    async def run(self, message):
        await self.client.send_message(message.channel, self.is_it_halloween())

    def pl(self, num, unit):
        # Pluralizes words if needed. (ie: avoid returning data as '1 days')

        unit = '{} {}'.format(str(int(num)), unit)
        return unit + 's' if num > 1 or isinstance(num, float) or num == 0 else unit

    def clean_time(self, seconds):
        # Formats datetime data into simple English for the user.

        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        num = [days, hours, minutes, seconds]
        unit = ['day', 'hour', 'minute', 'second']
        return ', '.join(self.pl(num[x],unit[x]) for x in range(4))

    def is_it_halloween(self):
        # Checks time until Halloween.

        now = dt.now(tz=None) # Sets to local timezone (PST for bot)
        s_now = str(now)

        if s_now[5:10] == '10-31':
            return "It's Halloween!! Yay! ^^"

        elif any(m in s_now[5:7] for m in ['11','12']):
            # Checks if month-day is past Halloween so we can update countdown year
            halloween = dt(now.year+1, 10, 31, 0, 0, 0)
            wait = halloween - now  # ex: 221 days, 3:57:36.017574
            time = self.clean_time(wait.total_seconds())
            # Convert wait time into seconds and format answer.
            return 'We already had it this year.. But only {} until next '\
                'Halloween!\n But who\'s counting.. Right? ^^;'.format(time)
        else:
            halloween = dt(now.year, 10, 31, 0, 0, 0)
            wait = halloween - now
            time = self.clean_time(wait.total_seconds())
            return f'Just {time} more to go until Halloween (in PST)!'
