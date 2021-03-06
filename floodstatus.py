
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import json
import random
import mysql.connector
import time
import requests;
#db = mysql.connector.connect(
        #host="35.192.122.73",
        #user="root",
        #passwd="1212312121",
        #database="flooddata"
#);

app = Flask(__name__)
CORS(app)
api = Api(app)
response1 = 0
def waterlevel_status(x):
        if x < 5:
		url1= "http://35.231.245.160:5000/notify/user/flood_detector:very%20high!!/17,1"
		response1 = requests.get(url1)
                return 'very high'
        elif 5 < x < 10:
                return 'high'
        else:
                return 'low'

#def alert(x):
	#if waterlevel_status(x) == "very high":
		#alert = "http://35.231.245.160:5000/notify/user/flood_detector: very high!!/17,1"
		#response = request.get(alert)
		#return 'very high'
	#elif waterlevel_status(x) == "high":
		#alert = "http://35.231.245.160:5000/notify/user/flood_detector: high!!/17,1"
                #response = request.get(alert)
                #return 'high'
	#else:
		#return 'low'

def waterlevel(x):
	 percentage = (x/20)*100      
	 return str(percentage)

@app.route('/api/v1/flood_detector/sensor_id/<id>', methods=['GET','POST'])
def flood_status(id=None):
	url = "http://35.222.51.59:8080/sensors/sensor_id/" + id
	response = requests.get(str(url))
        flood_status = response.json()
	data = []
        for i in range(len(flood_status)):
		coming_data = {'name':"flood_detector",'status':waterlevel_status(int(flood_status[i]["data"])), 'percentage':waterlevel(int(flood_status[i]["data"])), 'coordinate':(flood_status[i]["coordinate"])}
                print(data)
		data.append(coming_data)
		print(waterlevel_status(int(flood_status[i]["data"])))
	return json.dumps(data)

if __name__ == '__main__':
     app.run(host = '0.0.0.0', port='8080', threaded=True, debug=True)
