import csv

class House():
    def  __init__(self, house_id, x, y, output):
        self.id = house_id
        self.x_coordinate = int(x)
        self.y_coordinate = int(y)
        self.output = float(output)
        self.cables = []
        self.battery = None
        self.distance = 0
        self.destination = None
        self.to_battery = False
        self.latest_cable = [self.x_coordinate, self.y_coordinate]

    def has_cable(self):
        # ??? Does this work with a list??
        return self.cables is not None

    
