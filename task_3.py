import random

"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой — не больше медианы.
"""

array = [random.randint(0, 5) for i in range(21)]
print(array)
print(sorted(array))


def median(array):
    for i in array:
        left = 0
        right = 0
        equal = -1
        for j in array:
            if i < j:
                left += 1
            elif i > j:
                right += 1
            elif i == j:
                equal += 1
        if equal > 0:
            dif = abs(left - right)
            if equal - dif >= 0:
                return i
        elif left == len(array) // 2 and right == len(array) // 2:
            return i


print(median(array))
