from operations import add, sub, mult, div
from flask import Flask, request
app = Flask(__name__)


@app.route('/add')
def search_add():
    """ handles GET requests with query parameters a and b and then adds the two numbers together"""

    a = int(request.args["a"])
    b = int(request.args["b"])
    sum = add(a, b)

    return str(sum)


@app.route('/sub')
def search_sub():
    """ same but subtracts the two numbers"""

    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(sub(a, b))


@app.route('/mult')
def search_mult():
    """ same but multiplies the two numbers """

    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(mult(a, b))


@app.route('/div')
def search_div():
    """ same but divides the two numbers """

    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(div(a, b))
