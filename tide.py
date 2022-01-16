#!env/bin/python3

import requests
from bs4 import BeautifulSoup


class tide:

    def __init__(self):
        station_id=8465705 #New Haven

        url="https://tidesandcurrents.noaa.gov/api/datagetter?date=today&station="+str(station_id)+"&product=datums&units=metric&time_zone=edt&application=ports_screen&format=json"
        url="https://tidesandcurrents.noaa.gov/noaatidepredictions.html?id="+str(station_id)+"&legacy=1&units=metric"
        #token={'token': 'myBdXFajtSDoJUNBSARjoNAcOyQOmSEu'}

        #response=requests.get(url,headers=token)
        response=requests.get(url)
        #print(response.text)
        soup=BeautifulSoup(response.text,'html.parser')
        tide_table=soup.find('table')

        self.hl_table=  [[td.string for td in tr.find_all('td')] for tr in tide_table.find_all('tr') ]

    def draw_tide(self,draw,font,x,y):
        for i in self.hl_table:
            index=self.hl_table.index(i)
            draw.text((x,y+25*index), str(i[0].lower().replace(" ","")), font=font, fill=(0,0,0,255))
            hl=""
            if i[1]=="high ":
                hl="H"
            else:
                hl="L"
            draw.text((x+65,y+25*index), hl, font=font, fill=(0,0,0,255))


class quick_tide:

    def __init__(self):
        self.hl_table=  [['2:39 AM', 'high ', '2.17 m.'], ['9:06 AM', 'low ', '-0.07 m.'], ['3:18 PM', 'high ', '1.92 m.'], ['9:23 PM', 'low ', '0.20 m.']]

    def draw_tide(self,draw,font,x,y):
        for i in self.hl_table:
            index=self.hl_table.index(i)
            draw.text((x,y+25*index), str(i[0].lower().replace(" ","")), font=font, fill=(0,0,0,255))
            hl=""
            if i[1]=="high ":
                hl="H"
            else:
                hl="L"
            draw.text((x+65,y+25*index), hl, font=font, fill=(0,0,0,255))

