import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def make_scatter(csv_bateries, csv_houses):
    
    # grab battery data
    batteries = pd.read_csv(csv_bateries, sep=",", header = 0)

    # grab house data
    houses = pd.read_csv(csv_houses, sep=",", header = 0)
    
    # get coordinates of all the batteries 
    batteries_c = []

    for i in batteries['positie']:
        batteries_c.append(i.split(','))

    batteries_x = [int(i[0]) for i in batteries_c]
    batteries_y = [int(i[1]) for i in batteries_c]
       
    # get coordinates of all the houses
    houses_x = [int(i) for i in houses['x']]
    houses_y = [int(i) for i in houses['y']]
    
    # plot them in a grid 
    plt.scatter(batteries_x, batteries_y, c='red')
    plt.scatter(houses_x, houses_y, c='blue')
    plt.xticks(np.arange(0, 51, 10))
    plt.yticks(np.arange(0, 51, 10))
    plt.minorticks_on()

    plt.grid(which='major')
    plt.grid(which='minor', alpha = 0.25)
    plt.show()
 
def set_cable(c_battery, c_house, direction='reg'):
    
    # set an alternative orientation for the cable

    if direction == 'alt':
        
        x1 = c_battery[0]
        y1 = c_battery[1]
        x2 = c_house[0]
        y2 = c_house[1]
    
        plt.scatter(x1, y1, c='red')
        plt.scatter(x2, y2, c='black')
        plt.plot([x1, x2, x2], [y1, y1, y2],)
        plt.xticks(np.arange(0, 51, 10))
        plt.yticks(np.arange(0, 51, 10))
        plt.minorticks_on()

        plt.grid(which='major')
        plt.grid(which='minor', alpha = 0.25)
        plt.show()

    # regular orientation as a default 
    
    else:
        
        x1 = c_battery[0]
        y1 = c_battery[1]
        x2 = c_house[0]
        y2 = c_house[1]
    
        plt.scatter(x1, y1, c='red')
        plt.scatter(x2, y2, c='black')
        plt.plot([x1, x1, x2], [y1, y2, y2],)
        plt.xticks(np.arange(0, 51, 10))
        plt.yticks(np.arange(0, 51, 10))
        plt.minorticks_on()

        plt.grid(which='major')
        plt.grid(which='minor', alpha = 0.25)
        plt.show()
