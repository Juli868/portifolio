#!/usr/bin/python3
"""Define app routes."""
from flask import Flask, render_template, request, flash, redirect
from data_manag import Storage
from table import User, Flight
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
@app.route("/home")
def home():
    """Define welcome page of the app."""
    return render_template('home.html')


@app.route("/book")
def available():
    """Illustrate the available choices."""
    return render_template('flights.html')


@app.route("/login", )
def login():
    """Define the login page."""
    return render_template("login.html")


@app.route("/check", methods=["POST"])
def checker():
    """Check for the given input if are known."""
    mail = request.form("e_mail")
    password = request.form("password")
    users = Storage.all("User")
    for k and v in users:
        if k  = mail:
            if v = password:
                flash("Sign in successful.")
                return render_template("home.html")
            flash("Incorrect mail or password.")
            return render_template("sign_up.html")
    return url_for('/home')


@app.route("/signup", methods=['GET', 'POST'])
def sign_up():
    """Define the sign up form."""
    return render_template("sign_up.html")


@app.route("/register", methods=['POST'])
def register():
    """Save the given information on signup form."""
    f_name = request.form.get("Firstname")
    s_name = request.form.get("Secondname")
    mail = request.form.get("email")
    first_p = request.form.get("password_f")
    last_p = request.form.get("password_conf")
    if (first_p != last_p):
        flash("passwords don't match")
    new_user = User(f_name, s_name, mail, first_p)
    Storage.save(new_user)
    Storage.commit()
    flash("Account created, you can now log in", "info")
    return (url_for("login"))


if __name__ == '__main__':
    app.run(host=('0.0.0.0'), port='5500')
