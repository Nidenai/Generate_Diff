from gendiff.engine.parser import parse
from gendiff.formats.var import FORMATS


def get_diff(file1, file2):
    result = {}
    keys = sorted(set(file1) | set(file2))
    for key in keys:
        v1, v2 = file1.get(key), file2.get(key)
        if key in file1 and key not in file2:
            status = 'removed'
            result[(status, key)] = ["value", v1]
        if key in file2 and key not in file1:
            status = 'added'
            result[(status, key)] = ["value", v2]
        if key in file1 and key in file2:
            if v1 == v2:
                status = 'no change'
                if isinstance(v1, dict):
                    status = 'children'
                    result[(status, key)] = ['children', get_diff(v1, v2)]
                else:
                    result[(status, key)] = ["value", v1]
            else:
                status = 'changed'
                if isinstance(v1, dict) and isinstance(v2, dict):
                    status = 'no change'
                    result[(status, key)] = ['no change', get_diff(v1, v2)]
                elif isinstance(v1, dict):
                    result[(status, key)] = [['children', get_diff(v1, v1)],
                                             ['value', v2]]
                elif isinstance(v2, dict):
                    result[(status, key)] = [['value', v1],
                                             ['children', get_diff(v2, v2)]]
                else:
                    result[(status, key)] = [['value', v1], ['value', v2]]
    return result


def generate_diff(file1, file2, format_name='stylish'):
    file1, file2 = parse(file1, file2)
    return FORMATS[format_name](get_diff(file1, file2))
