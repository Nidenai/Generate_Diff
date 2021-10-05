def get_data(file1, file2):
    result = {}
    keys = sorted(set(file1) | set(file2))
    for key in keys:
        status, value = check_keys(key, file1, file2)
        result[(status, key)] = value
    return result