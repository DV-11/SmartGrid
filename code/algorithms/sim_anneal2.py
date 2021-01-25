from code.classes import grid, battery, house
from code.algorithms.randomize import random_assignment, create_cable
from code.visualization.visualize import make_scatter
from code.algorithms.greedy import greedy_assignment, find_distance
from code.algorithms.restricted import restricted_greedy
from code.algorithms.hillclimber import hillclimber
import random
from random import randrange
import json 

import random
import math

class SimulatedAnnealing(HillClimber):
    """
    The SimulatedAnnealing class that randomly reattaches a group of houses' cables. 
    Improvements or equivalent solutions are kept for the next iteration.
    Worse solutions are sometimes kept, depending on the temperature.
    """
    def __init__(self, grid, temperature=1):
        # Use the init of the Hillclimber class
        super().__init__(grid)

        # Starting temperature and current temperature
        self.T0 = temperature
        self.T = temperature

    def update_temperature(self):
        """
        This function implements a *exponential* cooling scheme.
        Alpha can be any value below 1 but above 0.
        Temperature will become zero after all iterations passed to the run()
        method have passed.
        """
        alpha = 0.99
        self.T = self.T * alpha

    def check_solution(self, grid):
        """
        Checks and accepts better solutions than the current solution.
        Also sometimes accepts solutions that are worse, depending on the current
        temperature.
        """
        # Calculate new value???
        # new_value = new_grid.calculate_value() !!!!!!!!
        # old_value = self.value???

        # Calculate the probability of accepting this new grid
        delta = new_value - old_value
        probability = math.exp(-delta / self.T)

        # Pull a random number between 0 and 1 and see if we accept the graph!
        if random.random() < probability:
            self.grid = new_grid
            self.value = new_value

        # Update the temperature
        self.update_temperature()
