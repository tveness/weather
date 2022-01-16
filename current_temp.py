#!env/bin/python3

import requests
import json
import datetime
station_id=8465705 #New Haven


def parse_time(in_string):
#"2020-05-18T00:00:00-04:00"
    current_time=datetime.datetime.strptime(in_string,"%Y-%m-%dT%H:%M:%S-04:00")
    return current_time.strftime("%-I%p").lower()

def ftoc(f):
    return str( round((f-32)*5./9))

url="https://api.weather.gov/gridpoints/LWX/96,70/forecast/hourly"
response=requests.get(url)
#print(response.text)
data=json.loads(response.text)
#print(data.keys())
#for i in data["properties"]["periods"]:
#    print(parse_time(i["startTime"])+": "+ftoc(i["temperature"])+"C "+i["shortForecast"].lower())

weather_list =  [ [ parse_time(i["startTime"]), ftoc(i["temperature"]), i["shortForecast"].lower()] for i in data["properties"]["periods"]]

print(weather_list[:10])
