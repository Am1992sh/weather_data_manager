import argparse
import csv
import re
import getAPI
from prettytable import PrettyTable

from weather_data_manager import WeatherCollector


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='File path', default='weather.csv')
    parser.add_argument('--data_type', help='Data type', choices=['humidity', 'temperature', 'wind_speed'])
    parser.add_argument('action', help='Action to perform', choices=['min', 'max', 'average', 'search'])
    parser.add_argument('search', help='Search', nargs="?")
    args = parser.parse_args()

    if args.path:
        if re.match(r"http.:\/\/",args.path):
            file_path = "temp.csv"
            getAPI.api_to_csv(args.path,file_path)
        else:
            file_path = args.path
        data_type = args.data_type
        first_data = find_data(file_path, data_type)
        display_data(file_path)
        maximum, minimum, average = operation_data(first_data)
        if args.action == 'min':
            print(minimum)
        elif args.action == 'max':
            print(maximum)
        elif args.action == 'average':
            print(average)
        elif args.action == 'search':
            search(file_path, data_type, args.search)


def find_data(file_path, data_type):
    data = []
    with WeatherCollector(file_path) as f:
        # with open(file_path) as f:
        csv_reader = csv.DictReader(f)
        data = [row[data_type] for row in csv_reader]
    return data


def operation_data(data):
    new_list = [float(i) for i in data]
    maximum = max(new_list)
    minimum = min(new_list)
    average = sum(new_list) / len(data)
    return maximum, minimum, average


def display_data(file_path):
    with WeatherCollector(file_path) as f:
        data = [i.replace("\n","").split(",") for i in f.readlines()]
        reader = PrettyTable(data[0])
        for i in data[1:]:
            reader.add_row(i)
        print(reader)


def search(file_path, data_type, search_key):
    with WeatherCollector(file_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            if row.get("city") == search_key:
                print(row[data_type])
            if row.get("date") == search_key:
                print(row[data_type])


# def find_max_data(find_data):
#     max_data=


if __name__ == '__main__':
    main()
