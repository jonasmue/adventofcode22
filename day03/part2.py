from common import *


def find_result(rucksacks):
    result = 0
    for i in range(0, len(rucksacks), 3):
        group = list(map(set, rucksacks[i:i + 3]))
        badge = set.intersection(*group)
        assert len(badge) == 1
        result += LETTERS[badge.pop()]
    return result


if __name__ == "__main__":
    inpt = get_input()
    result = find_result(inpt)
    print(result)
