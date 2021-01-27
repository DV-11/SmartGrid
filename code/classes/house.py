import csv

class House():
    def  __init__(self, house_id, x, y, output):
        self.id = house_id
        self.x_coordinate = int(x)
        self.y_coordinate = int(y)
        self.output = float(output)
        self.cables = []                # list of coordinates
        self.battery = None             # ID
        self.distance = 0               # distance to dest?
        self.destination = None         # coordinate
        self.to_battery = False
        self.latest_cable = [self.x_coordinate, self.y_coordinate]

    def has_cable(self):    # CHECK IF THIS WORKS
        # ??? Does this work with a list??
        return self.cables is not None

    def find_nearest_battery(self):
        pass

    def get_distance(self):
        # remove later
        pass

    def find_nearest_destination(self, grid): 
        pass

    def lay_simple_cable(self, house, battery):
        origin = [int(house.x_coordinate),int(house.y_coordinate)] # x = 0, y = 1
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

    def lay_random_cable(self, origin, destination):
        pass
        # starting coordinate & destination coordinate -> cables["x,y"]
        # current_coordinate = starting coordinate

        # while origin != destination
            # current_coordinate = random_move(current_coordinate)  # moves and adds to list and returns new coordinate

    def random_move(self):
        pass
        # moves 1 step and adds to list and returns new coordinate

        # move 1 step randomly
        # add new_coordinate to list
        # return new_coordinate
 
    
    # def get_distance(self, x, y, destination_x, destination_y):
    #     return 0

    def connect_battery(self, battery):
    #     self.battery = battery
    #     self.battery = 
        # Anything else?
        # lay_random_cable(origin, destination)
        pass

    def disconnect_battery(self):
        # self.battery = None
        # self.cables.clear()
        pass

    def get_possibilities(self, all_batteries): # untested
        """
        Returns a list of all available batteries that can be assigned to this house.
        """
        available = []

        for battery in all_batteries:
            if battery.remaining_capacity >= battery.capacity:
                available.append(battery)

        return available
