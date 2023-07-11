# How many reversible numbers are there below one-billion?
# Problem 145
# Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal)
# digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible;
# so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).
#
# There are 120 reversible numbers below one-thousand.
#
# How many reversible numbers are there below one-billion (10^9)?


def is_reversible(num):
    reverse = str(num)[::-1]
    if reverse[0] == '0':
        return False
    test_array = [int(char) for char in str(num + int(reverse))]
    for number in test_array:
        if number in [0, 2, 4, 6, 8]:
            return False
    return True


result = 0
old = 0
for x in range(1, 10 ** 9):
    if not x % 10000000:
        print(x // 10000000, 'percent complete')
    if is_reversible(x):
        new = len(str(x))
        if new > old:
            print(new)
            old = new
        result += 1
