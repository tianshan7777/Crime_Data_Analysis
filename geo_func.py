from math import asin, sin, acos, cos, radians, sqrt
EARTH_R = 6378.1
#adult walking speed: 1.4 m/s or 5.0 km/h
WALKING_DIS = 2.52
radius = WALKING_DIS / EARTH_R

#Calculate distance between two pointss
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # Radius of earth in kilometers is 6371
    km = EARTH_R * c
    return km

def find_lat(lat):

    lat_min = lat - radius
    lat_max = lat + radius

    return (lat_max, lat_min)

def find_lon(lat, lon):

    lat_T = asin(sin(lat)/cos(radius))
    delta_lon = acos( ( cos(radius) - sin(lat_T) * sin(lat) ) / ( cos(lat_T) * cos(lat) ) )
    lon_min = lon - delta_lon 
    lon_max = lon + delta_lon

    return (lon_max, lon_min)