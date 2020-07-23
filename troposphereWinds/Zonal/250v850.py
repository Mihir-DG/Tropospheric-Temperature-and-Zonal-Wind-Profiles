from netCDF4 import Dataset as dst
from matplotlib import pyplot as plt

nc = dst('../uwnd.mon.mean.nc', mode='r')
iterator = -120
while iterator < 0:
	profile850 = []
	for latitude in list(nc.variables['uwnd'])[iterator][2]:
		item = []
		for longitude in latitude:
			item.append(longitude)
		iterator += 1
		average = sum(item)/len(item)
		profile850.append(average)
iterator_a = -120
while iterator_a < 0:
	profile250 = []
	for latitude in list(nc.variables['uwnd'])[iterator_a][8]:
		item2 = []
		for longitude in latitude:
			item2.append(longitude)
		iterator_a += 1
		average = sum(item2)/len(item2)
		profile250.append(average)
print(nc.variables['level'][:])
a = plt.plot(nc.variables['lat'][:],profile850, color='r', label='850 mbar')
b = plt.plot(nc.variables['lat'][:],profile250, color='g', label='250 mbar')
plt.xlabel("Latitude (°)")
plt.ylabel("Wind (m/s)")
plt.legend()
plt.savefig("plot_250v850.png")
plt.show()
