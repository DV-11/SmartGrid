import random
import copy
from code.algorithms.greedy import find_distance
from code.algorithms.randomize import create_cable

# greedy algorithm that takes output and capacity into account
class restricted_greedy:
    def __init__(self, grid):
        pass

    def run(self, grid):
        all_batteries = list(grid.all_batteries.values())

        # make a list with each battery, max capacity and the current output
        capacities_and_outputs = []

        for Battery in all_batteries:
            capacities_and_outputs.append([Battery,float(Battery.capacity),0])

        # find the closest house to connect 
        for House in grid.all_houses.values():
            
            closest_distance = 100000000
            closest_battery = None

        # make sure the house is the closest and does not go over the max capacity 
            for Battery in capacities_and_outputs:
                distance = find_distance(House, Battery[0])
                if distance < closest_distance and Battery[2] + float(House.output) < Battery[1]:
                    closest_battery = Battery[0]
                    closest_distance = distance
                    

            # connect house to battery and update current output 
                House.battery = closest_battery
            for i in capacities_and_outputs:
                if i[0] == closest_battery: i[2] = i[2] + float(House.output)
 
        for House in grid.all_houses.values():
            create_cable(House, House.battery)   
            
        # return grid of connected houses and batteries 
        return grid




