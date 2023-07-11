# Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that a triangle
# is formed.
#
# Consider the following two triangles:
#
# A(-340,495), B(-153,-910), C(835,-947)
#
# X(-175,41), Y(-421,-714), Z(574,-645)
#
# It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.
#
# Using p102_triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of
# one thousand "random" triangles, find the number of triangles for which the interior contains the origin.
#
# NOTE: The first two examples in the file represent the triangles in the example given above. which -1000 ≤ x,
# y ≤ 1000, such that a triangle is formed.


def magnitude(vector):
    return sum(list(i ** 2 for i in vector)) ** 0.5


def dot_2d(vector1, vector2):
    return vector1[0] * vector2[0] + vector1[1] * vector2[1]


def angle(vector1, vector2):
    from math import acos
    return acos(dot_2d(vector1, vector2) / (magnitude(vector1) * magnitude(vector2)))


file = open('p102_triangles.txt', 'r')
origin_count, pi = 0, 3.14159265359
for data in file.readlines():
    triangle = [int(x) for x in data.split(',')]
    v1, v2, v3 = triangle[:2], triangle[2:4], triangle[4:]
    angles = sorted([angle(v1, v2), angle(v2, v3), angle(v3, v1)])
    if angles[0] + angles[1] >= pi:
        origin_count += 1
print(origin_count)