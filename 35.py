from eratosthenes import sieve

primes = sieve(1000000)
prime_set = set(primes)
prime_ct = 0

for prime in primes:
    # rotations
    test_rot = True
    rot_prime = prime
    for i in range(len(str(prime))):
        rot_prime = list(str(rot_prime))
        rot_prime.insert(0, rot_prime.pop())
        rot_prime = int(''.join(rot_prime))
        if rot_prime not in prime_set:
            test_rot = False
            break
    if test_rot:
        print prime
        prime_ct += 1

print "Num primes", prime_ct
