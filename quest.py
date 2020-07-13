#!/usr/bin/env python3
import argparse
import os

QUEST_ROOT = '.quest'


def init(args):
    """
    Initialize .quest directory
    :return:
    """
    if os.path.exists(QUEST_ROOT):
        print('Reinitializing Quest workspace')
    else:
        print('Initializing empty Quest workspace')
    os.makedirs(QUEST_ROOT, exist_ok=True)


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand')

    parser_init = subparsers.add_parser('init')
    parser_init.set_defaults(func=init)

    args = parser.parse_args()
    if args.subcommand is None:
        parser.print_help()
    else:
        args.func(args)


if __name__ == '__main__':
    main()
