max = 0
for k in range(1, 1000):
    for j in range(1, 1000):
        prod = k *j
        prodstr1 = str(prod)
        strlist = list(prodstr1)
        strlist.reverse()
        if ''.join(strlist) == prodstr1 and prod > max:
            max = prod


print max
        

