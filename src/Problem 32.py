# Pandigital products
# Problem 32
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
# for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier,
# and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9
# pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

result = []
for x in range(1, 100000):
    for y in range(1, 100000):
        test = str(x * y)
        digits = len(str(x)) + len(str(y))
        if len(test) > 9 - digits:
            break
        else:
            strung = [int(char) for char in test] + [int(char) for char in str(x)] + [int(char) for char in str(y)]
            if 0 not in strung:
                if len(set(strung)) == 9:
                    result.append(int(test))
print(sum(set(result)))
