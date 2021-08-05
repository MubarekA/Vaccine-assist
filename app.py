from flask import Flask, send_from_directory, request, redirect, render_template
from haversine.haversine import Unit
import requests
import haversine as hs
import os
import json
import time


app = Flask(__name__)

states = {
	'all_states' : requests.get("https://www.vaccinespotter.org/api/v0/states.json"),
	'US' : requests.get("https://www.vaccinespotter.org/api/v0/US.json"),
	'MS': requests.get("https://www.vaccinespotter.org/api/v0/states/MS.json")
}


def fetch_then_cache(url, name):
	cachepath = os.path.join('cache', name)
	if not os.path.exists('cache'):
		os.mkdir('cache')
	if os.path.exists(cachepath):
		with open(cachepath, 'r') as f:
			return json.loads(f.read())
	response = requests.get(url)
	data = response.json()
	with open(cachepath, 'w') as f:
			return f.write(json.dumps(data))
	return data

@app.route('/') #route decorator for server to run this html code then give to browser
def index():
	return send_from_directory('static', 'index.html')

@app.route('/static/<path:path>') #wildcard to make sure everything after path is captured
def static_assets(path: str):
	return send_from_directory('static', path)

global location1
# global get_locs
get_locs = {}
@app.route('/get_ajax_locations', methods=['POST','GET'])
def get_ajax_location():
	global location1
	global get_locs
	location1 = request.form["result"]
	# location1 = location
	# loc = location1.split(",")
	# lat = float(loc[0])
	# print(lat)

	# long = float(loc[1])
	# print(long)
	# get_locs['1'] = getLocations((lat,long))
	

	# print("get_locs",get_locs)
	return str(location1)

#retrieves location from UI 
@app.route('/get_user_location', methods=['POST'])
def get_user_location():
	global location1
	# global get_locs
	# time.sleep(5)
	# loc = location1.split(",")
	# lat = float(loc[0])
	# print(lat)

	# long = float(loc[1])
	# print(long)
	get_loc = getLocations((32.419536799999996,-90.1000917))
	return render_template('locations.html', locations= get_loc, index=0)

@app.route('/get_next_locations', methods=['POST'])
def get_next_locations():
	locations = request.form["locations"]
	index = request.form["index"]
	return render_template('locations.html', locations=json.loads(locations), index=int(index) + 10)

@app.route('/get_previous_locations', methods=['POST'])
def get_previous_locations():
	locations = request.form["locations"]
	index = request.form["index"]
	return render_template('locations.html', locations=json.loads(locations), index=max(0, int(index) - 10))

#this function uses haversine library to calculate distance between two coordinates and sorts them based on closest location
def getLocations(coord):
	all_states = states['MS'].json()
	i = 0  #counts the number of locations within defined distance
	places = []

	for providers in all_states["features"]:
		spot_latlong = (providers["geometry"]["coordinates"][1], providers["geometry"]["coordinates"][0])
		if((hs.haversine(coord, spot_latlong))<=5): #in km
			places.append([providers["properties"]["name"],providers["properties"]["url"],providers["properties"]["address"],providers["properties"]["city"],providers["properties"]["state"],hs.haversine(coord, spot_latlong)])
			i = i+1
	
	print("i",i)
	places.sort(key = lambda x:x[5])
	return places
	


print('Breakpoint me!')

if __name__ == '__main__':
	# app.run(debug=True)
    #host number, port, reruns the files automatically
	app.run('127.0.0.1', int(os.environ.get('PORT', 2000)), True)
