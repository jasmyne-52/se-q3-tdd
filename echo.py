#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Jasmyne Ford w/h/f study hall and classmates"


import sys
import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument(
        '-l', '--lower', help='convert text to lowercase', action='store_true')
    parser.add_argument(
        '-u', '--upper', help='convert text to uppercase', action='store_true')
    parser.add_argument(
        '-t', '--title', help='convert text to titlecase', action='store_true')
    parser.add_argument('text', help='text to be manipulated')
    return parser


def main(args):
    # Create a command line parser object with parsing rules
    parser = create_parser()
    ns = parser.parse_args(args)
    text = ns.text
    if not ns:
        parser.print_usage()
        sys.exit(1)
    elif ns.title:
        print(text.title())
    elif ns.lower:
        print(text.lower())
    elif ns.upper:
        print(text.upper())
    else:
        print(text)
    return


if __name__ == '__main__':
    main(sys.argv[1:])
