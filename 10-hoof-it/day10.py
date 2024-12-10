from itertools import chain
from util import chars_with_coords, c_add

DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

topology, trailheads = {}, []
for c, p in chars_with_coords("input.txt"):
    topology[p] = int(c)
    if c == '0': trailheads.append(p)

def paths_to_explore(pos):
    return [p for p in [c_add(pos, d) for d in DIRS]
            if topology.get(p, 0) == topology[pos] + 1]

def explore_peaks(pos, visited_peaks):
    if topology[pos] == 9: return [pos]
    paths = [explore_peaks(n, visited_peaks.copy())
             for n in paths_to_explore(pos)]
    return visited_peaks + list(chain.from_iterable(paths))

reachable_peaks = [explore_peaks(p, []) for p in trailheads]
p1 = sum(len(set(p)) for p in reachable_peaks)
p2 = sum(len(p) for p in reachable_peaks)

print(f"part1: {p1}, part2: {p2}")