class Grid():
    def __init__(self, source_file):
        self.size = pass
        self.all_batteries = []
        self.all_houses = []

    def load_batteries(self, source_file):

        batteries = {}
        with open(source_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            