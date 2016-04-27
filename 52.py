def same_digits(x, y):
    return set(list(str(x))) == set(list(str(y)))


def find_permutations():
    for n in range(2, 10):
        for i in range(10**n, int(1.7*10**n)):
            if (same_digits(2*i, 3*i) and same_digits(3*i, 4*i) and
                    same_digits(4*i, 5*i) and same_digits(5*i, 6*i)):
                return i


print find_permutations()