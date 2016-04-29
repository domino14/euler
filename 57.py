def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


def add_fractions(frac1, frac2):
    """
    >>> add_fractions((2, 1), (1, 2))
    (5, 2)

    >>> add_fractions((2, 1), (2, 5))
    (12, 5)

    >>> add_fractions((5, 12), (2, 1))
    (29, 12)

    >>> add_fractions((12, 29), (1, 1))
    (41, 29)

    >>> add_fractions((5, 7), (12, 8))   #     124/56
    (31, 14)
    """
    den = frac1[1] * frac2[1]
    num = frac1[0] * den / frac1[1] + frac2[0] * den / frac2[1]

    d = gcd(den, num)

    return ((num/d, den/d))


def reciprocal(frac):
    """
    >>> reciprocal((5, 2))
    (2, 5)

    >>> reciprocal((293, 341))
    (341, 293)
    """
    return (frac[1], frac[0])


def solve():
    frac = (2, 5)
    ans = 0
    for it in range(3, 1000):
        frac = reciprocal(add_fractions(frac, (2, 1)))
        result = add_fractions(frac, (1, 1))
        if len(str(result[0])) > len(str(result[1])):
            ans += 1
    return ans

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    n = solve()
    print n
