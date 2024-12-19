from functools import cache
from util import lines

@cache
def arrangements(pattern, towels):
    if not pattern: return 1
    prefixes = [t for t in towels if pattern.startswith(t)]
    return sum(arrangements(pattern[len(p):], towels) for p in prefixes)

all_lines = lines("input.txt", True, True)
towels = tuple(t.strip() for t in next(all_lines).split(','))
patterns = list(all_lines)

p1 = sum(1 for pattern in patterns if arrangements(pattern, towels))
p2 = sum(arrangements(pattern, towels) for pattern in patterns)

print(f"part1: {p1}, part2: {p2}")
