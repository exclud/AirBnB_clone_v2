#!/usr/bin/python3
"""This module serves as the main entry point for the flask application that
listens on 0.0.0.0, port 5000"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """Renders the index page

    Returns:
        _type_: _description_
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run()
