import json


def generate_diff(file_one, file_two):
    origin = load_file(file_one)
    modified = load_file(file_two)
    origin_keys = list(origin.keys())
    modified_keys = list(modified.keys())
    all_keys = sorted(set(origin_keys + modified_keys))
    res = ['{']
    for key in all_keys:
        if key not in origin_keys:
            res.append('+ {}: {}'.format(key, modified[key]))
        elif key not in modified_keys:
            res.append('- {}: {}'.format(key, origin[key]))
        else:
            if origin[key] == modified[key]:
                res.append('  {}: {}'.format(key, origin[key]))
            else:
                res.append('- {}: {}'.format(key, origin[key]))
                res.append('+ {}: {}'.format(key, modified[key]))
    res.append('}')
    return '\n'.join(res)


def load_file(file_path):
    return json.load(open(file_path))


def is_json(file1, file2)
    return file1.endswith(".json") and file2.endswith(".json")


def is_yaml(file1, file2):
    return file1.endswith((".yaml", ".yml")) and \
        file2.endswith((".yaml", ".yml"))