import random

"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
"""

array = [random.randint(-100, 99) for i in range(10)]
print(array)


def bubble_sort(array):
    for j in range(1, len(array)):
        for i in range(len(array) - j):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]


bubble_sort(array)
print(array)
