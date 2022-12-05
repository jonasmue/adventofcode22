from common import *


def find_result(instructions):
    stacks = [list(reversed(l)) for l in INITIAL_STACKS]
    for instruction in instructions:
        quantity, origin, destination = parse_instruction(instruction)
        stacks[destination] += stacks[origin][-quantity:]
        stacks[origin] = stacks[origin][:-quantity]
    return "".join([s[-1] for s in stacks])


if __name__ == "__main__":
    inpt = get_input()
    result = find_result(inpt)
    print(result)
