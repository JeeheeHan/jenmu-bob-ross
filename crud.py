"""Create, read, update and delete."""

from random import choice

# from model import db, Painting, connect_to_db

import csv
import pandas



def get_random_quote():
    """Open text file and get a random quote"""
    with open ("./data/quotes.txt", "r") as quotes:

        all_quotes = quotes.read().rstrip("\n").split("\n\n")

        quote = choice(all_quotes)

        return quote


# def get_paintings():
#     """Get a random painting."""

#     f = pandas.read_csv('./Bob_Ross_Paintings/data/bob_ross_paintings.csv')

#     return f['img_src']




if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    pass