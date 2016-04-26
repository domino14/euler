from eratosthenes import sieve

# This will factorize up until some large number.
s = sieve(1000000)


def p_factorize(n):
    """
    Return prime factors as an ordered list.

    >>> p_factorize(857)
    [857]

    >>> p_factorize(646)
    [2, 17, 19]

    >>> p_factorize(644)
    [2, 2, 7, 23]

    >>> p_factorize(15)
    [3, 5]

    >>> p_factorize(645)
    [3, 5, 43]

    """
    s_index = 0
    factors = []
    while n != 1:
        #print 'tryng to divide', n, s[s_index]
        quo, rem = divmod(n, s[s_index])
        if rem != 0:
            #print 'remainder was not 0, increase index', s_index
            s_index += 1
        else:
            #print 'remainder was 0, set n', quo
            n = quo
            #print 'append factor', s[s_index]
            factors.append(s[s_index])

    return factors


if __name__ == "__main__":
    import doctest
    doctest.testmod()
