from operator import and_, xor, or_
from itertools import takewhile, count
from util import lines

OPS = {'OR': or_, 'AND': and_, 'XOR': xor}

all_lines = lines("input.txt", True)
wires = {n:int(v) for n, v in (line.split(':') for line in takewhile(lambda x: len(x), all_lines))}
gates = [(op, i1, i2, out) for i1, op, i2, _, out in (line.split() for line in all_lines)]

def simulate(gates, wires):
    while gates:
        op, i1, i2, out = gates.pop(0)
        if i1 in wires and i2 in wires: wires[out] = OPS[op](wires[i1], wires[i2])
        else: gates.append((op, i1, i2, out))
    value = 0
    for ord, output in ((i, f"z{i:02d}") for i in count()):
        if not output in wires: break
        value |= wires[output] << ord
    return value

# Could not solve part 2 programmatically, this generates the dot code for a graph representation of the wires
# and operations, copy and paste here: https://dreampuf.github.io/GraphvizOnline/ and untangle the faulty
# adders taking note of output switches, which is part 2's solution
def create_graph(gates, wires):
    edges = []
    for op, i1, i2, out in gates:
        edges.append(f"{i1} -> {out}[label={op}]")
        edges.append(f"{i2} -> {out}[label={op}]")

    return f"""
       digraph G {{
          {";\n".join(e for e in sorted(edges))}
          {";\n".join(f"{n} [style=filled]" for n in sorted(wires))}
          {";\n".join(f"{g[3]} [style=filled,color=red]" for g in sorted(gates) if g[3].startswith("z"))}
       }}
    """

p1 = simulate(gates.copy(), wires.copy())
p2 = create_graph(gates, wires)
print(f"part1: {p1}, part2: \n\n{p2}")