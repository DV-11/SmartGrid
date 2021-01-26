import random
import copy
from .randomize2 import randomize_shared

class hillclimber(randomize_shared):

    def __init__(self, grid):
        self.grid = None
        self.n = 200
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
        # delete existing cables
        all_gone = []
        for House in houses:
            grid.all_batteries.get(House.battery).cables = list(set(grid.all_batteries.get(House.battery).cables))
            
            for i in range(len(House.cables)):
                if i == 0:
                    continue
                if House.cables[i] in all_gone:
                    continue
                print(House.cables[i])

                grid.all_batteries.get(House.battery).cables.remove(tuple(House.cables[i]))
                all_gone.append(House.cables[i])
            House.cables.clear()
            House.latest_cable = [House.x_coordinate, House.y_coordinate]
        # ensure that battery coordinates are still in Battery
        for Battery in grid.all_batteries.values():
            Battery.cables.append(tuple([Battery.x_coordinate, Battery.y_coordinate]))

        # create new cables
        for House in houses:
            self.get_destination(House, grid)
            if self.retry:
                self.fix_error()
            self.create_new_cable(House, grid)

    def run(self, grid):
        # Saves old grid
        self.grid = copy.deepcopy(grid)
        no_improvement = 0

        # Makes small changes every loop
        while no_improvement < self.n:
            new_grid = copy.deepcopy(self.grid)
            houses = self.find_to_mutate(new_grid)
            self.mutate_house_cable(houses, new_grid)
            print('old')
            print(self.calculate_cost(self.grid))
            print('new')
            print(self.calculate_cost(new_grid))
            
            if int(self.calculate_cost(self.grid)) > int(self.calculate_cost(new_grid)):
                no_improvement = 0
                print("found better solution")
                self.grid = new_grid
            else:
                no_improvement += 1

        # Returns best loop
        return self.grid

    def calculate_cost(self, grid):
        cable_cost = 0

        for Battery in grid.all_batteries.values():
            cable_cost += len(set(Battery.cables)) * Battery.cable_price
            cable_cost += Battery.battery_price

        return cable_cost

    def fix_error(self):
        pass