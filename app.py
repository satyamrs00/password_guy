import sqlite3
from flask import Flask, session, render_template, redirect, request
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required, apology, myhashing, myreversehashing

# configure application
app = Flask(__name__)

# ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# add a filter for retreiving password from hash
app.add_template_filter(myreversehashing)

# configure sqlite3 to use records database
conn = sqlite3.connect('password_guy.db', check_same_thread=False)

# create tables in database
conn.execute("CREATE TABLE IF NOT EXISTS credentials ( user_id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password_hash TEXT NOT NULL)")
conn.commit()
conn.execute("CREATE TABLE IF NOT EXISTS records ( record_id INTEGER PRIMARY KEY AUTOINCREMENT, user_id TEXT NOT NULL, website TEXT NOT NULL, web_username TEXT NOT NULL, web_pass_hash TEXT NOT NULL, FOREIGN KEY (user_id) REFERENCES credentials(user_id))")
conn.commit()

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def index():
    # goto home page

    # sql query to receive password information
    cursor = conn.execute("SELECT * FROM records WHERE user_id = ?", (session["user_id"], ))

    passdata = cursor.fetchall()

    return render_template("home.html", passdata=passdata)

@app.route("/login", methods=["GET", "POST"])
def login():
    # log user in

    # forget existing session
    session.clear()
    
    # if user got here through url or redirect
    if request.method == "GET":
        # show the login page
        return render_template("login.html")
    else:
    # if user got here through input

        # ensure username is provded
        if not request.form.get("username"):
            return apology("enter username")
        # ensure password is provided
        if not request.form.get("password"):
            return apology("enter password")

        # query database for username
        cursor = conn.execute("SELECT * FROM credentials WHERE username = ?", (request.form.get("username"),))

        # remembering the data in a variable
        username_info = cursor.fetchall()

        # ensure the username exists in database
        if len(username_info) == 0:
            return apology("username not registered")
        # ensure password matches for the user
        if not check_password_hash(username_info[0][2], request.form.get("password")):
            return apology("incorrect password")

        # remember the user
        session["user_id"] = username_info[0][0]
        
        # redirect user to the home page
        return redirect("/")

@app.route("/register", methods = ["GET", "POST"])
def register():
    # if user got here through url or redirect
    if request.method == "GET":
        # show the registration page
        return render_template("register.html")
    else:
        # ensure username is provided
        if not request.form.get("username"):
            return apology("enter username")
        # ensure password if provided
        if not request.form.get("password"):
            return apology("enter password")
        # ensure password is confirmed
        if not request.form.get("confirmation"):
            return apology("confirm password")
        # ensure given passwords match
        if request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords dont match")

        # query the database for username provided
        cursor = conn.execute("SELECT * FROM credentials WHERE username = ?", (request.form.get("username"),))

        # check if username already exists
        if len(cursor.fetchall()) == 1:
            return apology("username already exists")
        
        # update the database to enter new user
        conn.execute("INSERT INTO credentials (username, password_hash) VALUES (?, ?)", (request.form.get("username"), generate_password_hash(request.form.get("password"))))
        conn.commit()

        # query to get new user info
        cursor = conn.execute("SELECT * FROM credentials WHERE username = ?", (request.form.get("username"),))

        # remember the user
        session["user_id"] = cursor.fetchall()[0][0]

        # redirect to homepage
        return redirect("/")

@app.route("/logout", methods=["GET"])
def logout():
    # log user out
    # forget session id
    session.clear()

    # redirect to home page
    return redirect("/")

@app.route("/add_password", methods=["GET","POST"])
@login_required
def add_password():
    if request.method == "GET":
        return render_template("add_password.html")
    else:
        if not request.form.get("website"):
            return apology("no website provided")
        if not request.form.get("website_username"):
            return apology("no username provided")
        if not request.form.get("website_password"):
            return apology("no password provided")
        
        conn.execute("INSERT INTO records (user_id, website, web_username, web_pass_hash) VALUES (?, ?, ?, ?)", (session["user_id"], request.form.get("website"), request.form.get("website_username"), myhashing(request.form.get("website_password"))))
        conn.commit()
        return redirect("/")