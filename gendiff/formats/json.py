import json


def render(data):
    return json.dumps(format(data), indent=4)


def format(data):
    result = {}

    def check_value(*args):
        for item in args:
            value_type, value = item
            if value_type == "children":
                args = format(value)
        return args
    for item in data.keys():
        status, key = item
        if status == "changed":
            old, new = check_value(data[item][0], data[item][1])
            value = ["updated", old, new] 
        else:
            if status == "no change":
                value = check_value(data[item])
            else:
                value = [status, check_value(data[item])]
        result[key] = value
    return result
