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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')