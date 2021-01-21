from .house import House
from .battery import Battery
import json
import csv

class Grid():
    def __init__(self, battery_file, house_file):
        self.size = 50
        self.all_batteries = self.load_batteries(battery_file)
        self.all_houses = self.load_houses(house_file)
        self.all_cables = set()
        
    def json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def load_batteries(self, source_file):
        """
        Load all batteries from source file and adds them as an object in a dictionary.
        """
        batteries = {}

        with open (source_file) as in_file:
            reader = csv.DictReader(in_file)
            battery_id = 1

            for row in reader:
                positions = []

                # Extract each position from file and add to list
                for position in row['positie'].split(','):
                    if position.strip('[] ') != '':
                        positions.append(position.strip('[] '))

                batteries[battery_id] = Battery(battery_id, positions[0], positions[1], row['capaciteit'])
                battery_id += 1
            
        return batteries

    def load_houses(self, source_file):
        """
        Load all houses from source file and adds them as an object in a dictionary.
        """
        houses = {} # {id: House object}

        with open (source_file) as in_file:
            reader = csv.DictReader(in_file)
            house_id = 1

            # Create House object with data from file
            for row in reader:
                houses[house_id] = House(house_id, row['x'], row['y'], row['maxoutput'])
                house_id += 1
            
        return houses

    def is_solution(self):
        """
        Checks for battery capacity constraint. *Note: does not check for cables
        """
        for Battery in self.all_batteries.values():
            if float(Battery.remaining_capacity) > 0:
                return False

        return True

    def calculate_cost(self):
        pass