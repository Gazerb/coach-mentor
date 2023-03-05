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


@app.route("/")
def hello():
    return render_template("home.html")


@app.route("/show_bookings")
def show_bookings():
    bookings = list(mongo.db.bookings.find())
    print(bookings)
    return render_template("bookings.html", bookings=bookings)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)