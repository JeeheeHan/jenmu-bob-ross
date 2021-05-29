"""Server"""

from flask import Flask, render_template, request, redirect, jsonify, request, flash, jsonify, url_for
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

    new_video_link = new_paint.youtube_src

    return jsonify( {'quote':quote,\
            'new_paint': new_paint.img_src,\
            'new_colors':new_colors,\
            'vid_link':new_video_link} )



@app.route('/drawing', methods=["POST"])
def show_painting_page():
    """Render user paint-along page."""
    if request.method == "POST":
        paintingURL= request.form['paintingURL']
        youtubeURL = request.form['youtubeURL']
    print(paintingURL)
    print(youtubeURL)
    return render_template("drawing.html", youtubeURL = youtubeURL, paintingURL = paintingURL )


if __name__ == '__main__':
    connect_to_db(app)
    db.create_all()
    app.run(host='0.0.0.0', debug=True)