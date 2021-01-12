from .house import House
from .battery import Battery
import json

class Grid():
    def __init__(self,  battery_file, house_file):
        self.size = 50
        self.all_batteries = {}
        self.all_houses = {}
        self.load_batteries(battery_file)
        self.load_houses(house_file)
        self.all_cables = []
        
    def json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def load_batteries(self, source_file):
        with open (source_file) as f:
            # Creates batteries and saves them in a list
            line = f.readline()
            line = f.readline()
            line = line.split(',')
            while len(line) == 3:
                new_battery = Battery(line[0].replace("\", """), line[1].rstrip('"\"'), line[2].rstrip())
                coordinates = (line[0] + line[1])
                self.all_batteries.update({coordinates:new_battery})
                line = f.readline()
                line = line.split(',')

    def load_houses(self, source_file):
        with open (source_file) as f:
            # Creates houses and saves them in a list
            line = f.readline()
            line = f.readline()
            line = line.split(',')
            while len(line) == 3:
                new_house = House(line[0], line[1], line[2].rstrip('\n'))
                coordinates = (line[0] + line[1])
                self.all_houses.update({coordinates:new_house})
                line = f.readline()
                line = line.split(',')
    
    # note: does not work yet!
    def create_cable(self, house, battery):
        # stores coordinates and finds distance between house & battery
        house_coordinates = [house.x_coordinate, battery.y_coordinate]
        battery_coordinates = [battery.x_coordinate, battery.y_coordinate]
        horizontal_dist = battery.x_coordinate - house.x_coordinate
        if horizontal_dist < 0:
            horizontal_dist = horizontal_dist * -1
        vertical_dist = battery.y_coordinate - house.y_coordinate
        if vertical_dist < 0:
            vertical_dist = vertical_dist * -1
        distance = horizontal_dist + vertical_dist

        # sets temporary variables to check if cable already exists
        temp_cables = []
        newest_coordinates = house_coordinates
        self.all_cables.append(newest_coordinates)
        temp_cable_length = 0

        
        while temp_cable_length < distance:
            # simple way of finding a path to a battery, this is not always valid!

            while newest_coordinates[0] < battery.x_coordinate:
                newest_coordinates[0] = newest_coordinates[0] + 1
                self.all_cables.append(newest_coordinates)

            while newest_coordinates[0] > battery.x_coordinate:
                newest_coordinates[0] = newest_coordinates[0] - 1
                self.all_cables.append(newest_coordinates)

            while newest_coordinates[1] < battery.y_coordinate:
                newest_coordinates[1] = newest_coordinates[1] + 1
                self.all_cables.append(newest_coordinates)    
            
            while newest_coordinates[1] > battery.y_coordinate:
                newest_coordinates[1] = newest_coordinates[1] - 1
                self.all_cables.append(newest_coordinates) 


            