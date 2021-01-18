import random
from .functions import find_distance, make_cable

class randomize_shared():
    def __init__(self, grid):
        self.grid = grid 

    def find_destination(self, house):
        # Finds nearest cable or battery
        shortest_distance = float('inf')
        for Battery in self.grid.all_batteries.values():
            new_distance = find_distance(house, Battery.x_coordinate, Battery.y_coordinate)
            if new_distance < shortest_distance:
                shortest_distance = new_distance
                house.destination = tuple(Battery.x_coordinate, Battery.y_coordinate)

        for cable_count in range(len(self.grid.all_cables)):
            new_distance = find_distance(house, self.grid.all_cables(cable_count)(0),self.grid.all_cables(cable_count)(1))
            if new_distance < shortest_distance:
                shortest_distance = new_distance
                house.destination = tuple(self.grid.all_cables(cable_count)(0), self.grid.all_cables(cable_count)(1))
                house.distance = shortest_distance

    def create_shared_cable(self, house):
        current_distance = house.distance
        while current_distance > 0:
            horizontal_first = random.choice([True, False])
            make_cable(house, horizontal_first)

    def run(self):
        for House in self.grid.all_houses.values():
            self.create_shared_cable(House)
        