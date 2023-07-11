# Roman numerals
# Problem 89
# For a number written in Roman numerals to be considered valid there are basic rules which must be followed. Even
# though the rules allow some numbers to be expressed in more than one way there is always a "best" way of writing
# a particular number.
#
# For example, it would appear that there are at least six ways of writing the number sixteen:
#
# IIIIIIIIIIIIIIII
# VIIIIIIIIIII
# VVIIIIII
# XIIIIII
# VVVI
# XVI
#
# However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most
# efficient, as it uses the least number of numerals.
#
# The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in
# valid, but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules for
# this problem.
#
# Find the number of characters saved by writing each of these in their minimal form.
#
# Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.

data = open("p089_roman.txt", "r")


def roman_to_decimal(numeral):
    value = 0
    value_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40,
                  'XC': 90, 'CD': 400, 'CM': 900}
    sub_pairs = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
    while len(numeral) > 1:
        if numeral[:2] in sub_pairs:
            value += value_dict[numeral[:2]]
            numeral = numeral[2:]
        else:
            value += value_dict[numeral[0]]
            numeral = numeral[1:]
    return value + value_dict[numeral] if numeral else value


def decimal_to_roman(num, roman=''):
    if num == 0:
        return roman
    digit_place = 10 ** (len(str(num)) - 1)
    r_digit = num // digit_place
    numeral_repr = r_digit * digit_place
    roman_dict = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M', 4: 'IV', 9: 'IX', 40: 'XL',
                  90: 'XC', 400: 'CD', 900: 'CM'}
    if numeral_repr in roman_dict:
        return decimal_to_roman(num - numeral_repr, roman + roman_dict[numeral_repr])
    roman_digit = max([x for x in roman_dict.keys() if x <= numeral_repr])
    return decimal_to_roman(num - roman_digit, roman + roman_dict[roman_digit])


chars, chars_saved = 0, 0
for line in data.readlines():
    parsed = line.strip('\n')
    chars += len(parsed)
    number = roman_to_decimal(parsed)
    minimal_string = decimal_to_roman(number)
    chars_saved += len(minimal_string)
print(chars - chars_saved)
