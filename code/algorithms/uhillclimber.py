import random
import copy
from .hillclimber import hillclimber
from .u_random import u_random

class u_hillclimber(hillclimber):

    def __init__(self, grid):
        self.grid = None
        self.n = 1500
        self.houses_to_change = 2
        self.retry = False

    def mutate_house_cable(self, houses, grid):

        # Removes the cables of all houses which need their cables removed
        for i in houses:
            key = grid.all_houses.get(i).battery
            grid.all_batteries.get(key).remaining_capacity += grid.all_houses.get(i).output
            # Finds house and removes cables from battery
            for cable in grid.all_houses.get(i).cables:
                grid.all_batteries.get(key).cables.remove(tuple(cable))

            grid.all_houses.get(i).cables.clear()

        # Builds new cables for these houses
        for i in houses:
            grid.all_houses.get(i).distance = 0
            self.get_destination(grid.all_houses.get(i), grid)
            self.create_new_cable(grid.all_houses.get(i), grid)

    def calculate_cost(self, grid):
        cable_cost = 0

        for Battery in grid.all_batteries.values():
            cable_cost += len(set(Battery.cables)) * Battery.cable_price
        
        for House in grid.all_houses.values():
            cable_cost += len(House.cables)

        return cable_cost

    def fix_error(self):
        self.retry = False
        return self.grid
    

    def run(self, grid):
        # Saves old grid
        self.grid = copy.deepcopy(grid)
        no_improvement = 0
        print("Started hillclimbing...")
        print(f"Initial cost: {self.calculate_cost(grid)}")
        # Makes small changes every loop
        while no_improvement < self.n:
            new_grid = copy.deepcopy(self.grid)
            # Mutates a few houses
            houses = self.find_to_mutate(new_grid)
            self.mutate_house_cable(houses, new_grid)
            # Check if solution is valid
            if self.retry:
                new_grid = self.fix_error()
                continue
            # Save best solution
            if int(self.calculate_cost(self.grid)) > int(self.calculate_cost(new_grid)):
                no_improvement = 0
                self.grid = new_grid
                print(f"Found better solution: {self.calculate_cost(self.grid)}")
            else:
                no_improvement += 1
        
        # Returns best grid
        return self.grid