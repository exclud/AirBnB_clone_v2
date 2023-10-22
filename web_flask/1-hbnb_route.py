#!/usr/bin/python3
"""This module serves as the main entry point for the flask application"""


from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_world():
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

if __name__ == '__main__':
    app.run()
