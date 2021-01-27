import random
import copy

class randomize_shared():
    def __init__(self):
        self.grid = None
        self.retry = False
        self.n = 100
        self.best_cost = 0

    def get_destination(self, house, grid):   
        """
        Finds closest battery or cable from house.
        """
        shortest_distance = float('inf')
        no_battery_found = 0

        # Loops through all batteries and finds all cables connected to each battery
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
        """
        Creates cables and saves them in house and battery object
        """
        # This code is specifically for the hillclimber, which might have removed the house coordinates
        if [house.x_coordinate, house.y_coordinate] not in house.cables:
            house.latest_cable = ([house.x_coordinate, house.y_coordinate])
            house.cables.append([house.x_coordinate, house.y_coordinate])
            grid.all_batteries.get(house.battery).cables.append(tuple(house.latest_cable))
        

        # Starts a loop until the destination (battery or cable) cable is saved in the house object
        current_distance = house.distance
        while list(house.latest_cable) != list(house.destination):
            
            # Sets variables
            new_cable = list(house.latest_cable)
            saved_cable = new_cable.copy()
            saved_distance = current_distance

            # Exception for houses that already have a cable run through them
            if saved_distance == 0:
                break
            
            # Creates random cables until one has improved distance to battery/cable
            while saved_distance <= current_distance:
                # Resets new cable in case previous cable was inefficient 
                new_cable[0] = saved_cable[0]
                new_cable[1] = saved_cable[1]
                # Randomly choses a direction
                positive = random.choice([1, -1])
                horizontal = random.choice([True, False])
                # Adjusts new cable accordingly
                if horizontal:
                    new_cable[0] = new_cable[0] + positive
                else:
                    new_cable[1] = new_cable[1] + positive
                # Checks to see if distance has improved
                current_distance = self.get_distance(new_cable[0], new_cable[1], house.destination[0], house.destination[1])
            
            # Updates variables for next cable
            current_distance = saved_distance - 1
            house.latest_cable = new_cable
            # Saves new cable in house and battery
            house.cables.append(new_cable)
            grid.all_batteries.get(house.battery).cables.append(tuple(new_cable))
            
            

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
        """
        Resets values of all attributes in house and battery.
        """
        print('Solution invalid, retrying.')

        # Removes all cables from battery and resets capacity
        for Battery in self.grid.all_batteries.values():
            Battery.cables = [tuple([Battery.x_coordinate, Battery.y_coordinate])]
            Battery.remaining_capacity = Battery.capacity

        # Sets all attributes in House objects to their initial values
        for House in self.grid.all_houses.values():
            House.cables.clear()
            House.destination = None
            House.distance = 0
            House.latest_cable = [House.x_coordinate, House.y_coordinate]

        # Sets this attribute to false so this function does not have to get called next iteration
        self.retry = False
                
    def run(self, grid):
        """
        Randomizes order of all houses and creates a path to a battery or existing cable
        in a semi-random fashion.
        """
        # Saves grid
        self.grid = grid

        # Shuffles all keys to effectively randomize the order in which houses get their cables made
        all_keys = list(self.grid.all_houses.keys())
        random.shuffle(all_keys)

        # Loops through all houses by their key
        for key in range(len(all_keys)):
            # Finds the nearest battery/cable, provided there is enough capacity left
            self.get_destination(self.grid.all_houses.get(all_keys[key]), self.grid)

            # Is set to True if at least one house could not find a battery to connect to
            if self.retry: 

                # Removes current position of grid and retries for a solution
                self.fix_error()
                self.run(self.grid)

            # Creates a cable for each house to its destination
            self.create_new_cable(self.grid.all_houses.get(all_keys[key]), self.grid)         

        return grid