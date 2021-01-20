import random
import copy

class hillclimber():

    def __init__(self, grid):
        if grid.is_solution() == False:
            pass
        self.best_grid = copy.deepcopy(grid)
        self.no_improvement_count = 0
        self.n= 0
        self.mutation_count = 0

    def create_shared_cable(self, house, battery):
        pass

    def find_to_mutate(self):
        houses = []
        return houses

    def mutate_house_cable(self, house):
        pass

    def run(self, greedy):
        return self.best_grid
