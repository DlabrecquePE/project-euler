def gen_primes():
    """ Generate an infinite sequence of prime numbers """
    d, q = {}, 2
    while True:
        if q not in d:
            yield q
            d[q * q] = [q]
        else:
            for p in d[q]:
                d.setdefault(p + q, []).append(p)
            del d[q]
        q += 1


from functools import lru_cache
@lru_cache(maxsize=999999)
def pfactor(num):
    """ Returns a dict of prime factors of num          """
    """ dict keys are the prime factors                 """
    """ values contain the number of factors (exponent) """

    prime_factors, primes = {}, gen_primes()
    for prime in primes:
        while not num % prime:
            prime_factors[prime] = prime_factors.get(prime, 0) + 1
            num = num // prime
        if num == 1:
            return prime_factors
        if prime > num ** 0.5:
            prime_factors[num] = 1
            return prime_factors


def divisors(num):
    """ takes a dict of prime factors from pfactor()    """
    """ returns list of divisors                        """

    if num in [0,1]:
        return [1]

    num_dict = pfactor(num)

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
    return sorted(list(inner_divisors(num_dict)))


print(sum(divisors(276)[:-1]))
print(sum(divisors(396)[:-1]))
# chains, perfect = {}, []
# for x in range(270, 999):
#     print(x)
#     div_sum = sum(divisors(x)[:-1])
#     current_chain = [x]
#     while div_sum not in current_chain:
#         # print(x, div_sum, current_chain)
#         chains[x] = chains.get(x, []) + [div_sum]
#         current_chain.append(div_sum)
#         div_sum = sum(divisors(div_sum)[:-1])
# print(len(chains))


