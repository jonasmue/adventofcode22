def find_result(buffer, marker_length):
    for i in range(marker_length, len(buffer)):
        if len(set(buffer[i - marker_length:i])) == marker_length:
            return i
    return -1


def get_input():
    with open("input.txt") as f:
        return f.read()
