from flask import redirect, render_template, request, session, url_for
import csv
import requests


# clean input of additional spaces and make all letters uppercase
def formatInput(query):
	query = query.upper().replace(" ","")
	return query


#decide which file should be used
def getLookup(query):
	lookup = ""
	for c in query[:2]:
		if c.isalpha():
			lookup+=c
	return lookup

#search file for rows that match the postcode query
#only pick a few columns that give an overview of availability and speed
def searchFile(file, query):
	data = {}
	gotHeaders = False
	reader = csv.reader(file.splitlines(), delimiter = ",")
	listReader = list(reader)
	for row in listReader:
		if not gotHeaders:
			data["availability"] = []
			data["availability"].append([row[0].upper()] + row[3:10])
			data["speed"] = []
			data["speed"].append([row[0].upper()] + row[11:14] + row[19:22])
			gotHeaders = True
		if (row[0] == query or row[0].startswith(query)) and (len(data["availability"]) <50):
			data["availability"].append([row[0]] + row[3:10])
			data["speed"].append([row[0]] + row[11:14] + row[19:22])
	return data

#download CSV from online location
def getCSV(path):
	with requests.Session() as s:
		file = s.get(path, timeout=4)
		if file.status_code != 200:
			return ["error", str(file.status_code)]
		decodedFile = file.content.decode('utf-8')
	return decodedFile
