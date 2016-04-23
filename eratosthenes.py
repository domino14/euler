"""
An implementation of a sieve of Eratosthenes

"""


def sieve(n):
    """ Create a sieve up to n. """
    # Mark 0, 1 as not prime.
    nums = [False, False] + [True] * (n-2)
    p = 2
    while p < n:
        sieving = True
        m = 2
        while sieving:
            # Mark m*p as composite
            try:
                nums[m*p] = False

            except IndexError:
                # went beyond range, done sieving. Increase p.
                sieving = False
            m += 1

        p += 1
        while p < n and nums[p] is not True:
            p += 1

    primes = []
    for i, n in enumerate(nums):
        if n:
            primes.append(i)

    return primes


if __name__ == '__main__':
    print sieve(100000)
