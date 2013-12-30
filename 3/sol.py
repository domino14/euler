from math import sqrt

def isprime(num):
    """tests num for primality"""
    for n in range(2, int(sqrt(num))+1):
        if num % n == 0:
            return False
    else:
        return True


k = 600851475143
for n in range(int(sqrt(k)), 1, -1):
    if isprime(n):
        if k % n == 0:
            print n
            break

