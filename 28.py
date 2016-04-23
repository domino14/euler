"""


        73  74  75  76  77  78  79  80  81
        72  43  44  45  46  47  48  49  50
        71  42  21  22  23  24  25  26  51
        70  41  20  7   8   9   10  27  52
        69  40  19  6   1   2   11  28  53
        68  39  18  5   4   3   12  29  54
        67  38  17  16  15  14  13  30  55
        66  37  36  35  34  33  32  31  56
        65  64  63  62  61  60  59  58  57


1 - 9 - 25 - 49 - 81  == diffs are 8, 16, 24, 32, (40, 48, ...)
1 - 7 - 21 - 43 - 73  == diffs are 6, 14, 22, 30, (38, 46, ...)
1 - 3 - 13 - 31 - 57  == diffs are 2, 10, 18, 26, (34, 42, ...)
1 - 5 - 17 - 37 - 65  == diffs are 4, 12, 20, 28, (36, 44, ...)

9x9 -- 81
1001x1001 -- 1002001

"""
n = 1
accum = 1
eights = 2
top_right = 9
top_left = 7
bottom_right = 3
bottom_left = 5
limit = 1002001
while top_right <= limit:
    accum += top_right + top_left + bottom_right + bottom_left
    top_right += (eights * 8)
    top_left += (eights * 8) - 2
    bottom_right += (eights * 8) - 6
    bottom_left += (eights * 8) - 4
    print top_right, top_left, bottom_left, bottom_right
    eights += 1

print accum
