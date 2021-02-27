"""
https://drive.google.com/file/d/1jHSfA2UFnBWrFj_rVvdFcT97LD11lLQ0/view?usp=sharing
Найти сумму n элементов следующего ряда чисел:
1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
"""


SUM_CONST = -0.5
s = 0
first_d = 1

n = int(input("Type in natural number: "))

for i in range(n):
    s += first_d
    first_d *= SUM_CONST

print(f"Sum = {s}")
