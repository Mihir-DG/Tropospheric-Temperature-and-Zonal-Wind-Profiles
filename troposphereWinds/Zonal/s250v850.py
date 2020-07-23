from netCDF4 import Dataset as dst
from matplotlib import pyplot as plt
import numpy as np

nc = dst('../uwnd.mon.mean.nc', mode='r')

"""
winter_months = [1,2,12] #January, February, December
summer_months = [6,7,8] #June, July, August
#jan,feb,dec = [],[],[]
#jun,jul,aug = [],[],[]"""

def seasonalLatprof(month_index,alt) :
	a = range(853)[-122-month_index:-2-month_index:12]
	res = []
	for month in a:
		#YEARLY PROFILE
		profileMonthly = [] #np.empty(73,0)
		for latitude in nc.variables['uwnd'][month][alt]:
			profileMonthly.append(np.average(latitude))
		res.append(profileMonthly)
	print(np.array(res).shape)
	res = np.average(res,axis=0)
	print(np.array(res).shape)
	return res



if __name__ == "__main__":
	jan250 = seasonalLatprof(1,8)
	feb250 = seasonalLatprof(2,8)
	dec250 = seasonalLatprof(12,8)
	winprof250 = np.array([jan250,feb250,dec250])
	winprof250 = np.average(winprof250,axis=0)
	jun250 = seasonalLatprof(6,8)
	jul250 = seasonalLatprof(7,8)
	aug250 = seasonalLatprof(8,8)
	sumprof250 = np.array([jun250,jul250,aug250])
	sumprof250 = np.average(sumprof250,axis=0)
	plt.plot(nc.variables['lat'],sumprof250,label="Summer")
	plt.plot(nc.variables['lat'],winprof250,label="Winter")
	plt.legend()
	plt.xlabel("Latitude (°)")
	plt.ylabel("Zonal Wind (m/s)")
	plt.savefig("ws250.png")
	plt.show()





"""m1,m2,m3,m4,m5,m6 = [],[],[],[],[],[]
winter_indexes = {1:m1,2:m2,12:m3}
summer_indexes = {6:m4,7:m5,8:m6}
winter = []
summer = []

for ind in winter_indexes:
	a = range(853)[-122-ind:-2-ind:12]
	for year in a:
		for latitude in nc.variables['uwnd'][year][2]:
			average = np.average(latitude)
			winter_indexes[ind].append(average)
	winter.append(winter_indexes[ind])
	winter_indexes[ind]=[]
winter = np.average(winter,axis=0)
winter = slice_per(winter,73)
w850 = []
for i in winter:
	w850.append(sum(i)*0.1)
plot(w850)

# WINTER- 850mb
for ind in winter_indexes:
	a = range(853)[-122-ind:-2-ind:12]
	for month in a:
		for latitude in nc.variables['uwnd'][month][2]:
			average = sum(latitude)/len(latitude)
			winter_indexes[ind].append(average)
	winter.append(winter_indexes[ind])
	winter_indexes[ind]=[]
winter = np.average(winter,axis=0)
w850 = []
winter = slice_per(winter,73)
for elem in winter:
	w850.append(sum(elem)*0.1)

#WINTER- 250mbar
m1,m2,m3 = [],[],[]
winter = []
for ind in winter_indexes:
	a = range(853)[-122-ind:-2-ind:12]
	for month in a:
		for latitude in nc.variables['uwnd'][month][8]:
			average = sum(latitude)/len(latitude)
			winter_indexes[ind].append(average)
	winter.append(winter_indexes[ind])
	winter_indexes[ind]=[]
winter = np.average(winter,axis = 0)
w250 = []
winter = slice_per(winter,73)
for elem in winter:
	w250.append(sum(elem)*0.1)


#SUMMER - 850mb
for ind in summer_indexes:
	a = range(853)[-122-ind:-2-ind:12]
	for month in a:
		for latitude in nc.variables['uwnd'][month][2]:
			average = sum(latitude)/len(latitude)
			summer_indexes[ind].append(average)
	summer.append(summer_indexes[ind])
	summer_indexes[ind]=[]
summer = np.average(summer,axis=0)
s850 = []
summer = slice_per(summer,73)
for elem in summer:
	s850.append(sum(elem)*0.1)


#SUMMER - 250mbar
m4,m5,m6 = [],[],[]
summer = []
for ind in summer_indexes:
	a = range(853)[-122-ind:-2-ind:12]
	for month in a:
		for latitude in nc.variables['uwnd'][month][8]:
			average = sum(latitude)/len(latitude)
			summer_indexes[ind].append(average)
	summer.append(summer_indexes[ind])
	summer_indexes[ind]=[]
summer = np.average(summer,axis=0)
s250 = []
summer = slice_per(summer,73)
for elem in summer:
	s250.append(sum(elem)*0.1)
'''
fig = figure(figsize=(8,6))

#w250
plot(nc.variables['lat'],w250, label="Winter")
plot(nc.variables['lat'],s250, label="Summer")
xlabel("Latitude (°)")
ylabel("Wind (m/s)")
fig.legend()
savefig('ws250.png')
show()'''
print(nc.variables['lat'][:])
fig = figure(figsize=(8,6))
#plot(nc.variables['lat'][:],w850,color='blue', label="Winter", path_effects=[pe.SimpleLineShadow(shadow_color='purple', alpha=0.55), pe.Normal()] )
#plot(nc.variables['lat'][:],s850,color='red', label="Summer", path_effects=[pe.SimpleLineShadow(shadow_color='purple', alpha=0.55), pe.Normal()])
plot(w850,label='Winter')
plot(s850,label='Summer')
xlabel("Latitude (°)")
ylabel("Wind (m/s)")
fig.legend()
savefig('ws850.png')
show()
"""