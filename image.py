#!env/bin/python

import os, sys
import datetime
from PIL import Image, ImageDraw, ImageFont
from moon import draw_moon,moon_image
from tide import tide,quick_tide
from temp import temp







def int_to_roman(input):
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = []
    for i in range(len(ints)):
        count = int(input / ints[i])
        result.append(nums[i] * count)
        input -= ints[i] * count
    return str(''.join(result))
#print(int_to_roman(20))

im = Image.new('RGB',(800,480),(255,255,255))
draw = ImageDraw.Draw(im)

#draw.ellipse((100,100,150,200),fill=(255,0,0), outline=(0,0,0))


fnt_day = ImageFont.truetype("assets/SubVario-Condensed-Medium.otf", 80)
fnt_day = ImageFont.truetype("assets/OpenSans-Bold.ttf", 50)
fnt_q = ImageFont.truetype("assets/SubVario-Condensed-Medium.otf", 40)
fnt_q = ImageFont.truetype("assets/OpenSans-Bold.ttf", 20)
fnt_normal = ImageFont.truetype("assets/SubVario-Condensed-Medium.otf", 20)
fnt_normal = ImageFont.truetype("assets/OpenSans-Bold.ttf", 14)

# Get today's date
now=datetime.datetime.now()+datetime.timedelta(hours=-5)
today_string=now.strftime("%a %-d %b")
quarantine_start=datetime.datetime(2020,3,15,00,00,00)
quarantine_day=int(str((now-quarantine_start).days))
print(int_to_roman(quarantine_day))



#Draw today's date (+quaratine time!)
draw.text((90,40), today_string, font=fnt_day, fill=(0,0,0,255))
draw.line((180,105,480-180,105),fill=(0,0,0),width=2)
draw.text((200,110), "Day "+int_to_roman(quarantine_day), font=fnt_q, fill=(0,0,0,255))



#Generate 200x200 moon


# Draw tides

tide_obj=quick_tide()
draw.text((390,130),"Tides",font=fnt_q,fill=(0,0,0,255))
draw.rectangle((370,130,465,270),fill=None,outline=(0,0,0,255))
tide_obj.draw_tide(draw,fnt_normal,380,160)

# Draw weather table

temp_obj=temp()
#temp_obj.draw_weather_table(draw,fnt_normal,20,260)
temp_obj.draw_main_temp(draw,fnt_day,245,140)
temp_obj.draw_temp_graph(draw,fnt_normal,30,280)


#weather_image= Image.open("assets/icons/svg/wi-cloud.png").convert("RGBA")
#im.paste(weather_image,box=(140,125),mask=weather_image)
temp_obj.draw_icon(im,140,135)

#draw_moon(draw)
#draw.ellipse((100,100,150,200),fill=(255,0,0), outline=(0,0,0))
nh_map_image= Image.open("assets/nh_map_toner.png").convert("RGBA")
im.paste(nh_map_image,box=(480,110),mask=None)


mouse_image= Image.open("assets/mouse2.png").convert("RGBA")

#im.paste(mouse_image,box=(325,655),mask=mouse_image)
im.paste(moon_image(),box=(20,140))





im.save("test.png")


