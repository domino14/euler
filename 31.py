# coins = set(1, 2, 5, 10, 20, 50, 100, 200)

# string looks like
# from least to greatest:
# 3_1_1_0_2_1_1_0
import math
ways = set()

for c1 in range(201):
    print c1
    for c2 in range(101 - int(math.ceil(c1/2.))):
        for c5 in range(41 - int(math.ceil(c2*2/5.))):
            for c10 in range(21 - int(math.ceil(c5*5/10.))):
                for c20 in range(11 - int(math.ceil(c10*10/20.))):
                    for c50 in range(5 - int(math.ceil(c20*20/50.))):
                        for c100 in range(3 - int(math.ceil(c50*50/100.))):
                            for c200 in range(2 - int(math.ceil(c100*100/200.))):
                                if c200*200 + c100*100 + c50*50 + c20*20 + c10*10 + c5*5 + c2*2 + c1*1 == 200:
                                    ways.add('{0}_{1}_{2}_{3}_{4}_{5}_{6}_{7}'.format(
                                            c1, c2, c5, c10, c20, c50, c100, c200))

print len(ways)
