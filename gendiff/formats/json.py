import json


def render(data):
    return json.dumps(format(data), indent=4)


def format(data):
    result = {}
    for item in data.keys():
        status, key = item
        if status == "changed":
            old = check_value(data[item][0])
            new = check_value(data[item][1])
            value = ["updated", old, new]
        else:
            if status == "no change":
                value = check_value(data[item])
            else:
                value = [status, check_value(data[item])]
        result[key] = value
    return result


def check_value(value):
    value_type, value = value
    if value_type == "children":
        value = format(value)
    return value
