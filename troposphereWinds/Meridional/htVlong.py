from netCDF4 import Dataset as dst
from matplotlib import pyplot as plt
from numpy import array, mean, reshape

nc = dst('../vwnd.mon.mean.nc', mode='r')

def slice_per(source, step):
	return [source[i::step] for i in range(step)]

profiles = []
months = range(853)[-68:-8]
levels = [2,8]
for level in levels:
	profile = []
	for month in months:
		for latitude in nc.variables['vwnd'][month][level]:
 			profile.append(latitude)
	profiles.append(profile)

p850,p250 = profiles[0],profiles[1]

p850 = array(p850).flatten(order='C')
p850 = array(slice_per(p850,10512))
profile850 = []
for elem in p850:
	m = mean(elem)
	profile850.append(m)
profile850 = reshape(array(profile850),(144,73),order='F')
p850 = []
for elem in profile850:
	new = mean(elem)
	p850.append(new)

p250 = array(p250).flatten(order='C')
p250 = array(slice_per(p250,10512))
profile250 = []
for elem in p250:
	m = mean(elem)
	profile250.append(m)
profile250 = reshape(array(profile250),(144,73),order='F')
p250 = []
for elem in profile250:
	new = mean(elem)
	p250.append(new)
print(len(p250))

plt.plot(p850,label="850")
plt.plot(p250,label="250")
plt.legend()
plt.savefig("htVlong.png")
plt.show()