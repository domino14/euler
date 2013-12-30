n = 20

while True:
    for i in range(2, 21):
        if n % i != 0:
            break
    else:
        # success!
        print n
        break
    n = n + 20

