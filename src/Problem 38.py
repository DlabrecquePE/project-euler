# Pandigital multiples
# Problem 38
# Take the number 192 and multiply it by each of 1, 2, and 3:
#
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product
# of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
# which is the concatenated product of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer
# with (1,2, ... , n) where n > 1?

from itertools import permutations
tulip_array = list(permutations(range(1, 10)))
perm_array = []
for tulip in tulip_array:
    string_array = [str(elem) for elem in tulip]
    perm_array.append(''.join(string_array))

results = []
for x in range(9, 10000):
    concat_string, index = '', 1
    while len(concat_string) < 9:
        concat_string += str(x * index)
        index += 1
    if len(concat_string) == 9:
        if concat_string in perm_array:
            results.append(int(concat_string))

print(max(results))
