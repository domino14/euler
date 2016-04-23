from eratosthenes import sieve

# How far to go?
primes = sieve(1000000)
prime_set = set(primes)
print 'generated primes'
num_primes = 0

s = 0

for p in primes:
    if p <= 7:
        continue

    # truncate right
    passed = True
    p_str = list(str(p))
    while len(p_str) >= 2:
        p_str.pop()
        if int(''.join(p_str)) not in prime_set:
            passed = False
            break
    if not passed:
        continue
    # truncate left
    passed = True
    p_str = list(str(p))
    while len(p_str) >= 2:
        p_str.pop(0)
        if int(''.join(p_str)) not in prime_set:
            passed = False
            break
    if not passed:
        continue

    # We passed!
    print p
    num_primes += 1
    s += p

print "sum", s

