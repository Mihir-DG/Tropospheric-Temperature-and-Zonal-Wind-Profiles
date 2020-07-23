from netCDF4 import Dataset as dst
from matplotlib import pyplot as plt
import numpy as np

import matplotlib.patheffects as pe

nc = dst('../vwnd.mon.mean.nc', mode='r')

def slice_per(source, step):
	return [source[i::step] for i in range(step)]

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

def seasonalLatprof(month_index,alt) :
	a = range(853)[-122-month_index:-2-month_index:12]
	res = []
	for month in a:
		#YEARLY PROFILE
		profileMonthly = [] #np.empty(73,0)
		for latitude in nc.variables['vwnd'][month][alt]:
			profileMonthly.append(np.average(latitude))
		res.append(profileMonthly)
	print(np.array(res).shape)
	res = np.average(res,axis=0)
	print(np.array(res).shape)
	return res

if __name__ == "__main__":
	jan250 = seasonalLatprof(1,8)
	feb250 = seasonalLatprof(2,8)
	dec250 = seasonalLatprof(12,8)
	plt.plot(jan250)
	plt.plot(feb250)
	plt.plot(dec250)
"""
m1,m2,m3,m4,m5,m6 = [],[],[],[],[],[]
winter_indexes = {1:m1,2:m2,12:m3}
summer_indexes = {6:m4,7:m5,8:m6}
winter = []
summer = []
levels = [2]

#WINTER
for level in levels:
	season = []
	for seasonal in winter_indexes:
		months = range(858)[-128-seasonal:-8-seasonal:12]
		for month in months:
			for latitude in nc.variables['vwnd'][month][level]:
				avg = mean(latitude)
				season.append(avg)
		winter.append(season)

#SUMMER
for level in levels:
	season = []
	for seasonal in summer_indexes:
		months = range(858)[-128-seasonal:-8-seasonal:12]
		for month in months:
			for latitude in nc.variables['vwnd'][month][level]:
				avg = mean(latitude)
				season.append(avg)
		summer.append(season)

winter = array(winter).flatten()
print(array(winter).shape)
winter = array(slice_per(winter,3))
w250, w850 = split_list(winter)
w250, w850 = w250[0],w850[0]
w250 = slice_per(w250,73)
w850 = slice_per(w850,73)
print(array(w250).shape)
winter250, winter850 = [],[]
for elem in range(len(w850)):
	l1 = mean(w850[elem])
	winter850.append(l1)
	l2 = mean(w250[elem])
	winter250.append(l2)


summer = array(summer).flatten()
print(array(summer).shape)
summer = array(slice_per(summer,3))
s250, s850 = split_list(summer)
s250, s850 = s250[0],s850[0]
s250 = slice_per(s250,73)
s850 = slice_per(s850,73)
print(array(s250).shape)
summer250, summer850 = [],[]
for elem in range(len(s850)):
	l1 = mean(s850[elem])
	summer850.append(l1)
	l2 = mean(s250[elem])
	summer250.append(l2)

fig = figure()

x = nc.variables['lat'][::-1]
plot(x, winter250, label='Winter')
plot(x, summer250, label='Summer')
xlabel("Latitude (°)")
ylabel("Wind (m/s)")
legend()
savefig("ws850.png")
show()"""