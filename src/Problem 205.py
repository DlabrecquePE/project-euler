from itertools import product
from collections import Counter

pete_rolls = [sum(x) for x in product((1, 2, 3, 4), repeat=9)]
colin_rolls = [sum(x) for x in product((1, 2, 3, 4, 5, 6), repeat=6)]

pete_roll_dict = Counter(pete_rolls)
colin_roll_dict = Counter(colin_rolls)

pete_roll_range = sorted(pete_roll_dict.keys())



print(pete_roll_range)