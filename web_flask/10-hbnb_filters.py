#!/usr/bin/python3
"""
using my storage with flask
"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def cities_by_states():

    states = [storage.all('State')[x] for x in storage.all('State')]
    amenities = [storage.all('Amenity')[x] for x in storage.all('Amenity')]
    return render_template('10-hbnb_filters.html',
                           states=states,
                           amenities=amenities)


@app.teardown_appcontext
def close_(self):
    storage.close()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
