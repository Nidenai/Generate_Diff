from gendiff.formats.edit_message import edit_message


STATUS = {
    "added": "  + ",
    "removed": "  - ",
    "no change": "    "
}


def format(data):
    result = {}
    def unpach_values(value, value_type):
        if value_type == "children":
            return format(value)
        return value
    for item in data.keys():
        status, key = item
        if status == "changed":
            old_value_type, old_value = data[item][0]
            new_value_type, new_value = data[item][1]
            result[STATUS["removed"] + key] = unpach_values(
                old_value, old_value_type)
            result[STATUS["added"] + key] = unpach_values(
                new_value, new_value_type)
        else:
            value_type, value = data[item]
            result[STATUS[status] + key] = unpach_values(value, value_type)
    return result


def to_string(data, lvl=0):
    result = "{\n"
    for key, value in data.items():
        if isinstance(value, dict):
            value = to_string(value, lvl + 1)
        result += f"{'    ' * lvl}{key}: {value}\n"
    result += f"{'    ' * lvl}}}"
    return edit_message(result)


def render(data):
    return edit_message(to_string(format(data)))
