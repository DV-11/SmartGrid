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
        return self.cables is not None

    def lay_simple_cable(self, house, battery):
        origin = [int(house.x_coordinate),int(house.y_coordinate)] 
        destination = [int(battery.x_coordinate),int(battery.y_coordinate)]

        current_coordinate = origin

        # Move vertically
        if origin[1] >= destination[1]:
            while current_coordinate[1] > destination[1]:
                house.cables.append(tuple(current_coordinate))
                current_coordinate[1] -= 1
        else:
            while current_coordinate[1] < destination[1]:
                house.cables.append(tuple(current_coordinate))
                current_coordinate[1] += 1
        
        # Move horizontally
        if origin[0] >= destination[0]:
            while current_coordinate[0] > destination[0]:
                house.cables.append(tuple(current_coordinate))
                current_coordinate[0] -= 1
        else:
            while current_coordinate[0] < destination[0]:
                house.cables.append(tuple(current_coordinate))
                current_coordinate[0] += 1

    def get_possibilities(self, all_batteries): 
        """
        Returns a list of all available batteries that can be assigned to this house.
        """
        available = []

        for battery in all_batteries:
            if battery.remaining_capacity >= battery.capacity:
                available.append(battery)

        return available
