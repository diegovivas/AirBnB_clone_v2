#!/usr/bin/python3
"""
using my storage with flask
"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    lista = [storage.all('State')[x] for x in storage.all('State')]
    return render_template('7-states_list.html', lista=lista)


@app.teardown_appcontext
def close_(self):
    storage.close()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
