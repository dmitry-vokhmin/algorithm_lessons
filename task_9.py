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

for row in matrix:
    for idx, elem in enumerate(row):
        if elem < min_col_elem[idx]:
            min_col_elem[idx] = elem
print(f"{min_col_elem=}")

for elem in min_col_elem:
    if elem > max_elem:
        max_elem = elem

print(f"Max element: {max_elem}")
