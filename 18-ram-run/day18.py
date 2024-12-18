import heapq
from util import lines, c_add

DIRS = {(1, 0), (-1, 0), (0, -1), (0, 1)}

bounds = 70, 70
falling_bytes = [(int(line.split(',')[0]), int(line.split(',')[1]))
                 for line in lines("input.txt", True)]

def neighbours(corrupted, pos):
    return [c_add(pos, d) for d in DIRS
            if 0 <= c_add(pos, d)[0] <= bounds[0] and
               0 <= c_add(pos, d)[1] <= bounds[1] and
               not c_add(pos, d) in corrupted]

def find_exit(corrupted, start, end):
    queue = [(0, start)]
    visited = set()
    while queue:
        score, pos = heapq.heappop(queue)
        if pos == end: return score
        if pos in visited: continue
        visited.add(pos)
        for n in neighbours(corrupted, pos):
            heapq.heappush(queue, (score + 1, n))

p1 = find_exit(set(b for b in falling_bytes[:1024]), (0, 0), bounds)

corrupted = set()
while find_exit(corrupted, (0, 0), bounds):
    corrupted |= {byte := falling_bytes.pop(0)}

print(f"part1: {p1}, part2: {byte}")
