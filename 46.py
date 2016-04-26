from eratosthenes import sieve
import math
limit = 10e6
primes = set(sieve(int(limit)))
print 'genned primes'


def decompose(n):
    """
    Decompose the composite number n into the sum of a prime and twice a
    square. Return whether it was successful.

    2 x i^2 + p = n
    2 x i^2 = n - p
    2 x i^2 <= n - 2

    i^2 <= ((n-2)/2)
    i < sqrt((n-2)/2)
    """
    l = int(math.ceil(math.sqrt((n-2)/2.)))
    for p_sq in range(1, l):
        if n - (2 * p_sq * p_sq) in primes:
            return True

    return False

for n in range(37, int(limit), 2):
    if n % 2 == 0:
        continue
    if n in primes:
        continue
    # Try to "factorize" this composite into the sum of a prime and twice
    # a square.
    success = decompose(n)
    if not success:
        print n
        break
