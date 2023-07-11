# A Modified Collatz sequence
# Problem 277
# A modified Collatz sequence of integers is obtained from a starting value a1 in the following way:
#
# an+1 = an/3 if an is divisible by 3. We shall denote this as a large downward step, "D".
#
# an+1 = (4an + 2)/3 if an divided by 3 gives a remainder of 1. We shall denote this as an upward step, "U".
#
# an+1 = (2an - 1)/3 if an divided by 3 gives a remainder of 2. We shall denote this as a small downward step, "d".
#
# The sequence terminates when some an = 1.
#
# Given any integer, we can list out the sequence of steps.
# For instance if a1=231, then the sequence {an}={231,77,51,17,11,7,10,14,9,3,1} corresponds to the steps "DdDddUUdDD".
#
# Of course, there are other sequences that begin with that same sequence "DdDddUUdDD....".
# For instance, if a1=1004064, then the sequence is DdDddUUdDDDdUDUUUdDdUUDDDUdDD.
# In fact, 1004064 is the smallest possible a1 > 10^6 that begins with the sequence DdDddUUdDD.
#
# What is the smallest a1 > 10^15 that begins with the sequence "UDDDUdddDDUDDddDdDddDDUDDdUUDd"?


def modified_collatz(num):
    if num % 3 == 0:
        return num // 3, "D"
    if num % 3 == 1:
        return (4 * num + 2) // 3, "U"
    if num % 3 == 2:
        return (2 * num - 1) // 3, "d"


def find_value(value = 10 ** 15 + 3359500581):
    test_string = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
    while True:
        index = 0
        temp = (value, "")
        temp_string = ""
        while True:
            if index == len(test_string):
                return value
            temp = modified_collatz(temp[0])
            temp_string += temp[1]
            if temp[1] != test_string[index]:
                break
            index += 1
        value += 3486784401


print(find_value())
