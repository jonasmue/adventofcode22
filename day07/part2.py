from common import *

TOTAL_SIZE = 70000000
NEEDED_SPACE = 30000000


def find_result(instructions):
    fs = FileSystem()
    fs.parse_instructions(instructions)
    free_space = TOTAL_SIZE - fs.sizes["/"]
    to_delete = NEEDED_SPACE - free_space
    for s in sorted(fs.sizes.values()):
        if s > to_delete:
            return s


if __name__ == "__main__":
    inpt = get_input()
    result = find_result(inpt)
    print(result)
