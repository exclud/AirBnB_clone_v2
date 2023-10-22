#!/usr/bin/python3
"""
This module serves as the main entry point for the Flask web application.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Display an HTML page with a list of all
    State objects present in the storage.
    """
    # states = storage.all('State').values()
    # sorted_states = sorted(states, key=lambda x: x.name)
    # return render_template('7-states_list.html', states=sorted_states)
    data = storage.all(State)
    return render_template('7-states_list.html', total=data.values())


@app.teardown_appcontext
def teardown_db(exception):
    """
    Call storage.close() after each request.
    """
    if storage is not None:
        storage.close()


if __name__ == '__main__':
    app.run()
