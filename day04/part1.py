from common import *


def find_result(pairs):
    subset_sum = 0
    for p in pairs:
        s1, s2 = get_range_sets(p)
        if s1.issubset(s2) or s2.issubset(s1):
            subset_sum += 1
    return subset_sum


if __name__ == "__main__":
    inpt = get_input()
    result = find_result(inpt)
    print(result)
