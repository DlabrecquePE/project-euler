# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/
from collections import Counter


def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


# def primes_by_digits(n):
#     primer, primes = gen_primes(), []
#     while True:
#         test_prime = str(next(primer))
#         if len(test_prime) == n:
#             primes.append(test_prime)
#         elif len(test_prime) > n:
#             break
#     return primes


# def prime_search(prime_list, repeat):
#     short = []
#     for prime in prime_list:
#         digits = [char for char in prime]
#         if len(set(digits)) < len(digits) - repeat:
#             short.append(prime)
#     return short


# # %%
# search_primes = primes_by_digits(6)
# print(len(search_primes))

# # %%
# short = prime_search(search_primes, 2)

# len(short)
# print(short)

# shorter = [tuple(set(x)) for x in [char for char in [word for word in short]]]
# print(shorter)

# pattern = Counter(shorter)
# print(pattern)

from collections import Counter
from itertools import permutations

primer, max_prime = gen_primes(), 10 ** 5
prime, candidates = next(primer), []
while prime < max_prime:
    candidates.append(prime)
    prime = next(primer)
candidates = [num for num in candidates if len(str(num)) == 5]
print(len(candidates))

perms = list(permutations([1,1,1,0,0]))

num_list = []
for n in range(1000):   
    nums = [int(char) for char in str(n)]
    for per in perms:
        for x in range(10):
            new_num = [a if per[i] else x for a, i in nums, range(5)]
            print(new_num)


