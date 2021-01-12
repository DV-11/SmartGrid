import csv

class House():
    def  __init__(self, house_id, x, y, output):
        self.id = house_id
        self.x_coordinate = x
        self.y_coordinate = y
        self.output = output
        self.cables = []
        self.battery = None