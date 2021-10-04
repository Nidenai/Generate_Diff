import argparse
from gendiff.engine.parsing import generate_diff
from gendiff.formats import stylish
from gendiff.formats import json
from gendiff.formats import plain

FORMATS = {
    "stylish": stylish.render,
    'json': json.render,
    'plain': plain.render
}


def run():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument("-f", "--format", choices=FORMATS.keys(), default="stylish", help='output format (default: "stylish")')
    parser.add_argument("-V", "--version", action="version", version="%(prog)s 0.10.2")
    parsing(parser.parse_args())


def parsing(args):
    print(generate_diff(args.first_file, args.second_file))


