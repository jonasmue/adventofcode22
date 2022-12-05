from common import *


def find_result(instructions):
    stacks = [deque(l) for l in INITIAL_STACKS]
    for instruction in instructions:
        quantity, origin, destination = parse_instruction(instruction)
        for _ in range(quantity): stacks[destination].appendleft(stacks[origin].popleft())
    return "".join([s.popleft() for s in stacks])


if __name__ == "__main__":
    inpt = get_input()
    result = find_result(inpt)
    print(result)
