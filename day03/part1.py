from common import *


def find_result(rucksacks):
    result = 0
    for r in rucksacks:
        first, second = set(r[:len(r) // 2]), set(r[len(r) // 2:])
        duplicates = first.intersection(second)
        assert len(duplicates) == 1
        result += LETTERS[duplicates.pop()]
    return result


if __name__ == "__main__":
    inpt = get_input()
    result = find_result(inpt)
    print(result)
