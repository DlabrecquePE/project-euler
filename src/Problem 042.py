# Coded triangle numbers
# Problem 42
# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we
# form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle
# number then we shall call the word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
# English words, how many are triangle words?


def alpha_value(word):
    sum_array = []
    for char in word:
        sum_array.append(ord(char) - 64)
    return sum(sum_array)


data = open('data/p042_words.txt', 'r')
raw_data = data.read().split(',')
parsed = [word.strip('"') for word in raw_data]
tri_nums = [(n * (n + 1) / 2) for n in range(1, 20)]
result = []

for elem in parsed:
    if alpha_value(elem) in tri_nums:
        result.append((elem, alpha_value(elem)))

print(len(result))
