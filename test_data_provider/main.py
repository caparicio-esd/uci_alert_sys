from modules.data_provider import AbstractEntity
from sys import argv


def init():
    print(argv[1:])
    a = AbstractEntity()


if __name__ == "__main__":
    init()
