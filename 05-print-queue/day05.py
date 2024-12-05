from functools import cmp_to_key
from itertools import takewhile
from util import lines

lines_gen = lines("input.txt", True)
rules = [(int(l), int(r))
         for item in takewhile(lambda x: len(x) > 0, lines_gen)
         for l, r in [item.split('|')]]
updates = [[int(p) for p in row.split(',')] for row in lines_gen]

def cmp_updates(u1, u2):
    rule = next((r for r in rules if u1 in r and u2 in r), None)
    if not rule: return 0
    return -1 if rule[0] == u1 else 1

unfixed_middles, fixed_middles = [], []
for update in updates:
    s = sorted(update, key=cmp_to_key(cmp_updates))
    (unfixed_middles if update == s else fixed_middles).append(s[len(s) // 2])

print(f"part1: {sum(unfixed_middles)}, part2: {sum(fixed_middles)}")



