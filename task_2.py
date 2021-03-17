import random

"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

array = [round(random.uniform(0, 49.9), 1) for i in range(10)]
print(array)


def merge_sort(data):
    if len(data) <= 1:
        return data
    middle = len(data) // 2
    left = data[:middle]
    right = data[middle:]
    l = merge_sort(left)
    r = merge_sort(right)
    i = j = 0
    result = []
    while i < len(l) or j < len(r):
        if i >= len(l):
            result.append(r[j])
            j += 1
        elif j >= len(r):
            result.append(l[i])
            i += 1
        elif l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    return result


print(merge_sort(array))
