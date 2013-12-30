import time
from math import sqrt

s = time.time()
def isprime(num):
    """tests num for primality"""
    if num < 2:
        return False
    for n in range(2, int(sqrt(num))+1):
        if num % n == 0:
            return False
    else:
        return True

numprimes = 1
num = 3
while True:
    if isprime(num):
        numprimes = numprimes + 1
    num = num + 2
    if numprimes == 10001:
        break

print num-2
print time.time() - s
