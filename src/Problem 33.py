# Digit cancelling fractions
# Problem 33
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
# incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two
# digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

import fractions

stor = dict()
for x in range(10, 100):
    for y in range(x + 1, 100):
        stor[(x, y)] = 1

i_stor = stor.copy()
for fract in i_stor:
    a = set([char for char in str(fract[0])])
    b = set([char for char in str(fract[1])])
    if a == b:
        del stor[fract]
    else:
        cancel = int(*a.intersection(b))
        if cancel:
            stor[fract] = cancel
        else:
            del stor[fract]

for key, value in stor.items():
    a = [int(char) for char in str(key[0])]
    b = [int(char) for char in str(key[1])]
    a.remove(value)
    b.remove(value)
    stor[key] = (*a, *b)

i_stor = stor.copy()
for key, value in i_stor.items():
    if value[1] == 0:
        if __name__ == '__main__':
            del stor[key]

result = []
for key, value in stor.items():
    if key[0] / key[1] == value[0] / value[1]:
        result.append((key, value, key[0] / key[1]))

a = 1
b = 1
for fract in result:
    a *= fract[0][0]
    b *= fract[0][1]

print(b // fractions.gcd(a, b))