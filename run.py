import os
from flask import Flask, render_template
# First, we're importing our Flask class.

app = Flask(__name__)
# We're then creating an instance of this and storing it in a variable called app
# we can use __name__ which is a built-in Python variable
# Flask needs this so that it knows where to look for templates and static files
"""
In Python, a decorator starts with the @ symbol, which is also called pie-notation.
Effectively, a decorator is a way of wrapping functions.
"""
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)