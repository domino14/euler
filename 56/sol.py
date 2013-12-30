maxsum = 0
for i in range(1, 100):
    for j in range(1, 100):
        
        
        sum = 0
        for n in str(i**j):
            sum = sum+int(n)
        
        if sum > maxsum:
            maxsum = sum

print maxsum
