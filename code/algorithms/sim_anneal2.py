import random
import math

from code.algorithms.hillclimber import hillclimber


class SimulatedAnnealing(hillclimber):
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

    def check_solution(self, new_grid):
        """
        Checks and accepts better solutions than the current solution.
        Also sometimes accepts solutions that are worse, depending on the current
        temperature.
        """
        new_cost = self.calculate_cost(new_grid)
        old_cost = self.calculate_cost(self.grid)

        # Calculate the probability of accepting this new grid
        delta = new_cost - old_cost
        probability = math.exp(-delta / self.T)

        # Pull a random number between 0 and 1 and see if we accept the graph!
        if random.random() < probability:
            self.no_improvement = 0
            self.grid = new_grid
            self.cost = new_cost
            print(f"Accepted a different solution: {self.cost}!")
        else:
            self.no_improvement += 1

        # Update the temperature
        self.update_temperature()
