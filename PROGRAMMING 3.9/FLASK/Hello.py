from flask import Flask, render_template

app = Flask(__name__)

# CREATE A ROUTE DECORATOR
@app.route("/")
# def index():
#     return "<h1>Hello world!!!</h1>"
def index():
    return render_template("index.html")


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", user_name=name)
