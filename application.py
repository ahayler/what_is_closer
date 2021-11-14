import os
import geopy.distance

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///locations.db")

@app.route("/check", methods=["GET"])
def check():
    """gets the location, the choosen city and the other city and returns true or false depending on if the user picked the right one"""
    
    location = {"lat": request.args.get('loc_lat'), "lng": request.args.get('loc_lng')}
    choosen_city = {"lat": request.args.get('c_city_lat'), "lng": request.args.get('c_city_lng')}
    other_city = {"lat": request.args.get('o_city_lat'), "lng": request.args.get('o_city_lng')}
    
    dist_1 = geopy.distance.geodesic((location["lat"], location["lng"]), (choosen_city["lat"], choosen_city["lng"])).km
    dist_2 = geopy.distance.geodesic((location["lat"], location["lng"]), (other_city["lat"], other_city["lng"])).km
    dist_1_s = "{0:0.2f} km".format(round(dist_1, 2))
    dist_2_s = "{0:0.2f} km".format(round(dist_2, 2))
    
    print(dist_1)
    print(dist_2)
    result = bool(dist_1 < dist_2)
    print(result)
    if request.args.get('order') == "normal":
        data = {"dist_a": dist_1_s, "dist_b": dist_2_s, "result": result}
    else:
        data = {"dist_a": dist_2_s, "dist_b": dist_1_s, "result": result}
    
    print(data)
    print(location)
    print(choosen_city)
    print(other_city)
    
    return jsonify(data)

   
@app.route("/instructions")
def instructions():
    """Homepage"""
       
    # returns instrcutions.html
    return render_template("instructions.html")

    
@app.route("/")
def index():
    """Homepage"""
       
    # returns index.html
    return render_template("index.html")


@app.route("/leaderboard") 
def leaderboard():
    """returns all leaderboard data sorted by score"""
    data = db.execute("SELECT name, score FROM leaderboard ORDER BY score DESC")
    
    print(data)
    
    return render_template("leaderboard.html", data=data)
    
    
@app.route("/update", methods=["GET"])
def update():
    """Returns two random cities"""
    
    # gets city_a
    city_a = db.execute("SELECT city_ascii, lat, lng, country, iso3, admin_name FROM cities ORDER BY RANDOM() LIMIT 1;")
    
    # gets city_b
    city_b = city_a
    while(city_a[0]["city_ascii"] == city_b[0]["city_ascii"]):
        city_b = db.execute("SELECT city_ascii, lat, lng, country, iso3, admin_name FROM cities ORDER BY RANDOM() LIMIT 1;")
    
    # extracts the the data out of city_a & city_b
    a_data = city_a[0]
    b_data = city_b[0]
    
    data = [a_data, b_data]
    
    # returns the data
    return jsonify(data)

@app.route("/submit", methods=["POST"]) 
def submit():
    
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # gets name and score
        name = request.form.get('name')
        score = request.form.get('score')
        
        db.execute("INSERT INTO leaderboard (name, score) VALUES (:name, :score)", score = score, name = name)
        
    return redirect ("/leaderboard")
    
# declares main
def main():
    # gets city_a
    city_a = db.execute("SELECT city_ascii, lat, lng, country, iso3, admin_name FROM cities ORDER BY RANDOM() LIMIT 1;")
    city_b = city_a
    
    while(city_a[0]["city_ascii"] == city_b[0]["city_ascii"]):
        city_b = db.execute("SELECT city_ascii, lat, lng, country, iso3, admin_name FROM cities ORDER BY RANDOM() LIMIT 1;")
    
    print(city_a[0]["city_ascii"])
    print(city_b[0]["city_ascii"])
    

    
# calls main
if __name__ == "__main__":
    main()