from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def index():
    pass

@app.route("/day/<year>/<month>/<day>", methods = ["GET", "POST"])
def day(year, month, day):
    pass