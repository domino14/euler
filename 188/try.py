d = {}
for i in range(1000):
    x = 1777**i
    last = int(str(x)[-2:])
    if last in d:
        d[last]+=1
    else:
        d[last]=1

for key in d:
    print key, d[key]

print "num keys", len(d)
