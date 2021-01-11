from .house import House
from .battery import Battery
import csv
import json

class Grid():
    def __init__(self, house_file, battery_file):
        self.size = 50

        self.all_batteries = self.load_batteries(house_file)
        # self.all_houses = self.load_houses(battery_file)

        # self.all_cables = []
        
    def json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def load_batteries(self, source_file):
        
        """Load all batteries."""
        batteries = {} #{id: Battery object}

        with open (source_file) as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                batteries[row['positie']] = Battery(row['positie'], row['capaciteit'])
            
        return batteries

                # positions = []

                # Extract each positie from file and add to list
                # range(2)?
                # for position in row['positie'].split(','):
                #     if position.strip('[] ') != '':
                #         positions.append(position.strip('[] '))
                
                # print("positions: ", positions) # ['38', '12']

                # battery_id = battery.id??

                # print("row['positie']: ", row['positie'])  # 42,3
                # print("row['capaciteit']: ", row['capaciteit'])   # 1507.0
                # print("key: ", positions[0], positions[1])
                # print("(x, y, capacity) object input: ", positions[0], positions[1], row['capaciteit'])
                # new_battery = Battery(positions[0], positions[1], row['capaciteit'])

                # for capacity in row['capaciteit']:
                #     # capacity = ...
                #     # self.all_batteries[battery_id].add_capacity(capacity)
                #     print("capacity: ", capacity)   

            # print("self.all_batteries: ", self.all_batteries) 

    # def load_houses(self, source_file):
    #     """Load all houses."""
    #     with open (source_file) as f:
    #         # Creates houses and saves them in a list
    #         line = f.readline()
    #         line = f.readline()
    #         line = line.split(',')

    #         while len(line) == 3:
    #             new_house = House(line[0], line[1], line[2])
    #             coordinates = str('line[0],line[1]')
    #             self.all_houses.update({coordinates:new_house})
    #             line = f.readline()
    #             line = line.split(',')
            
    #         print("all houses: ", self.all_houses)
    
    # def create_cable(self, house, battery):
    #     # stores coordinates and finds distance between house & battery
    #     house_coordinates = [house.x_coordinate, battery.y_coordinate]
    #     battery_coordinates = [battery.x_coordinate, battery.y_coordinate]
    #     horizontal_dist = battery.x_coordinate - house.x_coordinate

    #     if horizontal_dist < 0:
    #         horizontal_dist = horizontal_dist * -1
    #     vertical_dist = battery.y_coordinate - house.y_coordinate

    #     if vertical_dist < 0:
    #         vertical_dist = vertical_dist * -1
    #     distance = horizontal_dist + vertical_dist

    #     # sets temporary variables to check if cable already exists
    #     temp_cables = []
    #     newest_coordinates = house_coordinates
    #     self.all_cables.append(newest_coordinates)
    #     temp_cable_length = 0

        
    #     while temp_cable_length < distance:
    #         # simple way of finding a path to a battery, this is not always valid!

    #         while newest_coordinates[0] < battery.x_coordinate:
    #             newest_coordinates[0] = newest_coordinates[0] + 1
    #             self.all_cables.append(newest_coordinates)

    #         while newest_coordinates[0] > battery.x_coordinate:
    #             newest_coordinates[0] = newest_coordinates[0] - 1
    #             self.all_cables.append(newest_coordinates)

    #         while newest_coordinates[1] < battery.y_coordinate:
    #             newest_coordinates[1] = newest_coordinates[1] + 1
    #             self.all_cables.append(newest_coordinates)    
            
    #         while newest_coordinates[1] > battery.y_coordinate:
    #             newest_coordinates[1] = newest_coordinates[1] - 1
    #             self.all_cables.append(newest_coordinates) 


            