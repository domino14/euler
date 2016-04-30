"""
An implementation of a sieve of Eratosthenes

"""
from bitarray import bitarray
import sys


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


class Sieve(object):
    """ An efficient Sieve of Eratosthenes class. Uses bitsets. """
    def generate(self, max_num):
        max_bytes = max_num/8 + 1
        nums = bitarray(max_bytes*8)
        nextprime = 2
        nums[0] = True
        nums[1] = True
        while nextprime + 1 < max_bytes * 8:
            k = nextprime
            while nextprime * k < max_bytes * 8:
                nums[nextprime * k] = True
                k += 1
            nextprime += 1
            while nextprime + 1 < max_bytes * 8 and nums[nextprime] is True:
                nextprime += 1
        self.sieve = nums
        f = open('sieve_%s.bin' % max_num, 'w')
        self.sieve.tofile(f)
        f.close()

    def print_sieve(self):
        for i in range(0, self.sieve.length()):
            print i,
            if self.sieve[i]:
                print 'Not prime'
            else:
                print 'PRIME'

    def load(self, max_num):
        nums = bitarray()
        f = open('sieve_%s.bin' % max_num)
        nums.fromfile(f)
        f.close()
        self.sieve = nums

    def is_prime(self, n):
        return not self.sieve[n]


# s = Sieve()
# s.load(1000)
# for n in range(1000):
#     if s.is_prime(n):
#         print 'Prime:', n

if __name__ == '__main__':
    max_num = int(sys.argv[1])
    s = Sieve()
    s.generate(max_num)
