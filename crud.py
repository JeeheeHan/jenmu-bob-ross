"""Create, read, update and delete."""

from random import choice
from sqlalchemy import func


from model import Painting, db, connect_to_db

import csv
import pandas
import ast

###### Random picks for front page ######
def get_random_quote():
    """Open text file and get a random quote"""
    with open ("./data/quotes.txt", "r") as quotes:

        all_quotes = quotes.read().rstrip("\n").split("\n\n")

        quote = choice(all_quotes)

        return quote

def get_random_painting():
    """SCALAR the random img_src """
    item = db.session.query(Painting).order_by(func.random()).first()
    return item


####### GET the colors ######
def break_down_hex_colors(item):
    hexes = ast.literal_eval(item.color_hex)

    return hexes



if __name__ == '__main__':
    from server import app
    connect_to_db(app)