import random
import copy

class hillclimber():

    def __init__(self, grid):
        self.best_grid = copy.deepcopy(grid)
        self.no_improvement_count = 0
        self.n= 0
        self.houses_to_change = 5

    def create_shared_cable(self, house):
        pass

    def find_to_mutate(self, grid):
        houses_list = list(grid.all_houses.values())
        houses_list = sorted(houses_list, key=lambda House:House.distance, reverse=True)
        to_change = []
        for i in range (self.houses_to_change):
            to_change.append(houses_list[i])
            random_number = random.randint(self.houses_to_change, len(houses_list))
            to_change.append(houses_list[random_number])
        return to_change

    def mutate_house_cable(self, houses):
        # delete existing cables
        for House in houses:
            for i in House.cables:
                print(i)
                print(self.best_grid.all_batteries.get(House.battery).cables)
                self.best_grid.all_batteries.get(House.battery).cables.remove(tuple(i))
        # create new cables
        for House in houses:
            self.create_shared_cable(House)

    def run(self, grid):
        houses = self.find_to_mutate(grid)
        self.mutate_house_cable(houses)
        return grid

    def calculate_cost(self, grid):
        cable_cost = 0
        for Battery in grid.all_batteries.values():
            cable_cost += len(Battery.cables) * 9
            cable_cost += 5000
        return cable_cost
