#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Displays “Hello HBNB!”"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return "HBNB"


@app.route('/c/<string:text>')
def displaytext(text):
    """Display C followed by variable entered by user"""
    return "C" + " " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(debug=True)
