"""Create, read, update and delete."""

from random import choice
from sqlalchemy import func


from model import Painting, db, connect_to_db

import csv
import pandas


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

    # Painting.query.order_by(func.random()).limit(1).scalar()

    # db.session.query(Painting).order_by(func.random()).scalar()

# db.session.query(Painting).filter(Painting.img_src).order_by(func.random(Painting.img_src)).limit(1).all()
# def get_paintings():
#     """Get a random painting."""

#     f = pandas.read_csv('./Bob_Ross_Paintings/data/bob_ross_paintings.csv')

#     return f['img_src']


#query function into DB goes here: colors sections with 2 buttons




if __name__ == '__main__':
    from server import app
    connect_to_db(app)