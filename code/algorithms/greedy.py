
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


# greedy that doesn't take capacities and outputs into account 
def greedy_assignment(grid):

    all_batteries = list(grid.all_batteries.values())

    # check every house
    for House in grid.all_houses.values():
        
        # placeholder variables
        closest_distance = 100000000
        closest_battery = None

        # check if a given battery is the closest one so far
        for Battery in all_batteries:
            distance = find_distance(House, Battery)

            # if so, update variables 
            if distance < closest_distance:
                closest_battery = Battery
                closest_distance = distance

        # connect house to closest battery
        House.battery = closest_battery
        
    return grid




