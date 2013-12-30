import math

def numFactorsOver2(n):
    num = 0
    for i in range (1, int(math.sqrt(n)) + 1):
        if n%i == 0:
            num = num + 1
    
    if int(math.floor(math.sqrt(n))) * int(math.floor(math.sqrt(n))) == n:
        num = num - 1 # if n is a perfect square then we're getting a lamina with no hole
    return num


def NofN():
    laminae = 0
    for t in range(8, 1000001):
        # only multiples of 4 can be expressed as the diff of two squares..
        # and odd numbers, but then c and i will have different parity so skip these
        if t % 4 != 0:
            continue     

        N = t/4 # an integer
        # count how many pairs of factors N has
        # this is the "type" for t
        type = numFactorsOver2(N)
        laminae = laminae + type

    print laminae

NofN()
