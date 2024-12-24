from collections import Counter
from functools import reduce
from itertools import pairwise
from util import lines

def next_secret(secret):
    secret = ((secret * 64) ^ secret) % 16777216
    secret = ((secret // 32) ^ secret) % 16777216
    secret = ((secret * 2048) ^ secret) % 16777216
    return secret

def gen_prices(secret, num):
    return [(secret := next_secret(secret) if i else secret) % 10 for i in range(num)]

def price_change_pairs(secret, num):
    numbers = gen_prices(secret, num)
    return ([(numbers[0], None)] +
            [(curr, curr - prev) for prev, curr in pairwise(numbers)])

def populate_price_counts(pairs):
    price_counter = Counter()
    for i in range(len(pairs) - 4 + 1):
        window = pairs[i: i + 4]
        changes = tuple(c[1] for c in window)
        if None not in changes and changes not in price_counter:
            price_counter[changes] = pairs[i + 3][0]
    return price_counter

initial_secrets = [int(line) for line in lines("input.txt")]

counts = Counter()
for initial_secret in initial_secrets:
    counts += populate_price_counts(price_change_pairs(initial_secret, 2000))

p1 = sum(reduce(lambda s, _: next_secret(s), range(2000), secret) for secret in initial_secrets)
p2 = counts.most_common(1)[0][1]

print(f"part1: {p1}, part2: {p2}")


