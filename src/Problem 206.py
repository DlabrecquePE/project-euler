# Concealed Square
# Problem 206
# Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
# where each “_” is a single digit.


def check_condition(num):
    string_array = [char for char in str(num)]
    for index in range(len(string_array)):
        if (index + 1) % 2:
            if int(string_array[index]) != (((index + 1) // 2) + 1) % 10:
                return False
    return True


low = 1010101010
high = 1389026623
for x in range(high, low, -1):
    if not x % 1000000:
        print(int((x-low)*100/(high-low)), 'percent complete')
    if check_condition(x ** 2):
        print(x, 'with square:', x ** 2)
        break
