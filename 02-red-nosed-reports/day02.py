from util import lines, cmp


def all_reports():
    for line in lines("input.txt"):
        yield [int(x) for x in line.split()]


def is_safe_pair(a, b, trend):
    return trend and (b - a) * trend > 0 and abs(b - a) <= 3


def is_safe(report):
    trend = cmp(report[1], report[0])
    for a, b in zip(report, report[1:]):
        if not is_safe_pair(a, b, trend):
            return False
    return True


def is_safe_dampen(report):
    return any(is_safe(report[:i] + report[i+1:]) for i in range(len(report)))


safe_reports = [is_safe(report) for report in all_reports()]
safe_reports_dampened = [is_safe_dampen(report) for report in all_reports()]
print(f"part1: {sum(safe_reports)}, part2: {sum(safe_reports_dampened)}")
