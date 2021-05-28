"""Create, read, update and delete"""

from random import choice
import csv

def get_random_quote():
    """Open text file and get a random quote"""
    with open ("./data/quotes.txt", "r") as quotes:

        all_quotes = quotes.read().rstrip("\n").split("\n\n")

        quote = choice(all_quotes)

        return quote

def get_random_painting():
    """Get a random painting from the csv file."""

    f = open('./Bob_Ross_Paintings/data/bob_ross_paintings.csv')
    paintings_f = csv.reader(f)
    
    for row in paintings_f:
        print(row)
        break

