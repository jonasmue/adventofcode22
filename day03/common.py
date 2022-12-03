LOWERCASE_LETTERS = {char: index + 1 for index, char in enumerate(map(chr, range(ord('a'), ord('z') + 1)))}
UPPERCASE_LETTERS = {char: index + 27 for index, char in enumerate(map(chr, range(ord('A'), ord('Z') + 1)))}
LETTERS = LOWERCASE_LETTERS | UPPERCASE_LETTERS


def get_input():
    with open("input.txt") as f:
        return [l.strip() for l in f.readlines()]
