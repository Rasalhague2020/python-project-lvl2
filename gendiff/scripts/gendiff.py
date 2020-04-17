#!/use/bin/env python3

import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('strings', metavar='first_file', type=str)
    parser.add_argument('strings', metavar='second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    print(args.accumulate(args.strings))


if __name__ == '__main__':
    main()
