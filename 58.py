from eratosthenes import Sieve
s = Sieve()
limit = 1000000000
s.load(limit)

n = 1
accum = 1
eights = 2
top_right = 3
top_left = 5
bottom_right = 9
bottom_left = 7
prime_total = 0
total_nums = 1   # Count the 1.
side_l = 3
while bottom_right <= limit:
    for possible in (bottom_left, bottom_right, top_left, top_right):
        if s.is_prime(possible):
            prime_total += 1
    total_nums += 4
    if prime_total / float(total_nums) < 0.1:
        print 'side length', side_l
        break

    side_l += 2
    bottom_right += (eights * 8)
    bottom_left += (eights * 8) - 2
    top_right += (eights * 8) - 6
    top_left += (eights * 8) - 4
    # print top_right, top_left, bottom_left, bottom_right
    eights += 1

print side_l, prime_total, float(total_nums)
