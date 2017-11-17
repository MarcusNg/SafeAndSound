import os
from flask import Flask, redirect, url_for, render_template, session, \
	request, flash

app = Flask(__name__)

@app.route("/map", methods=["GET", "POST"])
def map():

@app.route("/event", methods=["GET"])
def event():


if __name__ == "__main__":
	app.debug = True
	app.run()
