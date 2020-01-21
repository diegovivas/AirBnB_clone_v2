#!/usr/bin/python3
"""
using my storage with flask
"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():

    states = [storage.all('State')[x] for x in storage.all('State')]
    cities = [storage.all('City')[x] for x in storage.all('City')]
    return render_template('8-cities_by_states.html',
                           states=states, cities=cities)


@app.teardown_appcontext
def close_(self):
    storage.close()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
