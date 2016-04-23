def fact(n):
    """
    Return the factorial of n

    >>> [fact(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]

    >>> fact(30)
    265252859812191058636308480000000L
    """

    if n == 0:
        return 1
    return n * fact(n-1)


big_s = 0
# Have no idea what range to go to?
for num in range(3, 3000000):
    s = 0
    digs = list(str(num))
    for dig in digs:
        s += fact(int(dig))
    if str(s) == str(num):
        print s
        big_s += s

print
print big_s

if __name__ == "__main__":
    import doctest
    doctest.testmod()
