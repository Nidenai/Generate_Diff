import json
import yaml


def parse(file1, file2):
    if is_json(file1, file2):
        arg1 = json.load(open(file1))
        arg2 = json.load(open(file2))
    elif is_yaml(file1, file2):
        arg1 = yaml.safe_load(open(file1), Loader=yaml.FullLoader)
        arg2 = yaml.safe_load(open(file2), Loader=yaml.FullLoader)

    return arg1, arg2


def is_json(file1, file2):
    return file1.endswith(".json") and file2.endswith(".json")


def is_yaml(file1, file2):
    return file1.endswith((".yaml", ".yml")) and file2.endswith((".yaml", ".yml"))