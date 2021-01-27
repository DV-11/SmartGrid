import random
import copy
from .random_greedy import randomize_shared

class hillclimber(randomize_shared):

    def __init__(self, grid):
        self.grid = None
        self.n = 5
        self.houses_to_change = 2
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
        # Creates new cables in three parts
        # Uses result form to_mutate to find which cables to remove
        # Implements a loop to see which other houses need their cables to be removed as a result of
        # a cable from a different house missing.
        cables_to_remove = set()        # items can be added, but not changed
        houses_to_change = set()        
        batteries_to_change = set()

        # Puts cables from houses from initial list in the cables_to_remove set
        for House in houses:    # house object
            for cable in House.cables:  # cable: [10,47]
                cables_to_remove.add(tuple(cable)) 
                print("tuple(cable):", tuple(cable)) # (43, 32)
            houses_to_change.add(House.id)      # remove id??
            batteries_to_change.add(House.battery)

        print("1cables_to_remove:", cables_to_remove) # {(49, 23), (10, 34), ...}
        print("1batteries_to_change:", batteries_to_change) # {1, 2, 4, 5}
        print("1houses_to_change:", houses_to_change) # {73, 82, 86, 95}

        # Checks which houses also need their cables removed. Loops until no knew houses to change are found
        new_house_found = True
        while new_house_found:  # loops twice
            current_set_size = len(houses_to_change) # current_set_size: 4 , 35
            print("current_set_size:", current_set_size)

            for House in grid.all_houses.values():
                for cable in House.cables:
                    if tuple(cable) in cables_to_remove:
                        houses_to_change.add(House.id)
                        batteries_to_change.add(House.battery)
                        for i in House.cables:  
                            print("i:", i)                              # [43, 13]
                            print("tuple(cable):", tuple(cable))        # repeats the same many times!
                            cables_to_remove.add(tuple(cable))          # DOES NOTHING??
            if current_set_size == len(houses_to_change):
                new_house_found = False
            
        print("2cables_to_remove:", cables_to_remove) # same 
        print("2batteries_to_change:", batteries_to_change) # same, but could increase
        print("2houses_to_change:", houses_to_change) # much more

        # Removes the cables of all houses which need their cables removed
        houses_to_change = list(houses_to_change)
        for i in houses_to_change:  # 129 wouldnt it be better if house objects were saved in this list instead of house id
            print("i:", i)
            print("grid.all_houses.get(i).battery:", grid.all_houses.get(i).battery)
            key = grid.all_houses.get(i).battery   # 2 (which battery)
            print("key:", key)
            # Update remaining capacity
            grid.all_batteries.get(key).remaining_capacity += grid.all_houses.get(i).output # this is used_capacity not remaining
            print("grid.all_batteries.get(key).remaining_capacity:", grid.all_batteries.get(key).remaining_capacity)
            # Finds house and removes cables from battery

            print("1grid.all_houses.get(i).cables:", grid.all_houses.get(i).cables)

            for cable in grid.all_houses.get(i).cables: # [38, 18] in list of lists
                print("cable:", cable)
                grid.all_batteries.get(key).cables.remove(tuple(cable))

            grid.all_houses.get(i).cables.clear()
            print("2grid.all_houses.get(i):", grid.all_houses.get(i)) # house object
            print("2grid.all_houses.get(i).cables:", grid.all_houses.get(i).cables)

        # Ensures battery coordinates are still in battery.cables for creation of new cables
        for Battery in grid.all_batteries.values():
            if tuple([Battery.x_coordinate,Battery.y_coordinate]) not in Battery.cables:
                Battery.cables.append(tuple([Battery.x_coordinate,Battery.y_coordinate]))

        # Builds new cables for these houses
        for i in houses_to_change:
            grid.all_houses.get(i).distance = 0
            self.get_destination(grid.all_houses.get(i), grid)
            self.create_new_cable(grid.all_houses.get(i), grid)

    def run(self, grid):
        # Saves old grid
        self.grid = copy.deepcopy(grid)
        no_improvement = 0

        # Makes small changes every loop
        while no_improvement < self.n:
            new_grid = copy.deepcopy(self.grid)
            # Mutates a few houses
            houses = self.find_to_mutate(new_grid)
            self.mutate_house_cable(houses, new_grid)
            # Check if solution is valid
            if self.retry:
                print('error in solution, retrying')
                new_grid = self.fix_error()
            # Save best solution
            if int(self.calculate_cost(self.grid)) > int(self.calculate_cost(new_grid)):
                no_improvement = 0
                print("found better solution")
                self.grid = new_grid
            else:
                no_improvement += 1
        
        # Returns best grid
        return self.grid

    def calculate_cost(self, grid):
        cable_cost = 0

        for Battery in grid.all_batteries.values():
            cable_cost += len(set(Battery.cables)) * Battery.cable_price
            cable_cost += Battery.battery_price

        return cable_cost

    def fix_error(self):
        self.retry = False
        return self.grid