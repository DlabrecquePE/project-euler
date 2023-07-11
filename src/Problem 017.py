# Number letter counts
# Problem 17
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
# 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many
# letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains
# 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing
# out numbers is in compliance with British usage.


def number_word(num):
    words = {
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
        17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
        60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'one hundred', 200: 'two hundred',
        300: 'three hundred', 400: 'four hundred', 500: 'five hundred', 600: 'six hundred', 700: 'seven hundred',
        800: 'eight hundred', 900: 'nine hundred', 1000: 'one thousand'
    }

    if num in words:
        word_string = words[num]
    elif 100 < num < 1000:
        word_string = number_word(num // 100) + " hundred and " + number_word(num % 100)
    else:
        word_string = number_word((num // 10) * 10) + "-" + number_word(num % 10)
    return word_string


result_array = []
for x in range(1, 1001):
    word_list = number_word(x).replace('-', ' ').split()
    letter_count = [len(word) for word in word_list]
    result_array.append(sum(letter_count))
print(sum(result_array))
