#!env/bin/python3

import requests
import json
import datetime
from datetime import timedelta
from PIL import Image
import re







url="https://api.weather.gov/gridpoints/OKX/64,67"
response=requests.get(url)
data=json.loads(response.text)


def get_property(property_name,json_data,wrapper=lambda x:x):

    data_strip=json_data["properties"][property_name]["values"]

#    simple_data=[[parse_time(i["validTime"]),wrapper(i["value"])] for i in data_strip]
#Go through fields and count hours added, repeat this many times
    simple_data=[]
    for i in data_strip:
        full_time,repeat=i["validTime"].split("/")
        full_time=datetime.datetime.strptime(full_time,"%Y-%m-%dT%H:%M:%S+00:00")
        repeat=int(re.findall(r'\d+',repeat)[0])
        value=wrapper(i["value"])
        for j in range(repeat):
            actual_time=full_time+timedelta(hours=j)
            parsed_time=actual_time.strftime("%-I%p").lower()
            simple_data.append([parsed_time,value])

        





#    simple_data=[[i["validTime"],wrapper(i["value"])] for i in data_strip]
    return simple_data




temp_data=get_property("temperature",data,round)
precip_data=get_property("quantitativePrecipitation",data)
sky_cover_data=get_property("skyCover",data)
rel_humidity_data=get_property("relativeHumidity",data)


print(temp_data)
#print(precip_data)
#print(sky_cover_data)
#print(rel_humidity_data)

print(data["properties"].keys())

