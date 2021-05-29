
from model import db, connect_to_db
import pandas
import os

def add_image_to_db():
    """ Saving CSV into DB using panda lib """

    f = pandas.read_csv('./data/shortened_BR.csv')
    f.to_sql('paintings',os.environ.get('DATABASE_URL'), if_exists='replace')


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    db.create_all()
    add_image_to_db()