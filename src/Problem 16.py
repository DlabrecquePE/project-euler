# Power digit sum
# Problem 16
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?

digit_array = [int(char) for char in str(2 ** 1111)]
print(sum(digit_array))
