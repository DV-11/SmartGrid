import random

class randomize_shared():
    def __init__(self, grid):
        self.grid = None
        self.retry = False

    def get_destination(self, house, grid):   #get_nearest_destination?
        """
        Finds closest battery or cable from house.
        """
        shortest_distance = float('inf')
        no_battery_found = 0

        # Loops through all batteries and finds all cables connected to each battery?
        for Battery in grid.all_batteries.values():
            battery_cables = list(Battery.cables)
            
            # Find new solution when all batteries are full
            if Battery.remaining_capacity - house.output < 0:
                no_battery_found += 1

                if no_battery_found >= 5:
                    self.retry = True
                    break

                continue
            
            no_battery_found = 0

            # Finds distance for each viable destination
            for cable in range(len(battery_cables)):
                new_distance = self.get_distance(house.x_coordinate, house.y_coordinate, 
                                int(battery_cables[cable][0]), int(battery_cables[cable][1]))
                
                # Updates shortest distance and saves destination coordinates and battery ID
                if new_distance < shortest_distance:
                    shortest_distance = new_distance
                    house.destination = tuple([int(battery_cables[cable][0]), int(battery_cables[cable][1])])
                    house.battery = Battery.id

        # Update distance and remaining capacity when valid destination is found
        if self.retry == False:
            house.distance = self.get_distance(house.x_coordinate, house.y_coordinate, house.destination[0], house.destination[1])
            grid.all_batteries.get(house.battery).remaining_capacity -= house.output
        
    def get_distance(self, origin_x, origin_y, destination_x, destination_y):
        """
        Finds distance between two points using their coordinates.
        """
        horizontal_distance = abs(int(origin_x) - destination_x)
        vertical_distance = abs(int(origin_y) - destination_y)

        return vertical_distance + horizontal_distance

    def create_new_cable(self,house, grid):
        house.cables.append(house.latest_cable)
        grid.all_cables.add(tuple(house.latest_cable))
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
            
            current_distance = saved_distance - 1
            house.latest_cable = new_cable
            house.cables.append(new_cable)
            if tuple(new_cable) in grid.all_batteries.get(house.battery).cables:
                continue
            grid.all_batteries.get(house.battery).cables.append(tuple(new_cable))
            
            
            
            
            
            
    def run(self, grid):
        """
        Randomizes order of all houses and creates a path to a battery or existing cable
        in a semi-random fashion.
        """
        self.grid = grid
        # Loop through all houses in grid
        all_keys = list(self.grid.all_houses.keys())
        random.shuffle(all_keys)

        for key in range(len(all_keys)):
            self.get_destination(self.grid.all_houses.get(all_keys[key]), self.grid)

            if self.retry:
                self.fix_error()
                self.run(self.grid)
            self.create_new_cable(self.grid.all_houses.get(all_keys[key]), self.grid)
        return grid

    def calculate_cost(self, grid):
        """
        Calculates the cost of this configuration.
        """
        cable_cost = 0

        for Battery in grid.all_batteries.values():
            cable_cost += len(set(Battery.cables)) * Battery.cable_price
            cable_cost += Battery.battery_price

        return cable_cost
    
    def fix_error(self):
        
                print('Solution invalid, retrying.')
                self.grid.all_cables.clear()

                for Battery in self.grid.all_batteries.values():
                    Battery.cables = [tuple([Battery.x_coordinate, Battery.y_coordinate])]
                    Battery.remaining_capacity = Battery.capacity
                    Battery.houses.clear()

                for House in self.grid.all_houses.values():
                    House.cables.clear()
                    House.destination = None
                    House.distance = 0
                    House.latest_cable = [House.x_coordinate, House.y_coordinate]
            
                self.retry = False
                