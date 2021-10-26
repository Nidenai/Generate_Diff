import argparse
from gendiff.formats.var import FORMATS


def parse():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument("-f", "--format",
                        choices=FORMATS.keys(),
                        default="stylish",
                        help='output format (default: "stylish")')
    parser.add_argument("-V", "--version",
                        action="version",
                        version="%(prog)s 0.10.2")
    args = parser.parse_args()
    return args
