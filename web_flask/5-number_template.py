#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
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


@app.route('/python/')
@app.route('/python/<string:text>')
def python_is_cool(text="is cool"):
    """Display text based on input"""
    return "Python" + " " + text.replace("_", " ")


@app.route('/number/<int:n>')
def displayint(n):
    """Dispalys number passed in URL"""
    return str(n) + " " + "is a number"


@app.route('/number_template/<int:n>')
def numTemplate(n):
    """Displays HTML template with number passed in URL"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(debug=True)
