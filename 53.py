def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


def ncr(n, r):
    return float(factorial(n)) / (factorial(r) * factorial(n-r))


vals = 0
for n in range(1, 101):
    for r in range(1, n+1):
        if ncr(n, r) > 1000000:
            vals += 1

print vals
