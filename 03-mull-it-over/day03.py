import re
from util import whole_file

REGEX_MUL     = r"(?P<op>mul)\((\d+)?(?:,(\d+))*\)"
REGEX_DO_DONT = r"(?P<op>mul|do|don't)\((\d+)?(?:,(\d+))*\)"

def tokenize(regex, src):
    return [[match["op"]] + [int(t) for t in match.groups()[1:] if t]
            for match in re.finditer(regex, src)]


def parse(tokens):
    res, mul_enabled = 0, True
    for token in tokens:
        match token:
            case ["mul", a, b] if mul_enabled: res += a * b
            case ["do"]: mul_enabled = True
            case ["don't"]: mul_enabled = False
    return res

mem = whole_file("input.txt")
print((f"part1: {parse(tokenize(REGEX_MUL, mem))}, "
       f"part2: {parse(tokenize(REGEX_DO_DONT, mem))}"))

