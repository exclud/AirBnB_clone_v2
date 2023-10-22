#!/usr/bin/python3
"""
This module serves as the main entry point for the Flask web application.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Renders the greeting message "Hello HBNB!".
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Renders the message "HBNB".
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Renders "C " followed by the value of the text
    variable, replacing underscores with spaces.
    """
    return "C " + text.replace("_", " ")


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """
    Renders "Python " followed by the value of the text
    variable, replacing underscores with spaces.
    """
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Renders "n is a number" if n is an integer.
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Renders an HTML page displaying the number
    in an H1 tag, if n is an integer.
    """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Renders an HTML page displaying if the number
    is odd or even in an H1 tag, if n is an integer.
    """
    return render_template('6-number_odd_or_even.html',
                           number=n, parity='even' if n % 2 == 0 else 'odd')


if __name__ == '__main__':
    app.run()
