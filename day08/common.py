def get_input():
    with open("input.txt") as f:
        return [[int(char) for char in l.strip()] for l in f.readlines()]
