#!/usr/bin/python3
"""Starts a Flask web application with additional routes for number validation and odd/even check"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!' when accessing the root URL"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Displays 'HBNB' when accessing the /hbnb route"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """Displays 'C ' followed by the value of the text variable"""
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    """Displays 'Python ' followed by the value of the text variable (default: 'is cool')"""
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """Displays 'n is a number' only if n is an integer"""
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """Displays an HTML page with 'Number: n' inside the H1 tag only if n is an integer"""
    return render_template('5-number_template.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_number_odd_or_even(n):
    """Displays an HTML page with 'Number: n is even|odd' inside the H1 tag only if n is an integer"""
    odd_or_even = 'odd' if n % 2 != 0 else 'even'
    return render_template('6-number_odd_or_even.html', n=n, odd_or_even=odd_or_even)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)