import csv
from prettytable import PrettyTable


class WeatherCollector:
    def __init__(self, filepath):
        self.filepath = filepath
        self.file = None

    def __enter__(self):
        self.file = open(self.filepath, 'r')
        # reader = list(csv.reader(self.file))
        # if reader:
        #     my_table = PrettyTable(reader[0])
        #     for row in reader[1:]:
        #         my_table.add_row(row)
        #     print(my_table)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


# with WeatherCollector('weather.csv') as f:
#     pass
