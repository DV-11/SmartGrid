from code.classes import grid, battery, house
from code.algorithms import randomize
from code.algorithms import greedy as gr
import json 
# from code.visualization import visualize as visualization

if __name__ == "__main__":
    district = "district-1"

    # Create a grid from our data
    grid = grid.Grid(f"data/{district}/{district}_batteries.csv", f"data/{district}/{district}_houses.csv")

    # Create output file
    with open('output3.json', 'w') as f:
        f.write(grid.json())
