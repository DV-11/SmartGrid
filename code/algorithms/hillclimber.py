import random
import copy

class hillclimber():

    def __init__(self, grid):
        if grid.is_solution() == False:
            raise Exception("hillclimber should only be called with a solved grid!")
        self.best_grid = copy.deepcopy(grid)

    def create_shared_cable(self, house, battery):
        pass

    def mutate_house_cable(self):
        pass

    def mutate_grid(self):
        pass

    def check_solution(self): 
        pass

    def run(self):
        pass

