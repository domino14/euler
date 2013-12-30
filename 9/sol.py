from math import fabs, sqrt, floor
epsilon = 0.0001

for a in range(1, 500):
    for b in range(a, 500):
        c = sqrt(a*a + b*b)
        if fabs(c - floor(c)) < epsilon:
            if a + b + c == 1000:
                print floor(a*b*c)
                print a, b, c
                break

