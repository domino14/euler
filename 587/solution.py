# circle has unit radius
# origin is 0, 0 at the bottom left
# equation of line is y = mx
# m is (y2 - y1) / (x2 - x1)
# = 2 / (n * 2) =>  y = x/n where n is the number of circles
# equation of circle is (x-1)^2 + (y-1)^2 = 1
# (y-1)^2 = 1 - (x-1)^2
# y = 1 - sqrt(2x - x^2) 

# These lines intersect at
# y = x/n = 1 - sqrt(2x - x^2)
# x = (-sqrt(2) * n^(3/2) + n*n + n) / (n*n + 1)
import math
sqrt2 = math.sqrt(2)

def x(n):
    return (-sqrt2 * math.pow(n, 1.5) + n*n + n) / (n*n + 1)


def y(n):
    return x(n) * (1.0/n)


# The area of the L section is a constant, it's the square - circle area over 4
# (4 - pi) / 4
lsec = 1 - math.pi/4.0

# Figure out the area of the chord from x(n), y(n) to 1, 0, 
# and subtract this from the triangle with base 1 and height y(n)
# This is the area of the concave triangle

# See https://en.wikipedia.org/wiki/Circular_segment
# chord length (c) of chord from x(n), y(n) to 1, 0
# = sqrt(y(n)^2 + (1-x(n))^2)
# So area is R^2 / 2 (theta - sintheta)
# theta is 2*arcsin(c/2R)

def circ_seg(n):
    c = math.sqrt(y(n)*y(n) + (1-x(n))*(1-x(n)))
    theta = 2 * math.asin(c / 2)
    area = 0.5 * (theta - math.sin(theta))
    return area

# Putting it all together

def tri_area(n):
    return y(n) / 2.0

def rightConcaveFraction(n):
    return (tri_area(n) - circ_seg(n)) / lsec

n = 3
while True:
    rcf = rightConcaveFraction(n)
    if rcf < 0.001:
        print n
        break
    n += 1
