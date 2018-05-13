# Python 3.6.5
class Command:
    """An abstract class for creating commands."""
    def __init__(self, client):
        self.client = client
        self.name = None

    def run(self, message, args):
        pass
