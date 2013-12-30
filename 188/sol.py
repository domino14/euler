def lastNdigits(n, a, b):
    # a ^^ 1 = a
    # a ^^ (k+1) = a^(a ^^ k)

    result = 1
    for i in range(b):
        for j in range(a):
            result = 
