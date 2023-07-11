# Number spiral diagonals
# Problem 28
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


def draw_number_spiral(num):
    import numpy as np
    if not num % 2:
        return None
    spiral = np.zeros((num, num))
    row = (num // 2)
    col = row
    check = 'R'
    for step in range(1, (num ** 2) + 1):
        spiral[row][col] = step
        if check == 'R':
            if not spiral[row][col + 1]:
                check = 'D'
                col += 1
            else:
                row -= 1
        elif check == 'L':
            if not spiral[row][col - 1]:
                check = 'U'
                col -= 1
            else:
                row += 1
        elif check == 'U':
            if not spiral[row - 1][col]:
                check = 'R'
                row -= 1
            else:
                col -= 1
        elif check == 'D':
            if not spiral[row + 1][col]:
                check = 'L'
                row += 1
            else:
                col += 1
    return spiral

number_spiral = draw_number_spiral(1001)
print(int(number_spiral[::-1].transpose().trace() + number_spiral.trace() - 1))
