#!/usr/bin/env python

import argparse
from gendiff.engine.compare import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', metavar='FORMAT', help='set format of output')
    parsing(parser.parse_args())


def parsing(args):
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
