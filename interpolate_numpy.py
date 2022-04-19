import numpy as np

xdata = [60, 105]
ydata = [1.07, 1.01]

find = [85]
print("Find value for {}: {}".format(find,np.interp(find, xdata, ydata )))
