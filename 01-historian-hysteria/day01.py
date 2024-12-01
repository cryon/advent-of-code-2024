from util import lines
from collections import Counter

pairs = list(lines("input.txt"))

lefts = sorted([int(pair.split()[0]) for pair in pairs])
rights = sorted([int(pair.split()[1]) for pair in pairs])
diffs = [abs(a - b) for a, b in zip(lefts, rights)]

counts = Counter(rights)
scores = [v * counts[v] for v in lefts]

print(f"part1: {sum(diffs)}, part2: {sum(scores)}")
