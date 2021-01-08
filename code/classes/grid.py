from .house import House
from .battery import Battery

class Grid():
    def __init__(self, house_file, battery_file, size):
        self.size = size
        self.all_batteries = []
        self.all_houses = []
        self.load_batteries(house_file)
        self.load_houses(battery_file)

    def load_batteries(self, source_file):
        with open (source_file) as f:
            # Creates batteries and saves them in a list
            line = f.readline()
            while line != '\n':
                line = line.split(',')
                new_battery = Battery(line[0], line[1], line[2])
                self.all_batteries.append(new_battery)
                f.readline()

    def load_houses(self, source_file):
        with open (source_file) as f:
            # Creates houses and saves them in a list
            line = f.readline()
            while line != '\n':
                line = line.split(',')
                new_house = House(line[0], line[1], line[2])
                self.all_batteries.append(new_house)
                f.readline()
            