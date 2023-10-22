#!/usr/bin/python3
"""This module serves as the main entry point for the flask application that
listens on 0.0.0.0, port 5000"""


from flask import Flask

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
    Renders "C " followed by the value of the text variable,
    replacing underscores with spaces.
    """
    return "C " + text.replace("_", " ")


if __name__ == '__main__':
    app.run()
