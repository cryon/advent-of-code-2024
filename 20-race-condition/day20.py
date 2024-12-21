from collections import Counter
from util import chars_with_coords, c_add

DIRS = (1, 0), (-1, 0), (0, 1), (0, -1)

track = {}
start, end = (0, 0), (0, 0)
for c, p in chars_with_coords("input.txt"):
    if c != '#': track[p] = 0
    if c == 'S': start = p
    if c == 'E': end = p

def walk(track, current, end):
    dist = len(track)
    while current != end:
        track[current] = (dist := dist - 1)
        current = next((c_add(current, d) for d in DIRS if track.get(c_add(current, d)) == 0), end)
    return {k: v for k, v in sorted(track.items(), key=lambda item: item[1], reverse=True)}

def cheat_reachable(pos, n):
    return [(pos[0] + dx, pos[1] + dy)
            for dx in range(-n, n + 1)
            for dy in range(-n + abs(dx), n - abs(dx) + 1)]

def cheat_saved(path, cheat_depth):
    saved = Counter()
    for p, dist in path.items():
        for target in cheat_reachable(p, cheat_depth):
            steps_taken_to_cheat = abs(target[0] - p[0]) + abs(target[1] - p[1])
            if target in path and path[target] < dist - steps_taken_to_cheat:
                saved[dist - path[target] - steps_taken_to_cheat]+= 1
    return saved

path = walk(track, start, end)
p1 = sum(v for k, v in cheat_saved(path, 2).items() if k >= 100)
p2 = sum(v for k, v in cheat_saved(path, 20).items() if k >= 100)
print(f"part1: {p1}, part2: {p2}")
