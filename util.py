from itertools import zip_longest


def lines(path, strip=False, skip_empty=False):
    with open(path, "r") as input_file:
        for line in input_file:
            stripped = line.strip() if strip else line
            if skip_empty and not stripped:
                continue
            yield stripped


def whole_file(path):
    with open(path, "r") as input_file:
        return input_file.read()


def chars_with_coords(path):
    for y, line in enumerate(lines(path, True)):
        for x, c in enumerate(line):
            yield c, (x, y)


def chunker(iterable, size, fill = 0):
    seq = [iter(iterable)] * size
    return zip_longest(*seq, fillvalue=fill)


def cmp(a, b):
    return (a > b) - (a < b)


def c_add(t1, t2):
    return t1[0] + t2[0], t1[1] + t2[1]


def c_sub(t1, t2):
    return t1[0] - t2[0], t1[1] - t2[1]


def rot_cw(v):
    return -v[1], v[0]

