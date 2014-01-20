"""
Notes:

stdev of uniform distribution is (b - a) / sqrt(12)

sum of two uniform distributions is a triangular distribution

average number of numbers to get to S = 1 is actually e (or very close to it)
average number to cross S = 1 is around 0.641 (why?)
"""


import random

sr = random.SystemRandom()
def gen_random():
    """
    Not a cryptographic random for now. Returns 0 to 1.
    """
    return random.random()
    #return sr.random()

def game_iter():
    global first_rs, second_rs, first_sums_req, second_sums_req, first_ss, second_ss
    S = 0
    nums = 0
    while S <= 1:
        r = gen_random()
        S += r
        nums += 1
    first_r = r
    first_rs += first_r
    first_sums_req += nums
    first_ss += S
    nums = 0
    while S <= 2:
        r = gen_random()
        S += r
        nums += 1
    second_r = r
    second_rs += second_r
    second_sums_req += nums
    second_ss += S
    return second_r > first_r

first_sums_req = 0
second_sums_req = 0
iters = 0
second_wins = 0
first_rs = 0
second_rs = 0
first_ss = 0
second_ss = 0

while True:
    if game_iter():
        second_wins += 1
    iters += 1
    if iters % 1000 == 0:
        fi = float(iters)
        print '%% win: %f, first_r: %f, second_r: %f, %f, %f, %f, %f' % (
            second_wins / fi, first_rs / fi,
            second_rs / fi, first_sums_req / fi,
            second_sums_req / fi, first_ss / fi, second_ss / fi)
        
