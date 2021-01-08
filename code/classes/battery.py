import csv

class Battery():
    def __init__(self, x, y, capacity):
        self.id = 0
        self.x_coordinate = x
        self.y_coordinate = y
        self.capacity = capacity
        self.current_capacity = capacity
        self.cables = []
        self.houses = []
    
    def add_house(self, house):
        self.houses.append(house)
        self.current_capacity = self.current_capacity - house.output

    def add_cable(self, cable):
        self.cables.append(cable)