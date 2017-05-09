#We can see that the plot is linear, i.e. logarithmically increases, along the three data points between 600V and 800V. This is the "plateau" region. 

import matplotlib.pyplot as plt

line,caps,bars=plt.errorbar(
	[400,450,500,550,600,650,700,750,800,850,900,950,1000], #x data points
	[3.79,3.76,3.92,3.91,4.10,4.46,4.92,5.46,6.02,6.35,6.67,7.02,7.17], #y data points
	yerr=1,
	fmt="cs-",
	linewidth=3,
	elinewidth=0.5,
	ecolor='k',
	capsize=5,
	capthick=0.5,
	)

plt.setp(line,label="Log(counts/s) vs. Voltage")
plt.legend(numpoints=1,
	   loc=('upper left'))
plt.xlim((350,1050))
plt.ylim((0.50,11.0))

plt.show()
