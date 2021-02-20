"""
https://drive.google.com/file/d/1Yt03kbFWElEJ7rjQwpqfrOhRX-Qh0jfp/view?usp=sharing
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

a = int(input("Type in a free digit number: "))

digit_sum = (a // 100) + ((a // 10) % 10) + (a % 10)
digit_mul = (a // 100) * ((a // 10) % 10) * (a % 10)

print(f"{digit_sum = }\n{digit_mul = }")
