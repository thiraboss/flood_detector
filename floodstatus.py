
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

@app.route('/api/v1/province/<province>/district/<district>/flood_detector', methods=['GET','POST'])
def flood_status(province=None , district=None):
	url = "http://35.208.101.91:8080/sensors/project_id/flood_detector/" + province + '/' + district
	response = requests.get(url)
        flood_status = response.json()
	data = []
        for i in range(len(flood_status)):
		coming_data = {'name':"flood_detector",'status':waterlevel_status(int(flood_status[i]["sensor_data"])), 'percentage':waterlevel(int(flood_status[i]["sensor_data"])), 'province':(flood_status[i]["district"])}
                print(data)
		data.append(coming_data)
		print(waterlevel_status(int(flood_status[i]["sensor_data"])))
	return json.dumps(data)

if __name__ == '__main__':
     app.run(host = '0.0.0.0', port='8080', threaded=True, debug=True)
