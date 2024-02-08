#!/usr/bin/python3
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')
@app.route("/login")
def login():
    return render_template('login.html')
@app.route("/signup")
def sign_up():
    return render_template("sign_up.html")
if __name__ ==  '__main__':
    app.run(host=('0.0.0.0'), port='5500')
