import json


def render(data):
    return json.dumps(format(data), indent=4)


def format(data):
    result = {}
    for item in data.keys():
        status, key = item
        if status == "changed":
            value_type_old, value_old = data[item][0]
            if value_type_old == 'children':
                old = format(value_old)
            else:
                old = value_old
            value_type_new, value_new = data[item][1]
            if value_type_new == 'children':
                new = format(value_new)
            else:
                new = value_new
            value = ["updated", old, new]
        else:
            if status == "no change":
                value_type, value_value = data[item]
                if value_type == "children":
                    value = format(value_value)
                else:
                    value = value_value
            else:
                value_type, value_value = data[item]
                if value_type == "children":
                    middle_result = format(value_value)
                else:
                    middle_result = value_value
                value = [status, middle_result]
        result[key] = value
    return result
