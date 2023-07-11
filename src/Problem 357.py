import itertools as it


def erat3():
    D = {9: 3, 25: 5}
    yield 2
    yield 3
    yield 5
    MASK = 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0,
    MODULOS = frozenset((1, 7, 11, 13, 17, 19, 23, 29))

    for q in it.compress(
            it.islice(it.count(7), 0, None, 2),
            it.cycle(MASK)):
        p = D.pop(q, None)
        if p is None:
            D[q * q] = q
            yield q
        else:
            x = q + 2 * p
            while x in D or (x % 30) not in MODULOS:
                x += 2 * p
            D[x] = p


def pfactor(num, p):
    """ Returns a dict of prime factors of num          """
    """ dict keys are the prime factors                 """
    """ values contain the number of factors (exponent) """

    prime_factors = {}
    for prime in p:
        while not num % prime:
            prime_factors[prime] = prime_factors.get(prime, 0) + 1
            num = num // prime
        if num == 1:
            return prime_factors
        if prime > num ** 0.5:
            prime_factors[num] = 1
            return prime_factors


def divisors(num, p):
    """ takes a dict of prime factors from pfactor()    """
    """ returns list of divisors                        """

    num_dict = pfactor(num, p)

    def inner_divisors(num_dict, num_list={1}):
        if not num_dict:
            return num_list

        prime = min(num_dict.keys())
        exp = num_dict[prime]
        del num_dict[prime]
        back_list = inner_divisors(num_dict, num_list)
        work_list = [prime ** (i + 1) for i in range(exp)]
        for div in work_list:
            num_list = num_list.union(x * div for x in back_list)
        num_list = num_list.union(work_list).union(back_list)
        return num_list

    return sorted(list(inner_divisors(num_dict)))[1: -1]


max_num = 100000000
prime_list = []
primer = erat3()
index = 0
pair_dict = {}
prime = next(primer)
while prime <= max_num:
    prime_list.append(prime)
    div_list = divisors(prime - 1, prime_list)
    pair_sums = []
    index += 1
    if not index % 100000:
        print(index)
    while len(div_list) > 1:
        pair_sums.append(div_list.pop(0) + div_list.pop())
    if not div_list:
        pair_dict[prime - 1] = pair_sums
    prime = next(primer)

prime_set = set(prime_list)
res = [1, 2]
for num in pair_dict.keys():
    if pair_dict[num] and all(elem in prime_set for elem in pair_dict[num]):
        res.append(num)
print(sum(res))
