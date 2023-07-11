from time import time
from PEtools import gen_primes
from functools import lru_cache


def list_product(nums):
    total = 1
    for num in nums:
        total *= num
    return total


@lru_cache(maxsize=2**20)
def factorize(num):
    """ Returns a list of prime factors of num """
    root_num, factor_list, primes = num ** 0.5, set(), gen_primes()
    while True:
        prime = next(primes)
        while not num % prime:
            factor_list.add(prime)
            num = num // prime
        if num == 1:
            return factor_list
        if prime > root_num:
            factor_list.add(num)
            return factor_list


def totient(num):
    factors = factorize(num)
    numers, denoms = [x - 1 for x in factors], [x for x in factors]
    l_numers, l_denoms = list_product(numers), list_product(denoms)
    # print(num, numers, denoms, l_numers, l_denoms)
    return num * l_numers // l_denoms
    

start = time()
tot_list = [totient(x) for x in range(2,1000001)]

print(sum(tot_list), time() - start)