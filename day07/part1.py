from common import *


def find_result(instructions):
    fs = FileSystem()
    fs.parse_instructions(instructions)
    result = 0
    for size in fs.sizes.values():
        if size < 100000:
            result += size
    return result


if __name__ == "__main__":
    inpt = get_input()
    result = find_result(inpt)
    print(result)
