import requests


def api_to_csv():
    req = requests.get(
        "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m").json()

    text = ""
    value_lists = list(req["hourly"].values())
    keys = list(req["hourly"].keys())
    keys.insert(0, "city")
    text += ",".join(keys) + "\n"

    for row in zip(value_lists[0], value_lists[1], value_lists[2], value_lists[3]):
        list_to_csv_format = [str(i) for i in row]
        list_to_csv_format.insert(0, "berlin")
        text += ",".join(list_to_csv_format) + "\n"

    return text


