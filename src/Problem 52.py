# Permuted multiples
# Problem 52
# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different
# order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.


def find_number(num=1):
    test_variable = num
    while test_variable:
        test_string = str(test_variable)
        print(test_string)
        index = 6
        while index:
            if sorted(str(test_variable * index)) == sorted(test_string):
                index -= 1
                if not index:
                    return test_string
            else:
                break
        if len(str(test_variable * 6)) > len(test_string):
            test_variable = 10 ** len(test_string)
        else:
            test_variable += 1

print(find_number())
