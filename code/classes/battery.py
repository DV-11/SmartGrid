import csv

class Battery():
    def __init__(self, battery_id, x, y, capacity):
        self.id = battery_id
        self.x_coordinate = x
        self.y_coordinate= y
        # self.position = position
        self.capacity = float(capacity)
        self.remaining_capacity = float(capacity)
        self.cables = [tuple([self.x_coordinate, self.y_coordinate])]
        self.houses = []
