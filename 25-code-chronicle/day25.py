from itertools import combinations
from util import whole_file

schematics = whole_file("input.txt").split("\n\n")
p1 = sum(1 for s1, s2 in combinations(schematics, 2)
         if not any(c1 == '#' and c2 == '#' for c1, c2 in zip(s1, s2)))

print(f"part1: {p1}, part2: :-)")
