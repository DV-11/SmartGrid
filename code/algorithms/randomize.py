import random

# randomly assign a battery to each house to be connected without regard for outputs and capacities 
def random_assignment(grid):

    # take all batteries
    all_batteries = list(grid.all_batteries.values())

    # randomly assign a batterie to each house
    for House in grid.all_houses.values():
        House.battery = random.choice(all_batteries)

    # return grid with assignments 
    return grid

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
