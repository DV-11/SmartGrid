import copy
import random

#from .randomize import random_reconfigure_node

class HillClimber:
    """
    The HillClimber class that changes a couple random house cables in the grid to a random different configuration. 
    Each improvement or equivalent solution is kept for the next iteration.
    """
    def __init__(self, grid):
        if not grid.is_solution():
            raise Exeption("HillClimber requires a complete solution.")
        
        self.grid = copy.deepcopy(grid)
        self.cost = grid.calculate_cost()

    def mutate_houses(self, new_grid):
        """
        Changes the value of a couple random house cables with a new random valid configuration.
        """
        # random_config = random.choice()
        # available_houses = 
        # random_reconfigure_house(new_grid, random_config, available_houses)

    def mutate_grid(self, new_grid, number_of_houses=1):
        """
        Changes the cables of a number of houses with a random valid configuration.
        """
        # for _ in range(number_of_houses):
        #     self.mutate_single_house(new_grid)

    def check_solution(self, new_grid):
        """
        Checks and accepts better solutions than the current solution.
        """
        new_cost = new_grid.calculate_cost()
        old_cost = self.cost

        if new_cost <= old_cost:
            self.grid = new_grid
            self.cost = new_cost

    def run(self, iterations, verbose=False, mutate_houses_number=1):
        """
        Runs the hillclimber algorithm for a specific amount of iterations.
        """
        self.iterations = iterations

        for iteration in range(iterations):
            # Nice trick to only print if variable is set to True
            print(f'Iteration {iteration}/{iterations}, current cost: {self.cost}') if verbose else None

            # Create a copy of the graph to simulate the change
            new_grid = copy.deepcopy(self.grid)

            self.mutate_grid(new_grid, number_of_houses=mutate_houses_number)

            # Accept it if it is better
            self.check_solution(new_grid)

