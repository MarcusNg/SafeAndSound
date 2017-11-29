from utils.maps import *
from utils.events import *

from flask import Flask, redirect, url_for, render_template, session, request, flash
import requests, os, time, json

with open('api_keys.json', 'r') as f:
    data = f.read()
keys = json.loads(data)

GOOGLE_API_KEY = keys['GOOGLE_MAPS']
MEETUP_API_KEY = keys['MEETUP']

app = Flask(__name__)
app.secret_key = os.urandom(64)

@app.route("/", methods=["GET"])
def root():
    return redirect(url_for('map'))
    
@app.route("/map", methods=["GET", "POST"])
def map():
    events = []

    if request.method == 'POST':
        try:
            address = request.form["address"]
            radius = request.form["radius"]

            # Convert address to coordinates
            coords = convert_address(address)
            events = find_events(coords[0], coords[1], radius)
            return render_template('map.html', events=events, location=coords, GOOGLE_KEY=GOOGLE_API_KEY)
        except:
            flash("Please enter an address and radius.")
            
    return render_template('map.html', events=events, GOOGLE_KEY=GOOGLE_API_KEY)

@app.route("/event", methods=["POST"])
def event():
    nearby = []
    name = request.form["name"]
    timestamp = float(request.form["time"]) / 1000.0
    date = time.strftime('%m/%d/%Y, %A %H:%M', time.localtime(timestamp))
    description = request.form["description"]
    lat = request.form["lat"]
    lon = request.form["lon"]
    address = request.form["address"]
    event = [name, date, description, lat, lon, address]
    nearby = find_events(lat, lon, 2)
    return render_template('event.html', event=event, nearby=nearby)

if __name__ == "__main__":
    app.debug = True
    app.run()
