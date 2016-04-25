from pandigital import is_1_x_pandigital
import math
import itertools


def is_prime(p):
    """
    A primality test.

    >>> [is_prime(n) for n in (857, 859, 863, 877, 881, 883, 887, 907, 911)]
    [True, True, True, True, True, True, True, True, True]

    >>> is_prime(861)
    False

    >>> [is_prime(n) for n in (1, 2, 4, 6, 8, 7)]
    [False, True, False, False, False, True]

    """
    if p == 1:
        return False
    for n in range(2, int(math.sqrt(p))+1):
        if p % n == 0:
            return False
    return True


# Generate all combos

def solve():
    for n in range(9, 2, -1):
        # range is backwards as itertools.permutations generates
        # lexicographically sorted permutations in the order they're
        # given and we want to start with bigger numbers.
        for combo in itertools.permutations(''.join(
                ['%s' % x for x in range(n, 0, -1)]), n):
            if combo[-1] not in ('1', '3', '5', '7', '9'):
                # cannot possibly be prime
                continue
            to_test = int(''.join(combo))
            if is_prime(to_test):
                return to_test


print solve()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
