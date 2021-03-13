"""
https://drive.google.com/file/d/1Yt03kbFWElEJ7rjQwpqfrOhRX-Qh0jfp/view?usp=sharing
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

a = int(input("Type in an integer associated with letter in alphabet: "))

b = chr(a + 96)

print(f"{a} = {b}")
