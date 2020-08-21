from netCDF4 import Dataset as dst
from matplotlib import pyplot as plt
import numpy as np

nc = dst('../air.mon.mean.nc',mode='r')
time_range = range(-12,0)
n,s = [],[]
fullprofs = []
iterator = [0,6,12,18,24,30,36] 
legends = [90,75,60,45,30,15,0]
"""
for i in iterator:
	profs = [] 
	for year in time_range:
		yrAvg = []
		for level in nc.variables['air'][year]:
	 		yrAvg.append(np.sum(level[i])/144)
		profs.append(yrAvg)
	profs = np.array(profs).mean(axis=0)
	fullprofs.append(profs)
#Fullprofs indexed by order of iterator list
for i in range(7):
	plt.plot(fullprofs[i],nc.variables['level'],label=legends[i])

plt.ylabel("Pressure(mbar)")
plt.xlabel("Air Temperature (°C)")
plt.gca().invert_yaxis()
plt.legend()
plt.savefig('img_lat_meanTemp.png')
plt.show()
"""
levels = []
for year in time_range:
	yrAvg = []
	for level in nc.variables['air'][year]:
		equat = np.mean(level[36])
		pole = np.mean(level[0])
		yrAvg.append(equat-pole)
	levels.append(yrAvg)
levels = np.array(levels).mean(axis=0)
plt.plot(levels,nc.variables['level'])
plt.ylabel("Pressure (mbar)")
plt.xlabel("Temperature (°C)")
plt.gca().invert_yaxis()
plt.savefig("img_poleEquatdiff.png")
plt.show()
