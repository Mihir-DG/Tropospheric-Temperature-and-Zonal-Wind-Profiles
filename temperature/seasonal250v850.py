from netCDF4 import Dataset as dst
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.patheffects as pe


nc = dst('../air.mon.mean.nc', mode='r')

def slice_per(source, step):
	return [source[i::step] for i in range(step)]

m1,m2,m3,m4,m5,m6 = [],[],[],[],[],[]
winter_indexes = {1:m1,2:m2,12:m3}
summer_indexes = {6:m4,7:m5,8:m6}
winter = []
summer = []

def select(indexes,level,minor):
	for ind in indexes:
		a = range(853)[-122-ind:-2-ind:12]
		for month in a:
			for latitude in nc.variables['air'][month][2]:
				average = sum(latitude)/len(latitude)
				indexes[ind].append(average)
		minor.append(indexes[ind])
	minor = np.average(minor,axis=0)
	profile = []
	minor = slice_per(minor,73)
	for elem in minor:
		profile.append(sum(elem)*0.1)
	return profile

w850 = select(winter_indexes,2,winter)
w250 = select(winter_indexes,8,winter)
s850 = select(summer_indexes,2,summer)
s250 = select(summer_indexes,8,summer)

fig = plt.figure(figsize=(8,6))

#w250
plt.plot(nc.variables['lat'],w250, color='blue', label="Winter", path_effects=[pe.SimpleLineShadow(shadow_color='green', alpha=0.55), pe.Normal()])
plt.plot(nc.variables['lat'],s250, color='red', label="Summer", path_effects=[pe.SimpleLineShadow(shadow_color='green', alpha=0.55), pe.Normal()])
plt.xlabel("Latitude (°)")
plt.ylabel("Temperature (°C)")
fig.legend()
plt.savefig('ws250.png')

fig = plt.figure(figsize=(8,6))
plt.plot(nc.variables['lat'],w850,color='blue', label="Winter", path_effects=[pe.SimpleLineShadow(shadow_color='purple', alpha=0.55), pe.Normal()] )
plt.plot(nc.variables['lat'],s850,color='red', label="Summer", path_effects=[pe.SimpleLineShadow(shadow_color='purple', alpha=0.55), pe.Normal()])
plt.xlabel("Latitude (°)")
plt.ylabel("Temperature (°C)")
fig.legend()
plt.savefig('ws850.png')