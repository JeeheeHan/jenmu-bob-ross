"""Server"""

from flask import Flask, render_template, request, redirect, jsonify, request, flash, jsonify
from jinja2 import StrictUndefined

import crud


app = Flask(__name__)

app.secret_key = "SoSecret"
app.config['SESSION_TYPE'] = 'filesystem'


app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Render to the homepage"""
    
    quote = crud.get_random_quote()
    painting = crud.get_random_painting()

    return render_template("homepage.html",
                           quote=quote, 
                           painting=painting)


@app.route('/bobquotes', methods=["GET"])
def show_another_quote():
    """Server response to AJAX and get another quote"""

    quote = crud.get_random_quote()

    return jsonify({'quote':quote})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)