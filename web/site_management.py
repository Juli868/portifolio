#!/usr/bin/python3
from flask import Flask, render_template
from data_manag import Storage
from table import User, Flight
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("login_check", methods=["POST"])
def checker():
    mail = request.form.get("e_mail")
    password = request.form.get("password")


@app.route("save", methods=["POST"])
def signing_up:
    new_user = user()
    Storage.save(new_user)
    Storage.commit()


@app.route("/signup")
def sign_up():
    return render_template("sign_up.html")


if __name__ == '__main__':
    app.run(host=('0.0.0.0'), port='5500')
