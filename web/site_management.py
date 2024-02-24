#!/usr/bin/python3
"""Define app routes."""
from flask import Flask, render_template, request, flash, redirect, url_for
from data_manag import Storage
from table import User, Flight
from countries import countries, airports
from get_data import get_data

app = Flask(__name__)
app.url_map.strict_slashes = False
app.secret_key = "julias"


@app.route("/")
@app.route("/home")
def home():
    """Define welcome page of the app."""
    return render_template("home.html")


@app.route("/book")
def available():
    """Illustrate the available choices."""

    return render_template('flights.html', countries=countries, airports=airports)


@app.route("/login")
def login():
    """Define the login page."""
    return render_template("login.html")


@app.route("/check", methods=["POST"])
def checker():
    """Check for the given input if are known."""
    mail = request.form.get("e_mail")
    password = request.form.get("password")
    users = Storage.all("User")
    for k, v in users.items():
        if k == mail:
            if v == password:
                """flash("Sign in successful.")"""
                return redirect(url_for("home.html"))
            flash("Incorrect mail or password.")
            return redirect(url_for("sign_up.html"))
    #return redirect(url_for("flights.html"))


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
    storage = Storage()
    storage.reload()
    storage.save()
    storage.commit()
    flash("Account created, you can now log in", "info")
    return redirect(url_for("login"))


@app.route("/self")
def mi_self():
    """Describe my self."""
    return render_template("self.html")


@app.route("/search", methods=['POST'])
def search():
    """Search for data from the page"""
    ctry_from = request.form.get("country_from")
    ctry_to = request.form.get("country_to")
    airport_to = request.form.get("airport_to")
    airport_from = request.form.get("airport_from")
    data = get_data(airport_from, ctry_to)
    if type(data) == dict:
        real_data = data.get('data')
        return render_template("flights_next.html", real_data=real_data)
    return render_template('api_error.html', data=data)

if __name__ == '__main__':
    app.run(host=('0.0.0.0'), port='5500')
