from functools import cache
from itertools import pairwise
from util import lines

class HashableDict(dict):
    def __hash__(self): return hash(frozenset(self))

NUMERIC = HashableDict({'7': (0, 0), '8': (1, 0), '9': (2, 0),
                        '4': (0, 1), '5': (1, 1), '6': (2, 1),
                        '1': (0, 2), '2': (1, 2), '3': (2, 2),
                        '!': (0, 3), '0': (1, 3), 'A': (2, 3)})

DIRECTIONAL = HashableDict({'!': (0, 0), '^': (1, 0), 'A': (2, 0),
                            '<': (0, 1), 'v': (1, 1), '>': (2, 1)})

def pad_paths(start, goal, keyboard):
    illegal = keyboard['!']
    start, goal = keyboard[start], keyboard[goal]
    dx, dy = goal[0] - start[0], goal[1] - start[1]

    horizontal = '>' * dx + '<' * -dx
    vertical = 'v' * dy + '^' * -dy

    horizontal_first_legal = (start[0] + dx, start[1]) != illegal
    vertical_first_legal = (start[0], start[1] + dy) != illegal

    res = []
    if horizontal_first_legal: res.append(horizontal + vertical)
    if vertical_first_legal: res.append(vertical + horizontal)
    return res

@cache
def shortest_for_seq(code, keyboard, robot_depth):
    if not robot_depth: return len(code)
    length = 0
    for start, goal in pairwise('A' + code):
        length += min(shortest_for_seq(sequence + 'A', DIRECTIONAL, robot_depth - 1)
                      for sequence in pad_paths(start, goal, keyboard))
    return length

def complexity(code, robots):
    shortest = shortest_for_seq(code, NUMERIC, robots)
    num = int(''.join(c for c in code if '0' <= c <= '9'))
    return shortest * num

p1, p2 = 0, 0
for code in lines("input.txt", True):
    p1 += complexity(code, 3)
    p2 += complexity(code, 26)

print(f"part1: {p1}, part2: {p2}")

