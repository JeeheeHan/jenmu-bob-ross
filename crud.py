"""Create, read, update and delete"""

from random import choice

def get_random_quote():
    """Open text file and get a random quote"""
    with open ("./data/quotes.txt", "r") as quotes:

        all_quotes = quotes.read().rstrip("\n").split("\n\n")

        quote = choice(all_quotes)

        return quote


    

