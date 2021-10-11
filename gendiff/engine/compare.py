import argparse
from gendiff.engine.parsing import generate_diff
from gendiff.formats import stylish
from gendiff.formats import json
from gendiff.formats import plain
from gendiff.engine.engine import get_data

FORMATS = {
    "stylish": stylish.render,
    'json': json.render,
    'plain': plain.render
}


def gendiff():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument("-f", "--format", choices=FORMATS.keys(), default="stylish", help='output format (default: "stylish")')
    parser.add_argument("-V", "--version", action="version", version="%(prog)s 0.10.2")
    args = parser.parse_args()
    return args


def generation(file1, file2, format_name='stylish'):
    file1, file2 = parsing(file1, file2)
    return FORMATS[format_name](get_data(file1, file2))


def parsing(file1, file2):
    return generate_diff(file1, file2)


def run():
    parser = gendiff()
    diff = generation(
        parser.first_file,
        parser.second_file,
        parser.format
    )
    print(diff)
