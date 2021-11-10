from gendiff.engine.parser import parse
from gendiff.formats.var import FORMATS


def get_diff(data1, data2):
    result = {}
    keys = sorted(data1.keys() | data2.keys())
    for key in keys:
        v1, v2 = data1.get(key), data2.get(key)
        if key in data1 and key not in data2:
            status = "removed"
            value = ["value", v1]
        elif key in data2 and key not in data1:
            status = "added"
            value = ["value", v2]
        elif v1 == v2:
            status = "no change"
            value = ["value", v1]
        elif isinstance(v1, dict) and isinstance(v2, dict):
            status = "no change"
            value = ["children", get_diff(v1, v2)]
        else:
            status = "changed"
            value = [["value", v1], ["value", v2]]
        result[(status, key)] = value
    return result


def generate_diff(file1, file2, format_name='stylish'):
    file1 = parse(file1)
    file2 = parse(file2)
    return FORMATS[format_name](get_diff(file1, file2))
