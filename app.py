from flask import Flask, send_from_directory, request, redirect
from haversine.haversine import Unit
import requests
import haversine as hs


app = Flask(__name__)

states = {
	'all_states' : requests.get("https://www.vaccinespotter.org/api/v0/states.json"),
	'US' : requests.get("https://www.vaccinespotter.org/api/v0/US.json"),
	'MS': requests.get("https://www.vaccinespotter.org/api/v0/states/MS.json")
}


@app.route('/') #route decorator for server to run this html code then give to browser
def index():
	return send_from_directory('static', 'index.html')

@app.route('/static/<path:path>') #wildcard to make sure everything after path is captured
def static_assets(path: str):
	return send_from_directory('static', path)


#retrieves location from UI 
@app.route('/get_user_location', methods=['POST'])
def get_user_location():
	# location = request.form.innerhtml
	location = request.form["result"]
	# lat = str(location[str(location).index('Latitude: '):5])
	lat = float(location[location.index('Latitude: ')+10: location.index('Latitude: ')+20])
	long = float(location[location.index('Longitude: ')+10: location.index('Longitude: ')+20])
	print("Location is : " , location)
	print("/")
	print(lat)
	print(long)
	

	#get locations function returns all the location within given unit of distance in km
	get_locs = getLocations((lat,long))
	print(get_locs)
	

	return redirect("http://127.0.0.1:2000")

#this function uses haversine library to calculate distance between two coordinates and sorts them based on closest location
def getLocations(coord):
	
	limit = 5
	all_states = states['US'].json()
	# MS = states['MS'].json()
	i = 0  #counts the number of locations within defined distance
	places = []

	for providers in all_states["features"]:
		spot_latlong = (providers["geometry"]["coordinates"][1], providers["geometry"]["coordinates"][0])
		if((hs.haversine(coord, spot_latlong))<=5): #in km
			places.append([providers["properties"]["name"],providers["properties"]["address"],providers["properties"]["city"],providers["properties"]["state"],hs.haversine(coord, spot_latlong)])
			i = i+1
	
	print("i",i)
	places.sort(key = lambda x:x[4])
	return places




		

		

# def checkdistance():

# 	for x in all_states['features']


	
#put in repository then host on github pages is usedfor hosting pages
#unit, integration, end-to-end testing
print('Breakpoint me!')

if __name__ == '__main__':
	# app.run(debug=True)
    #host number, port, reruns the files automatically
	app.run('127.0.0.1', 2000, True)
