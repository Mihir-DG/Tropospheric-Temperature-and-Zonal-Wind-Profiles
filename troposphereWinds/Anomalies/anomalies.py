from netCDF4 import Dataset as dst
import cartopy.crs as ccrs
from numpy import mean,empty,shape,array,arange,sqrt
from matplotlib import pyplot as plt

u = dst('../../Zonal/uwnd.mon.mean.nc',mode='r')
v = dst('../../Meridional/vwnd.mon.mean.nc', mode='r')

months = range(853)[-68:-8]
level = 8

def slice_per(source, step):
	return [source[i::step] for i in range(step)]

def zonal_timeMean(v,dstname,months,level):
	avgs = []
	for month in months:
		for latitude in v.variables[dstname][month][8]:
			avgs.append(latitude)
	avgs = array(avgs).flatten()
	avgs = slice_per(avgs,10512)
	avg = []
	for elem in avgs:
		avg.append(mean(elem))
	avg = array(avg).reshape(73,144)
	return avg

vwnd = zonal_timeMean(v,'vwnd',months,level)
uwnd = zonal_timeMean(u,'uwnd',months,level)

Vmonth = u.variables['uwnd'][8][-6] #-1 for Jan
Umonth = v.variables['vwnd'][8][-12] #-7 for Jan

DV = Vmonth - vwnd
DU = Umonth - uwnd
x = u.variables['lon'][:]
y = u.variables['lat'][:][::-1]
x_list = []
y_list = []
for elem in x:
	new = str(elem)
	x_list.append(new)
for elem in y:
	new = str(elem)
	y_list.append(new)
fig = plt.figure(figsize=(7.5,9))
mag = sqrt(DU**2 + DV**2)
plt.quiver(DU,DV,color='black')
plt.contourf(x_list,y_list,mag,cmap='nipy_spectral',alpha=0.5)
plt.colorbar(orientation='horizontal')
plt.xlabel("Longitude (°)")
plt.ylabel("Latitude (°)")
plt.xticks(x_list[::20])
plt.yticks(y_list[::10])
plt.savefig("july250.png")
plt.show()






