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

    def has_cable(self):    # CHECK IF THIS WORKS
        # ??? Does this work with a list??
        return self.cables is not None

    def find_nearest_battery(self):
        pass

    def find_nearest_battery_or_cable(self):
        pass

    def lay_cable(self):
        pass

    def connect_battery(self, battery):
        self.battery = battery
        # Anything else?
        # lay_cable()?
        

    
