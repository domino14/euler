f = open("cipher1.txt")
line = f.read()
ss = line.split(',')
strs = []

for i in range(97, 123):
    for j in range(97, 123):
        for k in range(97, 123):
            upto = 1
            str = '--->'
            for t in ss:
                if upto == 1:
                    enc = i
                if upto == 2:
                    enc = j
                if upto == 3:
                    enc = k
                str = str + chr(int(t) ^ enc)
                upto = upto + 1
                if upto == 4:
                    upto = 1
            if str.count('the') > 0 and str.count('and') > 0 and str.count('of') > 0:
                strs.append(str)
                print i, j, k, str

print strs

i = 103
j = 111
k = 100
# 'god'
upto = 1
sum = 0
for t in ss:
    if upto == 1:
        enc = i
    if upto == 2:
        enc = j
    if upto == 3:
        enc = k

    sum = sum + (int(t)^enc)
    upto = upto + 1
    if upto == 4:
        upto = 1

print sum
