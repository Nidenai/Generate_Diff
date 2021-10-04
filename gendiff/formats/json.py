from json import dumps


def render(data):
    return dumps(data, indent=2)