from netCDF4 import Dataset as dst
import numpy as np
from matplotlib import pyplot as plt

tempnc = dst("../air.mon.mean.nc", mode='r')
zonalnc = dst("../uwnd.mon.mean.nc", mode='r')

#Datasets downloaded 21 Aug 2020
#Time length- 871 ==> 871/12 --> 7/12

def slice_per(source, step):
	return [source[i::step] for i in range(step)]

def zonal_data():
	months = range(871)[-68:-8]
	avgs = []
	levels = range(17)[0:12]
	for l in levels:
		item = []
		for m in months:
			for latitude in zonalnc.variables['uwnd'][m][l]:
				item.append(np.mean(latitude))
		item = slice_per(item,73)
		for elem in item:
			average = np.mean(elem)
			avgs.append(average)
	avgs = np.array(slice_per(avgs,73))
	return avgs.T

def temp_data():
	months = range(871)[-68:-8]
	avgs = []
	levels = range(17)[0:12]
	for l in levels:
		item = []
		for m in months:
			for latitude in tempnc.variables['air'][m][l]:
				item.append(np.mean(latitude))
		item = slice_per(item,73)
		for elem in item:
			average = np.mean(elem)
			avgs.append(average)
	avgs = np.array(slice_per(avgs,73))
	return avgs.T

if __name__ == "__main__":
	temp = temp_data()
	zonal = zonal_data()
	x = tempnc.variables['lat'][:]
	levels = tempnc.variables['level'][0:12]
	levels = levels[::-1]
	plt.contourf(x,levels,zonal,cmap='nipy_spectral',alpha=0.7)
	plt.colorbar()
	plt.contour(x,levels,temp,colors='black',levels=15)
	plt.xlabel("Latitude(°)")
	plt.ylabel("Altitude(mbar)")
	plt.savefig("windVtemp.png")
	plt.show()


