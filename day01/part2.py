from common import *


def find_result(calories):
    return sum(sorted([sum([int(c) for c in p.split("\n")]) for p in calories.split("\n\n")])[-3:])


if __name__ == "__main__":
    inpt = get_input()
    result = find_result(inpt)
    print(result)
