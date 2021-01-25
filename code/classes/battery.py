import csv

class Battery():
    def __init__(self, battery_id, x, y, capacity):
        self.id = battery_id
        self.x_coordinate = x
        self.y_coordinate= y
        self.capacity = float(capacity)
        self.remaining_capacity = float(capacity)
        self.cables = [tuple([self.x_coordinate, self.y_coordinate])]
        self.houses = []
        self.battery_price = 5000
        self.cable_price = 9
    
    def is_valid(self):
        """
        Returns whether the battery is valid. 
        A battery is valid when the capacity is not exceeded.
        """
        if self.remaining_capacity >= 0:
            return True

        return False
