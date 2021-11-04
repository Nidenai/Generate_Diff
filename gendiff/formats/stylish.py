from gendiff.formats.edit_message import edit_message
STATUS = {
    "added": "  + ",
    "removed": "  - ",
    "no change": "    "
}


def format(data):

    result = {}
    for head, body in data.items():
        status, key = head
        type_, value = body
        if type_ == 'children':
            result[STATUS[status] + key] = format(value)
        elif status == "changed":
            old_value_type, old_value = body[0]
            new_value_type, new_value = body[1]
            result[STATUS["removed"] + key] = convert_value(old_value)
            result[STATUS["added"] + key] = convert_value(new_value)
        else:
            result[STATUS[status] + key] = convert_value(value)
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


def convert_value(v):
    if not isinstance(v, dict):
        return v

    result = {}
    for key, value in v.items():
        new_key = '   {}'.format(key)
        result[new_key] = convert_value(value)
    return result
