#!/usr/bin/python3
"""
run flask app
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """return hello hbnb!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return hello hbnb!"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C_is(text):
    """return hello hbnb!"""
    text = text.replace("_", " ")
    return 'C %s' % text


@app.route('/python/', strict_slashes=False)
def Pyton_():
    return Python_is('is cool')


@app.route('/python/<text>', strict_slashes=False)
def Python_is(text):
    """return hello hbnb!"""
    text = text.replace("_", " ")
    return 'Python %s' % text


@app.route('/number/<int:number>', strict_slashes=False)
def Number_is(number):
    """return hello hbnb!"""
    return '%s is a number' % number

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
