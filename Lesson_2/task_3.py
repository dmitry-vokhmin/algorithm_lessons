"""
https://drive.google.com/file/d/1jHSfA2UFnBWrFj_rVvdFcT97LD11lLQ0/view?usp=sharing
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""


def func(n):
    if n == 0:
        return ""
    return f"{n % 10}{func(n // 10)}"


x = int(input("Type in a natural number: "))
rev_x = func(x)
print(f"Reversed order: {rev_x}")
