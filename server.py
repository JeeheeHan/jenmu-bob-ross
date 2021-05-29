"""Server"""

from flask import Flask, render_template, request, redirect, jsonify, request, flash, jsonify
from jinja2 import StrictUndefined

import crud
from model import Painting, db, connect_to_db


app = Flask(__name__)

app.secret_key = "SoSecret"
app.config['SESSION_TYPE'] = 'filesystem'


app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Render to the homepage"""
    
    quote = crud.get_random_quote()
    painting = crud.get_random_painting()
    list_hex = crud.break_down_hex_colors(painting)


    return render_template("homepage.html",
                           quote=quote, 
                           painting=painting, 
                           list_hex=list_hex)


@app.route('/bobquotes', methods=["GET"])
def show_another_quote():
    """Server response to AJAX and get another quote"""

    quote = crud.get_random_quote()
    new_paint = crud.get_random_painting()
    new_colors = crud.break_down_hex_colors(new_paint)

    return jsonify( {'quote':quote, 'new_paint': new_paint.img_src, 'new_colors':str(new_colors)} )


if __name__ == '__main__':
    connect_to_db(app)
    db.create_all()
    app.run(host='0.0.0.0', debug=True)