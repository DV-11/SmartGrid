def find_distance(house, battery):
    horizontal_distance = house.x_coordinate - battery.x_coordinate
    vertical_distance = house.y_coordinate - battery.y_coordinate
    if horizontal_distance < 0:
        horizontal_distance = horizontal_distance * -1
    if vertical_distance < 0:
        vertical_distance = vertical_distance * -1 
    return horizontal_distance + vertical_distance