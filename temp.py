#!env/bin/python3


from scipy.interpolate import interp1d
import numpy as np
import requests
import json
import datetime
from PIL import Image


class temp:
    def __init__(self):
        station_id=8465705 #New Haven


        def parse_time(in_string):
        #"2020-05-18T00:00:00-04:00"
            current_time=datetime.datetime.strptime(in_string,"%Y-%m-%dT%H:%M:%S-05:00")
            return current_time.strftime("%-I%p").lower()

        def ftoc(f):
            return str( round((f-32)*5./9))

        url="https://api.weather.gov/gridpoints/LWX/96,70/forecast/hourly?units=si"
        print("Getting weather data")
        url="https://api.weather.gov/gridpoints/OKX/64,67/forecast/hourly?units=si"
        user_agent={"User-agent": "weather@unbearablylight.com"}
        response=requests.get(url,headers=user_agent)
#        print(response.text)
        data=json.loads(response.text)

        self.weather_list =  [ [ parse_time(i["startTime"]), (i["temperature"]), i["shortForecast"].lower()] for i in data["properties"]["periods"]]

    def get_weather(self):
        return self.weather_list[:12]

    def draw_weather_table(self,draw,font,x,y):
    #[['4pm', '15', 'partly sunny'], ['5pm', '14', 'partly sunny'], ['6pm', '15', 'mostly cloudy'], ['7pm', '14', 'mostly cloudy'], ['8pm', '13', 'partly cloudy'], ['9pm', '12', 'partly cloudy'],
        for i in self.weather_list[:9]:
            index=self.weather_list.index(i)
            draw.text((x,y+25*index), str(i[0].lower().replace(" ","")), font=font, fill=(0,0,0,255))
            draw.text((x+65,y+25*index), i[1]+"°C", font=font, fill=(0,0,0,255))

#    print(weather_list[:10])
    def draw_main_temp(self,draw,font,x,y):
        draw.text((x,y), str(self.weather_list[0][1])+"°C", font=font, fill=(0,0,0,255))

    icon_lookup={"partly cloudy": "wi-day-cloudy.png", "mostly clear": "wi-night-clear.png", "sunny": "wi-day-sunny.png", "mostly sunny": "wi-day-sunny-overcast.png", "partly sunny": "wi-day-sunny-overcast.png", "mostly cloudy": "wi-cloudy.png", "patchy fog":"wi-fog.png"}
    
    def draw_icon(self,im,x,y):
        description=self.weather_list[0][2]
        if description not in self.icon_lookup.keys():
            print(description)
        else:
            weather_image= Image.open("assets/icons/"+self.icon_lookup[description]).convert("RGBA")
            im.paste(weather_image,box=(x,y),mask=weather_image)


    def draw_temp_graph(self,draw,font,x,y):
        min_temp=min([int(i[1]) for i in self.weather_list[:12]])
        max_temp=max([int(i[1]) for i in self.weather_list[:12]])

        width=400-10
        height=150

        bottom_left=[x+20,y+height-10]
        bottom_right=[x+width,y+height-10]
        top_right=[x+width,y+5]
        top_left=[x+20,y+5]

        draw.line((x+20,y+height,20+x+width,y+height),fill=(0,0,0),width=2)
        draw.line((x+20,y+height,20+x,y+5),fill=(0,0,0),width=2)
        temp_range=max_temp-min_temp+4

        #draw y-axis
        for i in range(0,temp_range,2):
            ycoord=y+height-height*i/temp_range-10
            draw.text((x-13,ycoord), str(i+min_temp-2)+"°C", font=font, fill=(0,0,0,255))
        for i in self.weather_list[:9]:
            draw.text((x+20 + (width-20)/8 * (self.weather_list[:9].index(i)) ,ycoord+height+10), str(i[0]), font=font, fill=(0,0,0,255))

        #draw pts on curve
        points=[]
        for i in range(9):
            ptx= x+20+(width-20)/8*(i)
            pty=y+height - (height)*(int(self.weather_list[i][1])-min_temp+2)/(max_temp-min_temp+4)
            points.append((ptx,pty))


        #Scipy interpolate
        xpts=[i[0] for i in points]
        ypts=[i[1] for i in points]

        f1=interp1d(xpts,ypts,kind='cubic')


        xpts_new=np.linspace(xpts[0],xpts[-1],num=300,endpoint=True)
        points_new=[(x,f1(x)) for x in xpts_new]


        draw.line(points_new,fill=(0,0,0),width=2,joint="curve")

#        #Dashed line
#        d=8
#        for i in range(0,len(points_new)-d,d):
#            delta=int(d/2)
#            draw.line([points_new[i][0],points_new[i][1],points_new[i+delta][0],points_new[i+delta][1]],fill=(0,0,0),width=0)
#


        




