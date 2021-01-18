def find_distance(house, destination_x, destination_y):
    horizontal_distance = house.x_coordinate - destination_x
    if horizontal_distance < 0:
        horizontal_distance = horizontal_distance * - 1
        house.destination[0] = 'right'
    else:
        house.destination[0] = 'left'
    vertical_distance = house.y_coordinate - destination_y
    if vertical_distance < 0:
        vertical_distance = vertical_distance * - 1
        house.destination[1] = 'up'
    else:
        house.destination[1] = 'down'

    return horizontal_distance + vertical_distance

def make_cable(house, horizontal_first):
    if horizontal_first:
        if house.x_coordinate == house.destination[0]:
            return None    
    else:
        if house.y_coordinate == house.destination[1]:
            return None
    