# Powerful digit counts
# Problem 63
# The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.
#
# How many n-digit positive integers exist which are also an nth power?

integer_list = []
for power in range(99):
    x = 1
    while len(str(x ** power)) <= power:
        if len(str(x ** power)) == power:
            integer_list.append(x ** power)
        x += 1

print(len(integer_list))