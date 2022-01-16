from astral import moon

from PIL import Image, ImageDraw, ImageFont
import datetime

#print(moon.phase(datetime.date.today()))


def draw_moon(in_draw):
    phase= moon.phase(datetime.date.today())
    in_draw.ellipse((300,100,400,200),fill=(255,0,0))

def moon_image():
    width=90
    phase= moon.phase(datetime.date.today())
    moon_shift=0.5*width*(phase-14)/28
    im1 = Image.new('RGB',(100,100),(255,255,255))
    draw1 = ImageDraw.Draw(im1)
#    draw1.ellipse((0,0,width,width),fill=(0,0,0),outline=(0,0,0))
#    draw1.ellipse((width/2 - abs(moon_shift) ,0,width/2+abs(moon_shift),width),fill=(255,255,255))

    if phase<7:
        #draw left black semicircle
        draw1.chord((0,0,width,width),-90,90,fill=(0,0,0))
        #draw right white semicircle
        draw1.chord((0,0,width,width),90,270,fill=(255,255,255))

        #draw black growing segment
        A=(7-phase)/7 *width/2
        draw1.ellipse((width/2 - A,0,width/2+A,width),fill=(0,0,0))
    elif phase<14:
        #draw left black semicircle
        draw1.chord((0,0,width,width),-90,90,fill=(0,0,0))
        #draw right white semicircle
        draw1.chord((0,0,width,width),90,270,fill=(255,255,255))

        #draw white growing segment
        A=(14-phase)/7 *width/2
        draw1.ellipse((width/2 - A,0,width/2+A,width),fill=(255,255,255))
    elif phase<21:
        #draw left white semicircle
        draw1.chord((0,0,width,width),90,270,fill=(255,255,255))
        #draw right black semicircle
        draw1.chord((0,0,width,width),-90,90,fill=(0,0,0))

        #draw white growing segment
        A=(21-phase)/7 *width/2
        draw1.ellipse((width/2 - A,0,width/2+A,width),fill=(255,255,255))
    else:
        #draw left white semicircle
        draw1.chord((0,0,width,width),90,270,fill=(255,255,255))
        #draw right black semicircle
        draw1.chord((0,0,width,width),-90,90,fill=(0,0,0))

        #draw black growing segment
        A=(28-phase)/7 *width/2
        draw1.ellipse((width/2 - A,0,width/2+A,width),fill=(0,0,0))



#    if moon_shift<0:
#        draw1.rectangle((0 ,0,width/2,width),fill=(255,255,255))
#    else:
#        draw1.rectangle((width/2 ,0,width,width),fill=(255,255,255))

    draw1.ellipse((0,0,width,width),fill=None,outline=(0,0,0))
    return im1







