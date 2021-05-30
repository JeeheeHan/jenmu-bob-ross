from flask import Flask
from flask_sqlalchemy import SQLAlchemy


import pandas
import os

db = SQLAlchemy()


#### Helper function to create DB######
def connect_to_db(flask_app, db_uri = os.environ.get('DATABASE_URL'), echo=True):
    if db_uri.startswith("postgres://"):
        db_uri = db_uri.replace("postgres://", "postgresql://", 1)

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = False
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {"pool_size": 20}

    db.app = flask_app
    db.init_app(flask_app)

    print('Connect to DB!')

class Painting(db.Model):
    """Painting Table that stores cols and row from csv file"""
    __tablename__ = "paintings"

    painting_index = db.Column(db.String,
                            primary_key=True)
    img_src = db.Column(db.String)
    painting_title = db.Column(db.String)
    colors = db.Column(db.String)
    youtube_src = db.Column(db.String)
    color_hex = db.Column(db.String)
    
    def __repr__(self):
        return f'<Painting Index:{self.painting_index} Title:{self.painting_title}>'


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    db.create_all()
