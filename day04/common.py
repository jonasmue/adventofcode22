def get_range_set(e):
    start, end = e.split("-")
    return set(range(int(start), int(end) + 1))


def get_range_sets(pair):
    e1, e2 = pair.split(",")
    return get_range_set(e1), get_range_set(e2)


def get_input():
    with open("input.txt") as f:
        return [l.strip() for l in f.readlines()]
