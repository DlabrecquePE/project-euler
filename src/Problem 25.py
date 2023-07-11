# 1000-digit Fibonacci number
# Problem 25
# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
#
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
import functools


@functools.lru_cache(maxsize=4)
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


fib_dict = {}
old_length = 0
for x in range(1, 25000):
    new_length = len(str(fib(x)))
    if new_length > old_length:
        fib_dict[new_length] = x
        old_length = new_length

print(fib_dict[1000])

