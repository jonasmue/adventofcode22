from common import *


def find_result(calories):
    current_max = 0
    current_sum = 0
    for c in calories.split("\n"):
        if c == "":
            current_max = max(current_sum, current_max)
            current_sum = 0
            continue
        current_sum += int(c)
    return current_max


if __name__ == "__main__":
    inpt = get_input()
    result = find_result(inpt)
    print(result)
