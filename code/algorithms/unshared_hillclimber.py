import random
import copy
from .hillclimber import hillclimber
from .randomize import randomize

class unshared_hillclimber(randomize):

    def __init__(self):
        self.grid = None
        self.n = 50
        self.houses_to_change = 5
        self.retry = False

    def find_to_mutate(self, grid):
        """
        Returns houses with longest distance to their destination along with a few random ones
        """
        # Sorts all houses based on distance
        houses_list = list(grid.all_houses.values())
        houses_list = sorted(houses_list, key=lambda House:House.distance, reverse=True)
        to_change = []

        # Picks houses with longest disance and a few random houses to change
        for i in range (self.houses_to_change):
            to_change.append(houses_list[i])
            random_number = random.randint(self.houses_to_change, len(houses_list) - 1)
            to_change.append(houses_list[random_number])
        
        return to_change

    def mutate_house_cable(self, houses, grid):
        """
        Removes all cables from previously chosen houses and creates new ones
        """
        # Removes the cables of all houses which need their cables removed
        for House in houses:
            House.cables.clear()
            House.latest_cable = tuple([(House.x_coordinate, House.y_coordinate)])
            # Restores capacity of corresponding battery
            grid.all_batteries.get(House.battery).remaining_capacity += House.output

        # Assigns new destination to houses and creates cable
        self.random_assignment(grid, houses)
        for House in houses:
            battery = grid.all_batteries.get(House.battery)
            self.create_cable(House, battery)
        
    def calculate_cost(self, grid):
        """
        Returns cost of current cable configuration
        """
        cost = 5000 * len(grid.all_batteries.values())
        for House in grid.all_houses.values():
            cost += 9 * len(House.cables)
        return cost

    def fix_error(self):
        """
        Returns old grid to undo changes that led to error
        """
        self.retry = False
        return self.grid
    
    def run(self, grid, houses_to_change, iterations):
        """
        Starts with a random solution and makes small changes until 
        no improvements have been found for a number of iterations chosen by user
        """
        # Saves user input
        self.houses_to_change = houses_to_change

        # Saves initial solution
        self.grid = copy.deepcopy(grid)

        # Sets variable and informs user
        no_improvement = 0
        print("Started hillclimbing...")
        print(f"Initial cost: {self.calculate_cost(grid)}")

        # Makes small changes every loop
        while no_improvement < iterations:
            new_grid = copy.deepcopy(self.grid)

            # Mutates a few houses
            houses = self.find_to_mutate(new_grid)
            self.mutate_house_cable(houses, new_grid)

            # Check if solution is valid, if not: makes changes undone
            if self.retry:
                new_grid = self.fix_error()
                continue

            # Save best solution
            if self.calculate_cost(self.grid) > self.calculate_cost(new_grid):
                no_improvement = 0
                self.grid = new_grid
                print(f"Found better solution: {self.calculate_cost(self.grid)}")
            else:
                no_improvement += 1
        
        # Returns best grid
        return self.grid