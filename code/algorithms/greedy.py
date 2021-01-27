from operator import itemgetter

# find the distance between a house and a battery 
def find_distance(house, battery):
    
    #derermine horizontal and vertical distance 
    horizontal_distance = int(house.x_coordinate) - int(battery.x_coordinate)
    vertical_distance = int(house.y_coordinate) - int(battery.y_coordinate)
    
    # get only the absolute distance regardless of direction 
    if horizontal_distance < 0:
        horizontal_distance *= -1
    
    if vertical_distance < 0:
        vertical_distance *= -1 

    # return total distance 
    return horizontal_distance + vertical_distance

# get the coordenates of a cable between a house and a battery 
def create_cable(house, battery):
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


# greedy algorithm that takes output and capacity into account
class restricted_greedy():
    def __init__(self, grid):
        pass

    def run(self, grid, district_number):
        all_batteries = list(grid.all_batteries.values())

        # Makes a list with each battery, max capacity and the current output
        capacities_and_outputs = []

        # Makes a list with houses and their outputs 
        by_output= []

        for Battery in all_batteries:
            capacities_and_outputs.append([Battery,float(Battery.capacity),0])

        # Finds the closest house to connect 
        for House in grid.all_houses.values():
            by_output.append([House, float(House.output)])
        

        # order houses by output for district 3
        if district_number == 3:
            by_output = sorted(by_output, key=itemgetter(1), reverse= True)

        for House in by_output:
            closest_distance = 100000000
            closest_battery = None

        # make sure the house is the closest and does not go over the max capacity 
            for Battery in capacities_and_outputs:
                distance = find_distance(House[0], Battery[0])
                
                if distance < closest_distance and Battery[2] + House[1] < Battery[1]:
                    closest_battery = Battery[0]
                    closest_distance = distance
                    
            # connect house to battery and update current output 
                House[0].battery = closest_battery
            
            for i in capacities_and_outputs:
                if i[0] == closest_battery: i[2] = i[2] + House[1]
 
        for House in grid.all_houses.values():
            create_cable(House, House.battery)   
 
        # return grid of connected houses and batteries  
        return grid
    
    def calculate_cost(self, grid):

        # initial empty cost
        total_cost = 0

        # add cost of batteries
        total_cost += (5000 * len(grid.all_batteries.values()))

        # add cost of cables
        for House in grid.all_houses.values():
            total_cost += (len(House.cables) - 1) * 9
        
        # return total
        return total_cost   