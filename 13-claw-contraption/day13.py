import re
from collections import namedtuple

from util import lines, chunker, c_add

BUTTON_REGEX = r"X(?P<X>[+-]\d+), Y(?P<Y>[+-]\d+)"
PRIZE_REGEX  = r"X=(?P<X>\d+), Y=(?P<Y>\d+)"

Machine = namedtuple("Machine", "a b prize")

def parse_machine(row1, row2, row3):
    a = re.search(BUTTON_REGEX, row1)
    b = re.search(BUTTON_REGEX, row2)
    p = re.search(PRIZE_REGEX, row3)
    return Machine((int(a["X"]), int(a["Y"])),
                   (int(b["X"]), int(b["Y"])),
                   (int(p["X"]), int(p["Y"])))

def solve_machine(m, prize_offset = 0):
    px, py = c_add(m.prize, (prize_offset, prize_offset))

    det = m.a[0] * m.b[1] - m.a[1] * m.b[0]
    a = px * m.b[1] - py * m.b[0]
    b = py * m.a[0] - px * m.a[1]

    if a % det or b % det: return 0, 0
    return int(a / det), int(b / det)

machines = [parse_machine(r1, r2, r3)
            for r1, r2, r3
            in chunker(lines("input.txt", True, True), 3)]

p1 = sum((a * 3 + b)
         for a, b in (solve_machine(m)
         for m in machines))

p2 = sum((a * 3 + b)
         for a, b in (solve_machine(m, 10000000000000)
         for m in machines))

print(f"part1: {p1}, part2: {p2}")