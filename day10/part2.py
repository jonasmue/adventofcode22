from common import *


def draw(image, cycle, register):
    pixel_position = cycle % 40
    if pixel_position in [register - 1, register, register + 1]:
        image[-1].append("#")
    else:
        image[-1].append(".")


def find_result(instructions):
    image = [[]]
    def f_during(cycle, register): draw(image, cycle, register)
    def f_after(*_): image.append([])
    run_instructions(instructions, 0, f_during, f_after)
    return image


if __name__ == "__main__":
    inpt = get_input()
    result = find_result(inpt)
    for line in result:
        print("".join(line))
