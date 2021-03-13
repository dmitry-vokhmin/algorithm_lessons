"""
https://drive.google.com/file/d/1Yt03kbFWElEJ7rjQwpqfrOhRX-Qh0jfp/view?usp=sharing
Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""

a = input("Type in the first lowercase letter: ")
b = input("Type in the second lowercase letter: ")

c = abs(ord(a) - ord(b)) - 1

print(f"{a} = {ord(a) - 96}, {b} = {ord(b) - 96}\n"
      f"range between them: {c} letters")
