import json


def render(data):
    return json.dumps(data, indent=2)