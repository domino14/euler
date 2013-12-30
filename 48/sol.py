sum = 0
for i in range(1, 1001):
    sum = sum + i**i

m = str(sum)
print m[len(m)-10:len(m)]

