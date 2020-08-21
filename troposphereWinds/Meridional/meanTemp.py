from netCDF4 import Dataset as dst
from matplotlib import pyplot as plt
import numpy as np

nc = dst("../air.mon.mean.nc",mode="r")
time_range = range(-12,0)
months = []
for month in time_range:
	m = []
	for lvl in nc.variables['air'][month]:
		l = np.sum(lvl)/(73*144)
		m.append(l)
	months.append(m)

levels = np.array(months).mean(axis=0)
print(nc.variables['level'][:])
print((levels[8]-levels[2]))
plt.xlabel("Temperature (°C)")
plt.ylabel("Pressure (mbar)")
plt.plot(levels,nc.variables['level'])
plt.gca().invert_yaxis()
plt.savefig("img_meanTemp.png")
plt.show()