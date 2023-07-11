# Non-abundant sums
# Problem 23
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
# the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this
# sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum
# of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be
# written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even
# though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than
# this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


def proper_divisors(number):
    divisors = []
    for count in range(1, number):
        if not number % count:
            divisors.append(count)
    return divisors


def abundant(num):
    output_array = []
    for count in range(1, num):
        if sum(proper_divisors(count)) > count:
            output_array.append(count)
    return output_array

a = abundant(28123)
elim_list = list(range(1, 28124))
for i, x in enumerate(a):
    print(i, 'of', len(a), 'complete')
    for y in a[i:]:
        test = x + y
        if test > 28123:
            break
        if test in elim_list:
            elim_list.remove(test)

print(sum(elim_list))
