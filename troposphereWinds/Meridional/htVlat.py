from netCDF4 import Dataset as dst
from matplotlib import pyplot as plt
from numpy import array,mean,arange
from pathlib import Path

nc = dst(str(Path.home())+'/Desktop/vwnd.mon.mean.nc', mode='r')

def slice_per(source, step):
	return [source[i::step] for i in range(step)]

months = range(858)[-68:-8]
levels = [2,8]
profiles = []
for level in levels:
	profile = []
	for month in months:
		for latitude in nc.variables['vwnd'][month][level]:
			lat = mean(latitude)
			profile.append(lat)
	profiles.append(profile)
p850,p250 = profiles[0],profiles[1]
p850,p250 = array(slice_per(p850,73)),array(slice_per(p250,73))
profile850, profile250 = [],[]
p850 = mean(p850,axis=1)
p250 = mean(p250,axis=1)
x = nc.variables['lat']
plt.plot(x, p250,label='250')
plt.plot(x, p850,label='850')
plt.axhline(0,color='black',alpha=0.4)
plt.xlabel("Latitude (°)")
plt.ylabel("Wind (m/s)")
plt.legend()
plt.savefig('htVlat.png')
plt.show()
