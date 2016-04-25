"""
a^2 + b^2 = c^2
p = a + b + c

"""


def solutions(p):
    """
    Find number of solutions for a right triangle with integral sides.

    >>> len(solutions(120))
    3
    """
    sols = set()
    for a in range(1, p-2):
        for b in range(1, a-1):
            c = p - a - b
            if a**2 + b**2 == c**2:
                sols.add((a, b, c))

    return sols


max_sols = 0
max_p = None
for p in range(3, 1001):
    num_sols = len(solutions(p))
    if num_sols > max_sols:
        max_sols = num_sols
        max_p = p

print max_p, solutions(max_p)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
