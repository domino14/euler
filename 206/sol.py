# yes, brute force!

for i in range(1010101010, 1389026624, 10):
    rep = str(i**2)
    if (rep[0] == '1' and rep[2] == '2' and rep[4] == '3' and rep[6] == '4' and rep[8] == '5' and rep[10] == '6' and rep[12] == '7' and rep[14] == '8' and rep[16] == '9' and rep[18] == '0'):
        print i
        break



