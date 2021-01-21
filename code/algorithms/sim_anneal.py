from code.classes import grid, battery, house
from code.algorithms.randomize import random_assignment, create_cable
from code.visualization.visualize import make_scatter
from code.algorithms.greedy import greedy_assignment, find_distance
from code.algorithms.restricted import restricted_greedy
from code.algorithms.hillclimber import hillclimber
import random
from random import randrange
import json 

def sim_anneal(grid, repetitions):
    
    all_batteries = list(grid.all_batteries.values())
    grid = random_assignment(grid) 
    score = grid.calculate_cost()

    for i in range(repetitions):
        
        temp_grid = grid
        house = None
        stopper = randrange(len(temp_grid.all_houses.values()))
        counter = 0
        for i in temp_grid.all_houses.values():
            if counter == stopper:
                house = i
            counter = counter + 1
        house.battery = random.choice(all_batteries)
        new_score = temp_grid.calculate_cost()
        if new_score < score:
            grid = temp_grid

    return grid

district = "district-1"
grid = grid.Grid(f"data/{district}/{district}_batteries.csv", f"data/{district}/{district}_houses.csv")
grid = sim_anneal(grid, 10000000)

for House in grid.all_houses.values():
    create_cable(House, House.battery)

print("Total cost:", grid.calculate_cost())

make_scatter(grid.all_batteries.values(), grid.all_houses.values())