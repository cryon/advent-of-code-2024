from itertools import combinations, accumulate, repeat, takewhile
from util import chars_with_coords, c_sub, c_add

bounds = 0, 0
antennas = {}
for c, p in chars_with_coords("input.txt"):
    bounds = max(p[0], bounds[0]), max(p[1], bounds[1])
    if c!= '.': antennas.setdefault(c, []).append(p)

def gen_antinodes(p1, p2):
    return (accumulate(repeat(c_sub(p1, p2)), c_add, initial=p1),
            accumulate(repeat(c_sub(p2, p1)), c_add, initial=p2))

def in_bounds(position):
    return 0 <= position[0] <= bounds[0] and 0 <= position[1] <= bounds[1]

antinode_generators = [gen_antinodes(l1, l2)
                       for frequency, locations in antennas.items()
                       for l1, l2 in combinations(locations, 2)]

antinodes, antinodes_with_harmonics = set(), set()

for generators in antinode_generators:
    for generator in generators:
        nodes = list(takewhile(in_bounds, generator))
        if len(nodes) > 1: antinodes.add(nodes[1])
        antinodes_with_harmonics.update(nodes)

print(f"part1: {len(antinodes)}, part2: {len(antinodes_with_harmonics)}")
