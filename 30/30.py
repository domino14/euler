nums_found = []
for i in range(10, 295246):   # 9^5 * 5 + 1
    # Decompose into its digits
    digits = list(str(i))
    the_sum = 0
    for digit in digits:
        the_sum += int(digit)**5
    if the_sum == i:
        nums_found.append(i)

print sum(nums_found)
