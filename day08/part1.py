from common import *


def visit_from(the_map, visible, direction):
    width, height = len(the_map[0]), len(the_map)
    if direction == "E" or direction == "W":
        for y in range(height):
            current_max = -1
            for x in range(width):
                current_height = the_map[y][x]
                if current_height > current_max:
                    visible[y][x] = 1
                    current_max = current_height
                    if current_max == 9:
                        break
    if direction == "N":
        for x in range(width):
            current_max = -1
            for y in range(height):
                current_height = the_map[y][x]
                if current_height > current_max:
                    visible[y][x] = 1
                    current_max = current_height
                    if current_max == 9:
                        break
    if direction == "W":
        for y in range(height):
            current_max = -1
            for x in range(width - 1, -1, -1):
                current_height = the_map[y][x]
                if current_height > current_max:
                    visible[y][x] = 1
                    current_max = current_height
                    if current_max == 9:
                        break
    if direction == "S":
        for x in range(width):
            current_max = -1
            for y in range(height - 1, -1, -1):
                current_height = the_map[y][x]
                if current_height > current_max:
                    visible[y][x] = 1
                    current_max = current_height
                    if current_max == 9:
                        break


def find_result(map):
    width, height = len(map[0]), len(map)
    visible = [[0 for _ in range(width)] for _ in range(height)]
    for direction in ["N", "E", "S", "W"]:
        visit_from(map, visible, direction)
    return sum(sum(visible, []))


if __name__ == "__main__":
    inpt = get_input()
    result = find_result(inpt)
    print(result)
