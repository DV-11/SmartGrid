import random
from .greedy import find_distance

class randomize_shared():
    def __init__(self, grid):
        self.grid = grid 

    def find_nearest_battery(self, house):
        # Finds nearest cable or battery
        shortest_distance = float('inf')
        for Battery in self.grid.all_batteries.values():
            new_distance = find_distance(house, Battery)
            if new_distance < shortest_distance:
                shortest_distance = new_distance
                house.destination = tuple(Battery.x_coordinate, Battery.y_coordinate)

        for cable_count in range(len(self.grid.all_cables)):
            cable_x_coordinate = self.grid.all_cables(cable_count)(0)
            cable_y_coordinate = self.grid.all_cables(cable_count)(1)
            horizontal_distance = int(house.x_coordinate) - int(cable_x_coordinate)
            vertical_distance = int(house.y_coordinate) - int(cable_y_coordinate)
            if horizontal_distance < 0:
                horizontal_distance = horizontal_distance * -1
            if vertical_distance < 0:
                vertical_distance = vertical_distance * -1 
            new_distance = horizontal_distance + vertical_distance
            
            if new_distance < shortest_distance:
                shortest_distance = new_distance
                house.destination = self.grid.all_cables(cable_count)

    def create_shared_cable(self, house):
        pass

    def run(self):
        for House in self.grid.all_houses.values():
            self.create_shared_cable(House)
        