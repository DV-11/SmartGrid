import random, copy

class u_random():
    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)
        self.retry = False

    # randomly assign a battery to each house to be connected without regard for outputs and capacities 
    def random_assignment(self, grid, houses):

        # take all batteries
        all_batteries = list(grid.all_batteries.values())
        random.shuffle(all_batteries)
        no_battery_found = 0
        # randomly assign a battery to each house
        for House in houses:
            if no_battery_found >= 5:
                self.retry = True
                break

            for Battery in all_batteries:
                if Battery.remaining_capacity - House.output > 0:
                    House.battery = Battery.id
                    House.destination = tuple([Battery.x_coordinate, Battery.y_coordinate])
                    Battery.remaining_capacity -= House.output
                    no_battery_found = 0
                    break
                else: 
                    no_battery_found += 1
                
        # return grid with assignments 
        return grid

    # get the coordenates of a cable between a house and a battery 
    def create_cable(self, house, battery):
        # set coordinates to ints 
        battery_c = [int(battery.x_coordinate),int(battery.y_coordinate)]
        house_c = [int(house.x_coordinate),int(house.y_coordinate)]

        # first points where the cable goes through 
        latest = house_c

        # determine which points in the grid the cable goes through 
        if house_c[1] >= battery_c[1]:
            while latest[1] > battery_c[1]:
                house.cables.append(tuple(latest))
                latest[1] = latest[1]-1
        else:
            while latest[1] < battery_c[1]:
                house.cables.append(tuple(latest))
                latest[1] = latest[1]+1
            
        if house_c[0] >= battery_c[0]:
            while latest[0] > battery_c[0]:
                house.cables.append(tuple(latest))
                latest[0] = latest[0] - 1
        else:
            while latest[0] < battery_c[0]:
                house.cables.append(tuple(latest))
                latest[0] = latest[0] + 1
            
        # final destination of the cable
        house.cables.append(tuple(battery_c))

    def calculate_cost(self, grid):
        cost = 5000 * len(grid.all_batteries.values())
        for House in grid.all_houses.values():
            cost += 9 * len(House.cables)
        return cost
        
    def run(self, grid):
        # Assigns a battery to each house
        houses = grid.all_houses.values()
        self.random_assignment(grid, houses)

        # Retries if configuration was invalid
        if self.retry:
            self.retry = False
            print("found error in solution, retrying")
            grid = self.grid
            self.run(grid)

        # Creates cable for each house
        for House in houses:
            self.create_cable(House, grid.all_batteries.get(House.battery))

        # Returns grid with cables    
        return grid