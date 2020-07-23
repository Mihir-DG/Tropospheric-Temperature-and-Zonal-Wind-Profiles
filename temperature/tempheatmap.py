import cartopy.crs as ccrs
from cartopy.util import add_cyclic_point
from netCDF4 import Dataset as dst
from numpy import mean,empty,shape,array
from matplotlib.pyplot import contourf,plot,show,savefig,colorbar,figure, setp, axes

nc = dst('../air.mon.mean.nc',mode='r')

def slice_per(source, step):
	return [source[i::step] for i in range(step)]


def select(altitude):
	months = range(863)[-480:-2]
	avgs = []
	count = 0
	for month in months:
		for latitude in nc.variables['air'][month][altitude]:
			avgs.append(latitude)
	avgs = array(avgs).flatten()
	avgs = slice_per(avgs,10512)
	avg = []
	for elem in avgs:
		avg.append(mean(elem))
	avg = array(avg).reshape(73,144)
	return avg

def make_graph(Dataset, Name, filename, central):
	lats = nc.variables['lat'][:]
	lons = nc.variables['lon'][:]
	avg, lons = add_cyclic_point(Dataset, coord=lons)
	fig = figure()
	ax = axes(projection=ccrs.NorthPolarStereo(central_longitude=central))
	cs = contourf(lons,lats,avg,cmap='nipy_spectral',alpha=0.8, transform=ccrs.PlateCarree())
	ax.coastlines()
	colorbar(orientation='horizontal')
	plot()
	savefig("NorthPolarStereo/"+str(Name)+".png")

if __name__ == "__main__":
	profile850 = select(8)
	make_graph(profile850,250,0,0)