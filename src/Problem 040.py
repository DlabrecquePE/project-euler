# Champernowne's constant
# Problem 40
# An irrational decimal fraction is created by concatenating the positive integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the value of the following expression.
#
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

concat = ''
index = 1
while len(concat) < 1000001:
    concat = concat + str(index)
    index += 1

strung = concat[0]+concat[9]+concat[99]+concat[999]+concat[9999]+concat[99999]+concat[999999]
strung_array = [int(char) for char in strung]
res = 1
for x in strung_array:
    res *= x

print(res)
