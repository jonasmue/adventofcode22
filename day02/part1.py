from common import *

SHAPE_MAP = {'X': 'A', 'Y': 'B', 'Z': 'C'}


def game_score(opponent, my):
    if SHAPE_MAP[my] == opponent:
        return 3
    if opponent == WIN_MAP[SHAPE_MAP[my]]:
        return 0
    return 6


def find_result(rounds):
    score = 0
    for r in rounds:
        opponent, my = r.split()
        score += SCORE_MAP[SHAPE_MAP[my]]
        score += game_score(opponent, my)
    return score


if __name__ == "__main__":
    inpt = get_input()
    result = find_result(inpt)
    print(result)
