def reverse_num(num):
    """
    >>> reverse_num(7337)
    7337

    """
    return int(str(num)[::-1])


def is_palindrome(num):
    """
    >>> is_palindrome(7337)
    True
    """
    return str(num) == str(reverse_num(num))


iteration_limit = 50
lychrels = 0
for n in range(1, 10000):
    iterations = 0
    s = n
    lychrel = True
    while iterations < iteration_limit:
        rev = reverse_num(s)
        s += rev
        if is_palindrome(s):
            lychrel = False
            break

        iterations += 1

    if lychrel:
        lychrels += 1

print 'Num lychrels:', lychrels


if __name__ == "__main__":
    import doctest
    doctest.testmod()