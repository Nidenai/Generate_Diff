import argparse
from gendiff.formats.var import FORMATS
from gendiff.engine.parser import parse


def generation():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument("-f", "--format",
                        choices=FORMATS.keys(),
                        default="stylish",
                        help='output format (default: "stylish")')
    parser.add_argument("-V", "--version",
                        action="version",
                        version="%(prog)s 0.10.2")
    args = parser.parse_args()
    return args


def get_diff(file1, file2):
    result = {}
    keys = sorted(set(file1) | set(file2))
    for key in keys:
        status, value = check_keys(key, file1, file2)
        result[(status, key)] = value
    return result


def check_keys(key, before, after):
    if key in before and key in after:
        return key_remained(before[key], after[key])
    elif key in before:
        return key_in_one_file(before[key], "removed")
    elif key in after:
        return key_in_one_file(after[key], "added")


def key_remained(before, after):
    if before == after:
        status = "no change"
        if is_child(before):
            value = ["children", get_diff(before, after)]
        else:
            value = ["value", before]
    else:
        status = "changed"
        if is_child(before) and is_child(after):
            status = "no change"
            value = ["children", get_diff(before, after)]
        elif is_child(before):
            value = [
                ["children", get_diff(before, before)],
                ["value", after]
            ]
        elif is_child(after):
            value = [
                ["value", before],
                ["children", get_diff(after, after)]
            ]
        else:
            value = [["value", before], ["value", after]]
    return status, value


def key_in_one_file(data, status):
    if is_child(data):
        return status, ["children", get_diff(data, data)]
    return status, ["value", data]


def is_child(data):
    return isinstance(data, dict)


def generate_diff(file1, file2, format_name='stylish'):
    file1, file2 = parse(file1, file2)
    return FORMATS[format_name](get_diff(file1, file2))
