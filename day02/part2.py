from common import *

OUTCOME_MAP = {'X': 0, 'Y': 3, 'Z': 6}


def game_score(opponent, outcome):
    if outcome == 'Y':
        return SCORE_MAP[opponent]
    if outcome == 'X':
        return SCORE_MAP[LOSE_MAP[opponent]]
    return SCORE_MAP[WIN_MAP[opponent]]


def find_result(rounds):
    score = 0
    for r in rounds:
        opponent, outcome = r.split()
        score += OUTCOME_MAP[outcome]
        score += game_score(opponent, outcome)
    return score


if __name__ == "__main__":
    inpt = get_input()
    result = find_result(inpt)
    print(result)
