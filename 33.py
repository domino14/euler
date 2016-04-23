from copy import deepcopy

fractions = []


def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


for num in range(10, 100):
    for den in range(10, 100):
        digsnum = list(str(num))
        digsden = list(str(den))
        if len(set(digsnum)) == 1 or len(set(digsden)) == 1:
            continue
        if num == den:
            continue
        div = num / float(den)
        if div > 1:
            continue
        for dn in digsnum:
            if dn in digsden and dn != '0':
                dnc = deepcopy(digsnum)
                ddc = deepcopy(digsden)
                dnc.remove(dn)
                ddc.remove(dn)
                if ddc[0] == '0':
                    continue
                if float(dnc[0]) / float(ddc[0]) == div:
                    fractions.append((num, den))

num_prod = 1
den_prod = 1

for frac in fractions:
    num_prod *= frac[0]
    den_prod *= frac[1]

g = gcd(num_prod, den_prod)
print den_prod / g
