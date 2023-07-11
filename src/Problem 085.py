def rect_count(n , m):
    return m * (m + 1) * n * (n + 1) // 4


max_rect, solutions = 2000000, {}
x = y = int(((8 * max_rect ** 0.5 + 1) ** 0.5 - 1) / 2) # define start point based on max_rect
while y > 0:
    while rect_count(x, y) < max_rect:
        x += 1
    x -= 1
    solutions[(x, y)] = rect_count(x, y)
    y -= 1
best_grid = max(solutions, key=solutions.get)
print(best_grid[0] * best_grid[1])
