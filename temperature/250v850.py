from netCDF4 import Dataset as dst
from matplotlib import pyplot as plt

nc = dst('air.mon.mean.nc',mode='r')

time = 120
limit = 852
init = limit-time
#nc.variables['level'][2] --> 850 millibar
#air  --> time --> level --> latitude --> longitude
count = 0
#print(nc.variables['level'][:])
def latitudinal(level):
	iterator = -120
	while iterator < 0:
		profile = []
		for latitude in list(nc.variables['air'])[iterator][level]:
			item = []
			for longitude in latitude:
				item.append(longitude)
			iterator += 1
			average = sum(item)/len(item)
			profile.append(average)
	return profile

profile850 = latitudinal(2)
profile250 = latitudinal(8)
a = plt.plot(nc.variables['lat'][:],profile850, color='r', label='850mbar')
b = plt.plot(nc.variables['lat'][:],profile250, color='g', label='250mbar')
plt.xlabel("Latitude (°)")
plt.ylabel("Temperature (m/s)")
plt.legend(loc="upper left")
plt.savefig("plot_250v850.png")
plt.show()