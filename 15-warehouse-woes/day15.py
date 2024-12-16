from itertools import takewhile
from util import lines, c_add, chars_with_coords

DIRS = {'>': (1, 0), '<': (-1, 0), '^': (0, -1), 'v': (0, 1)}
HORIZONTAL = {(0, 1), (0, -1)}

def parse_input(path, wide = False):
    warehouse, robot = {}, (0, 0)
    all_lines = lines(path, True)
    for y, line in enumerate(takewhile(len, all_lines)):
        for x_candidate, c in enumerate(line):
            x = x_candidate * 2 if wide else x_candidate
            if c == '@':
                robot = x, y
                warehouse[(x, y)] = '.'
                if wide: warehouse[(x + 1, y)] = '.'
            elif wide and c == 'O':
                warehouse[(x, y)] = '['
                warehouse[(x + 1, y)] = ']'
            else:
                warehouse[(x, y)] = c
                if wide: warehouse[(x + 1, y)] = c
    return warehouse, robot, [c for line in all_lines for c in line]

def swap(warehouse, pos1, pos2):
    warehouse[pos1], warehouse[pos2] = warehouse[pos2], warehouse[pos1]

def can_move(warehouse, pos, dir, forked=False):
    if warehouse[pos] == '#': return False
    if warehouse[pos] == '.': return True

    can_move_wide = True
    if dir in HORIZONTAL and not forked:
        if warehouse[pos] == '[':
            can_move_wide = can_move(warehouse, c_add(pos, (1, 0)), dir, True)
        if warehouse[pos] == ']':
            can_move_wide = can_move(warehouse, c_add(pos, (-1, 0)), dir, True)

    target = c_add(pos, dir)
    return can_move_wide and can_move(warehouse, target, dir)

def move(warehouse, pos, dir, forked = False):
    if warehouse[pos] == '.': return

    if dir in HORIZONTAL and not forked:
        if warehouse[pos] == '[':
            move(warehouse, c_add(pos, (1, 0)), dir, True)
        if warehouse[pos] == ']':
            move(warehouse, c_add(pos, (-1, 0)), dir, True)

    target = c_add(pos, dir)
    move(warehouse, target, dir)
    swap(warehouse, pos, target)

def run_robot(warehouse, robot, moves):
    for m in moves:
        direction = DIRS[m]
        target = c_add(robot, direction)
        if can_move(warehouse, target, direction):
            move(warehouse, target, direction)
            robot = target
    return robot

warehouse, robot, movements = parse_input("input.txt")
run_robot(warehouse, robot, movements)
p1 = sum(x + y * 100 for (x, y), c in warehouse.items() if c == 'O')

warehouse, robot, movements = parse_input("input.txt", True)
run_robot(warehouse, robot, movements)
p2 = sum(x + y * 100 for (x, y), c in warehouse.items() if c == '[')

print(f"part1: {p1}, part2: {p2}")
