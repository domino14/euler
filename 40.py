"""
A fast brute force solution to this problem. This is probably NOT the
way it should be done, and I could probably learn a lot if I did it with
number theory :P

"""


def champer():
    the_str = ''
    for n in range(1, 1000000 + 1):
        the_str += str(n)
    print int(the_str[1-1]) * int(the_str[10-1]) * int(the_str[100-1]) * (
        int(the_str[1000-1])) * int(the_str[10000-1]) * int(
        the_str[100000-1]) * int(the_str[1000000-1])

champer()
