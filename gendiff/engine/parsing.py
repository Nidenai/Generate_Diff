import json
import yaml


def generate_differenses(file_one, file_two):
    if file_one[-1] == 'n':
        insert_data = is_json(file_one, file_two)
    else:
        insert_data = is_yaml(file_one, file_two)
    one, two = insert_data
    return one, two


def is_json(file_one, file_two):
    one = json.load(open(file_one))
    two = json.load(open(file_two))
    return (one, two)

def is_yaml(file_one, file_two):
    one = yaml.safe_load(open(file_one))
    two = yaml.safe_load(open(file_two))
    return (one, two)
