data_entries = [
    {"timestamp": 10, "count": 5, "type": "enter"},
    {"timestamp": 8, "count": 2, "type": "enter"},
    {"timestamp": 6, "count": 0, "type": "enter"},
    {"timestamp": 6, "count": 0, "type": "exit"},
    {"timestamp": 8, "count": 1, "type": "exit"},
    {"timestamp": 10, "count": 0, "type": "exit"},
]


def sort_data_by_earliest_timestamp(data_entries):
    return [entry for entry in sorted(data_entries, key=lambda d: d["timestamp"])]


def busiest_time_period(data_entries):

    count_enter = 0
    count_exit = count_enter

    sorted_entries = sort_data_by_earliest_timestamp(data_entries)

    for data in sorted_entries:
        if data["type"] == "enter" and data["count"] > count_enter:
            count_enter = data["count"]
        if data["type"] == "exit" and data["count"] < count_exit:
            count_exit = data["count"]
    period = []

    time_exit = []
    time_enter = []
    for data in sorted_entries:
        if data["count"] == count_exit and data["type"] == "exit":
            time_exit.append(data["timestamp"])
        elif data["count"] == count_enter and data["type"] == "enter":
            time_enter.append(data["timestamp"])
    busy_time = (max(time_enter), max(time_exit))
    return busy_time


print(busiest_time_period(data_entries))
