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
                return 'very high'
        elif 5 < x < 10:
                return 'high'
        else:
                return 'low'

def waterlevel(x):
	 percentage = 100-(x*5)      
	 return str(percentage)

@app.route('/api/v1/province/<province>/district/<district>/flood_detector', methods=['GET','POST'])
def flood_status(province=None , district=None):
	url = "http://35.208.101.91:8080/sensors/project_id/flood_detector/" + province + '/' + district
        url1 = "http://35.231.245.160:5000/notify/user/flood_detector: very high!!/"
	response1 = request.get(url1)
	print(response1)
	response = requests.get(url)
        flood_status = response.json()
	data = []
        for i in range(len(flood_status)):
		coming_data = {'name':"flood_detector",'status':waterlevel_status(int(flood_status[i]["sensor_data"])), 'percentage':waterlevel(int(flood_status[i]["sensor_data"])), 'province':(flood_status[i["district"]])}
                print(data)
		data.append(coming_data)
		print(waterlevel_status(int(flood_status[i]["sensor_data"])))
	return json.dumps(data)

if __name__ == '__main__':
     app.run(host = '0.0.0.0', port='8080', threaded=True, debug=True)
