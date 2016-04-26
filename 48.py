from eratosthenes import sieve

s = set(sieve(10000))
inc = 3330
for i in range(999, 10000, 2):
    i2 = i + 3330
    i3 = i + 6660
    if i in s and i2 in s and i3 in s:
        si1 = set(list(str(i)))
        si2 = set(list(str(i2)))
        si3 = set(list(str(i3)))

        if si1 == si2 and si2 == si3:
            print '{0}{1}{2}'.format(i, i+3330, i+6660)
