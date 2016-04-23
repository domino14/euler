s = 0
for num in range(1000000):
    br = "{0:b}".format(num)
    if str(num) == str(num)[::-1] and str(br) == str(br)[::-1]:
        s += num

print s