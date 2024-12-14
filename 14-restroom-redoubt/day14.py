import re
from collections import namedtuple
from functools import reduce
from itertools import count
from operator import mul

from util import lines

ROBOT_REGEX = r"p=(?P<s1>-?\d+),(?P<s2>-?\d+) v=(?P<v1>-?\d+),(?P<v2>-?\d+)"

bounds = (101, 103)
qx1, qx2 = range(0, bounds[0] // 2), range(bounds[0] // 2 + 1, bounds[0])
qy1, qy2 = range(0, bounds[1] // 2), range(bounds[1] // 2 + 1, bounds[1])

Robot = namedtuple("Robot", "start vel")

def walk(robot, seconds):
    return ((robot.start[0] + robot.vel[0] * seconds) % bounds[0],
            (robot.start[1] + robot.vel[1] * seconds) % bounds[1])

def robots_in_quadrants(robot_locations):
    return (sum(1 for p in robot_locations if p[0] in qx1 and p[1] in qy1),
            sum(1 for p in robot_locations if p[0] in qx2 and p[1] in qy1),
            sum(1 for p in robot_locations if p[0] in qx1 and p[1] in qy2),
            sum(1 for p in robot_locations if p[0] in qx2 and p[1] in qy2))

def has_consecutive_robots(locations, consecutive):
    for l in locations:
        if {(x, l[1]) for x in range(l[0], l[0] - consecutive, -1)}.issubset(locations):
            return True
    return False

def find_pattern(robots):
    for i in count(0):
        # Found the value 8 by manually increasing it until a pattern emerged
        if has_consecutive_robots({walk(r, i) for r in robots}, 8):
            return i

robots = []
for line in lines("input.txt"):
    m = re.match(ROBOT_REGEX, line)
    robots.append(Robot((int(m["s1"]), int(m["s2"])), (int(m["v1"]), int(m["v2"]))))

p1 = reduce(mul, robots_in_quadrants([walk(r, 100) for r in robots]))
p2 = find_pattern(robots)

print(f"part1: {p1}, part2: {p2}")
