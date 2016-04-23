pan = set('%s' % x for x in range(1, 10))
products = set()

for a in range(2, 4988):
    for b in range(2, 4988):
        product = a * b
        if len(str(a)) + len(str(b)) + len(str(product)) == 9:
            if set(list(str(product)) + list(str(a)) + list(str(b))) == pan:
                print a, b, product
                products.add(product)


print sum(list(products))