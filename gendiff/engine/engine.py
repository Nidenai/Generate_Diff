def get_data(file1, file2):
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