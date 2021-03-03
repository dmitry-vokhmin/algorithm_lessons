import random
"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

COL_NUM = 5
ROW_SIZE = 5
MIN_ITEM = 0
MAX_ITEM = 10
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(ROW_SIZE)] for _ in range(COL_NUM)]
print(*matrix, sep='\n')

min_col_elem = [float("inf")] * len(matrix[0])
max_elem = float("-inf")

for i_row, row in enumerate(matrix):
    for i_elem, elem in enumerate(row):
        if elem < min_col_elem[i_elem]:
            min_col_elem[i_elem] = elem
        if i_row == len(matrix) - 1:
            if min_col_elem[i_elem] > max_elem:
                max_elem = min_col_elem[i_elem]

print(f"{min_col_elem=}")

print(f"Max element: {max_elem}")
