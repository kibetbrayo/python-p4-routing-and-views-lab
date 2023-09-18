#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<name>')
def print_string(name):
    print(name)
    return name

@app.route('/count/<int:param>')
def count(param):
    numbers='\n'.join(str(i) for i in range(param + 1))
    return numbers


@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1+ num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    if result is not None:
        return str(result)
    else:
        return 'Invalid operation'    


if __name__ == '__main__':
    app.run(port=5555, debug=True)
