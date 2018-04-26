from random import shuffle  # Used to randomly mix list of facts.


def f_facts(subject):
    # NOT FOR USER INPUT.
    # Allows <subject>facts.txt to be called for reusability.
    with open(f'{subject}facts.txt', 'r') as f:
        facts = f.readlines()
        shuffle(facts)
        fact = facts[0].replace('\n', '')
        return fact
