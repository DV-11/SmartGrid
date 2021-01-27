from code.classes import grid, battery, house
from code.algorithms.u_random import u_random
from code.visualization.visualize import make_scatter
from code.algorithms.restricted import restricted_greedy
from code.algorithms.hillclimber import hillclimber
from code.algorithms.random_greedy import randomize_shared
from code.algorithms.sim_anneal import simulated_annealing

import json 


if __name__ == "__main__":

    # Allows user to choose a district
    valid_numbers = [1, 2, 3]
    district_number = 0

    while district_number not in valid_numbers:
        district_number = int(input("Choose a district (1, 2, 3) \n"))

    district = f"district-{district_number}"

    # Create a grid from data
    grid = grid.Grid(f"data/{district}/{district}_batteries.csv", f"data/{district}/{district}_houses.csv")
    print(f"Loading grid with data from district-{district_number}.")

    # Calculate combined battery capacity and combined house output
    total_capacity = 0
    for Battery in grid.all_batteries.values():
        total_capacity += Battery.capacity

    total_output = 0
    for House in grid.all_houses.values():
        total_output += House.output

    # Allows user to choose an algorithm
    all_algorithms = {"random_unique": u_random(grid), "restricted_greedy": restricted_greedy(grid), "shared_randomize" : randomize_shared(grid), "hillclimber": hillclimber(grid), "simulated_annealing": simulated_annealing(grid, temperature=19)}
    chosen_algorithm = None
    while chosen_algorithm not in all_algorithms:
        chosen_algorithm = input(f"Choose an algorithm {all_algorithms.keys()} \n")

    # Runs chosen algorithm
    print(f"Running algorithm: {chosen_algorithm}.")
    chosen_algorithm = all_algorithms.get(chosen_algorithm)

    # if isinstance(chosen_algorithm, hillclimber):
    #     grid = randomize_shared(grid).run(grid)

    if isinstance(chosen_algorithm, restricted_greedy):
        grid = restricted_greedy(grid).run(grid, district_number)
    elif isinstance(chosen_algorithm, hillclimber):
        grid = randomize_shared(grid).run(grid)
        grid = chosen_algorithm.run(grid, 1500)
    elif isinstance(chosen_algorithm, simulated_annealing):
        grid = chosen_algorithm.run(grid, 1500)
    else:
        grid = chosen_algorithm.run(grid)
    
    # Print cost
    print('Total cost:',f'{chosen_algorithm.calculate_cost(grid)}')

    # plot batteries, houses, and cables onto a grid as a scatter plot 
    make_scatter(grid.all_batteries.values(), grid.all_houses.values(), chosen_algorithm)

    # Creates output file
    grid.all_cables = list(grid.all_cables)
    with open('output.json', 'w') as f:
        f.write(grid.json())


  