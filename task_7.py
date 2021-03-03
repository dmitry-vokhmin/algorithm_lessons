import random
"""
В одномерном массиве целых чисел определить два наименьших элемента. 
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_first = float("inf")
min_second = 0

for idx, digit in enumerate(array):
    if digit < min_first:
        if idx == 0:
            min_second = digit
        else:
            min_second = min_first
        min_first = digit
    elif digit < min_second:
        min_second = digit

print(f"First: {min_first} Second: {min_second}")
