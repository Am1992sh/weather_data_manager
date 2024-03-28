import csv
from prettytable import PrettyTable


class WeatherCollector:
    def __init__(self, filepath):
        self.filepath = filepath
        self.file = None

    def __enter__(self):
        self.file = open(self.filepath, 'r')
        reader = list(csv.reader(self.file))
        if reader:
            myTable = PrettyTable(reader[0])
            for row in reader[1:]:
                myTable.add_row(row)
            print(myTable)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


with WeatherCollector('weather.csv') as f:
    pass
