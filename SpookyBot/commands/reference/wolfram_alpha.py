# Python 3.6.4
import wolframalpha
# Solves basically any question you can give Wolfram Alpha. Nice.


def solve(question):
    app_id = open("wolframalpha_app_id.txt").readline().rstrip()
    client = wolframalpha.Client(app_id)
    data = client.query(question)
    return next(data.results).text
