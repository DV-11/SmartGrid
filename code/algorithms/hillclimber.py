import random
import copy
from .random_greedy import randomize_shared

class hillclimber(randomize_shared):

    def __init__(self, grid):
        self.grid = None
        self.n = 50
        self.houses_to_change = 2
        self.retry = False

    def new_destination(self, house, grid):
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

    def new_cable(self,house, grid):
        if [house.x_coordinate, house.y_coordinate] not in house.cables:
            house.latest_cable = ([house.x_coordinate, house.y_coordinate])
            house.cables.append([house.x_coordinate, house.y_coordinate])
            grid.all_batteries.get(house.battery).cables.append(tuple(house.latest_cable))
        current_distance = house.distance

        while list(house.latest_cable) != list(house.destination):
            new_cable = list(house.latest_cable)
            saved_cable = new_cable.copy()
            saved_distance = current_distance

            if saved_distance == 0:
                break

            while saved_distance <= current_distance:
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
            grid.all_batteries.get(house.battery).cables.append(tuple(new_cable))
            house.cables.append(new_cable)

    def find_to_mutate(self, grid):
        """
        Returns houses with longest distance to their destination along with a few random ones
        """
        # Sorts all houses based on distance
        houses_list = list(grid.all_houses.values())
        houses_list = sorted(houses_list, key=lambda House:House.distance, reverse=True)
        to_change = []

        # Picks houses with longest disance and a few random houses to change
        for i in range (self.houses_to_change):
            to_change.append(houses_list[i])
            random_number = random.randint(self.houses_to_change, len(houses_list) - 1)
            to_change.append(houses_list[random_number])
        
        return to_change

    def mutate_house_cable(self, houses, grid):
        # Creates new cables in three parts
        # Uses result form to_mutate to find which cables to remove
        # Implements a loop to see which other houses need their cables to be removed as a result of
        # a cable from a different house missing.
        cables_to_remove = set()
        houses_to_change = set()
        batteries_to_change = set()

        # Puts cables from houses from initial list in the cables_to_remove set
        for House in houses:
            for cable in House.cables:
                cables_to_remove.add(tuple(cable))
            houses_to_change.add(House.id)
            batteries_to_change.add(House.battery)

        # Checks which houses also need their cables removed. Loops until no knew houses to change are found
        new_house_found = True
        while new_house_found:
            current_set_size = len(houses_to_change)
            for House in grid.all_houses.values():
                for cable in House.cables:
                    if tuple(cable) in cables_to_remove:
                        houses_to_change.add(House.id)
                        batteries_to_change.add(House.battery)
                        for i in House.cables:
                            cables_to_remove.add(tuple(i))
            if current_set_size == len(houses_to_change):
                new_house_found = False

        # Removes the cables of all houses which need their cables removed
        houses_to_change = list(houses_to_change)
        for i in houses_to_change:
            key = grid.all_houses.get(i).battery
            grid.all_batteries.get(key).remaining_capacity += grid.all_houses.get(i).output
            # Finds house and removes cables from battery
            for cable in grid.all_houses.get(i).cables:
                grid.all_batteries.get(key).cables.remove(tuple(cable))

            grid.all_houses.get(i).cables.clear()

        # Ensures battery coordinates are still in battery.cables for creation of new cables
        for Battery in grid.all_batteries.values():
            if tuple([Battery.x_coordinate,Battery.y_coordinate]) not in Battery.cables:
                Battery.cables.append(tuple([Battery.x_coordinate,Battery.y_coordinate]))

        # Builds new cables for these houses
        for i in houses_to_change:
            grid.all_houses.get(i).distance = 0
            self.new_destination(grid.all_houses.get(i), grid)
            self.new_cable(grid.all_houses.get(i), grid)

    def calculate_cost(self, grid):
        cable_cost = 0

        for Battery in grid.all_batteries.values():
            cable_cost += len(set(Battery.cables)) * Battery.cable_price
            cable_cost += Battery.battery_price

        return cable_cost

    def fix_error(self):
        self.retry = False
        return self.grid

    def run(self, grid):
        # Saves old grid
        self.grid = copy.deepcopy(grid)
        no_improvement = 0

        # Makes small changes every loop
        while no_improvement < self.n:
            new_grid = copy.deepcopy(self.grid)
            # Mutates a few houses
            houses = self.find_to_mutate(new_grid)
            self.mutate_house_cable(houses, new_grid)
            # Check if solution is valid
            if self.retry:
                print('error in solution, retrying')
                new_grid = self.fix_error()
            # Save best solution
            if int(self.calculate_cost(self.grid)) > int(self.calculate_cost(new_grid)):
                no_improvement = 0
                print("found better solution")
                self.grid = new_grid
                print(self.calculate_cost(self.grid))
            else:
                no_improvement += 1
        
        # Returns best grid
        return self.grid

    
