from collections import defaultdict
from util import chars_with_coords, c_add

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def neighbours(pos):
    return [c_add(pos, d) for d in DIRS]

def connected_plots(pos, visited):
    visited.add(pos)
    neighbour_plots = [p for p in neighbours(pos) if garden.get(p) == garden[pos]]
    res = [pos]
    for n in neighbour_plots:
        if n in visited: continue
        res.extend(connected_plots(n, visited))
    return res

def area(group):
    return len(group)

def perimeter(group):
    return sum(1 for pos in group for n in neighbours(pos) if n not in group)

def sides(group):
    res = 0
    for d in DIRS:
        width_axis = 1 if d[0] else 0
        depth_axis = 0 if d[0] else 1

        fence_by_depth = defaultdict(list)
        for pos in group:
            if c_add(pos, d) not in group:
                fence_by_depth[pos[depth_axis]].append(pos[width_axis])

        for depth in fence_by_depth.values():
            sorted_on_width_axis = sorted(depth)
            num_parts = 1
            for i in range(1, len(sorted_on_width_axis)):
                if sorted_on_width_axis[i] != sorted_on_width_axis[i - 1] + 1:
                    num_parts += 1
            res += num_parts
    return res

garden = {p: v for v, p in chars_with_coords("input.txt")}
groups = set()
while garden:
    pos = next(iter(garden))
    plots = connected_plots(pos, set())
    groups.add(tuple(plots))
    garden = {p: garden[p] for p in garden if p not in plots}

p1 = sum(area(group) * perimeter(group) for group in groups)
p2 = sum(area(group) * sides(group) for group in groups)

print(f"part1: {p1}, part2: {p2}")
