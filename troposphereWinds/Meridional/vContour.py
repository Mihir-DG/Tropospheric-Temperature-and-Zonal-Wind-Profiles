from netCDF4 import Dataset as dst 
from numpy import mean,array
from matplotlib.pyplot import contourf,plot,show,savefig,colorbar,figure, setp,xlabel,ylabel
def slice_per(source, step):
	return [source[i::step] for i in range(step)]
nc = dst("../vwnd.mon.mean.nc",mode='r')
months = range(853)[-61:-1]
avgs = []
levels = range(17)[1:12]
for l in levels:
	item = []
	for m in months:
		for latitude in nc.variables['vwnd'][m][l]:
			item.append(mean(latitude))
	item = slice_per(item,73)
	for elem in item:
		average = mean(elem)
		avgs.append(average)

avgs = array(slice_per(avgs,73))
x = nc.variables['lat'][:]
levels = ['925','850','700','600','500','400','300','250','200','150','100']
avgs = avgs.T
cs = contourf(x,levels,avgs,15,cmap='nipy_spectral')
colorbar()
xlabel("Latitude (°)")
ylabel("Altitude (mbar)")
plot()
savefig("colormap.png")
show()

"""
cs = contourf(x,levels,avgs,15,cmap='nipy_spectral')
colorbar()
plot()
savefig("colormap.png")
show()
"""