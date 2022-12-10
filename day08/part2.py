from common import *


def get_look_distance(map, x, y, direction):
    width, height = len(map[0]), len(map)
    current_height = map[y][x]
    distance = 0
    if direction == "S":
        for y_delta in range(y + 1, height):
            distance += 1
            if map[y_delta][x] >= current_height: break
    if direction == "N":
        for y_delta in range(y - 1, -1, -1):
            distance += 1
            if map[y_delta][x] >= current_height: break
    if direction == "E":
        for x_delta in range(x - 1, -1, -1):
            distance += 1
            if map[y][x_delta] >= current_height: break
    if direction == "W":
        for x_delta in range(x + 1, width):
            distance += 1
            if map[y][x_delta] >= current_height: break
    return distance


def find_result(map):
    width, height = len(map[0]), len(map)
    the_max = 0
    for y in range(height):
        for x in range(width):
            scenic_score = 1
            scenic_score *= get_look_distance(map, x, y, "N")
            scenic_score *= get_look_distance(map, x, y, "W")
            scenic_score *= get_look_distance(map, x, y, "S")
            scenic_score *= get_look_distance(map, x, y, "E")
            the_max = max(scenic_score, the_max)
    return the_max


if __name__ == "__main__":
    inpt = get_input()
    result = find_result(inpt)
    print(result)
