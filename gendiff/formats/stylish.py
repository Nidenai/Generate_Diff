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
            result[STATUS["removed"] + key] = old_value
            result[STATUS["added"] + key] = new_value
        else:
            result[STATUS[status] + key] = value
    return result


def to_string(data, lvl=0):
    result = "{\n"
    for key, value in data.items():
        if isinstance(value, dict):
            value = to_string(value, lvl + 2)
        result += f"{'    ' * lvl}{key}: {value}\n"
    result += f"{'    ' * lvl}}}"
    return edit_message(result)


def render(data):
    return edit_message(to_string(format(data)))


def convert_value(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                convert_value(value)
            else:
                return '{}\n\t{}:{}\n\t{}'.format('{', key, value, '}')
    return data
