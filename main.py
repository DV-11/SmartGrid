from code.classes import grid, battery, house
from code.algorithms.randomize import random_assignment, create_cable
from code.visualization.visualize import make_scatter
from code.algorithms.greedy import greedy_assignment, find_distance
from code.algorithms.restricted import restricted_greedy
from code.algorithms.hillclimber import hillclimber
from code.algorithms.randomize2 import randomize_shared

import json 
# from code.visualization import visualize as visualization


if __name__ == "__main__":

    # Allows user to choose a district
    valid_numbers = [1, 2, 3]
    district_number = 0
    while district_number not in valid_numbers:
        district_number = int(input("Choose a district (1, 2, 3) \n"))
    district = f"district-{district_number}"

    # Create a grid from data
    grid = grid.Grid(f"data/{district}/{district}_batteries.csv", f"data/{district}/{district}_houses.csv")
 
    # Allows user to choose an algorithm
    all_algorithms = {"restricted_greedy": restricted_greedy(grid), "hillclimber": hillclimber(grid), "shared_randomize" : randomize_shared(grid)}
    chosen_algorithm = None
    while chosen_algorithm not in all_algorithms:
        chosen_algorithm = input(f"Choose an algorithm {all_algorithms.keys()} \n")

    # Runs chosen algorithm
    chosen_algorithm = all_algorithms.get(chosen_algorithm)
    if isinstance(chosen_algorithm, hillclimber):
        grid = randomize_shared(grid).run(grid)
    grid = chosen_algorithm.run(grid)
    
    # Print cost
    print(f'Total cost: {chosen_algorithm.calculate_cost(grid)}')

    # plot batteries, houses, and cables onto a grid as a scatter plot 
    make_scatter(grid.all_batteries.values(), grid.all_houses.values())

    # Creates output file
    grid.all_cables = list(grid.all_cables)
    with open('output4.json', 'w') as f:
        f.write(grid.json())
  