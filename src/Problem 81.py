# Path sum: two ways
# Problem 81
# In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the
# right and down, is indicated in bold red and is equal to 2427.
#
# matrix = [[131, 673, 234, 103, 18],
#           [201, 96, 342, 965, 150],
#           [630, 803, 746, 422, 111],
#           [537, 699, 497, 121, 956],
#           [805, 732, 524, 37, 331]]
#
# Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file
# containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.

data = open('data/p081_matrix.txt', 'r')
matrix = []
for line in data.readlines():
    matrix.append([int(char) for char in line.split(',')])

flag = True
for z in range(2):
    for y in range(len(matrix)):
        for x in range(y + 1):
            row, column = x, y - x
            left = matrix[row][column - 1] if column - 1 >= 0 else 2 ** 32
            up = matrix[row - 1][column] if row - 1 >= 0 else 2 ** 32
            minimum = min([left, up]) if left != up else 0
            matrix[row][column] = matrix[row][column] + minimum
    for i, row in enumerate(matrix.copy()):
        matrix[i] = list(reversed(row))
    if flag:
        matrix = list(reversed(matrix))
    flag = False
print(min([matrix[i][i] for i in range(len(matrix[0]))]))
