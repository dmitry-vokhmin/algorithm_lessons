import sys
import random

"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. 
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
"""
"""
Lesson 3 Task 9
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

first = []
second = []
third = []


def memory(obj):
    memory_sum = 0
    for item in obj:
        memory_sum += sys.getsizeof(item)
        if hasattr(item, "__iter__"):
            for itm in item:
                memory_sum += sys.getsizeof(itm)
                if hasattr(itm, "__iter__"):
                    memory_sum += memory(itm)
    return memory_sum


COL_NUM = 5
ROW_SIZE = 5
MIN_ITEM = 0
MAX_ITEM = 10
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(ROW_SIZE)] for _ in range(COL_NUM)]

first.append(matrix)
second.append(matrix)
third.append(matrix)

# First
min_col_elem = [float("inf")] * len(matrix[0])
first.append(min_col_elem)
max_elem = float("-inf")
first.append(max_elem)

for i_row, row in enumerate(matrix):
    for i_elem, elem in enumerate(row):
        if elem < min_col_elem[i_elem]:
            min_col_elem[i_elem] = elem
        if i_row == len(matrix) - 1:
            if min_col_elem[i_elem] > max_elem:
                max_elem = min_col_elem[i_elem]
    else:
        first.append(elem)
        first.append(i_elem)
else:
    first.append(row)
    first.append(i_row)
print(max_elem)

print(memory(first))  # memory = 2240 (Python 3.8.7 [MSC v.1928 64 bit (AMD64)] on win64)

# Second
max_elem = float("-inf")
second.append(max_elem)

for j in range(len(matrix[0])):
    min_elem = matrix[0][j]
    for i in range(len(matrix)):
        if matrix[i][j] < min_elem:
            min_elem = matrix[i][j]
    if max_elem == float("-inf") or max_elem < min_elem:
        max_elem = min_elem
    else:
        second.append(i)
else:
    second.append(j)
    second.append(min_elem)
print(max_elem)

print(memory(second))  # memory = 1580 (Python 3.8.7 [MSC v.1928 64 bit (AMD64)] on win64)


# Third
max_elem = float("-inf")
third.append(max_elem)
third.append(zip(*matrix))

for itm in zip(*matrix):
    row_min = min(itm)
    if row_min > max_elem:
        max_elem = row_min
else:
    third.append(itm)
    third.append(row_min)

print(max_elem)

print(memory(third))   # memory = 2840 (Python 3.8.7 [MSC v.1928 64 bit (AMD64)] on win64)

# Вывод: второй вариант самый экономный, потому что не создается дополнительнй массива и в циклах for используется
# только одна переменная (j or i)
