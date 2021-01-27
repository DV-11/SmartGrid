import random

class randomize_shared():
    def __init__(self, grid):
        self.grid = None
        self.retry = False

    def random_assignment(grid, possibilities):
        """
        Randomly assign each house with one of the batteries.
        """
        for house in graph.all_houses.values():
            house.set_value(random.choice(possibilities))

    def random_reconfigure_house(grid, house, possibilities): # !!!!!!!!
        """
        Takes a house and randomly re-connects to one of the available batteries.
        """
        house.disconnect_battery()
        # fix broken cables?
        house.connect_battery(random.choice(possibilities)) # possibilities is list of available batteries 

    # def random_reconfigure_shared_house(grid, house, possibilities):
    #     """
    #     Takes a house and randomly re-connects to one of the available batteries while.
    #     """
    #     house.disconnect_battery()
    #     # fix broken cables?
    #     house.connect_battery(random.choice(possibilities)) # possibilities is list of available batteries 
    
    
    def random_reconfigure_houses(grid, houses, possibilities):
        """
        Takes a list of houses and randomly re-connects each house to one of the available batteries.
        """
        for house in houses:
            random_reconfigure_house(grid, house, possibilities)

        def random_reconfigure_shared_houses(grid, houses, possibilities):
        """
        Takes a list of houses and randomly re-connects each house to one of the available batteries.
        """
        for house in houses:
            random_reconfigure_house(grid, house, possibilities)
        
        # fix broken cables
        # for each house in all_houses
            # if cables[-1] last coordinate != destination
            # cables.clear()
            # random_reconfigure_house(grid, house, possibilities):


    
    
    
    
    def get_destination(self, house, grid):   #get_nearest_destination? # stap 2
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

    def create_new_cable(self, house, grid): #stap 3
        house.cables.append(house.latest_cable)     # add latest cable to list in house
        grid.all_cables.add(tuple(house.latest_cable))  # add latest cable to list in grid
        current_distance = house.distance           # set current distance

        # Laying the cable
        while list(house.latest_cable) != list(house.destination):  # 
            new_cable = list(house.latest_cable)    # ??
            saved_cable = new_cable.copy()          # copy??
            saved_distance = current_distance       # copy current distance?

            # Repeat as long as distance is not 0
            while saved_distance <= current_distance and saved_distance != 0:   # Repeat while distance is 0?
                new_cable[0] = saved_cable[0]
                new_cable[1] = saved_cable[1]
                positive = random.choice([1, -1])       
                horizontal = random.choice([True, False])

                # Randomly move vertically or horizontally
                if horizontal:
                    new_cable[0] += positive
                else:
                    new_cable[1] += positive
                
                current_distance = self.get_distance(new_cable[0], new_cable[1], house.destination[0], house.destination[1])
            
            # Update current distance, latest cable, and cables
            current_distance = saved_distance - 1
            house.latest_cable = new_cable
            house.cables.append(new_cable)

            if tuple(new_cable) in grid.all_batteries.get(house.battery).cables:
                continue

            # Adding 1 cable to the list
            grid.all_batteries.get(house.battery).cables.append(tuple(new_cable))
            
            
            
            
            
            
    def run(self, grid):
        """
        Randomizes order of all houses and creates a path to a battery or existing cable
        in a semi-random fashion.
        """
        self.grid = grid
        # Choose random order for looping alll houses    stap 1
        all_house_keys = list(self.grid.all_houses.keys())
        random.shuffle(all_house_keys)        

        # Find nearest battery or cable     stap 2
        for key in range(len(all_keys)):
            self.get_destination(self.grid.all_houses.get(all_keys[key]), self.grid)

            if self.retry:
                self.fix_error()
                self.run(self.grid)

            # Lay cable in the shortest manner with a random route      stap 3
            self.create_new_cable(self.grid.all_houses.get(all_keys[key]), self.grid)

        return grid


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
                