import random
import copy

def random_assignment(grid):
    all_batteries = list(grid.all_batteries.values())
    for House in grid.all_houses.values():
        House.battery = random.choice(all_batteries)
    return grid

def create_cable(house, battery):
    # Sets cable to right y-coordinate
    latest_y = house.y_coordinate
    latest_x = house.x_coordinate

    while latest_y < battery.y_coordinate:
        latest_y -= 1
        new_cable = (latest_x, latest_y)
        house.cables.append(new_cable)

    while latest_y > battery.y_coordinate:
        latest_y += 1
        new_cable = (latest_x, latest_y)
        house.cables.append(new_cable)

    while latest_x < battery.x_coordinate:
        latest_x -= 1
        new_cable = (latest_x, latest_y)
        house.cables.append(new_cable)

    while latest_x > battery.x_coordinate:
        latest_x += 1
        new_cable = (latest_x, latest_y)
        house.cables.append(new_cable)