import copy
import re
from types import SimpleNamespace

from util import whole_file

INPUT_REGEX = (r"Register A: (?P<A>\d+)\s*"
               r"Register B: (?P<B>\d+)\s*"
               r"Register C: (?P<C>\d+)\s*"
               r"Program: (?P<Program>[\d,]+)")

def parse_input(path):
    m = re.match(INPUT_REGEX, whole_file(path))
    s = SimpleNamespace(a=int(m["A"]), b=int(m["B"]), c=int(m["C"]), ic=0, buffer=[])
    p = [int(op) for op in m["Program"].split(',')]
    return s, p

def combo(state, oper):
    match oper:
        case 0 | 1 | 2 | 3: return oper
        case 4: return state.a
        case 5: return state.b
        case 6: return state.b

def adv(state, oper):
    state.a = state.a // 2 ** combo(state, oper)
    state.ic += 2

def bxl(state, oper):
    state.b = state.b ^ oper
    state.ic += 2

def bst(state, oper):
    state.b = combo(state, oper) % 8
    state.ic += 2

def jnz(state, oper):
    state.ic = oper if state.a else state.ic + 2

def bxc(state, _):
    state.b = state.b ^ state.c
    state.ic += 2

def out(state, oper):
    state.buffer.append(combo(state, oper) % 8)
    state.ic += 2

def bdv(state, oper):
    state.b = state.a // 2 ** combo(state, oper)
    state.ic += 2

def cdv(state, oper):
    state.c = state.a // 2 ** combo(state, oper)
    state.ic += 2

opcode_handlers = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

def run_program(state, program, a = None):
    if a: state.a = a
    while state.ic < len(program) - 1:
        op, oper = program[state.ic], program[state.ic + 1]
        opcode_handlers[op](state, oper)
    return state.buffer

# Manually disassembled the given program to derive this bruteforce solution
def reverse(wanted):
    lower, upper = 0, 8**len(wanted) - 1
    for i in range(len(wanted) - 1, -1, -1):
        for a in range(lower, lower + upper):
            out = run_program(copy.deepcopy(initial_state), program, a)
            if out == wanted: return a
            if out == wanted[i:]:
                lower = a * 8
                break

initial_state, program = parse_input("input.txt")

p1 = ",".join(str(c) for c in run_program(copy.deepcopy(initial_state), program))
p2 = reverse(program)

print(f"part1: {p1}, part2: {p2}")
