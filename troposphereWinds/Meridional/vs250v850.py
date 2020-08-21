from netCDF4 import Dataset as dst
from matplotlib import pyplot as plt
import numpy as np
from pathlib import Path
import matplotlib.patheffects as pe

nc = dst(str(Path.home())+'/Desktop/vwnd.mon.mean.nc', mode='r')

def slice_per(source, step):
	return [source[i::step] for i in range(step)]

def seasonalLatprof(month_index,alt) :
	a = range(858)[-128-month_index:-8-month_index:12]
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
	jun250 = seasonalLatprof(6,8)
	jul250 = seasonalLatprof(7,8)
	aug250 = seasonalLatprof(8,8)
	x = nc.variables['lat']
	plt.plot(x,jun250,label="Jun")
	plt.plot(x,jul250,label="Jul")
	plt.plot(x,aug250,label="Aug")
	plt.legend()
	plt.savefig("monthlySum250.png")
	plt.show()
	fig = plt.figure()
	mn = np.array([jun250,jul250,aug250])
	plt.plot(x,mn.mean(axis=0))
	plt.savefig("avgSum250.png")
	plt.show()
	
	
"""
m1,m2,m3,m4,m5,m6 = [],[],[],[],[],[]
Sumter_indexes = {1:m1,2:m2,12:m3}
summer_indexes = {6:m4,7:m5,8:m6}
Sumter = []
summer = []
levels = [2]

#SumTER
for level in levels:
	season = []
	for seasonal in Sumter_indexes:
		months = range(858)[-128-seasonal:-8-seasonal:12]
		for month in months:
			for latitude in nc.variables['vwnd'][month][level]:
				avg = mean(latitude)
				season.append(avg)
		Sumter.append(season)

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

Sumter = array(Sumter).flatten()
print(array(Sumter).shape)
Sumter = array(slice_per(Sumter,3))
w250, w250 = split_list(Sumter)
w250, w250 = w250[0],w250[0]
w250 = slice_per(w250,73)
w250 = slice_per(w250,73)
print(array(w250).shape)
Sumter250, Sumter250 = [],[]
for elem in range(len(w250)):
	l1 = mean(w250[elem])
	Sumter250.append(l1)
	l2 = mean(w250[elem])
	Sumter250.append(l2)


summer = array(summer).flatten()
print(array(summer).shape)
summer = array(slice_per(summer,3))
s250, s250 = split_list(summer)
s250, s250 = s250[0],s250[0]
s250 = slice_per(s250,73)
s250 = slice_per(s250,73)
print(array(s250).shape)
summer250, summer250 = [],[]
for elem in range(len(s250)):
	l1 = mean(s250[elem])
	summer250.append(l1)
	l2 = mean(s250[elem])
	summer250.append(l2)

fig = figure()

x = nc.variables['lat'][::-1]
plot(x, Sumter250, label='Sumter')
plot(x, summer250, label='Summer')
xlabel("Latitude (°)")
ylabel("Sumd (m/s)")
legend()
savefig("ws250.png")
show()"""