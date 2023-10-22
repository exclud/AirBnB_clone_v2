#!/usr/bin/python3
"""
This module serves as the main entry point for the Flask web application.
"""

from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """
    Display an HTML page with a list of all State objects.
    """
    states = storage.all('State').values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('states.html', states=sorted_states)


@app.route('/states/<string:id>', strict_slashes=False)
def state_with_id(id):
    """
    Display an HTML page for a specific State and its associated cities.
    """
    state = storage.get('State', id)
    return render_template('state_cities.html', state=state)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Call storage.close() after each request.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
