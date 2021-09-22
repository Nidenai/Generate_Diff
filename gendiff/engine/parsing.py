import json
import yaml


def generate_diff(file_one, file_two):
    if file_one[-1] == 'n':
        insert_data = is_json(file_one, file_two)
    else:
        insert_data = is_yaml(file_one, file_two)
    one, two = insert_data
    one_keys = list(one.keys())
    two_keys = list(two.keys())
    all_keys = sorted(set(one_keys + two_keys))
    res = ['{']
    for key in all_keys:
        if key not in one_keys:
            res.append('+ {}: {}'.format(key, two[key]))
        elif key not in two_keys:
            res.append('- {}: {}'.format(key, one[key]))
        else:
            if one[key] == two[key]:
                res.append('  {}: {}'.format(key, one[key]))
            else:
                res.append('- {}: {}'.format(key, one[key]))
                res.append('+ {}: {}'.format(key, two[key]))
    res.append('}')
    return '\n'.join(res)


def is_json(file_one, file_two):
    one = json.load(open(file_one))
    two = json.load(open(file_two))
    return (one, two)

def is_yaml(file_one, file_two):
    one = yaml.safe_load(open(file_one))
    two = yaml.safe_load(open(file_two))
    return (one, two)
