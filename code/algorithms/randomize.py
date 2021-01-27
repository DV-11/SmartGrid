import random, copy, operator

class randomize():
    def __init__(self, grid):
        self.grid = None
        self.retry = False
        self.first = True

    # Randomly assigns a battery to each house to be connected without regard for outputs and capacities 
    def random_assignment(self, grid, houses):

        # Takes all batteries
        all_batteries = list(grid.all_batteries.values())
        random.shuffle(all_batteries)
            
        # Randomly assign a battery to each house
        for House in houses:
            no_battery_found = 0

            # Checks per battery if there is still room, if so connects, otherwise counts this
            for Battery in all_batteries:
                if Battery.remaining_capacity - House.output > 0:
                    House.destination = tuple([Battery.x_coordinate, Battery.y_coordinate])
                    House.battery = Battery.id
                    Battery.remaining_capacity -= House.output
                    no_battery_found = 0
                    break
                else: 
                    no_battery_found += 1

                # If no battery was found, sets variable to retry to true and ends loop
                if no_battery_found >= 5:
                    self.retry = True
                    break

        # Returns grid 
        return grid

    def create_cable(self, house, battery):

        # Convert coordinates to integers
        house_c = [int(house.x_coordinate),int(house.y_coordinate)]
        destination_c = [int(battery.x_coordinate), int(battery.y_coordinate)]

        # Sets orientation to house coordinates 
        latest = house_c

        # Adds cables in direction until they reach coordinates of destination 
        if house_c[1] >= destination_c[1]:
            while latest[1] > destination_c[1]:
                house.cables.append(tuple(latest))
                latest[1] = latest[1]-1
        else:
            while latest[1] < destination_c[1]:
                house.cables.append(tuple(latest))
                latest[1] = latest[1]+1
            
        if house_c[0] >= destination_c[0]:
            while latest[0] > destination_c[0]:
                house.cables.append(tuple(latest))
                latest[0] = latest[0] - 1
        else:
            while latest[0] < destination_c[0]:
                house.cables.append(tuple(latest))
                latest[0] = latest[0] + 1
            
        # Adds the final cable 
        house.cables.append(tuple(destination_c))

    def calculate_cost(self, grid):
        # Calcultes cost
        cost = 5000 * len(grid.all_batteries.values())
        for House in grid.all_houses.values():
            cost += 9 * len(House.cables)
        return cost

    def run(self, grid):
        # Assigns a battery to each house
        if self.first:
            self.grid = copy.deepcopy(grid)
        houses = list(grid.all_houses.values())
    
        self.random_assignment(grid, houses)
    
        # Retries if configuration was invalid
        if self.retry:
            self.retry = False
            self.first = False
            grid = self.grid
            self.run(grid)

        # Creates cable for each house
        for House in houses:
            self.create_cable(House, grid.all_batteries.get(House.battery))

        # Returns grid with cables    
        return grid