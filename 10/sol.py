from math import sqrt

def isprime(num):
    """tests num for primality"""
    if num < 2:
        return False
    for n in range(2, int(sqrt(num))+1):
        if num % n == 0:
            return False
    else:
        return True

sum = 2
for n in range(3, 2000000,2):
    if isprime(n):
        sum = sum + n

print sum
