import functools
from util import whole_file

@functools.cache
def blink(stone, t):
    if not t: return 1
    if not stone: return blink(1, t - 1)
    if (s := str(stone)) and len(s) % 2 == 0:
        l, r = int(s[0:len(s)//2]), int(s[len(s)//2:])
        return blink(l, t - 1) + blink(r, t - 1)
    return blink(stone * 2024, t - 1)

stones = [int(s) for s in whole_file("input.txt").split()]

p1 = sum(blink(stone, 25) for stone in stones)
p2 = sum(blink(stone, 75) for stone in stones)

print(f"part1: {p1}, part2: {p2}")