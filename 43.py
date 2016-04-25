import itertools


def num_from_index(n, index):
    """ Get a 3 digit number from the combo starting at index. """
    return int(n[index:index+3])

s = 0

for combo in itertools.permutations(''.join(
        ['%s' % x for x in range(9, -1, -1)]), 10):
    n = ''.join(combo)
    if (num_from_index(n, 1) % 2 == 0 and
        num_from_index(n, 2) % 3 == 0 and
        num_from_index(n, 3) % 5 == 0 and
        num_from_index(n, 4) % 7 == 0 and
        num_from_index(n, 5) % 11 == 0 and
        num_from_index(n, 6) % 13 == 0 and
            num_from_index(n, 7) % 17 == 0):
        s += int(n)
        print n


print 'Sum', s
