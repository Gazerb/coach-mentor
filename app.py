import os

from flask import Flask, flash, render_template,  redirect, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash


if os.path.exists("env.py"):
    import env


app = Flask(__name__)


# Configuration values for flask_pymongo
# Documentation at http://flask-pymongo.readthedocs.io/en/latest/#configuration
app.config['MONGO_DBNAME'] = os.environ.get('DB_NAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# loads home page on start up


@app.route("/")
def hello():
    return render_template("index.html")

# Route for mentors page


@app.route("/show_mentors")
def show_mentors():
    mentors = list(mongo.db.mentors.find())
    return render_template("mentors.html", mentors=mentors)

# route for register page with code to take details and add them to the DB


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # checks if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        # collects user details and submits it to the DB
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "email": request.form.get("email"),
            "contact_number": request.form.get("contact_number"),
            "team": request.form.get("team")
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")

# Route for login page


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # Alerts user of invalid password
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile", methods=["GET", "POST"])
def profile():
    # grab the session user's username from db
    current_user = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=current_user)

    return redirect(url_for("login"))

# Route for user to log out


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))

# Route to make a booking with the mentors


@app.route("/make_a_booking", methods=["GET", "POST"])
def make_a_booking():
    if request.method == "POST":
        booking = {
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "email": request.form.get("email"),
            "contact_number": request.form.get("contact_number"),
            "team": request.form.get("team"),
            "date": request.form.get("date"),
            "time": request.form.get("time"),
            "booking_reason": request.form.get("booking_reason"),
            "created_by": session["user"]
        }
        # Inserts the booking information into the DB
        mongo.db.bookings.insert_one(booking)
        flash("Booking completed, A mentor will be in touch")
        return redirect(url_for("make_a_booking"))

    return render_template("make_a_booking.html")

# Route for user to see their bookings


@app.route("/show_bookings")
def show_bookings():
    bookings = list(mongo.db.bookings.find({"created_by": session["user"]}))
    return render_template("bookings.html", bookings=bookings)

# Route for user to edit their booking


@app.route("/edit_booking/<bookings_id>", methods=['GET', 'POST'])
def edit_booking(bookings_id):
    if request.method == "POST":
        submit = {
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "email": request.form.get("email"),
            "contact_number": request.form.get("contact_number"),
            "team": request.form.get("team"),
            "date": request.form.get("date"),
            "time": request.form.get("time"),
            "booking_reason": request.form.get("booking_reason"),
            "created_by": session["user"]
        }
        # Replaces data of booking to match changes made by the user
        mongo.db.bookings.replace_one({"_id": ObjectId(bookings_id)}, submit)
        flash("Booking Updated")
        return redirect(url_for("show_bookings"))

    bookings = mongo.db.bookings.find_one({"_id": ObjectId(bookings_id)})
    return render_template("edit_booking.html", bookings=bookings)

# Route for user to cancel a booking made


@app.route("/delete_booking/<bookings_id>")
def delete_booking(bookings_id):
    mongo.db.bookings.delete_one({"_id": ObjectId(bookings_id)})
    flash("Booking cancelled")
    return redirect(url_for("show_bookings"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
