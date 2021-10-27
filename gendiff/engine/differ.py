from gendiff.engine.parser import parse
from gendiff.formats.var import FORMATS


def get_diff(data1, data2):
    result = {}
    keys = sorted(data1.keys() | data2.keys())
    for key in keys:
        v1, v2 = data1.get(key), data2.get(key)
        if key in data1 and key not in data2:
            status = 'removed'
            value = ["value", v2]
        elif key in data2 and key not in data1:
            status = 'added'
            value = ["value", v2]
        elif key in data1 and key in data2:
            if v1 == v2:
                status = 'no change'
                value = ["value", v1]
            else:
                status = 'changed'
                value = [['value', v1], ['value', v2]]
        result[(status, key)] = value
    return result


def generate_diff(file1, file2, format_name='stylish'):
    file1, file2 = parse(file1, file2)
    return FORMATS[format_name](get_diff(file1, file2))
