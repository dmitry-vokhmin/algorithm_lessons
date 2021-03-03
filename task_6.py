import random
"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. 
Сами минимальный и максимальный элементы в сумму не включать.
"""

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_d = [float("-inf"), 0]
min_d = [float("inf"), 0]
elem_sum = 0

for idx, digit in enumerate(array):
    if digit > max_d[0]:
        max_d[0] = digit
        max_d[1] = idx
    if digit < min_d[0]:
        min_d[0] = digit
        min_d[1] = idx

if min_d[1] > max_d[1]:
    print("Sum = 0")
else:
    for digit in range(min_d[1] + 1, max_d[1]):
        elem_sum += array[digit]
    print(f"Sum = {elem_sum}")
