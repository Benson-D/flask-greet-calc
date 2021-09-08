# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)


@app.get('/<operation>')
def do_math(operation):
    """get operation name from url,
       and call the corresponding function from operations.py on values from params a and b """
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    if operation == "add":
        return f"<h1>The result is {add(a, b)}</h1>"
    if operation == "sub":
        return f"<h1>The result is {sub(a, b)}</h1>"
    if operation == "mult":
        return f"<h1>The result is {mult(a, b)}</h1>"
    if operation == "div":
        return f"<h1>The result is {div(a, b)}</h1>"
