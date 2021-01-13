from code.classes import grid, battery, house
from code.algorithms.randomize import random_assignment, create_cable
from code.visualization.visualize import make_scatter
from code.algorithms.greedy import greedy_assignment, find_distance
import json 
# from code.visualization import visualize as visualization

if __name__ == "__main__":
    district = "district-1"

    # Create a grid from our data
    grid = grid.Grid(f"data/{district}/{district}_batteries.csv", f"data/{district}/{district}_houses.csv")

    # Runs random algorithm
    grid = greedy_assignment(grid)
    
    for House in grid.all_houses.values():
        create_cable(House, House.battery)

    # Calculates cost
    total_cost = 0
    for Battery in grid.all_batteries.values():
        total_cost += 5000

    for House in grid.all_houses.values():
        total_cost += (len(House.cables) - 1) * 9

    print(total_cost)
    # Create output file
    with open('output4.json', 'w') as f:
        f.write(grid.json())

    # plot batteries, houses, and cables onto a grid as a scatter plot 
    make_scatter(grid.all_batteries.values(), grid.all_houses.values())
