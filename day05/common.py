from collections import deque

INITIAL_STACKS = [
    ["P", "G", "R", "N"],
    ["C", "D", "G", "F", "L", "B", "T", "J"],
    ["V", "S", "M"],
    ["P", "Z", "C", "R", "S", "L"],
    ["Q", "D", "W", "C", "V", "L", "S", "P"],
    ["S", "M", "D", "W", "N", "T", "C"],
    ["P", "W", "G", "D", "H"],
    ["V", "M", "C", "S", "H", "P", "L", "Z"],
    ["Z", "G", "W", "L", "F", "P", "R"]
]


def parse_instruction(line):
    split = line.split()
    return int(split[1]), int(split[3]) - 1, int(split[5]) - 1


def get_input():
    with open("input.txt") as f:
        return [l.strip() for l in f.readlines()][10:]
