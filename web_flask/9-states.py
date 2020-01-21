#!/usr/bin/python3
"""
using my storage with flask
"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def _states():

    states = [storage.all('State')[x] for x in storage.all('State')]
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def id_states(id):

    states = [storage.all('State')[x] for x in storage.all('State')]
    for x in states:
        if x.id == id:
            cities = x.cities
            state = x
            return render_template('9-states.html',
                                   state=state,
                                   cities=cities)
    nf = 'Not found!'
    return render_template('9-states.html', nf=nf)


@app.teardown_appcontext
def close_(self):
    storage.close()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
