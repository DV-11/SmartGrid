import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from code.algorithms.greedy import restricted_greedy

# create a scatter plot on a grid to represent the districts
def make_scatter(batteries_data, houses_data, algorithm):
    
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

    # back to original code
    plt.scatter(batteries_x, batteries_y, c='red')
    plt.scatter(houses_x, houses_y, c='blue')

    # add cables
    for i in houses_data:
        i.cables
        points_x = []
        points_y = []

        for j in i.cables:
            points_x.append(j[0])
            points_y.append(j[1])

        # restricted algorithm returns a differnt output, so it needs a different approach 
        if isinstance(algorithm, restricted_greedy): 
            
            # plot cables with different colors depending on the target battery 
            if i.battery.id == 1:
                plt.plot(points_x, points_y, c='green')

            elif i.battery.id == 2:
                plt.plot(points_x, points_y, c='cyan')

            elif i.battery.id == 3:
                plt.plot(points_x, points_y, c='orange')
        
            elif i.battery.id == 4:
                plt.plot(points_x, points_y, c='purple')

            elif i.battery.id == 5:
                plt.plot(points_x, points_y, c='brown')

        # plot cables with different colors depending on the target battery, for all the other algorithms  
        else: 
            if i.battery == 1:
                plt.plot(points_x, points_y, c='green')

            elif i.battery == 2:
                plt.plot(points_x, points_y, c='cyan')

            elif i.battery == 3:
                plt.plot(points_x, points_y, c='orange')
        
            elif i.battery == 4:
                plt.plot(points_x, points_y, c='purple')

            elif i.battery == 5:
                plt.plot(points_x, points_y, c='brown')

    # display the resulting plot and also save it as a png image
    plt.show()
    plt.savefig('visualization.png')
 

