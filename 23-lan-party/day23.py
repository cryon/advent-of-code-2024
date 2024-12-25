from collections import defaultdict
from itertools import combinations
from util import lines

network = defaultdict(set)
for line in lines("input.txt", True):
    c1, c2 = line.split('-')
    network[c1].add(c2)
    network[c2].add(c1)

def triple(network, only_with_santa = False):
    triple = set()
    for computer, connections in network.items():
        if only_with_santa and not computer.startswith('t'): continue
        for c1, c2 in combinations(connections, 2):
            if c1 in network[c2] and c2 in network[c1]:
                triple.add(frozenset((computer, c1, c2)))
    return triple

def enlarge_sub_nets(network, sub_nets):
    super_nets = set()
    for sub_net in sub_nets:
        node = list(sub_net)[0]
        for connection in network[node]:
            if connection not in sub_net and network[connection].issuperset(sub_net):
                super_nets.add(sub_net | {connection})
    return super_nets

sub_nets = triple(network)
while True:
    new = enlarge_sub_nets(network, sub_nets)
    if not new: break
    sub_nets = new

p1 = len(triple(network, only_with_santa=True))
p2 = ",".join(sorted(list(sub_nets)[0]))
print(f"part1: {p1}, part2: {p2}")
