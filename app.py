from utils.maps import *
from utils.events import *

from flask import Flask, redirect, url_for, render_template, session, request, flash
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return redirect(url_for('map'))
    
@app.route("/map", methods=["GET", "POST"])
def map():
    events = find_events(40.713, -74.007, 1)
    return render_template('map.html', events=events)

@app.route("/event", methods=["GET"])
def event():
    print(find_events(40.713, -74.007, 1))
    return render_template('event.html')

if __name__ == "__main__":
	app.debug = True
	app.run()
