import os

QUEST_ROOT = '.quest'


def init():
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
    init()


if __name__ == '__main__':
    main()