import csv
import numpy as np
import matplotlib.pyplot as plt


        
c = [(38,12),(43,13),(42,3),(49,23),(3,45)]

x_c = [i[0] for i in c]
y_c = [i[1] for i in c]

plt.scatter(x_c, y_c)
plt.xticks(np.arange(0, 51, 10))
plt.yticks(np.arange(0, 51, 10))
plt.minorticks_on()

plt.grid(which='major')
plt.grid(which='minor', alpha = 0.25)
plt.show()
