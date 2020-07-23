from netCDF4 import Dataset as dst 
from numpy import mean,array
from matplotlib import pyplot as plt

def slice_per(source, step):
	return [source[i::step] for i in range(step)]

nc = dst('../air.mon.mean.nc',mode='r')

def select():
	months = range(853)[-61:-1]
	avgs = []
	levels = range(17)[1:12]
	for l in levels:
		item = []
		for m in months:
			for latitude in nc.variables['air'][m][l]:
				item.append(mean(latitude))
		item = slice_per(item,73)
		for elem in item:
			average = mean(elem)
			avgs.append(average)
	avgs = array(slice_per(avgs,73))
	x = nc.variables['lat'][:]
	levels = ['925','850','700','600','500','400','300','250','200','150','100']
	return avgs.T

def make_graph(Dataset):
	x = nc.variables['lat'][:]
	levels = ['925','850','700','600','500','400','300','250','200','150','100']
	cs = plt.contour(x,levels,Dataset,colors='blue',levels=15)
	plt.clabel(cs)
	plt.xlabel("Latitude (°)")
	plt.ylabel("Altitude (mbar)")
	plt.plot()
	plt.savefig("contour_map.png")


if __name__ == "__main__":
	avg = select()
	make_graph(avg)

