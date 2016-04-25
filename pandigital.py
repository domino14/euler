def is_1_x_pandigital(n, x):
    """
    Test if n is 1-x pandigital.

    >>> is_1_x_pandigital(918273645, 9)
    True

    >>> is_1_x_pandigital(192384576, 9)
    True

    >>> is_1_x_pandigital(198483720, 9)
    False

    >>> is_1_x_pandigital(999819996299943999249990, 9)
    False

    >>> is_1_x_pandigital(35124, 5)
    True
    """
    pan = set(['%s' % t for t in range(1, x+1)])
    return len(str(n)) == x and set(list(str(n))) == pan


if __name__ == "__main__":
    import doctest
    doctest.testmod()
