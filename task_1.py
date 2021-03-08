import random
import timeit
import cProfile

"""
Проанализировать скорость и сложность одного любого алгоритма из разработанных 
в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.

Lesson 3 task 4
Определить, какое число в массиве встречается чаще всего.
"""

SIZE_1 = 1000
MIN_ITEM_1 = 0
MAX_ITEM_1 = 100
array_1 = [random.randint(MIN_ITEM_1, MAX_ITEM_1) for _ in range(SIZE_1)]

SIZE_2 = 2000
MIN_ITEM_2 = 0
MAX_ITEM_2 = 1000
array_2 = [random.randint(MIN_ITEM_2, MAX_ITEM_2) for _ in range(SIZE_2)]

SIZE_3 = 3000
MIN_ITEM_3 = 0
MAX_ITEM_3 = 10000
array_3 = [random.randint(MIN_ITEM_3, MAX_ITEM_3) for _ in range(SIZE_3)]

SIZE_4 = 4000
MIN_ITEM_4 = 0
MAX_ITEM_4 = 100000
array_4 = [random.randint(MIN_ITEM_4, MAX_ITEM_4) for _ in range(SIZE_4)]


# 1. Самый быстрый вариант
def dict_sol(array):
    digit_dict = {}
    max_count = 0
    result = 0

    for digit in array:
        if digit in digit_dict:
            digit_dict[digit] += 1
        else:
            digit_dict[digit] = 1

        if digit_dict[digit] > max_count:
            max_count = digit_dict[digit]
            result = digit


print(timeit.timeit("dict_sol(array_1)", number=100, globals=globals()))  # 0.0007870999999999989 SIZE=100
print(timeit.timeit("dict_sol(array_2)", number=100, globals=globals()))  # 0.0092536 SIZE=1000
print(timeit.timeit("dict_sol(array_3)", number=100, globals=globals()))  # 0.11252410000000002 SIZE=10000
print(timeit.timeit("dict_sol(array_4)", number=100, globals=globals()))  # 1.2020278 SIZE=100000

cProfile.run("dict_sol(array_4)")  # SIZE=100000
"""         
    4 function calls in 0.012 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.012    0.012 <string>:1(<module>)
        1    0.011    0.011    0.011    0.011 task_1.py:30(dict_sol)
        1    0.000    0.000    0.012    0.012 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


# 2. Более медленный вариант
def count_sol(array):
    max_count = 0
    result = 0

    for digit in array:
        count = array.count(digit)
        if count > max_count:
            max_count = count
            result = digit


print(timeit.timeit("count_sol(array_1)", number=100, globals=globals()))  # 1.0179695 SIZE=1000
print(timeit.timeit("count_sol(array_2)", number=100, globals=globals()))  # 4.090891200000001 SIZE=2000
print(timeit.timeit("count_sol(array_3)", number=100, globals=globals()))  # 9.2119408 SIZE=3000
print(timeit.timeit("count_sol(array_4)", number=100, globals=globals()))  # 16.313734099999998 SIZE=4000

cProfile.run("count_sol(array_4)")  # SIZE=4000
"""
         4004 function calls in 0.163 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.163    0.163 <string>:1(<module>)
        1    0.000    0.000    0.163    0.163 task_1.py:67(count_sol)
        1    0.000    0.000    0.163    0.163 {built-in method builtins.exec}
     4000    0.163    0.000    0.163    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


# 3. Самый медленный
def double_count_sol(array):
    max_count = None
    result = 0
    for digit in array:
        if max_count is None:
            max_count = array.count(digit)
        if array.count(digit) > array.count(max_count):
            max_count = array.count(digit)
            result = digit


print(timeit.timeit("double_count_sol(array_1)", number=100, globals=globals()))  # 2.4534987 SIZE=1000
print(timeit.timeit("double_count_sol(array_2)", number=100, globals=globals()))  # 8.9769507 SIZE=2000
print(timeit.timeit("double_count_sol(array_3)", number=100, globals=globals()))  # 25.288660999999998 SIZE=3000
print(timeit.timeit("double_count_sol(array_4)", number=100, globals=globals()))  # 44.790097599999996 SIZE=4000

cProfile.run("double_count_sol(array_4)")  # SIZE=4000
"""
         12005 function calls in 0.451 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.451    0.451 <string>:1(<module>)
        1    0.002    0.002    0.451    0.451 task_1.py:99(double_count_sol)
        1    0.000    0.000    0.451    0.451 {built-in method builtins.exec}
    12001    0.449    0.000    0.449    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

"""
Вывод: 
1) использования словаря и поиск элементов в словаре дает нам сложность данного алгоритма O(n)
2) использование метода count на каждой итерации цикла усложняет алгоритм до сложности O(n**2)
3) использование в сравнение два метода count на каждой итерации цикла дает нам сложность O(n**3)
"""
