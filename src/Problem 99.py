# Largest exponential
# Problem 99
# Comparing two numbers written in index form like 2^11 and 3^7 is not difficult, as any calculator would confirm
# that 2^11 = 2048 < 3^7 = 2187.
#
# However, confirming that 632382^518061 > 519432^525806 would be much more difficult, as both numbers contain over
# three million digits.
#
# Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with
#     a base/exponent pair on each line, determine which line number has the greatest numerical value.
#
# NOTE: The first two lines in the file represent the numbers in the example given above.
from math import log

data = open("p099_base_exp.txt", "r")

result = []
for line in data.readlines():
    base, exponent = [int(string) for string in line.split(',')]
    result.append(exponent * log(base))
print(result.index(max(result)) + 1)