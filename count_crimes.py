from math import radians
import pandas as pd 
import numpy as np 
import geo_func

WALKING_DIS = 2.52

crime = pd.read_csv('crime_clean.csv')
properties = pd.read_csv('rent_clean.csv')

#lat_max = 47.6161
#lat_min = 47.3449
#lon_max = 19.3376
#lon_min = 18.9196

#Only compare with the points within the bbox
pro_lat = properties['latitude'].values.tolist()
pro_lon = properties['longitude'].values.tolist()
cri_lat = crime['lat'].values.tolist()
cri_lon = crime['lon'].values.tolist()
cri_number = []

for i, j in zip(pro_lat, pro_lon):

	counter = 0

	lat, lon = map(radians, [i, j])
	print('in radians:', lat, lon)

	#bounding box
	lat_max, lat_min = geo_func.find_lat(lat)
	print('max & min lat:', lat_max, lat_min)
	lon_max, lon_min = geo_func.find_lon(lat, lon)
	print('max & min lon:', lon_max, lon_min)

	for k, l in zip(cri_lat, cri_lon):

		k, l = map(radians, [k, l])

		if(k < lat_max and k > lat_min):
			if(l < lon_max and l > lon_min):
				print('-------------within area-----------')
				hav_dis = geo_func.haversine(l, k, lon, lat)

				if hav_dis <= WALKING_DIS:
					counter += 1

	cri_number.append(counter)

properties['Crimes'] = pd.Series(cri_number)
properties.to_csv('10minswalk.csv', index=False)




