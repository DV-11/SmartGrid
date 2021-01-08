import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def make_scatter(csv_bateries, csv_houses):
    
    csv_path = csv_bateries

    batteries = pd.read_csv(csv_bateries, sep=",", header = 0)


    csv_path = csv_houses

    houses = pd.read_csv(csv_houses, sep=",", header = 0)

    batteries_c = []

    for i in batteries['positie']:
        batteries_c.append(i.split(','))

    batteries_x = [int(i[0]) for i in batteries_c]
    batteries_y = [int(i[1]) for i in batteries_c]
    
    houses_x = [int(i) for i in houses['x']]
    houses_y = [int(i) for i in houses['y']]
    
    
    plt.scatter(batteries_x, batteries_y, c='red')
    plt.scatter(houses_x, houses_y, c='blue')
    plt.xticks(np.arange(0, 51, 10))
    plt.yticks(np.arange(0, 51, 10))
    plt.minorticks_on()

    plt.grid(which='major')
    plt.grid(which='minor', alpha = 0.25)
    plt.show()
