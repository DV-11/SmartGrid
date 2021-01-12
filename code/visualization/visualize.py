import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def make_scatter(batteries_data, houses_data):
    
    # grab battery data
    batteries_x = []
    batteries_y = []

    for i in batteries_data:
        batteries_x.append(int(i.x_coordinate))
        batteries_y.append(int(i.y_coordinate))

    # grab house data
    houses_x = []
    houses_y = []

    for i in houses_data:
        houses_x.append(int(i.x_coordinate))
        houses_y.append(int(i.y_coordinate))
    
    # this bit is taken from https://stackoverflow.com/questions/24943991/change-grid-interval-and-specify-tick-labels-in-matplotlib
    # couldn't figure out how to change the frequence of the subticks on my own
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    major_ticks = np.arange(0, 51, 10)  
    minor_ticks = np.arange(0, 51, 1)

    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(major_ticks)
    ax.set_yticks(minor_ticks, minor=True)

    ax.grid(which='both')

    ax.grid(which='minor', alpha=0.2)
    ax.grid(which='major', alpha=0.5)

    # back to oiriginal code
    plt.scatter(batteries_x, batteries_y, c='red')
    plt.scatter(houses_x, houses_y, c='blue')

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


