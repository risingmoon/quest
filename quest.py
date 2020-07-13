#!/usr/bin/env python3
import argparse
import os
from pathlib import Path

QUEST_HOME = '.quest/envs'
QUEST_ENVS = '.quest/envs'
QUEST_HEAD = '.quest/HEAD'


class Fatal(RuntimeError):
    pass

    def __init__(self, message):
        super().__init__('fatal: %s' % message)


class Error(RuntimeError):

    def __init__(self, message):
        super().__init__('error: %s' % message)


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
    env_path = Path(QUEST_ENVS) / args.env
    if args.e:
        try:
            env_path.mkdir()
        except FileExistsError as e:
            raise Fatal("An environment named '%s' already exists." % args.env) from None

    if env_path.exists():
        print("Switched to %s environment '%s'" % ('a new' if args.e else '', args.env))
        with open(QUEST_HEAD, 'w') as f:
            f.write('%s' % args.env)
    else:
        raise Error("'%s' did not match any environment in quest" % args.env)


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand')

    parser_init = subparsers.add_parser('init')
    parser_init.set_defaults(func=init)

    parser_checkout = subparsers.add_parser('checkout')
    parser_checkout.add_argument('env', type=str, help='environment', action='store')
    parser_checkout.add_argument('-e', help='create new environment', action='store_true')
    parser_checkout.set_defaults(func=checkout)

    args = parser.parse_args()
    if args.subcommand is None:
        parser.print_help()
    else:
        args.func(args)


if __name__ == '__main__':
    main()
