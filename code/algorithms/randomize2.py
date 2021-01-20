import random

class randomize_shared():
    def __init__(self, grid):
        self.grid = grid 

    def get_destination(self, house):
        """
        Finds closest battery or cable from house
        """

        shortest_distance = float('inf')

        # Loops through all batteries and finds all cables connected to them to find nearest destination
        for Battery in self.grid.all_batteries.values():
            battery_cables = list(Battery.cables)

            for cable in range(len(battery_cables)):
                new_distance = self.get_distance(house.x_coordinate, house.y_coordinate, 
                int(battery_cables[cable][0]), int(battery_cables[cable][1]))
                
                # Updates shortest distance and saves both coordinates of cable/battery as well as the 
                # id of the corresponding battery for retrieving it later.
                if new_distance < shortest_distance:
                    shortest_distance = new_distance
                    house.destination = tuple([int(battery_cables[cable][0]), int(battery_cables[cable][1])])
                    house.battery = Battery.id

        house.distance = self.get_distance(house.x_coordinate, house.y_coordinate, house.destination[0], house.destination[1])
        self.grid.all_batteries.get(house.battery).remaining_capacity -= house.output
        
    def get_distance(self, origin_x, origin_y, destination_x, destination_y):
        """
        Finds distance between two points using their coordinates
        """
        horizontal_distance = int(origin_x) - destination_x
        if horizontal_distance < 0:
            horizontal_distance *= -1
        vertical_distance = int(origin_y) - destination_y
        if vertical_distance < 0:
            vertical_distance *= -1
        return vertical_distance + horizontal_distance

    def create_new_cable(self,house):
        house.cables.append(house.latest_cable)
        self.grid.all_cables.add(tuple(house.latest_cable))
        current_distance = house.distance
        while list(house.latest_cable) != list(house.destination):
            new_cable = list(house.latest_cable)
            saved_cable = new_cable.copy()
            saved_distance = current_distance
            while saved_distance <= current_distance and saved_distance != 0:
                new_cable[0] = saved_cable[0]
                new_cable[1] = saved_cable[1]
                positive = random.choice([1, -1])
                horizontal = random.choice([True, False])
                if horizontal:
                    new_cable[0] = new_cable[0] + positive
                else:
                    new_cable[1] = new_cable[1] + positive
                current_distance = self.get_distance(new_cable[0], new_cable[1], house.destination[0], house.destination[1])
            house.latest_cable = new_cable
            house.cables.append(new_cable)
            self.grid.all_batteries.get(house.battery).cables.append(tuple(new_cable))
            current_distance = saved_distance - 1
            
    def run(self, grid):
        """
        Randomizes order of all houses and creates a path to a battery or existing cable
        in a semi-random fashion
        """
        # Loop through all houses in grid
        all_keys = list(self.grid.all_houses.keys())
        # Randomize order of keys
        random.shuffle(all_keys)
        for key in range(len(all_keys)):
            self.get_destination(self.grid.all_houses.get(all_keys[key]))
            self.create_new_cable(self.grid.all_houses.get(all_keys[key]))
        return grid
    
    def calculate_cost(self, grid):
        cable_cost = 0
        for Battery in grid.all_batteries.values():
            cable_cost += len(Battery.cables) * 9
            cable_cost += 5000
        return cable_cost