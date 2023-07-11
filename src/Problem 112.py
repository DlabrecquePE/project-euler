def is_bouncy(num):
    num_list = [int(char) for char in str(num)]
    prev, dir = num_list.pop(0), 0
    while num_list:
        curr = num_list.pop(0)
        diff = curr - prev
        if dir:
            if (diff < 0 and dir > 0) or (diff > 0 and dir < 0):
                return True
        prev, dir = curr, diff if not dir else dir
    return False


percentage, n, b_count = 0.99, 0, 0
while True:
    if is_bouncy(n):
        b_count += 1
        if b_count / n >= percentage:
            print(n)
            break
    n += 1
