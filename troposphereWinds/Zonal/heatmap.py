import cartopy.crs as ccrs
from cartopy.util import add_cyclic_point
from netCDF4 import Dataset as dst
from numpy import mean,empty,shape,array
from matplotlib.pyplot import contourf,plot,show,savefig,colorbar,figure, setp, axes

def slice_per(source, step):
	return [source[i::step] for i in range(step)]
nc = dst('../../uwnd.mon.mean.nc',mode='r')
months = range(853)[-480:-2]
avgs = []
levels = [2,8]
count = 0
for month in months:
	for latitude in nc.variables['uwnd'][month][2]:
		avgs.append(latitude)
avgs = array(avgs).flatten()
avgs = slice_per(avgs,10512)
avg = []
for elem in avgs:
	avg.append(mean(elem))
avg = array(avg).reshape(73,144)
lats = nc.variables['lat'][:]
lons = nc.variables['lon'][:]
avg, lons = add_cyclic_point(avg, coord=lons)
fig = figure()
fig.suptitle("Zonal Wind At 850 millibars")
ax = axes(projection=ccrs.PlateCarree(central_longitude=0))
cs = contourf(lons,lats,avg,cmap='nipy_spectral',alpha=0.8, transform=ccrs.PlateCarree())
ax.coastlines()
colorbar(orientation='horizontal')
plot()
savefig("850.png")
show()