from eratosthenes import sieve

s = sieve(1000000)
prime_set = set(s)
summands = sieve(50000)

consecutives = 0
the_prime = 0

print 'evaluating', len(summands), 'summands'
for i, p in enumerate(summands):
    p_list = []
    for j in range(i, len(summands)):
        p_list.append(summands[j])
        the_sum = sum(p_list)
        if the_sum in prime_set:
            if len(p_list) > consecutives:
                consecutives = len(p_list)
                the_prime = the_sum


print the_prime, consecutives
