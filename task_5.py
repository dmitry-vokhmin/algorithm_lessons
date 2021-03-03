import random
"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве. 
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». 
Это два абсолютно разных значения.
"""

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_neg_digit = float("-inf")
pos = 0

for idx, digit in enumerate(array):
    if digit < 0:
        if digit > max_neg_digit:
            max_neg_digit = digit
            pos = idx

print(f"Number: {max_neg_digit}, position: {pos}")
