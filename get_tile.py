from math import sin,pi,log,floor

lng=-72.926285
lat=41.305376


#lat=41.850
#lng=-87.65

z=12

#If z==1, and we 

TILE_SIZE=256


#Web Mercator projection
def project(lat,lng):
    siny=sin(lat*pi/180)
    

#    siny=min(max(siny,-.9999),.9999)
    newlat= TILE_SIZE*( 0.5- log( (1+siny ) / (1-siny)) / (4*pi)   )
    newlng= TILE_SIZE*( 0.5+ lng/360.  ) 
    return [newlng,newlat]

world_coord=project(lat,lng)

scale=1<<z

pixel_coord=[ i*scale for i in world_coord]

tile_coord=[floor(i/TILE_SIZE) for i in pixel_coord]


print(lat,lng,z)
print(world_coord)
print(pixel_coord)
print(z,tile_coord)




