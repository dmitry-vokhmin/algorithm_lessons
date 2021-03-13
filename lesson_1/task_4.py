import random

"""
https://drive.google.com/file/d/1Yt03kbFWElEJ7rjQwpqfrOhRX-Qh0jfp/view?usp=sharing
Написать программу, которая генерирует в указанных пользователем границах:
● случайное целое число, ● случайное вещественное число, ● случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""

integer_1 = int(input("Type in the first integer: "))
integer_2 = int(input("Type in the second integer: "))

float_1 = float(input("Type in the first float number: "))
float_2 = float(input("Type in the second float number: "))

char_1 = input("Type in the first lowercase letter: ")
char_2 = input("Type in the second lowercase letter: ")

a = random.randint(integer_1, integer_2)
b = random.uniform(float_1, float_2)
c = chr(random.randint(ord(char_1), ord(char_2)))

print(f"Random number from {integer_1} to {integer_2} = {a}\n"
      f"Random float number from {float_1} to {float_2} = {b}\n"
      f"Random letter from {char_1} to {char_2} = {c}")
