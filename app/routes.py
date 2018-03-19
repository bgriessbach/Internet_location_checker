from app import app
from flask import Flask, flash, redirect, render_template, request, session, url_for
from app import helpers as h
import configparser
import os
data = []
error = {
	"hideError":True,
	"message":""
}
@app.route('/', methods=["POST", "GET"])
def index():
	return render_template('index.html', error=error)

@app.route('/search', methods=["POST"])
def search():
	query = request.form.get("query")
	query = h.formatInput(query)
	lookup = h.getLookup(query)
	config = configparser.ConfigParser()
	config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
	print(config)
	datapath = config["DEFAULT"]["DATAPATH"] + config["DEFAULT"]["FILEPREFIX"]
	datapath += lookup + ".csv"
	csvFile = h.getCSV(datapath)
	data = h.searchFile(csvFile, query)
	return render_template('tableview.html', speed=data["speed"], availability=data["availability"])