# Find numbers a, b of the form n^2 + an + b, where the most primes are
# produced with consecutive values of n starting with 0,
# for a, b ranging between -1000 and 1000

from eratosthenes import sieve

# go up to 1000^2 + 1000*1000 + 1000 == 2001000
limit = 2001000
primes = set(sieve(limit))

max_n = 0
the_a = None
the_b = None
for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        n = 0
        eq = n*n + a*n + b
        while eq in primes:
            n += 1
            eq = n*n + a*n + b
        if n > max_n:
            max_n = n
            the_a = a
            the_b = b

print max_n, the_a, the_b
print the_a * the_b