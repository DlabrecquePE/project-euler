# Arithmetic expressions
# Problem 93
# By using each of the digits from the set, {1, 2, 3, 4}, exactly once,
# and making use of the four arithmetic operations (+, −, *, /) and
# brackets/parentheses, it is possible to form different positive integer
# targets.
#
# For example,
#
# 8 = (4 * (1 + 3)) / 2
# 14 = 4 * (3 + 1 / 2)
# 19 = 4 * (2 + 3) − 1
# 36 = 3 * 4 * (2 + 1)
#
# Note that concatenations of the digits, like 12 + 34, are not allowed.
#
# Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different
# target numbers of which 36 is the maximum, and each of the numbers 1 to 28
# can be obtained before encountering the first non-expressible number.
#
# Find the set of four distinct digits, a < b < c < d, for which the longest set
# of consecutive positive integers, 1 to n, can be obtained, giving your answer
# as a string: abcd.

from itertools import permutations
from itertools import product
from collections import defaultdict

numbers = list(permutations(range(1,10), 4))
operations = list(product(['+', '-', '*', '/'], repeat=3))
results = defaultdict(set)
op_funcs = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}
for number_set in numbers:
    number_key = tuple(sorted(number_set))
    for op_list in operations:
        a, b, c, d, o1, o2, o3 = *number_set, *op_list
        t1 = op_funcs[o3](op_funcs[o2](op_funcs[o1](a,b), c), d)
        t2 = op_funcs[o3](op_funcs[o1](a,b), op_funcs[o2](c,d))
        targets = set(num for num in [t1,t2] if num >= 1)
        results[number_key] = results[number_key].union(targets)

longest = {}
for num_set, target_set in results.items():
    count, t_list = 0, sorted(list(target_set))
    if t_list[0] == 1:
        while True:
            diff = t_list[1] - t_list[0]
            if diff < 1:
                t_list.pop(1)
            elif diff == 1:
                count += 1
                t_list.pop(0)
            else:
                break
    longest[num_set] = count
print(max(longest, key=longest.get))
