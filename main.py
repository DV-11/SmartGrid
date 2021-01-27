from code.classes import grid, battery, house
from code.algorithms.randomize import randomize
from code.visualization.visualize import make_scatter
from code.algorithms.greedy import restricted_greedy
from code.algorithms.hillclimber import hillclimber
from code.algorithms.uhillclimber import u_hillclimber
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

    # Allows user to choose an algorithm
    unique_cables_algorithms = {"randomize": randomize(grid), "greedy": restricted_greedy(grid), "hillclimber": u_hillclimber(grid)}
    shared_cables_algorithms = {"randomize" : randomize_shared(grid), "hillclimber": hillclimber(grid), "simulated annealing": simulated_annealing(grid, temperature=10000),}
    chosen_algorithm = None

    valid_choices = ["yes", "no"]
    choice = None
    while choice not in valid_choices:
        choice = input("Would you like to run an algorithm where cables can be shared? (yes/no)\n")
    

    if choice == 'no':
        chosen_algorithm = input(f"Choose an algorithm {unique_cables_algorithms.keys()} \n")
        print(f"Running algorithm: {chosen_algorithm}.")
        chosen_algorithm = unique_cables_algorithms.get(chosen_algorithm)
    else:
        chosen_algorithm = input(f"Choose an algorithm {shared_cables_algorithms.keys()} \n")
        print(f"Running algorithm: {chosen_algorithm}.")
        chosen_algorithm = shared_cables_algorithms.get(chosen_algorithm)
    # Runs chosen algorithm
    
    

    if isinstance(chosen_algorithm, restricted_greedy):
        grid = restricted_greedy(grid).run(grid, district_number)

    elif isinstance(chosen_algorithm, hillclimber):
        to_change = int(input("How many houses would you like to change per iteration (recommend 2-5)\n"))
        iterations = int(input("How many times should the program run without improving before quitting?\n"))
        grid = randomize_shared(grid).run(grid)
        grid = chosen_algorithm.run(grid, to_change, iterations)

    elif isinstance(chosen_algorithm, simulated_annealing):
        iterations = int(input("How many times should the program run without improving before quitting?\n"))
        grid = chosen_algorithm.run(grid, iterations)

    elif isinstance(chosen_algorithm, u_hillclimber):
        to_change = int(input("How many houses would you like to change per iteration (recommend 2-5)\n"))
        iterations = int(input("How many times should the program run without improving before quitting?\n"))
        grid = randomize(grid).run(grid)
        grid = chosen_algorithm.run(grid, to_change, iterations)
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


  