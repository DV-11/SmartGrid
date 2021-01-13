import random
import copy


def find_distance(house, battery):
    horizontal_distance = int(house.x_coordinate) - int(battery.x_coordinate)
    vertical_distance = int(house.y_coordinate) - int(battery.y_coordinate)
    if horizontal_distance < 0:
        horizontal_distance = horizontal_distance * -1
    if vertical_distance < 0:
        vertical_distance = vertical_distance * -1 
    return horizontal_distance + vertical_distance


def greedy_assignment(grid):
    all_batteries = list(grid.all_batteries.values())

    for House in grid.all_houses.values():
        
        closest_distance = 100000000
        closest_battery = None

        for Battery in all_batteries:
            distance = find_distance(House, Battery)
            if distance < closest_distance:
                closest_battery = Battery
                closest_distance = distance

        House.battery = closest_battery
    return grid




