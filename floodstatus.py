
from flask import Flask, request
from flask_restful import Resource, Api
import json
import random

app = Flask(__name__)
api = Api(app)

import requests
import time

def waterlevel_status(x):
        if x < 5:
                return 'low'
        elif x > 5.1 and x < 10:
                return 'high'
        else:
                return 'very high'

def waterlevel(x):
        if x >= 10:
                return '100'
        else:
                percentage = (x/10)*100
                return str(percentage)

@app.route('/flood_detector/<location>')
def flood_status(location):
	url = "http://35.208.101.91:8080/sensors/project_id/flood_detector/" + location
        response = requests.get(url)
        flood_status = response.json()
	data = []
        for i in range(len(flood_status)):
		coming_data = {'name':"flood_detector",'status':waterlevel_status(int(flood_status[i]["sensor_data"])), 'percentage':waterlevel(int(flood_status[i]["sensor_data"])), 'location':'thirawat'}
                print(data)
		data.append(coming_data)
		print(waterlevel_status(int(flood_status[i]["sensor_data"])))
	return json.dumps(data)

if __name__ == '__main__':
     app.run(host = '0.0.0.0', port='8080', threaded=True, debug=True)
