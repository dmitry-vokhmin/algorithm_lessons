from math import sqrt
import timeit
import cProfile

"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
"""


# 1. C помощью алгоритма «Решето Эратосфена».
# Сложность данного алгоритма O(n) однако он ограничен 1.000.000, так как множитель 17 считает числа до этого значение,
# если нужно более большое число нужно увеличить множитель но это замедлит весь алгоритм


def find_prime_number_1(n):
    result = []
    m = 2
    lst = list(range(n * 17))
    while len(result) != n:
        if lst[m] != 0:
            result.append(m)
            j = m * 2
            while j < n * 17:
                lst[j] = 0
                j = j + m
        m += 1
    return result.pop()


print(timeit.timeit("find_prime_number_1(1000)", number=100, globals=globals()))  # 0.3543463
print(timeit.timeit("find_prime_number_1(2000)", number=100, globals=globals()))  # 0.7418861
print(timeit.timeit("find_prime_number_1(4000)", number=100, globals=globals()))  # 1.5812488999999998
print(timeit.timeit("find_prime_number_1(8000)", number=100, globals=globals()))  # 3.3467857999999997

cProfile.run("find_prime_number_1(8000)")
"""
         89804 function calls in 0.044 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.044    0.044 <string>:1(<module>)
        1    0.038    0.038    0.043    0.043 task_2.py:20(find_prime_number_1)
        1    0.000    0.000    0.044    0.044 {built-in method builtins.exec}
    81799    0.005    0.000    0.005    0.000 {built-in method builtins.len}
     8000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
"""

print(find_prime_number_1(1000))


# 2. Без использования «Решета Эратосфена».
# Сложность данного логарифма ближе к O(n) однако с более большими числами может превратиться в O(n log n)

def find_prime_number_2(n):
    count = 1
    i = 1
    while count < n:
        i += 2
        for j in range(2, 1 + int(sqrt(i))):
            if i % j == 0:
                break
        else:
            count += 1
    return i


print(find_prime_number_2(1000))

print(timeit.timeit("find_prime_number_2(1000)", number=100, globals=globals()))  # 0.33028109999999966
print(timeit.timeit("find_prime_number_2(2000)", number=100, globals=globals()))  # 0.8395479000000003
print(timeit.timeit("find_prime_number_2(4000)", number=100, globals=globals()))  # 2.2458347000000005
print(timeit.timeit("find_prime_number_2(8000)", number=100, globals=globals()))  # 6.1721641

cProfile.run("find_prime_number_2(8000)")
"""
         40903 function calls in 0.067 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.067    0.067 <string>:1(<module>)
        1    0.063    0.063    0.067    0.067 task_2.py:47(find_prime_number_2)
        1    0.000    0.000    0.067    0.067 {built-in method builtins.exec}
    40899    0.004    0.000    0.004    0.000 {built-in method math.sqrt}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""
