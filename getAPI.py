import requests


def api_to_csv(url,filepath):
    req = requests.get(url).json()

    text = ""
    value_lists = list(req["hourly"].values())
    keys = ["city","date","humidity","temperature","wind_speed"]
    text += ",".join(keys) + "\n"

    for row in zip(value_lists[0], value_lists[1], value_lists[2], value_lists[3]):
        list_to_csv_format = [str(i) for i in row]
        list_to_csv_format.insert(0, "berlin")
        text += ",".join(list_to_csv_format) + "\n"

    with open(filepath,"w") as w:
        w.write(text)
