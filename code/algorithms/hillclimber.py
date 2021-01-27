import random
import copy
from .random_greedy import randomize_shared

class hillclimber(randomize_shared):

    def __init__(self, grid):
        self.grid = None
        self.houses_to_change = 2
        self.retry = False
        self.no_improvement = 0

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
        # Creates new cables in three parts
        # Uses result form to_mutate to find which cables to remove
        # Implements a loop to see which other houses need their cables to be removed as a result of
        # a cable from a different house missing.
        cables_to_remove = set()
        houses_to_change = set()

        # Puts cables from houses from initial list in the cables_to_remove set 1
        for House in houses:
            for cable in House.cables:
                cables_to_remove.add(tuple(cable))
            houses_to_change.add(House.id)

        # Finds houses with half broken cables 2
        new_house_found = True
        while new_house_found:
            current_set_size = len(houses_to_change)
            for House in grid.all_houses.values():
                for cable in House.cables:
                    if tuple(cable) in cables_to_remove:
                        houses_to_change.add(House.id)
                        for i in House.cables:
                            cables_to_remove.add(tuple(i))
                        break
            if current_set_size == len(houses_to_change):
                new_house_found = False

        # Removes the cables of all houses which need their cables removed 3
        houses_to_change = list(houses_to_change)
        for i in houses_to_change:
            key = grid.all_houses.get(i).battery
            grid.all_batteries.get(key).remaining_capacity += grid.all_houses.get(i).output    
            # Finds house and removes cables from battery
            for cable in grid.all_houses.get(i).cables:
                grid.all_batteries.get(key).cables.remove(tuple(cable))

            grid.all_houses.get(i).cables.clear()

        # Ensures battery coordinates are still in battery.cables for creation of new cables 4
        for Battery in grid.all_batteries.values():
            if tuple([Battery.x_coordinate,Battery.y_coordinate]) not in Battery.cables:
                Battery.cables.append(tuple([Battery.x_coordinate,Battery.y_coordinate]))

        # Builds new cables for these houses
        random.shuffle(houses_to_change)
        for i in houses_to_change:
            grid.all_houses.get(i).distance = 0
            self.get_destination(grid.all_houses.get(i), grid)
            self.create_new_cable(grid.all_houses.get(i), grid)

    def calculate_cost(self, grid):
        cable_cost = 0

        for Battery in grid.all_batteries.values():
            cable_cost += len(set(Battery.cables)) * Battery.cable_price
            cable_cost += Battery.battery_price

        return cable_cost

    def fix_error(self):
        self.retry = False
        return self.grid
    
    def check_solution(self, new_grid):
        """
        Checks and accepts better solutions than the current solution.
        """
        new_cost = self.calculate_cost(new_grid)
        old_cost = self.calculate_cost(self.grid) 

        # Save best solution
        if old_cost > new_cost:
            self.no_improvement = 0
            self.grid = new_grid
            self.cost = new_cost
            print(f"Found a better solution: {self.cost}!")
        else:
            self.no_improvement += 1

    def run(self, grid, to_change, iterations):
        """
        Runs the hillclimber algorithm for a specific amount of iterations.
        """
        self.houses_to_change = to_change
        self.iterations = iterations

        # Saves old grid
        self.grid = copy.deepcopy(grid)
        print("Started hillclimbing...")
        print(f"Initial cost: {self.calculate_cost(grid)}")
        
        # Makes small changes every loop
        while self.no_improvement < self.iterations:
            new_grid = copy.deepcopy(self.grid)
            
            # Mutates a few houses
            houses = self.find_to_mutate(new_grid)
            self.mutate_house_cable(houses, new_grid)
            
            # Check if solution is valid
            if self.retry:
                new_grid = self.fix_error()
                continue
            
            # Save best solution
            self.check_solution(new_grid)
        
        # Returns best grid
        return self.grid