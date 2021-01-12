import csv

class Battery():
    def __init__(self, battery_id, x, y, capacity):
        self.id = battery_id
        self.x_position = x
        self.y_position = y
        # self.position = position
        self.capacity = capacity
        self.reserved_capacity = 0
        self.cables = []
        self.houses = []
    
    def add_house(self, house):
        self.houses.append(house)
        # self.reserved_capacity = self.reserved_capacity - house.output
        self.reserved_capacity = self.reserved_capacity + house.output

    def add_cable(self, cable):
        self.cables.append(cable)