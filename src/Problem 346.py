# Strong Repunits
# Problem 346
#
# The number 7 is special, because 7 is 111 written in base 2, and 11 written in base 6
# (i.e. 710 = 116 = 1112). In other words, 7 is a repunit in at least two bases b > 1.
#
# We shall call a positive integer with this property a strong repunit. It can be verified that there are 8 strong
# repunits below 50: {1,7,13,15,21,31,40,43}.
# Furthermore, the sum of all strong repunits below 1000 equals 15864.
# Find the sum of all strong repunits below 1012.

from math import floor
repunits = set()
max_number = 10 ** 12
for base in range(2, floor(max_number ** 0.5)):
    repunit = base ** 2 + base ** 1 + base ** 0
    exponent = 3
    while repunit < max_number:
        repunits.add(repunit)
        repunit += base ** exponent
        exponent += 1
print(sum(repunits) + 1)

