#!/usr/bin/env python

import argparse

from gendiff import generator


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    # parser.parse_args()
    args = parser.parse_args()

    generator.generate_diff(args.first_file, args.second_file)


if __name__ == '__main__':
    main()