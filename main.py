from code.classes import grid, battery, house
from code.algorithms.randomize import random_assignment, create_cable
from code.algorithms import greedy as gr
from code.visualization.visualize import make_scatter
import json 
# from code.visualization import visualize as visualization

if __name__ == "__main__":
    district = "district-1"

    # Create a grid from our data
    grid = grid.Grid(f"data/{district}/{district}_batteries.csv", f"data/{district}/{district}_houses.csv")

    # Runs random algorithm
    grid = random_assignment(grid)
    
    for House in grid.all_houses.values():
        create_cable(House, House.battery)

    # Create output file
    with open('output4.json', 'w') as f:
        f.write(grid.json())

    # plot batteries and houses onto a grid as a scatter plot 
    make_scatter(grid.all_batteries.values(), grid.all_houses.values())
