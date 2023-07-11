# Double-base palindromes
# Problem 36
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)


def _stringify(num):
    array = []
    string = str(num)
    for x in range(len(string)):
        array.append(string[x])
    return array


def _gen_palidrome_number():
    array = []
    for x in range(1, 1000000):
        test = _stringify(x)
        for y in range(len(test)):
            if test[y - 1] != test[-y]:
                break
        else:
            array.append(x)
    return array


def _dec_to_bin(x):
    return int(bin(x)[2:])


palin_nums = _gen_palidrome_number()
sum_array = []
for i in palin_nums:
    binary = _dec_to_bin(i)
    strung = _stringify(binary)
    for j in range(len(strung)):
        if strung[j - 1] != strung[-j]:
            break
    else:
        sum_array.append(i)

print(sum(sum_array))
