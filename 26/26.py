def divide_to_accuracy(x, y, digits):
    """
    x / y to digits accuracy.
    :x an integer
    :y an integer
    :digits the number of digits after the decimal point

    Return a string representing the accuracy.
    """
    accumulator = ''
    # Implement grade school division algorithm?
    quotient, remainder = divmod(x, y)
    accumulator += str(quotient) + '.'
    for d in range(digits):
        x = remainder * 10
        quotient, remainder = divmod(x, y)
        accumulator += str(quotient)

    return accumulator

# '082082'


def string_repeats(s):
    """ This returns the repeating string within s, but it assumes s
    only consists of repeating strings (so we must remove prefix) """
    double = s + s
    idx = double.find(s, 1, -1)
    if idx == -1:
        return None
    return double[:idx]


def recurring_cycle_length(x, y):
    """ Find the length of the recurring cycle when dividing x / y """

    accumulator = ''
    # Implement grade school division algorithm?
    quotient, remainder = divmod(x, y)
    accumulator += str(quotient) + '.'
    after_dec = ''
    max_rep_length = 0
    max_prefix_length = 10  #
    num_times_1 = 0
    for d in range(2000):
        x = remainder * 10
        quotient, remainder = divmod(x, y)
        after_dec += str(quotient)
        for i in range(max_prefix_length):
            rep = string_repeats(after_dec[i:])
            if rep:
                if len(rep) > max_rep_length:
                    max_rep_length = len(rep)
                if len(rep) == 1:
                    num_times_1 += 1
        if num_times_1 > 10:
            break
    return max_rep_length

# 0.0|102040816326530612244897959183673469387755|102040
cycle_length = 0
d = 0
for i in range(1, 1000):
    l = recurring_cycle_length(1, i)
    if l > cycle_length:
        cycle_length = l
        d = i
    print i, recurring_cycle_length(1, i)

# God I hate this hacky solution.
print "Longest length is", cycle_length, "for d =", d
