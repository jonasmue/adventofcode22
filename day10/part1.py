from common import *


def find_result(instructions):
    signal_strengths = []
    def f_after(cycle, register): signal_strengths.append(cycle * register)
    run_instructions(instructions, 20, lambda _: None, f_after)
    return sum(signal_strengths)


if __name__ == "__main__":
    inpt = get_input()
    result = find_result(inpt)
    print(result)
