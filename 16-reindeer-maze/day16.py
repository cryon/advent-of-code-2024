import heapq
from util import chars_with_coords, c_add, rot_cw, rot_ccw

walls, start, end = set(), (0, 0), (0, 0)
for c, p in chars_with_coords("input.txt"):
    if c == 'S': start = p
    if c == 'E': end = p
    if c == '#': walls.add(p)

def walk_maze(walls, start, end):
    visited = []
    best = float("inf")
    cheapest_so_far = {}

    queue = [(0, start, (1, 0), [start])]
    while queue:
        cost, pos, d, path = heapq.heappop(queue)
        if cost > cheapest_so_far.get((pos, d), float("inf")): continue
        cheapest_so_far[pos, d] = cost

        if pos == end and cost <= best:
            visited.extend(path)
            best = cost

        for rot, rot_cost  in [(d, 1), (rot_cw(d), 1001), (rot_ccw(d), 1001)]:
            candidate = c_add(pos, rot) # an extra move on rotations therefore 1001 above
            if candidate not in walls:
                heapq.heappush(queue, (cost + rot_cost, candidate, rot, path + [candidate]))

    return best, visited

best, visited = walk_maze(walls, start, end)
print(f"part1: {best}, part2: {len(set(visited))}")
