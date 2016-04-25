import sys


def gen_pen(n):
    """ Generate n pentagonal numbers."""
    l = []
    for i in range(1, n+1):
        l.append(i*(3*i - 1)/2)
    return l


# Let's try 10000. Naive solution.
pentagonal_numbers = set(gen_pen(10000))
min_diff = sys.maxint
for p in pentagonal_numbers:
    for q in pentagonal_numbers:
        if p == q:
            continue
        if p + q in pentagonal_numbers and abs(p - q) in pentagonal_numbers:
            if abs(p - q) < min_diff:
                min_diff = abs(p - q)


print min_diff
