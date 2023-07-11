# Reciprocal cycles
# Problem 26
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators
# 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit
# recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.


def fract(num, rem = 1):
    return divmod(10 * rem, num)

fract_dict = {}
for x in range(2, 1000):
    fract_dict[x] = [fract(x)]
    while fract_dict[x][-1][1]:
        test = fract(x, fract_dict[x][-1][1])
        if test in fract_dict[x]:
            fract_dict[x].append("repeat")
            fract_dict[x].append(test)
            break
        elif test[1] == 0:
            fract_dict[x].append("terminate")
            fract_dict[x].append(test)
        else:
            fract_dict[x].append(test)

result = [len(value) for value in fract_dict.values()]
print(result.index(max(result)) + 2)