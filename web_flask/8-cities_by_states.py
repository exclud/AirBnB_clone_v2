#!/usr/bin/python3
"""
This module serves as the main entry point for the Flask web application.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Display an HTML page with a list of
    all State objects and associated City objects present in storage.
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('cities_by_states.html', states=sorted_states)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Call storage.close() after each request.
    """
    storage.close()


if __name__ == '__main__':
    app.run()
