from functools import reduce
from itertools import product
from operator import add, mul
from util import lines

def concat(l, r):
    return int(str(l) + str(r))

def solvable(value, numbers, operators):
    for arrangement in product(operators, repeat=len(numbers) - 1):
        if reduce(lambda acc, t: t[0](acc, t[1]), zip(arrangement, numbers[1:]), numbers[0]) == value:
            return True
    return False

equations = [(int(l), [int(num) for num in r.split()])
             for line in lines("input.txt")
             for l, r in [line.split(':')]]

p1 = sum(val for val, numbers in equations if solvable(val, numbers, [add, mul]))
p2 = sum(val for val, numbers in equations if solvable(val, numbers, [add, mul, concat]))

print(f"part1: {p1}, part2: {p2}")

