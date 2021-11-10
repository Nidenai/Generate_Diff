import json
import yaml


def parse(file):
    if is_json(file):
        data = json.load(open(file))
    elif is_yaml(file):
        data = yaml.load(open(file), Loader=yaml.FullLoader)
    return data


def is_json(file1):
    return file1.endswith(".json")


def is_yaml(file1):
    return file1.endswith((".yaml", ".yml"))
