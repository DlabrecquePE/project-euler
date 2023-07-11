# Longest Collatz sequence
# Problem 14
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

from time import time
from functools import lru_cache

@ lru_cache(maxsize=2**18)
def collatz_chain(n):
    if n == 1: return [1]
    if n % 2: return [n] + collatz_chain(3 * n + 1)
    else: return [n] + collatz_chain(n // 2)

@lru_cache(maxsize=2**18)
def collatz_chain_length(n):
    if n == 1: return 1
    if n % 2: return collatz_chain_length(3 * n + 1) + 1
    else: return collatz_chain_length(n // 2) + 1


n_max = 1000000
n_min = n_max // 2
# This is a brute force approach. We will not need to seach below n / 2,
# because all those values map to 2n values with greater collatz numbers.
# it is also not neccessay to test even numbers. The biggest collatz sequence
# from an odd number is larger then the maximum even number sequence.
n_range = range(n_min, n_max, 2) if n_min % 2 else range(n_min + 1, n_max, 2)
start = time()
chain_lengths = ((collatz_chain_length(n), n) for n in n_range)
print(max(chain_lengths))
print(time() - start)
