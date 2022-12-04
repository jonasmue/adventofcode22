from common import *


def find_result(pairs):
    overlap_sum = 0
    for p in pairs:
        s1, s2 = get_range_sets(p)
        intersection = s1.intersection(s2)
        if len(intersection):
            overlap_sum += 1
    return overlap_sum


if __name__ == "__main__":
    inpt = get_input()
    result = find_result(inpt)
    print(result)
