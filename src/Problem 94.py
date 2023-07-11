def square_gen():
    N = 1
    while True:
        yield N ** 2
        N += 1


print('Set 1:')
a, almost, sq_gen, perimeter, a_inc = 17, [], square_gen(), 50, 16
while perimeter < 10 ** 3:
    root, perimeter, sq = (a + 1) * (3 * a - 1), 3 * a - 1, next(sq_gen)
    if root > sq:
        sq = next(sq_gen)
        print('1', a, root, perimeter, sq)
    elif root == sq:
        print('integral solution found: ', a, root, perimeter, sq)
        almost.append(perimeter)
        a += a_inc
    else:
        a += a_inc
        
print('Set 2:')
a, almost, perimeter = 1, [], 4
while perimeter < 10 ** 9:
    root, perimeter = (a - 1) * (3 * a + 1), 3 * a + 1
    r_test = root ** 0.5
    if r_test == int(r_test):
        almost.append(perimeter)
        print('integral solution found: ', a, root, perimeter)
    a += 1

print('total: ', sum(almost))