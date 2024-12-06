from util import chars_with_coords, c_add, rot_cw

obstacles = set()
UP, bounds, guard_position = (0, -1), (0, 0), (0, 0)

for c, p in chars_with_coords("input.txt"):
    bounds = max(p[0], bounds[0]), max(p[1], bounds[1])
    match c:
        case '#': obstacles.add(p)
        case '^': guard_position = p

def in_bounds(position):
    return 0 <= position[0] <= bounds[0] and 0 <= position[1] <= bounds[1]

def walk(position, direction, extra_obstacle = None):
    visited = {}
    while in_bounds(position):
        if direction in visited.get(position, []): return False
        visited.setdefault(position, set()).add(direction)

        while (c_add(position, direction) in obstacles or
               c_add(position, direction) == extra_obstacle):
            direction = rot_cw(direction)

        position = c_add(position, direction)
    return visited

locations = walk(guard_position, UP)
loops = [l for l in locations if not walk(guard_position, UP, l)]

print(f"part1: {len(locations)}, part2: {len(loops)}")
