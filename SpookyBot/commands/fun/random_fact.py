from random import shuffle  # Used to randomly mix list of facts.
import os

def random_fact(subject):
    # NOT FOR USER INPUT.
    # Allows <subject>facts.txt to be called for reusability.
    with open(os.path.realpath(f'../resources/facts/{subject}.txt'), 'r') as f:
        facts = f.readlines()
        shuffle(facts)
        fact = facts[0].replace('\n', '')
        return fact
