triangle_nums = set()

for n in range(1000):
    triangle_nums.add(0.5*n * (n+1))


def is_triangle(n):
    return n in triangle_nums


f = open("p042_words.txt")
wds = f.read()
f.close()

word_list = wds.split(',')

triangles = 0
for word in word_list:
    score = 0
    for letter in word:
        if letter == '"':
            continue
        score += ord(letter) - ord('A') + 1
    if is_triangle(score):
        print word
        triangles += 1

print triangles
