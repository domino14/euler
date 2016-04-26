from factorize import p_factorize

n = 647
found_4 = []
while True:
    num_distinct = len(set(p_factorize(n)))
    if num_distinct == 4:
        found_4.append(n)
    else:
        found_4 = []
    if len(found_4) == 4:
        break
    n += 1

print n - 3
