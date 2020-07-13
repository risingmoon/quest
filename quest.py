#!/usr/bin/env python3
import argparse
import os

QUEST_HOME = '.quest/envs'


def init(args):
    """
    Initialize .quest directory

    :param args:
    :return:
    """
    if os.path.exists(QUEST_HOME):
        print('Reinitializing Quest workspace')
    else:
        print('Initializing empty Quest workspace')
    os.makedirs(QUEST_HOME, exist_ok=True)


def checkout(args):
    """
    Ability to change or create env

    :param args:
    :return:
    """
    print('checkout')


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand')

    parser_init = subparsers.add_parser('init')
    parser_init.set_defaults(func=init)

    parser_checkout = subparsers.add_parser('checkout')
    parser_checkout.set_defaults(func=checkout)

    args = parser.parse_args()
    if args.subcommand is None:
        parser.print_help()
    else:
        args.func(args)


if __name__ == '__main__':
    main()
