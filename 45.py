def gen_nums():
    i = 1
    while True:
        yield (i * (i+1) / 2, i * (3*i - 1) / 2, i * (2*i - 1))
        i += 1

# def gen_pentagons(n):
#     for i in range(n):
#         yield i * (3*i - 1) / 2


# def gen_hexagons(n):
#     for i in range(n):
#         yield i * (2*i - 1)

tris = set()
pens = set()
hexes = set()

n_all = 0

for num_tuple in gen_nums():
    tris.add(num_tuple[0])
    pens.add(num_tuple[1])
    hexes.add(num_tuple[2])
    if num_tuple[0] in pens and num_tuple[0] in hexes:
        n_all += 1
        print num_tuple[0]
    if n_all == 3:
        break