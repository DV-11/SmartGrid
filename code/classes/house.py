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

    def find_nearest_destination(self):
        # TODO
        shortest_distance = float('inf')

        # Loop through all batteries and put its cables in a list
        for battery in grid.all_batteries.values():
            battery_cables = list(battery.cables)

            # Save each coordinate's distance as new distance
            for cable in range(len(battery_cables)):
                new_distance = self.get_distance(x_coordinate, y_coordinate, 
                    int(battery_cables[cable][0]), int(battery_cables[cable][1]))

                # Keep track of shortest distanc
                if new_distance < shortest_distance:
                    shortest_distance = new_distance
                    # self.destination = tuple([int(battery_cables[cable][0]), int(battery_cables[cable][1])])



        return battery

    def lay_cable(self):
        pass
 
    def connect_battery(self, battery):
        self.battery = battery
        # Anything else?
        # lay_cable()?
        

    
