from collections import Counter
from util import lines, c_add

DIRS = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
HAYSTACK = {(x, y): c for y, line in enumerate(lines("input.txt", True)) for x, c in enumerate(line)}

def search(needle, pos, direction):
    for letter in needle:
        if HAYSTACK.get(pos) != letter: return False
        pos = c_add(pos, direction)
    return True

mas_locations = [c_add(p, direction)
                 for p in HAYSTACK
                 for direction in DIRS[1::2]
                 if search("MAS", p, direction)]

xmases = sum(search("XMAS", p, direction) for p in HAYSTACK for direction in DIRS)
crosses = sum(1 for count in Counter(mas_locations).values() if count == 2)

print(f"part1: {xmases}, part2: {crosses}")
