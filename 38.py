def concat_product(num, n):
    """
    Get concatenated product of num and (1, ..., n)

    >>> concat_product(9, 5)
    918273645

    >>> concat_product(192, 3)
    192384576

    >>> concat_product(35, 2)
    3570

    """
    prod = ''
    for x in range(1, n+1):
        prod += str(num * x)

    return int(prod)


def is_19_pandigital(n):
    """
    Is 1-9 pandigital.

    >>> is_19_pandigital(918273645)
    True

    >>> is_19_pandigital(192384576)
    True

    >>> is_19_pandigital(198483720)
    False

    >>> is_19_pandigital(999819996299943999249990)
    False

    """
    return len(str(n)) == 9 and set(list(str(n))) == pan

biggest = 0
pan = set(['%s' % n for n in range(1, 10)])
for i in range(1, 9999):
    for n in range(1, 6):
        cp = concat_product(i, n)
        if is_19_pandigital(cp):
            biggest = cp

print biggest


if __name__ == "__main__":
    import doctest
    doctest.testmod()
