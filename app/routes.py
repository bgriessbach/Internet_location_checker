from app import app
from flask import Flask, flash, redirect, render_template, request, session, url_for
from app import helpers as h
import configparser
import os
data = []
error = {
	"showError":False,
	"message":""
}
@app.route('/', methods=["POST", "GET"])
def index():
	return render_template('index.html', error=error)

@app.route('/results', methods=["POST", "GET"])
def results():
	error["showError"] = False
	if not request.form.get("query"):
		return raiseError("No Postcode found!")
	query = request.form.get("query")
	query = h.formatInput(query)
	if len(query) < 2:
		return raiseError("The Postcode is too short. Query: "+ query +". Please enter a longer Postcode to limit results.")	
	lookup = h.getLookup(query)
	if len(lookup) < 1:
		return raiseError("This Postcode seems incorrect. No data file could be found. Query: " + query +"." )
	config = configparser.ConfigParser()
	config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
	try:
		datapath = config["DEFAULT"]["DATAPATH"] + config["DEFAULT"]["FILEPREFIX"]
	except:
		return raiseError("Cannot identify data location. Please contact Customer Support.")
	datapath += lookup + ".csv"
	csvFile = h.getCSV(datapath)
	if csvFile[0] == "error":
		return raiseError("Could not download data. Make sure the Postcode is correct. Otherwise please contact Customer Support. Error: " + csvFile[1])	
	data = h.searchFile(csvFile, query)
	if len(data['availability']) < 2:
		return raiseError("No results could be found for this Postcode. Query: " + query +".")	
	return render_template('tableview.html', speed=data["speed"], availability=data["availability"])
@app.route('/<path:path>')
def catch_all(path):
	return raiseError("Route not found: /" + path)

# basic error handling that returns to main with error
def raiseError(message):
	error['message'] = message
	error['showError'] = True
	return redirect(url_for("index"))