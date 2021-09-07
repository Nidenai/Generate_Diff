#!/usr/bin/env python

import argparse


def main():

    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('passes', metavar='first_file', type=str)
    parser.add_argument('passes', metavar='second_file', type=str)

    args = parser.parse_args()
    print(args.accumulate(args.integers))



if __name__ == '__main__':
    main()