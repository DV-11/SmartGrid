from .house import House
from .battery import Battery

class Grid():
    def __init__(self, house_file, battery_file):
        self.size = 50
        self.all_batteries = {}
        self.all_houses = {}
        self.load_batteries(house_file)
        self.load_houses(battery_file)
        self.all_cables = []

    def load_batteries(self, source_file):
        with open (source_file) as f:
            # Creates batteries and saves them in a list
            line = f.readline()
            while line != '\n':
                line = line.split(',')
                new_battery = Battery(line[0], line[1], line[2])
                self.all_batteries.update({[line[0], line[1]]:new_battery})
                f.readline()

    def load_houses(self, source_file):
        with open (source_file) as f:
            # Creates houses and saves them in a list
            line = f.readline()
            while line != '\n':
                line = line.split(',')
                new_house = House(line[0], line[1], line[2])
                self.all_houses.update({[line[0],line[1]]:new_house})
                f.readline()
    
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


            