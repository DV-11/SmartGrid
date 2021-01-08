from code.classes import grid, battery, house
from code.algorithms import randomize
from code.algorithms import greedy as gr
# from code.visualization import visualize as visualization

if __name__ == "__main__":
    district = "district-1"

    # Create a grid from our data
    grid = grid.Grid(f"data/{district}/{district}_batteries.csv", f"data/{district}/{district}_houses.csv")


