SCORE_MAP = {'A': 1, 'B': 2, 'C': 3}
WIN_MAP = {'A': 'B', 'B': 'C', 'C': 'A'}
LOSE_MAP = {'A': 'C', 'B': 'A', 'C': 'B'}


def get_input():
    with open("input.txt") as f:
        return [l.strip() for l in f.readlines()]
