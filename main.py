from code.classes import grid, battery, house
from code.algorithms import randomize
from code.algorithms import greedy as gr
# from code.visualization import visualize as visualization

if __name__ == "__main__":
    district = "district-1"

    # Create a grid from our data
    grid = grid.Grid(f"data/{district}/{district}_batteries.csv", f"data/{district}/{district}_houses.csv")

    # temp
    with open('listfile.txt', 'w') as f:
        for Battery in grid.all_batteries:
            f.write(Battery.x_coordinate, Battery.y_coordinate)
        for House in grid.all_houses:
            f.write()
    
