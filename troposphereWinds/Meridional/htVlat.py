from netCDF4 import Dataset as dst
from matplotlib import pyplot as plt
from numpy import array,mean,arange

nc = dst('../vwnd.mon.mean.nc', mode='r')

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
for elem in range(len(p850)): #for elem in p850:
	p8 = p850[elem]		# Correct for 24-27: profile850 = np.mean(p850,axis=0)
	p8 = mean(p8)
	profile850.append(p8)
	p2 = p250[elem]
	p2 = mean(p2)
	profile250.append(p2)

x = nc.variables['lat'][::-1] # REVERSE!!!!!!
plt.plot(x, profile250,label='250')
plt.plot(x, profile850,label='850')
plt.xlabel("Latitude (°)")
plt.ylabel("Wind (m/s)")
plt.legend()
plt.savefig('htVlat.png')
plt.show()
