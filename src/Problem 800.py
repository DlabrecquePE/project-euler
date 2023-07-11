import itertools as it
import numpy as np


def erat3( ):
    D = { 9: 3, 25: 5 }
    yield 2
    yield 3
    yield 5
    MASK= 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0,
    MODULOS= frozenset( (1, 7, 11, 13, 17, 19, 23, 29) )

    for q in it.compress(
            it.islice(it.count(7), 0, None, 2),
            it.cycle(MASK)):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = q + 2*p
            while x in D or (x%30) not in MODULOS:
                x += 2*p
            D[x] = p


maxsize = 800800 * np.log(800800)
primer, prime_dict, total = erat3(), {}, 0
log2 = np.log(2)
while True:
    p = next(primer)
    logp = np.log(p)
    size_test = p * log2 + 2 * logp
    if size_test >= maxsize:
        break
    prime_dict[p] = logp

prime_list = list(prime_dict.keys())
while prime_list:
    test, lentest = prime_list.pop(), len(prime_list)
    if lentest % 10000 == 0:
        print(test, lentest)
    for x, prime in enumerate(prime_list):
        if test * prime_dict[prime] + prime * prime_dict[test] >= maxsize:
            total += x
            break
        if len(prime_list) == x + 1:
            total += (x + 1) * (x + 2) // 2
            prime_list = False
print(total, 'is the solution')
