import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env


"""
First, we're importing our Flask class,
Uppercase F in Flask says that it's a class.
"""

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

"""
We're then creating an instance of this and storing it in a variable called app
we can use __name__ which is a built-in Python variable
Flask needs this so that it knows where to look for templates and static files

In Python, a decorator starts with the @ symbol,
which is also called pie-notation.
Effectively, a decorator is a way of wrapping functions.
"""


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
        """
        print("Hello, is anybody there?")
        print(request.form.get("name"))
        print(request.form["email"])
        By using .get(), if the form doesn't actually have
        a key of 'name' or 'email' for example,
        then it would display 'None' by default.
        However, by just using request.form[], if there isn't
        a 'name' or 'email' key on our
        form, instead of returning 'None', it would throw an exception.
        """
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
